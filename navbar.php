<?php
$currentScript = basename($_SERVER['SCRIPT_NAME'] ?? $_SERVER['PHP_SELF'] ?? '');
$currentUri = $_SERVER['REQUEST_URI'] ?? '';
$isModulePage = (strpos($currentScript, 'module-') === 0);

$modulesList = [
  'sales-invoicing-erp-sri-lanka'     => ['file' => 'module-sales.php',     'num' => '01', 'name' => 'Sales & POS', 'icon' => 'fa-cash-register'],
  'crm-software-sri-lanka'           => ['file' => 'module-crm.php',       'num' => '02', 'name' => 'CRM Hub', 'icon' => 'fa-users-viewfinder'],
  'inventory-management-sri-lanka'   => ['file' => 'module-inventory.php', 'num' => '03', 'name' => 'Purchasing & Inventory', 'icon' => 'fa-boxes-stacked'],
  'finance-accounting-erp-sri-lanka' => ['file' => 'module-finance.php',   'num' => '04', 'name' => 'Finance & Cheques', 'icon' => 'fa-money-check-dollar'],
  'project-management-erp-sri-lanka' => ['file' => 'module-projects.php',  'num' => '05', 'name' => 'Projects & Tasks', 'icon' => 'fa-diagram-project'],
  'erp-reporting-analytics-sri-lanka'=> ['file' => 'module-reports.php',   'num' => '06', 'name' => 'Reports & BI', 'icon' => 'fa-chart-pie'],
  'ai-erp-software-sri-lanka'        => ['file' => 'module-ai.php',        'num' => '07', 'name' => 'Neural AI Insights', 'icon' => 'fa-brain'],
  'hrms-payroll-software-sri-lanka'  => ['file' => 'module-hr.php',        'num' => '08', 'name' => 'HR & Payroll', 'icon' => 'fa-users-gear'],
  'erp-admin-module-sri-lanka'       => ['file' => 'module-admin.php',     'num' => '09', 'name' => 'Administration & Security', 'icon' => 'fa-sliders'],
];
?>
<!-- start: Hamburger Menu -->
<div class="hamburger-area d-lg-none">
  <div class="hamburger_bg"></div>
  <div class="hamburger_wrapper">
    <div class="hamburger_inner">
      <div class="hamburger_top d-flex align-items-center justify-content-between">
        <div class="hamburger_logo">
          <a href="index.php" class="mobile_logo">
            <img src="assets/images/logos/hetxa-logo-white.png" alt="Hetxa Logo" decoding="async">
          </a>
        </div>
        <div class="hamburger_close">
          <button class="hamburger_close_btn"><i class="fa-thin fa-times"></i></button>
        </div>
      </div>
      <div class="hamburger_menu">
        <div class="mobile_menu"></div>
      </div>
      <div class="hamburger-infos">
        <h5 class="hamburger-title">Contact Info</h5>
        <div class="contact-info">
          <div class="contact-item">
            <span class="subtitle">WhatsApp Helpline</span>
            <a class="contact-link" href="https://wa.me/94774341227?text=Hi%20Hetxa,%20I'd%20like%20to%20learn%20more%20about%20Hetxa%20BOS." target="_blank"><i class="fa-brands fa-whatsapp text-success me-1"></i> +94 77 434 1227</a>
          </div>
          <div class="contact-item">
            <span class="subtitle">Sales Hotline</span>
            <a class="contact-link" href="tel:+94702115937"><i class="fa-solid fa-phone text-orange me-1"></i> +94 70 211 5937</a>
          </div>
          <div class="contact-item">
            <span class="subtitle">Email</span>
            <a class="contact-link" href="mailto:hello@hetxa.com"><i class="fa-solid fa-envelope me-1"></i> hello@hetxa.com</a>
          </div>
          <div class="contact-item">
            <span class="subtitle">Location</span>
            <span class="contact-link"><i class="fa-solid fa-location-dot text-danger me-1"></i> 140/1, Moratuwa Road, Piliyandala 10300, Sri Lanka.</span>
          </div>
        </div>
      </div>
    </div>
    <div class="hamburger-socials">
      <h5 class="hamburger-title">Follow Us</h5>
      <div class="social-links style-3">
        <ul>
          <li><a href="https://www.facebook.com/" target="_blank"><i class="fa-brands fa-facebook-f"></i></a></li>
          <li><a href="https://www.instagram.com/" target="_blank"><i class="fa-brands fa-instagram"></i></a></li>
          <li><a href="https://x.com/" target="_blank"><i class="fa-brands fa-x-twitter"></i></a></li>
          <li><a href="https://www.linkedin.com/" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a></li>
        </ul>
      </div>
    </div>
  </div>
</div>
<!-- end: Hamburger Menu -->

