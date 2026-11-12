<?php
/**
 * ==============================================================================
 * HETXA BOS - LEAD & CONTACT FORM PROCESSING HANDLER
 * Handles AJAX & standard POST submissions, sends branded HTML email,
 * logs inquiries securely to data/leads.csv, and returns JSON response.
 * ==============================================================================
 */

// 1. ENVIRONMENT CONFIGURATION LOADER (.env)
require_once __DIR__ . '/includes/env.php';

// 2. SMTP, RECIPIENT & TURNSTILE SETTINGS (LOADED DIRECTLY FROM .env)
define('USE_SMTP', (bool)get_env_val('USE_SMTP', false));
define('SMTP_HOST', (string)get_env_val('SMTP_HOST', 'mail.hetxa.com'));
define('SMTP_PORT', (int)get_env_val('SMTP_PORT', 465));
define('SMTP_SECURE', (string)get_env_val('SMTP_SECURE', 'ssl'));
define('SMTP_USER', (string)get_env_val('SMTP_USER', 'hello@hetxa.com'));
define('SMTP_PASS', (string)get_env_val('SMTP_PASS', ''));

define('ADMIN_EMAIL', (string)get_env_val('ADMIN_EMAIL', 'hello@hetxa.com'));
define('BACKUP_EMAIL', (string)get_env_val('BACKUP_EMAIL', 'sales@hetxa.com'));
define('SENDER_NAME', (string)get_env_val('SENDER_NAME', 'Hetxa BOS Lead System'));
define('SENDER_EMAIL', (string)get_env_val('SENDER_EMAIL', 'hello@hetxa.com'));
define('WHATSAPP_HOTLINE', (string)get_env_val('WHATSAPP_HOTLINE', '94774341227'));

define('TURNSTILE_ENABLED', (bool)get_env_val('TURNSTILE_ENABLED', false));
define('TURNSTILE_SECRET_KEY', (string)get_env_val('TURNSTILE_SECRET_KEY', ''));

// 3. SET RESPONSE HEADERS (JSON FOR AJAX)
header('Content-Type: application/json; charset=UTF-8');

// Only allow POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode([
        'status'  => 'error',
        'message' => 'Invalid request method. Only POST is accepted.'
    ]);
    exit;
}

// 3. HONEYPOT ANTI-SPAM TRAP
// If hidden bot trap field is filled, silently exit with success (bots think it worked)
if (!empty($_POST['website_hp_check']) || !empty($_POST['fax_number_empty'])) {
    echo json_encode([
        'status'  => 'success',
        'message' => 'Thank you! Your inquiry has been received.'
    ]);
    exit;
}

// 4. SANITIZE & EXTRACT FORM INPUTS
// Supports both contact.php and index.php form field names
$name     = trim(strip_tags($_POST['fullName'] ?? $_POST['cfName3'] ?? ''));
$email    = trim(filter_var($_POST['email'] ?? $_POST['cfEmail3'] ?? '', FILTER_SANITIZE_EMAIL));
$phone    = trim(strip_tags($_POST['phone'] ?? $_POST['cfPhone3'] ?? ''));
$company  = trim(strip_tags($_POST['company'] ?? $_POST['cfCompany3'] ?? ''));
if ($company === '') $company = 'Not specified';
$solution = trim(strip_tags($_POST['solution'] ?? $_POST['cfSubject3'] ?? 'General Inquiry'));
if ($solution === '') $solution = 'General Inquiry';
$budget   = trim(strip_tags($_POST['budget'] ?? $_POST['cfBudget3'] ?? ''));
if ($budget === '') $budget = 'Not specified';
$branches = trim(strip_tags($_POST['branches'] ?? 'Not specified'));
$timeline = trim(strip_tags($_POST['timeline'] ?? 'Not specified'));
$message  = trim(strip_tags($_POST['message'] ?? $_POST['cfMessage3'] ?? ''));
$source   = trim(strip_tags($_POST['source'] ?? (isset($_POST['cfName3']) ? 'Homepage Contact Section' : 'Contact Us Page')));

// Validation
$errors = [];
if (empty($name) || strlen($name) < 2) {
    $errors[] = 'Full name is required (minimum 2 characters).';
}
if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors[] = 'A valid business email address is required.';
}
if (empty($phone) || strlen($phone) < 8) {
    $errors[] = 'A valid phone / WhatsApp contact number is required.';
}

if (!empty($errors)) {
    http_response_code(422);
    echo json_encode([
        'status'  => 'error',
        'message' => implode(' ', $errors),
        'errors'  => $errors
    ]);
    exit;
}

// 4B. CLOUDFLARE TURNSTILE VERIFICATION
if (TURNSTILE_ENABLED && !empty(TURNSTILE_SECRET_KEY)) {
    $turnstileToken = trim($_POST['cf-turnstile-response'] ?? '');
    if ($turnstileToken === '') {
        http_response_code(422);
        echo json_encode([
            'status'  => 'error',
            'message' => 'Please complete the Cloudflare security verification before submitting.'
        ]);
        exit;
    }

    $verifyPayload = http_build_query([
        'secret'   => TURNSTILE_SECRET_KEY,
        'response' => $turnstileToken,
        'remoteip' => $_SERVER['REMOTE_ADDR'] ?? ''
    ]);
    $verifyUrl = 'https://challenges.cloudflare.com/turnstile/v0/siteverify';
    $verifyResponse = false;

    if (function_exists('curl_init')) {
        $ch = curl_init($verifyUrl);
        curl_setopt_array($ch, [
            CURLOPT_POST           => true,
            CURLOPT_POSTFIELDS     => $verifyPayload,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_TIMEOUT        => 10,
        ]);
        $verifyResponse = curl_exec($ch);
        curl_close($ch);
    } else {
        $ctx = stream_context_create([
            'http' => [
                'method'  => 'POST',
                'header'  => "Content-Type: application/x-www-form-urlencoded\r\n",
                'content' => $verifyPayload,
                'timeout' => 10,
            ]
        ]);
        $verifyResponse = @file_get_contents($verifyUrl, false, $ctx);
    }

    $verifyData = $verifyResponse ? json_decode($verifyResponse, true) : null;
    if (empty($verifyData['success'])) {
        http_response_code(422);
        echo json_encode([
            'status'  => 'error',
            'message' => 'Security verification failed. Please refresh the check and try again.'
        ]);
        exit;
    }
}

// Clean phone for WhatsApp / tel link
$cleanPhone = preg_replace('/[^0-9]/', '', $phone);
if (substr($cleanPhone, 0, 1) === '0' && strlen($cleanPhone) === 10) {
    $waPhone = '94' . substr($cleanPhone, 1);
} else {
    $waPhone = $cleanPhone;
}

// 5. SECURELY LOG LEAD TO CSV (LEADS DATABASE BACKUP)
$dataDir = __DIR__ . '/data';
if (!is_dir($dataDir)) {
    @mkdir($dataDir, 0755, true);
    // Protect data folder with .htaccess
    @file_put_contents($dataDir . '/.htaccess', "Order Allow,Deny\nDeny from all\n");
}

$leadsFile = $dataDir . '/leads.csv';
$isNewFile = !file_exists($leadsFile);

$logHandle = @fopen($leadsFile, 'a');
if ($logHandle) {
    if ($isNewFile) {
        // Write CSV header
        fputcsv($logHandle, [
            'Timestamp',
            'Source',
            'Client Name',
            'Email',
            'Phone',
            'Company',
            'Solution',
            'Branches',
            'Budget',
            'Timeline',
            'Message',
            'IP Address',
            'User Agent'
        ]);
    }

    fputcsv($logHandle, [
        date('Y-m-d H:i:s'),
        $source,
        $name,
        $email,
        $phone,
        $company,
        $solution,
        $branches,
        $budget,
        $timeline,
        $message,
        $_SERVER['REMOTE_ADDR'] ?? 'Unknown',
        $_SERVER['HTTP_USER_AGENT'] ?? 'Unknown'
    ]);
    fclose($logHandle);
}

// 6. BUILD MODERN BRANDED HTML EMAIL NOTIFICATION
$emailSubject = "🚀 New ERP Lead: " . $name . " - " . ($company !== 'Not specified' ? $company : $solution);