<!-- start: Header Area (Standard Floating) -->
<header class="header-area header-3 h10-header header-absolute section-gap-x">
  <div class="header-bottom">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12">
          <div class="header-wrapper">
            <!-- site logo -->
            <div class="site_logo">
              <a class="logo" href="index.php"><img src="assets/images/logos/hetxa-logo.png" alt="Hetxa Logo" decoding="async"></a>
            </div>

            <!-- navigation -->
            <div class="menu-area d-none d-lg-inline-flex align-items-center">
              <nav id="mobile-menu" class="mainmenu">
                <ul>
                  <li class="<?php echo ($currentScript === 'index.php' || empty($currentScript)) ? 'current-menu-ancestor' : ''; ?>"><a href="index.php">Home</a></li>
                  <li class="has-dropdown <?php echo $isModulePage ? 'current-menu-ancestor' : ''; ?>"><a href="index.php#modules">Modules</a>
                    <ul class="sub-menu modules-dropdown">
                      <?php foreach ($modulesList as $slug => $mod): 
                        $isActive = ($currentScript === $mod['file'] || strpos($currentUri, $slug) !== false);
                      ?>
                        <li class="<?php echo $isActive ? 'active current-menu-item' : ''; ?>">
                          <a href="<?php echo $slug; ?>" class="<?php echo $isActive ? 'active' : ''; ?>">
                            <i class="fa-solid <?php echo $mod['icon']; ?>"></i> 
                            <span>Module <?php echo $mod['num']; ?>: <?php echo $mod['name']; ?></span>
                            <?php if ($isActive): ?>
                              <span class="mod-current-badge"><i class="fa-solid fa-check"></i> Current</span>
                            <?php endif; ?>
                          </a>
                        </li>
                      <?php endforeach; ?>
                    </ul>
                  </li>
                  <li class="<?php echo ($currentScript === 'about.php') ? 'current-menu-ancestor' : ''; ?>"><a href="about.php">About</a></li>
                  <li class="<?php echo ($currentScript === 'contact.php') ? 'current-menu-ancestor' : ''; ?>"><a href="contact.php">Contact</a></li>
                  <li class="<?php echo ($currentScript === 'blog.php') ? 'current-menu-ancestor' : ''; ?>"><a href="blog.php">Blogs</a></li>
                </ul>
              </nav>
            </div>

            <!-- header right info -->
            <div class="header-right-item d-none d-lg-inline-flex">
              <div class="header-button">
                <a class="tj-primary-btn" href="contact.php">
                  <span class="btn-text"><span>Request Demo</span></span>
                  <span class="btn-icon"><i class="tji-arrow-right-long"></i></span>
                </a>
              </div>
            </div>

            <!-- mobile menu bar -->
            <div class="menu_bar mobile_menu_bar d-lg-none">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</header>
<!-- end: Header Area -->

<!-- start: Header Area (Sticky Cloned) -->
<header class="header-area header-3 h10-header header-duplicate header-sticky section-gap-x">
  <div class="container-fluid">
    <div class="row">
      <div class="col-12">
        <div class="header-wrapper">
          <!-- site logo -->
          <div class="site_logo">
            <a class="logo" href="index.php"><img src="assets/images/logos/hetxa-logo.png" alt="Hetxa Logo" decoding="async"></a>
          </div>

          <!-- navigation -->
          <div class="menu-area d-none d-lg-inline-flex align-items-center">
            <nav class="mainmenu">
              <ul>
                <li class="<?php echo ($currentScript === 'index.php' || empty($currentScript)) ? 'current-menu-ancestor' : ''; ?>"><a href="index.php">Home</a></li>
                <li class="has-dropdown <?php echo $isModulePage ? 'current-menu-ancestor' : ''; ?>"><a href="index.php#modules">Modules</a>
                  <ul class="sub-menu modules-dropdown">
                    <?php foreach ($modulesList as $slug => $mod): 
                      $isActive = ($currentScript === $mod['file'] || strpos($currentUri, $slug) !== false);
                    ?>
                      <li class="<?php echo $isActive ? 'active current-menu-item' : ''; ?>">
                        <a href="<?php echo $slug; ?>" class="<?php echo $isActive ? 'active' : ''; ?>">
                          <i class="fa-solid <?php echo $mod['icon']; ?>"></i> 
                          <span>Module <?php echo $mod['num']; ?>: <?php echo $mod['name']; ?></span>
                          <?php if ($isActive): ?>
                            <span class="mod-current-badge"><i class="fa-solid fa-check"></i> Current</span>
                          <?php endif; ?>
                        </a>
                      </li>
                    <?php endforeach; ?>
                  </ul>
                </li>
                <li class="<?php echo ($currentScript === 'about.php') ? 'current-menu-ancestor' : ''; ?>"><a href="about.php">About</a></li>
                <li class="<?php echo ($currentScript === 'contact.php') ? 'current-menu-ancestor' : ''; ?>"><a href="contact.php">Contact</a></li>
                <li class="<?php echo ($currentScript === 'blog.php') ? 'current-menu-ancestor' : ''; ?>"><a href="blog.php">Blogs</a></li>
              </ul>
            </nav>
          </div>

          <!-- header right info -->
          <div class="header-right-item d-none d-lg-inline-flex">
            <div class="header-button">
              <a class="tj-primary-btn" href="contact.php">
                <span class="btn-text"><span>Request Demo</span></span>
                <span class="btn-icon"><i class="tji-arrow-right-long"></i></span>
              </a>
            </div>
          </div>

          <!-- mobile menu bar -->
          <div class="menu_bar mobile_menu_bar d-lg-none">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>
      </div>
    </div>
  </div>
</header>
<!-- end: Header Area -->