$htmlBody = '<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>' . htmlspecialchars($emailSubject) . '</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #F8FAFC; margin: 0; padding: 20px; color: #1E293B; }
    .email-container { max-width: 620px; margin: 0 auto; background: #FFFFFF; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08); border: 1px solid #E2E8F0; }
    .header { background: linear-gradient(135deg, #FF5E14 0%, #D84305 100%); padding: 32px 30px; text-align: center; color: #FFFFFF; }
    .header h1 { margin: 0; font-size: 24px; font-weight: 800; letter-spacing: -0.5px; }
    .header p { margin: 6px 0 0; font-size: 14px; opacity: 0.92; }
    .badge { display: inline-block; background: rgba(255, 255, 255, 0.2); padding: 4px 12px; border-radius: 999px; font-size: 12px; font-weight: 600; margin-top: 10px; }
    .content { padding: 30px; }
    .lead-card { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 20px; margin-bottom: 24px; }
    .row { display: flex; margin-bottom: 14px; border-bottom: 1px dashed #E2E8F0; padding-bottom: 12px; }
    .row:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
    .label { width: 38%; font-size: 13px; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 0.5px; }
    .value { width: 62%; font-size: 15px; font-weight: 600; color: #0F172A; word-break: break-word; }
    .value a { color: #FF5E14; text-decoration: none; font-weight: 700; }
    .notes-box { background: #FFF7ED; border-left: 4px solid #FF5E14; padding: 16px; border-radius: 6px; font-size: 14px; line-height: 1.6; color: #9A3412; margin-top: 18px; }
    .actions { text-align: center; padding: 10px 0 20px; }
    .btn { display: inline-block; padding: 12px 22px; font-size: 14px; font-weight: 700; border-radius: 8px; text-decoration: none; margin: 4px 6px; }
    .btn-wa { background: #25D366; color: #FFFFFF !important; }
    .btn-call { background: #FF5E14; color: #FFFFFF !important; }
    .btn-reply { background: #0F172A; color: #FFFFFF !important; }
    .footer { background: #0F172A; color: #94A3B8; text-align: center; padding: 20px; font-size: 12px; }
    .footer a { color: #FF5E14; text-decoration: none; }
  </style>
</head>
<body>
  <div class="email-container">
    <div class="header">
      <h1>New Customer Inquiry</h1>
      <p>Direct lead submitted through Hetxa website</p>
      <span class="badge">Source: ' . htmlspecialchars($source) . '</span>
    </div>
    <div class="content">
      <div class="lead-card">
        <table width="100%" cellpadding="6" cellspacing="0" border="0">
          <tr>
            <td class="label" style="width:35%; font-weight:bold; color:#64748B;">👤 Client Name:</td>
            <td class="value" style="font-weight:bold; color:#0F172A;">' . htmlspecialchars($name) . '</td>
          </tr>
          <tr>
            <td class="label" style="font-weight:bold; color:#64748B;">📞 Contact Phone:</td>
            <td class="value"><a href="tel:' . htmlspecialchars($phone) . '" style="color:#FF5E14; font-weight:bold;">' . htmlspecialchars($phone) . '</a></td>
          </tr>
          <tr>
            <td class="label" style="font-weight:bold; color:#64748B;">✉️ Email Address:</td>
            <td class="value"><a href="mailto:' . htmlspecialchars($email) . '" style="color:#FF5E14;">' . htmlspecialchars($email) . '</a></td>
          </tr>
          <tr>
            <td class="label" style="font-weight:bold; color:#64748B;">🏢 Company / Business:</td>
            <td class="value" style="font-weight:bold;">' . htmlspecialchars($company) . '</td>
          </tr>
          <tr>
            <td class="label" style="font-weight:bold; color:#64748B;">💼 Solution Required:</td>
            <td class="value" style="color:#D84305; font-weight:bold;">' . htmlspecialchars($solution) . '</td>
          </tr>';

if ($branches !== 'Not specified') {
    $htmlBody .= '<tr>
            <td class="label" style="font-weight:bold; color:#64748B;">🏪 Outlets / Branches:</td>
            <td class="value">' . htmlspecialchars($branches) . '</td>
          </tr>';
}

if ($budget !== 'Not specified') {
    $htmlBody .= '<tr>
            <td class="label" style="font-weight:bold; color:#64748B;">💰 Expected Budget:</td>
            <td class="value">' . htmlspecialchars($budget) . '</td>
          </tr>';
}

if ($timeline !== 'Not specified') {
    $htmlBody .= '<tr>
            <td class="label" style="font-weight:bold; color:#64748B;">⏱️ Implementation:</td>
            <td class="value">' . htmlspecialchars($timeline) . '</td>
          </tr>';
}

$htmlBody .= '<tr>
            <td class="label" style="font-weight:bold; color:#64748B;">📅 Submission Time:</td>
            <td class="value">' . date('M j, Y - g:i A (T)') . '</td>
          </tr>
        </table>';

if (!empty($message)) {
    $htmlBody .= '<div class="notes-box">
          <strong>📝 Project Notes / Client Requirements:</strong><br>
          ' . nl2br(htmlspecialchars($message)) . '
        </div>';
}

$htmlBody .= '</div>
      <div class="actions">
        <a href="https://wa.me/' . urlencode($waPhone) . '" class="btn btn-wa" style="background:#25D366; color:#ffffff; padding:10px 18px; border-radius:6px; text-decoration:none; font-weight:bold; display:inline-block; margin:4px;">💬 Chat on WhatsApp</a>
        <a href="tel:' . urlencode($phone) . '" class="btn btn-call" style="background:#FF5E14; color:#ffffff; padding:10px 18px; border-radius:6px; text-decoration:none; font-weight:bold; display:inline-block; margin:4px;">📞 Call Client</a>
        <a href="mailto:' . htmlspecialchars($email) . '?subject=' . urlencode('Hetxa ERP Inquiry Follow-up - ' . $name) . '" class="btn btn-reply" style="background:#0F172A; color:#ffffff; padding:10px 18px; border-radius:6px; text-decoration:none; font-weight:bold; display:inline-block; margin:4px;">✉️ Reply by Email</a>
      </div>
    </div>
    <div class="footer">
      This notification was automatically sent by the Hetxa BOS website lead capture engine.<br>
      BeesPoint (Pvt) Ltd • 140/1, Moratuwa Road, Piliyandala. • <a href="https://www.beespoint.com">www.beespoint.com</a>
    </div>
  </div>
</body>
</html>';

// 7. SEND EMAIL HELPER (AUTHENTICATED SMTP via PHPMailer OR Native PHP mail())
function send_hetxa_mail($to, $subject, $htmlBody, $altBody, $options = [], &$errorOut = null) {
    $toName       = $options['toName'] ?? '';
    $cc           = $options['cc'] ?? '';
    $replyToEmail = $options['replyToEmail'] ?? '';
    $replyToName  = $options['replyToName'] ?? '';

    if (defined('USE_SMTP') && USE_SMTP === true && file_exists(__DIR__ . '/includes/phpmailer/PHPMailer.php')) {
        require_once __DIR__ . '/includes/phpmailer/Exception.php';
        require_once __DIR__ . '/includes/phpmailer/PHPMailer.php';
        require_once __DIR__ . '/includes/phpmailer/SMTP.php';

        try {
            $mail = new PHPMailer\PHPMailer\PHPMailer(true);
            $mail->isSMTP();
            $mail->Host       = SMTP_HOST;
            $mail->SMTPAuth   = true;
            $mail->Username   = SMTP_USER;
            $mail->Password   = SMTP_PASS;
            $mail->SMTPSecure = (strtolower(SMTP_SECURE) === 'ssl')
                ? PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_SMTPS
                : PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
            $mail->Port       = (int)SMTP_PORT;
            $mail->CharSet    = 'UTF-8';
            $mail->Timeout    = 10; // Avoid blocking UI if remote SMTP server times out

            // Sender & Recipients
            $mail->setFrom(SENDER_EMAIL, SENDER_NAME);
            $mail->addAddress($to, $toName);
            if (!empty($cc) && $cc !== $to) {
                $mail->addCC($cc);
            }
            if (!empty($replyToEmail)) {
                $mail->addReplyTo($replyToEmail, $replyToName);
            }

            // Content
            $mail->isHTML(true);
            $mail->Subject = $subject;
            $mail->Body    = $htmlBody;
            $mail->AltBody = $altBody;

            $mail->send();
            return true;
        } catch (\Exception $e) {
            $errorOut = $e->getMessage();
            error_log('Hetxa Mailer SMTP Error (' . $to . '): ' . $errorOut);
        }
    }

    // Native PHP mail() fallback
    $headers = [];
    $headers[] = 'MIME-Version: 1.0';
    $headers[] = 'Content-type: text/html; charset=UTF-8';
    $headers[] = 'From: ' . SENDER_NAME . ' <' . SENDER_EMAIL . '>';
    if (!empty($replyToEmail)) {
        $replyHeader = !empty($replyToName) ? ($replyToName . ' <' . $replyToEmail . '>') : $replyToEmail;
        $headers[] = 'Reply-To: ' . $replyHeader;
    }
    if (!empty($cc) && $cc !== $to) {
        $headers[] = 'Cc: ' . $cc;
    }
    $headers[] = 'X-Mailer: PHP/' . phpversion();
    return @mail($to, $subject, $htmlBody, implode("\r\n", $headers));
}

// Send Lead Notification to Admin
$mailError = null;
$adminAltBody = "New Hetxa ERP Lead: $name | Company: $company | Phone: $phone | Email: $email | Solution: $solution | Notes: $message";
$adminCc = (defined('BACKUP_EMAIL') && !empty(BACKUP_EMAIL) && BACKUP_EMAIL !== ADMIN_EMAIL) ? BACKUP_EMAIL : '';
$mailSent = send_hetxa_mail(
    ADMIN_EMAIL,
    $emailSubject,
    $htmlBody,
    $adminAltBody,
    [
        'cc'           => $adminCc,
        'replyToEmail' => $email,
        'replyToName'  => $name,
    ],
    $mailError
);

// 8. SEND THANK-YOU CONFIRMATION EMAIL TO THE USER
$userSubject = "Thank you for contacting Hetxa BOS - We received your inquiry";
$userHtmlBody = '<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>' . htmlspecialchars($userSubject) . '</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #F8FAFC; margin: 0; padding: 20px; color: #1E293B; }
    .email-container { max-width: 620px; margin: 0 auto; background: #FFFFFF; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08); border: 1px solid #E2E8F0; }
    .header { background: linear-gradient(135deg, #FF5E14 0%, #D84305 100%); padding: 32px 30px; text-align: center; color: #FFFFFF; }
    .header h1 { margin: 0; font-size: 24px; font-weight: 800; letter-spacing: -0.5px; }
    .header p { margin: 6px 0 0; font-size: 14px; opacity: 0.92; }
    .content { padding: 30px; font-size: 15px; line-height: 1.65; color: #334155; }
    .summary-card { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 18px 20px; margin: 20px 0; }
    .actions { text-align: center; padding: 10px 0 16px; }
    .footer { background: #0F172A; color: #94A3B8; text-align: center; padding: 20px; font-size: 12px; }
    .footer a { color: #FF5E14; text-decoration: none; }
  </style>
</head>
<body>
  <div class="email-container">
    <div class="header">
      <h1>Thank You, ' . htmlspecialchars($name) . '!</h1>
      <p>We have received your inquiry at Hetxa BOS</p>
    </div>
    <div class="content">
      <p>Hi ' . htmlspecialchars($name) . ',</p>
      <p>Thank you for reaching out to <strong>Hetxa</strong>. Your inquiry has been received by our specialist team, and we will review your requirements and get back to you within <strong>15 minutes</strong> during business hours (Mon–Fri, 9:00 AM – 5:30 PM / Sat: 9:00 AM - 2:00 PM).</p>
      <div class="summary-card">
        <div style="font-size:12px; font-weight:700; color:#64748B; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:10px;">Your Inquiry Summary</div>
        <table width="100%" cellpadding="5" cellspacing="0" border="0" style="font-size:14px;">
          <tr>
            <td style="width:38%; color:#64748B; font-weight:bold;">Solution:</td>
            <td style="color:#0F172A; font-weight:bold;">' . htmlspecialchars($solution) . '</td>
          </tr>';

if ($company !== 'Not specified') {
    $userHtmlBody .= '<tr>
            <td style="color:#64748B; font-weight:bold;">Company:</td>
            <td style="color:#0F172A;">' . htmlspecialchars($company) . '</td>
          </tr>';
}

if ($branches !== 'Not specified') {
    $userHtmlBody .= '<tr>
            <td style="color:#64748B; font-weight:bold;">Outlets / Branches:</td>
            <td style="color:#0F172A;">' . htmlspecialchars($branches) . '</td>
          </tr>';
}

if (!empty($message)) {
    $userHtmlBody .= '<tr>
            <td style="color:#64748B; font-weight:bold; vertical-align:top;">Message:</td>
            <td style="color:#0F172A;">' . nl2br(htmlspecialchars($message)) . '</td>
          </tr>';
}

$userHtmlBody .= '</table>
      </div>
      <p>Need immediate assistance? You can connect with our team right away:</p>
      <div class="actions">
        <a href="https://wa.me/' . urlencode(WHATSAPP_HOTLINE) . '" style="background:#25D366; color:#ffffff; padding:11px 20px; border-radius:8px; text-decoration:none; font-weight:bold; display:inline-block; margin:4px;">💬 WhatsApp (077 434 1227)</a>
        <a href="tel:+94774341227" style="background:#FF5E14; color:#ffffff; padding:11px 20px; border-radius:8px; text-decoration:none; font-weight:bold; display:inline-block; margin:4px;">📞 Call Sales (077 434 1227)</a>
      </div>
      <div class="summary-card" style="margin-top:16px; font-size:13px; line-height:1.8;">
        <div style="font-size:12px; font-weight:700; color:#64748B; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:8px;">Direct Contact Directory</div>
        📞 <strong>Sales:</strong> <a href="tel:+94774341227" style="color:#FF5E14; text-decoration:none;">077 434 1227</a> (WhatsApp)<br>
        📞 <strong>Sales &amp; Inquiries:</strong> <a href="tel:+94741588728" style="color:#FF5E14; text-decoration:none;">074 158 8728</a><br>
        🛠️ <strong>Support:</strong> <a href="tel:+94767170522" style="color:#FF5E14; text-decoration:none;">076 717 0522</a><br>
        ☎️ <strong>Main Office:</strong> <a href="tel:+94112617664" style="color:#FF5E14; text-decoration:none;">0112 617 664</a><br>
        👤 <strong>CEO Direct:</strong> <a href="tel:+94702115937" style="color:#0F172A; text-decoration:none;">070 211 5937</a> <span style="color:#64748B;">(Important matters only)</span><br>
        🌐 <strong>Website:</strong> <a href="https://www.beespoint.com" style="color:#FF5E14; text-decoration:none;">www.beespoint.com</a><br>
        📍 <strong>Address:</strong> 140/1, Moratuwa Road, Piliyandala.
      </div>
      <p style="margin-bottom:0;">Best regards,<br><strong>The Hetxa BOS Team</strong><br><span style="font-size:13px; color:#64748B;">hello@hetxa.com • www.beespoint.com</span></p>
    </div>
    <div class="footer">
      140/1, Moratuwa Road, Piliyandala.<br>
      <a href="https://www.beespoint.com">www.beespoint.com</a>
    </div>
  </div>
</body>
</html>';

$userAltBody = "Hi $name,\n\nThank you for contacting Hetxa BOS. We have received your inquiry regarding $solution and our team will reach out within 15 minutes during business hours.\n\nDirect Contacts:\nSales (WhatsApp): 077 434 1227\nSales & Inquiries: 074 158 8728\nSupport: 076 717 0522\nMain Office: 0112 617 664\nCEO Direct: 070 211 5937 (Important matters only)\nWebsite: www.beespoint.com\nAddress: 140/1, Moratuwa Road, Piliyandala.\n\nBest regards,\nHetxa BOS Team | hello@hetxa.com";
$userMailError = null;
$userMailSent = send_hetxa_mail(
    $email,
    $userSubject,
    $userHtmlBody,
    $userAltBody,
    [
        'toName'       => $name,
        'replyToEmail' => ADMIN_EMAIL,
        'replyToName'  => 'Hetxa BOS Team',
    ],
    $userMailError
);

// 9. RETURN JSON RESPONSE
echo json_encode([
    'status'         => 'success',
    'message'        => 'Thank you! Your inquiry has been successfully sent to the Hetxa team. We will review your requirements and reach out within 15 minutes.',
    'mail_sent'      => $mailSent,
    'user_mail_sent' => $userMailSent,
    'wa_url'         => 'https://wa.me/' . WHATSAPP_HOTLINE . '?text=' . urlencode(
        "Hi Hetxa, I just submitted an inquiry on your website.\n*Name:* $name\n*Company:* $company\n*Solution:* $solution"
    )
]);
exit;

