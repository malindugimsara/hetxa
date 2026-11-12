<!doctype html>
<html class="no-js" lang="en">

<head>
  <meta charset="utf-8">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- Primary Meta Tags -->
  <title>Administration, User Roles &amp; Multi-Branch Settings Module | Hetxa BOS</title>
  <meta name="title" content="Administration, User Roles &amp; Multi-Branch Settings Module | Hetxa BOS">
  <meta name="description"
    content="Centralized enterprise administration with Hetxa BOS: Master Contacts, User Management &amp; RBAC permissions, Multi-Branch Business Locations, Payment Accounts, RAMIS Taxes, and Custom Document Templates.">
  <meta name="keywords"
    content="Enterprise ERP Administration Sri Lanka, Role Based Access Control Colombo, Multi-Branch Management Software, ERP Audit Trail, RAMIS Tax Settings, Barcode Settings ERP">
  <meta name="author" content="Hetxa (Pvt) Ltd">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <link rel="canonical" href="https://hetxa.com/module-admin.php">

  <!-- Geo Targeting for Sri Lanka -->
  <meta name="geo.region" content="LK">
  <meta name="geo.placename" content="Piliyandala, Colombo, Sri Lanka">
  <meta name="geo.position" content="6.8018;79.9227">
  <meta name="ICBM" content="6.8018, 79.9227">

  <!-- Open Graph / Facebook / WhatsApp -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="en_LK">
  <meta property="og:url" content="https://hetxa.com/module-admin.php">
  <meta property="og:site_name" content="Hetxa BOS">
  <meta property="og:title" content="Administration &amp; System Settings Module - Hetxa BOS">
  <meta property="og:description"
    content="Granular role permissions, tamper-evident audit logs, multi-branch business locations, payment accounts, and automated IRD RAMIS tax configurations.">
  <meta property="og:image" content="https://hetxa.com/assets/images/modules/admin.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="https://hetxa.com/module-admin.php">
  <meta name="twitter:title" content="Administration &amp; System Settings Module - Hetxa BOS">
  <meta name="twitter:description"
    content="Granular role permissions, tamper-evident audit logs, multi-branch business locations, payment accounts, and automated IRD RAMIS tax configurations.">
  <meta name="twitter:image" content="https://hetxa.com/assets/images/modules/admin.png">

  <!-- Mobile & Theme -->
  <meta name="theme-color" content="#FF5E14">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

  <!-- Favicon & Brand Icons -->
  <link rel="shortcut icon" type="image/x-icon" href="favicon.ico?v=<?php echo time(); ?>">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/images/fav.png?v=<?php echo time(); ?>">
  <link rel="icon" type="image/png" sizes="192x192" href="assets/images/logos/hetxa-favicon.png?v=<?php echo time(); ?>">
  <link rel="apple-touch-icon" sizes="180x180" href="assets/images/apple-touch-icon.png?v=<?php echo time(); ?>">

  <!-- JSON-LD Structured Data Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Product",
        "@id": "https://hetxa.com/module-admin.php#product",
        "name": "Hetxa BOS - Administration & Security Governance Module",
        "description": "Enterprise administration module providing master contact directories, granular role-based permissions, multi-branch business locations, payment accounts, and IRD RAMIS tax compliance.",
        "brand": {
          "@type": "Brand",
          "name": "Hetxa"
        },
        "category": "ERP Security & Administration Software",
        "image": "https://hetxa.com/assets/images/modules/admin.png",
        "offers": {
          "@type": "Offer",
          "priceCurrency": "LKR",
          "price": "Custom Enterprise",
          "availability": "https://schema.org/InStock",
          "url": "https://hetxa.com/module-admin.php"
        }
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://hetxa.com/"
          },
          {
            "@type": "ListItem",
            "position": 2,
            "name": "Modules",
            "item": "https://hetxa.com/index.php#modules"
          },
          {
            "@type": "ListItem",
            "position": 3,
            "name": "Administration & Security",
            "item": "https://hetxa.com/module-admin.php"
          }
        ]
      }
    ]
  }
  </script>

  <!-- CSS here -->
  <link rel="stylesheet" href="assets/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/css/font-awesome-pro.min.css">
  <link rel="stylesheet" href="assets/css/animate.min.css">
  <link rel="stylesheet" href="assets/css/bexon-icons.css">
  <link rel="stylesheet" href="assets/css/nice-select.css">
  <link rel="stylesheet" href="assets/css/swiper.min.css">
  <link rel="stylesheet" href="assets/css/venobox.min.css">
  <link rel="stylesheet" href="assets/css/odometer-theme-default.css">
  <link rel="stylesheet" href="assets/css/meanmenu.css">
  <link rel="stylesheet" href="assets/css/main.css?v=<?php echo time(); ?>">
  <link rel="stylesheet" href="assets/css/hetxa-custom.css?v=<?php echo time(); ?>">
</head>

<body>
  <div class="body-overlay"></div>

  <!-- back to top start -->
  <div id="tj-back-to-top"><span id="tj-back-to-top-percentage"></span></div>
  <!-- back to top end -->

  <!-- start: magic cursor -->
  <div id="magic-cursor">
    <div id="ball"></div>
  </div>
  <!-- end: magic cursor -->

  <!-- start: Search Popup -->
  <div class="search-popup-overlay"></div>
  <!-- end: Search Popup -->

  <?php include 'navbar.php'; ?>

  <div id="smooth-wrapper">
    <div id="smooth-content">
      <main id="primary" class="site-main">

        <!-- ===================================================================
             1. BREADCRUMB / HERO SECTION (SPLIT 2-COLUMN SHOWCASE)
             =================================================================== -->
        <section class="mod-admin-hero">
          <div class="container">
            <div class="row align-items-center g-5">
              <!-- Left Column: Copy & Actions -->
              <div class="col-12 col-lg-6">
                <!-- Module Badge -->
                <div class="mod-badge-pill wow fadeInUp" data-wow-delay=".2s">
                  <i class="fa-solid fa-user-shield text-orange"></i> Module 09: Administration &amp; Governance
                </div>

                <!-- Title -->
                <h1 class="mod-hero-title wow fadeInUp" data-wow-delay=".25s">
                  Enterprise Administration, User Roles &amp; <span class="text-orange">System Governance.</span>
                </h1>

                <!-- Description -->
                <p class="mod-hero-desc wow fadeInUp" data-wow-delay=".3s">
                  Take centralized control of your organization. Manage master <strong>Contacts</strong>, define precise <strong>User Roles &amp; Permissions</strong>, and configure enterprise <strong>Settings</strong> across multi-branch locations, payment accounts, IRD RAMIS taxes, and invoice templates.
                </p>

                <!-- Hero Action Buttons -->
                <div class="mod-hero-actions wow fadeInUp" data-wow-delay=".35s">
                  <a class="tj-primary-btn" href="contact.php">
                    <span class="btn-text"><span>Request Live Demo</span></span>
                    <span class="btn-icon"><i class="tji-arrow-right-long"></i></span>
                  </a>
                  <a href="https://wa.me/94741588728?text=Hi%20Hetxa,%20I'd%20like%20to%20chat%20about%20the%20Administration%20Module." target="_blank" class="btn-hero-whatsapp">
                    <i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp
                  </a>
                </div>
              </div>

              <!-- Right Column: 3D Administration Showcase -->
              <div class="col-12 col-lg-6">
                <div class="sales-hero-visual-wrap wow fadeInRight" data-wow-delay=".3s">
                  <div class="sales-hero-glow-bg"></div>

                  <!-- Floating HUD Chip 1 (Top Right) -->
                  <div class="sales-hud-chip chip-top-right">
                    <div class="chip-icon" style="background: rgba(255, 94, 20, 0.12); color: #FF5E14;">
                      <i class="fa-solid fa-users-gear"></i>
                    </div>
                    <div class="chip-info">
                      <span class="chip-label">User Management</span>
                      <span class="chip-val">Granular RBAC Permissions</span>
                    </div>
                  </div>

                  <!-- 3D Admin Graphic Image -->
                  <div class="sales-hero-img-box">
                    <img src="assets/images/modules/admin.png" alt="Hetxa Enterprise Administration, User Management & System Settings" loading="eager" decoding="async">
                  </div>

                  <!-- Floating HUD Chip 2 (Bottom Left) -->
                  <div class="sales-hud-chip chip-bottom-left">
                    <div class="chip-icon" style="background: rgba(34, 197, 94, 0.14); color: #16a34a;">
                      <i class="fa-solid fa-location-dot"></i>
                    </div>
                    <div class="chip-info">
                      <span class="chip-label">Organization</span>
                      <span class="chip-val">Multi-Branch Locations</span>
                    </div>
                  </div>

                  <!-- Floating HUD Chip 3 (Bottom Right) -->
                  <div class="sales-hud-chip chip-bottom-right">
                    <div class="chip-icon" style="background: rgba(14, 165, 233, 0.14); color: #0284c7;">
                      <i class="fa-solid fa-sliders"></i>
                    </div>
                    <div class="chip-info">
                      <span class="chip-label">System Settings</span>
                      <span class="chip-val">Tax &amp; Invoice Document Rules</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ===================================================================
             2. TRACTION & PERFORMANCE METRICS STRIP
             =================================================================== -->
        <section class="mod-metrics-bar">
          <div class="container">
            <div class="row g-4">
              
              <div class="col-6 col-lg-3">
                <div class="mod-metric-card wow fadeInUp" data-wow-delay=".2s">
                  <div class="stat-val">100%</div>
                  <div class="stat-title">Granular RBAC Control</div>
                  <p class="stat-desc">Precise action-level permissions for view, create, edit, delete, and invoice approvals.</p>
                </div>
              </div>

              <div class="col-6 col-lg-3">
                <div class="mod-metric-card wow fadeInUp" data-wow-delay=".3s">
                  <div class="stat-val">Unlimited</div>
                  <div class="stat-title">Business Locations</div>
                  <p class="stat-desc">Connect retail outlets, central warehouses, and distribution depots in one network.</p>
                </div>
              </div>

              <div class="col-6 col-lg-3">
                <div class="mod-metric-card wow fadeInUp" data-wow-delay=".4s">
                  <div class="stat-val">100%</div>
                  <div class="stat-title">RAMIS Tax Compliance</div>
                  <p class="stat-desc">Built-in Sri Lanka VAT 18%, SSCL 2.5%, and WHT tax ledger mappings.</p>
                </div>
              </div>

              <div class="col-6 col-lg-3">
                <div class="mod-metric-card wow fadeInUp" data-wow-delay=".5s">
                  <div class="stat-val">24/7</div>
                  <div class="stat-title">Audit Trail &amp; 2FA</div>
                  <p class="stat-desc">Immutable audit logs record every price change, discount override, and system login.</p>
                </div>
              </div>

            </div>
          </div>
        </section>

        <!-- ===================================================================
             3. CORE ARCHITECTURE SECTION (CONTACTS, USER MGMT & SETTINGS)
             =================================================================== -->
        <section class="mod-section-alt mod-core-arch-section">
          <!-- Architectural Background Decorative Elements -->
          <div class="core-arch-bg-decor" aria-hidden="true">
            <div class="arch-orb arch-orb-top"></div>
            <div class="arch-orb arch-orb-sell"></div>
            <div class="arch-orb arch-orb-pos"></div>
            <div class="arch-grid-matrix"></div>
            
            <!-- Blueprint Technical Reticle (Top Right) -->
            <div class="arch-geo-shape shape-top-right">
              <svg width="420" height="420" viewBox="0 0 420 420" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="210" cy="210" r="190" stroke="#FF5E14" stroke-width="1.2" stroke-dasharray="5 7" opacity="0.22" />
                <circle cx="210" cy="210" r="145" stroke="#CBD5E1" stroke-width="1" opacity="0.4" />
                <circle cx="210" cy="210" r="100" stroke="#FF5E14" stroke-width="1.5" stroke-dasharray="3 5" opacity="0.3" />
                <circle cx="210" cy="210" r="50" stroke="#CBD5E1" stroke-width="1" opacity="0.45" />
                <line x1="210" y1="0" x2="210" y2="420" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="4 4" opacity="0.3" />
                <line x1="0" y1="210" x2="420" y2="210" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="4 4" opacity="0.3" />
                <circle cx="210" cy="20" r="3.5" fill="#FF5E14" opacity="0.5" />
                <circle cx="210" cy="400" r="3.5" fill="#FF5E14" opacity="0.5" />
                <circle cx="20" cy="210" r="3.5" fill="#FF5E14" opacity="0.5" />
                <circle cx="400" cy="210" r="3.5" fill="#FF5E14" opacity="0.5" />
              </svg>
            </div>

            <!-- Blueprint Technical Schematic Node (Bottom Left) -->
            <div class="arch-geo-shape shape-bottom-left">
              <svg width="360" height="360" viewBox="0 0 360 360" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="25" y="25" width="310" height="310" rx="24" stroke="#10B981" stroke-width="1.2" stroke-dasharray="6 6" opacity="0.22" />
                <rect x="65" y="65" width="230" height="230" rx="16" stroke="#CBD5E1" stroke-width="1" opacity="0.35" />
                <circle cx="180" cy="180" r="75" stroke="#10B981" stroke-width="1.5" opacity="0.28" />
                <circle cx="180" cy="180" r="8" fill="#10B981" opacity="0.45" />
                <line x1="180" y1="25" x2="180" y2="335" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="4 4" opacity="0.25" />
                <line x1="25" y1="180" x2="335" y2="180" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="4 4" opacity="0.25" />
              </svg>
            </div>

            <!-- Faint Architectural Blueprint Grid Lines / Nodes in Center -->
            <div class="arch-center-line"></div>
          </div>

          <div class="container">
            <div class="row justify-content-center mb-5">
              <div class="col-12 col-lg-8 text-center">
                <div class="sec-heading style-3">
                  <span class="sub-title wow fadeInUp space" data-wow-delay=".2s">
                    <i class="tji-box"></i> CORE ARCHITECTURE
                  </span>
                  <h2 class="sec-title wow fadeInUp" data-wow-delay=".3s">
                    Centralized Governance, Secure Access &amp; <span class="text-orange">System Settings</span>
                  </h2>
                  <p class="sec-desc wow fadeInUp" data-wow-delay=".4s" style="color: #64748B; max-width: 720px; margin: 15px auto 0;">
                    From master customer and supplier registries to role-based user permissions, multi-branch business locations, and financial configurations.
                  </p>
                </div>
              </div>
            </div>

            <!-- ==========================================
                 ENGINE 1: ACCESS & ENTITY GOVERNANCE (CONTACTS & USERS)
                 ========================================== -->
            <div class="submod-pillar-header wow fadeInUp" data-wow-delay=".2s">
              <div class="submod-pillar-badge sell-badge">
                <i class="fa-solid fa-users-gear"></i> <span>ACCESS &amp; ENTITIES &bull; Contacts &amp; User Management</span>
              </div>
              <span class="submod-pillar-note"><i class="fa-solid fa-check text-orange"></i> Master Registries &amp; Role-Based Access Control</span>
            </div>

            <div class="row g-4 mb-5">
              
              <!-- Sub-Module 01: Contacts -->
              <div class="col-12 col-md-6">
                <div class="submod-card wow fadeInLeft" data-wow-delay=".15s">
                  <div class="submod-icon">
                    <i class="fa-solid fa-address-book"></i>
                  </div>
                  <span class="submod-num">ADMIN &bull; SUITE 01</span>
                  <h4 class="submod-title">Contacts (Customers &amp; Suppliers)</h4>
                  <p class="submod-desc">
                    Centralize customer, supplier, wholesale buyer, and vendor profiles with credit limits, payment terms, KYC documents, and ledgers.
                  </p>
                  <ul class="submod-features">
                    <li><i class="fa-solid fa-check"></i> <strong>Unified Master Directory:</strong> Both customers and suppliers in one searchable database.</li>
                    <li><i class="fa-solid fa-check"></i> <strong>Credit Ceilings &amp; Terms:</strong> Enforce strict credit limits and payment windows automatically.</li>
                    <li><i class="fa-solid fa-check"></i> <strong>Tax Numbers &amp; KYC:</strong> Store RAMIS TIN/VAT numbers and business registration files.</li>
                  </ul>
                </div>
              </div>

              <!-- Sub-Module 02: User Management -->
              <div class="col-12 col-md-6">
                <div class="submod-card wow fadeInLeft" data-wow-delay=".3s">
                  <div class="submod-icon">
                    <i class="fa-solid fa-user-lock"></i>
                  </div>
                  <span class="submod-num">ADMIN &bull; SUITE 02</span>
                  <h4 class="submod-title">User Management &amp; Permissions</h4>
                  <p class="submod-desc">
                    Define custom roles (Admin, Cashier, Auditor, Inventory Officer) with granular permissions across all modules and action buttons.
                  </p>
                  <ul class="submod-features">
                    <li><i class="fa-solid fa-check"></i> <strong>Granular Role Matrix:</strong> 100+ toggles for view, add, edit, delete, export &amp; print.</li>
                    <li><i class="fa-solid fa-check"></i> <strong>Branch &amp; Terminal Locks:</strong> Restrict cashiers and managers strictly to assigned outlets.</li>
                    <li><i class="fa-solid fa-check"></i> <strong>Two-Factor Auth (2FA):</strong> Require OTP verification for high-privilege executive logins.</li>
                  </ul>
                </div>
              </div>

            </div>

            <!-- ==========================================
                 ENGINE 2: ENTERPRISE SETTINGS & CONFIGURATIONS
                 ========================================== -->
            <div class="submod-pillar-header wow fadeInUp" data-wow-delay=".2s">
              <div class="submod-pillar-badge pos-badge">
                <i class="fa-solid fa-gear"></i> <span>SETTINGS ENGINE &bull; System, Org, Finance &amp; Documents</span>
              </div>
              <span class="submod-pillar-note"><i class="fa-solid fa-check text-green" style="color:#10b981;"></i> Complete Enterprise Configuration</span>
            </div>

            <div class="row g-4">
              
              <!-- Sub-Module 03: System Settings -->
              <div class="col-12 col-md-6 col-lg-3">
                <div class="submod-card wow fadeInLeft" data-wow-delay=".15s">
                  <div class="submod-icon">
                    <i class="fa-solid fa-sliders"></i>
                  </div>
                  <span class="submod-num">SETTINGS &bull; SYSTEM</span>
                  <h4 class="submod-title">General, SMS &amp; Email</h4>
                  <p class="submod-desc">
                    Configure company branding, fiscal calendar, base currency, timezones, and SMS/WhatsApp notification gateways.
                  </p>
                  <ul class="submod-features">
                    <li><i class="fa-solid fa-check"></i> Currency &amp; fiscal year rules</li>
                    <li><i class="fa-solid fa-check"></i> SMS &amp; WhatsApp cloud gateways</li>
                    <li><i class="fa-solid fa-check"></i> Automated email digest delivery</li>
                  </ul>
                </div>
              </div>

              <!-- Sub-Module 04: Organization Settings -->
              <div class="col-12 col-md-6 col-lg-3">
                <div class="submod-card wow fadeInLeft" data-wow-delay=".3s">
                  <div class="submod-icon">
                    <i class="fa-solid fa-building-flag"></i>
                  </div>
                  <span class="submod-num">SETTINGS &bull; ORGANIZATION</span>
                  <h4 class="submod-title">Business Locations</h4>
                  <p class="submod-desc">
                    Setup multi-branch outlets, regional hubs, and warehouses with individual invoice prefixes, tax numbers, and contact details.
                  </p>
                  <ul class="submod-features">
                    <li><i class="fa-solid fa-check"></i> Branch-specific invoice prefixes</li>
                    <li><i class="fa-solid fa-check"></i> Regional manager allocations</li>
                    <li><i class="fa-solid fa-check"></i> Inter-branch stock transfer paths</li>
                  </ul>
                </div>
              </div>

              <!-- Sub-Module 05: Finance Settings -->
              <div class="col-12 col-md-6 col-lg-3">
                <div class="submod-card wow fadeInLeft" data-wow-delay=".45s">
                  <div class="submod-icon">
                    <i class="fa-solid fa-money-check-dollar"></i>
                  </div>
                  <span class="submod-num">SETTINGS &bull; FINANCE</span>
                  <h4 class="submod-title">Payment &amp; Taxes</h4>
                  <p class="submod-desc">
                    Configure payment methods (Cash, Card, QR, Bank, Cheques), payment accounts, and Sri Lanka IRD RAMIS VAT &amp; SSCL tax rules.
                  </p>
                  <ul class="submod-features">
                    <li><i class="fa-solid fa-check"></i> EDC card terminal mappings</li>
                    <li><i class="fa-solid fa-check"></i> Bank &amp; cash drawer ledgers</li>
                    <li><i class="fa-solid fa-check"></i> RAMIS VAT 18% &amp; SSCL 2.5%</li>
                  </ul>
                </div>
              </div>

              <!-- Sub-Module 06: Document Settings -->
              <div class="col-12 col-md-6 col-lg-3">
                <div class="submod-card wow fadeInLeft" data-wow-delay=".6s">
                  <div class="submod-icon">
                    <i class="fa-solid fa-print"></i>
                  </div>
                  <span class="submod-num">SETTINGS &bull; DOCUMENTS</span>
                  <h4 class="submod-title">Invoices &amp; Barcodes</h4>
                  <p class="submod-desc">
                    Customize invoice schemes, quotation letterheads, terms &amp; conditions, and barcode label printer sticker templates.
                  </p>
                  <ul class="submod-features">
                    <li><i class="fa-solid fa-check"></i> Custom invoice numbering reset</li>
                    <li><i class="fa-solid fa-check"></i> Logo, terms &amp; footer designer</li>
                    <li><i class="fa-solid fa-check"></i> Barcode label sticker layouts</li>
                  </ul>
                </div>
              </div>

            </div>
          </div>
        </section>

        <!-- ===================================================================
             4. DEEP DIVE SHOWCASE (USER MANAGEMENT & SETTINGS)
             =================================================================== -->
        <section class="mod-section-dark">
          <div class="container">
            
            <!-- Section Heading -->
            <div class="row justify-content-center deep-dive-heading-wrap">
              <div class="col-12 col-lg-8 text-center">
                <div class="sec-heading style-3">
                  <span class="sub-title wow fadeInUp space" data-wow-delay=".2s">
                    <i class="tji-box"></i> DEEP DIVE SHOWCASE
                  </span>
                  <h2 class="sec-title wow fadeInUp" data-wow-delay=".3s">
                    Granular Access Control &amp; <span class="text-orange">Enterprise Multi-Branch Settings</span>
                  </h2>
                  <p class="sec-desc wow fadeInUp" data-wow-delay=".4s" style="max-width: 720px; margin: 15px auto 0;">
                    Explore the live administration interface in action: from configuring custom employee roles to managing multi-branch business locations and payment accounts.
                  </p>
                </div>
              </div>
            </div>

            <!-- Deep Dive Row 1: User Roles & Permissions Matrix UI -->
            <div class="row align-items-center g-5 mod-deep-dive-row">
              <div class="col-12 col-lg-6 order-2 order-lg-1">
                <div class="mod-dive-text">
                  <span class="badge-pill-sm"><i class="fa-solid fa-user-lock"></i> SECURITY GOVERNANCE &bull; RBAC MATRIX</span>
                  <h3>Granular Enterprise Roles &amp; Hierarchical Access Boundaries</h3>
                  <p>
                    Ensure each employee only accesses what is strictly required for their operational duties. Hetxa BOS allows defining custom organizational roles—from Cashiers and Store Managers to Inventory Controllers and Financial Auditors—with exhaustive permissions and branch-level boundaries.
                  </p>
                  <div class="mod-points-grid">
                    <div class="mod-point-card">
                      <div class="point-icon"><i class="fa-solid fa-user-shield"></i></div>
                      <div class="point-text">
                        <strong>Role-Based Access (RBAC)</strong>
                        <span>Control view, edit, delete, export &amp; discount permissions per user</span>
                      </div>
                    </div>
                    <div class="mod-point-card">
                      <div class="point-icon"><i class="fa-solid fa-location-crosshairs"></i></div>
                      <div class="point-text">
                        <strong>Branch-Level Restrictions</strong>
                        <span>Lock employees to specific outlets, terminals, or warehouses</span>
                      </div>
                    </div>
                    <div class="mod-point-card">
                      <div class="point-icon"><i class="fa-solid fa-key"></i></div>
                      <div class="point-text">
                        <strong>Two-Factor Authentication</strong>
                        <span>Enforce 2FA protection for all management and financial accounts</span>
                      </div>
                    </div>
                    <div class="mod-point-card">
                      <div class="point-icon"><i class="fa-solid fa-clock-rotate-left"></i></div>
                      <div class="point-text">
                        <strong>Immutable Audit Trail</strong>
                        <span>Records every login, bill edit, void, and price modification</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-12 col-lg-6 order-1 order-lg-2">
                <div class="mod-dive-img-card wow fadeInRight" data-wow-delay=".3s">
                  <div class="mod-dive-browser-bar">
                    <div class="dots">
                      <span class="dot red"></span>
                      <span class="dot yellow"></span>
                      <span class="dot green"></span>
                    </div>
                    <div class="url-pill"><i class="fa-solid fa-lock"></i> hetxa.cloud/admin/user-roles</div>
                  </div>
                  <div class="mod-dive-img-wrap">
                    <img src="assets/images/modules/admin-roles-ui.png" alt="Hetxa BOS User Roles List, Granular Role-Based Access Control (RBAC) and Security Permissions Interface">
                    <div class="mod-dive-float-tag">
                      <i class="fa-solid fa-user-lock text-orange"></i>
                      <span>Role-Based Access Control (RBAC)</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Deep Dive Row 2: General Settings & Legal Business Identity UI -->
            <div class="row align-items-center g-5 mod-deep-dive-row">
              <div class="col-12 col-lg-6">
                <div class="mod-dive-img-card wow fadeInLeft" data-wow-delay=".3s">
                  <div class="mod-dive-browser-bar">
                    <div class="dots">
                      <span class="dot red"></span>
                      <span class="dot yellow"></span>
                      <span class="dot green"></span>
                    </div>
                    <div class="url-pill"><i class="fa-solid fa-lock"></i> hetxa.cloud/admin/settings/general</div>
                  </div>
                  <div class="mod-dive-img-wrap">
                    <img src="assets/images/modules/admin-settings-ui.png" alt="Hetxa BOS General Settings, Legal Business Identity, RAMIS Tax Configuration and Dual Brand Logos">
                    <div class="mod-dive-float-tag">
                      <i class="fa-solid fa-building-flag text-green" style="color: #10b981;"></i>
                      <span>Business Identity &amp; RAMIS Tax</span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-12 col-lg-6">
                <div class="mod-dive-text">
                  <span class="badge-pill-sm"><i class="fa-solid fa-building-flag"></i> ORGANIZATION &bull; GENERAL SETTINGS</span>
                  <h3>Business Identity, Legal Compliance &amp; Multi-Theme Branding</h3>
                  <p>
                    Centralize your corporate profile across every customer touchpoint. Manage legal business names, browser workspace titles, IRD RAMIS tax identification numbers, and dual-mode high-resolution company logos for light and dark operational interfaces.
                  </p>
                  <div class="mod-points-grid">
                    <div class="mod-point-card green-accent">
                      <div class="point-icon"><i class="fa-solid fa-stamp"></i></div>
                      <div class="point-text">
                        <strong>Legal Business Identity</strong>
                        <span>Enforce unified registered company name across receipts, invoices &amp; PDFs</span>
                      </div>
                    </div>
                    <div class="mod-point-card green-accent">
                      <div class="point-icon"><i class="fa-solid fa-file-invoice-dollar"></i></div>
                      <div class="point-text">
                        <strong>RAMIS Tax Compliance</strong>
                        <span>Official IRD RAMIS TIN &amp; VAT number integration for audit verification</span>
                      </div>
                    </div>
                    <div class="mod-point-card green-accent">
                      <div class="point-icon"><i class="fa-solid fa-palette"></i></div>
                      <div class="point-text">
                        <strong>Multi-Theme Corporate Logos</strong>
                        <span>Dedicated high-res logos for light &amp; dark operational modes</span>
                      </div>
                    </div>
                    <div class="mod-point-card green-accent">
                      <div class="point-icon"><i class="fa-solid fa-window-maximize"></i></div>
                      <div class="point-text">
                        <strong>Workspace Title Prefix</strong>
                        <span>Dynamic browser tab identification for multi-window management</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Deep Dive Row 3: SMS & Email Gateways & Multi-Branch Document Automation UI -->
            <div class="row align-items-center g-5 mod-deep-dive-row">
              <div class="col-12 col-lg-6 order-2 order-lg-1">
                <div class="mod-dive-text">
                  <span class="badge-pill-sm"><i class="fa-solid fa-envelope-circle-check"></i> COMMUNICATIONS &bull; SMS &amp; EMAIL ENGINE</span>
                  <h3>Enterprise SMTP Relay &amp; Multi-Branch Document Automation</h3>
                  <p>
                    Automate transactional communications directly to customers, suppliers, and regional managers. Connect enterprise SMTP servers, configure cloud SMS gateways, and enable 1-click automatic dispatch for Invoices, Quotations, Proformas, and Purchase Orders across all active branches.
                  </p>
                  <div class="mod-points-grid">
                    <div class="mod-point-card blue-accent">
                      <div class="point-icon"><i class="fa-solid fa-server"></i></div>
                      <div class="point-text">
                        <strong>Enterprise SMTP Relay</strong>
                        <span>High-deliverability outgoing email integration with TLS/SSL encryption</span>
                      </div>
                    </div>
                    <div class="mod-point-card blue-accent">
                      <div class="point-icon"><i class="fa-solid fa-paper-plane"></i></div>
                      <div class="point-text">
                        <strong>Multi-Branch Document Dispatch</strong>
                        <span>Automatic PDF email triggering on invoice generation across 100% of branches</span>
                      </div>
                    </div>
                    <div class="mod-point-card blue-accent">
                      <div class="point-icon"><i class="fa-solid fa-file-signature"></i></div>
                      <div class="point-text">
                        <strong>Quotations &amp; PO Dispatch</strong>
                        <span>Instant automated distribution of supplier POs and customer proformas</span>
                      </div>
                    </div>
                    <div class="mod-point-card blue-accent">
                      <div class="point-icon"><i class="fa-solid fa-bell"></i></div>
                      <div class="point-text">
                        <strong>Critical System Alerts</strong>
                        <span>Immediate alerts for password resets, shift closures &amp; security warnings</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-12 col-lg-6 order-1 order-lg-2">
                <div class="mod-dive-img-card wow fadeInRight" data-wow-delay=".3s">
                  <div class="mod-dive-browser-bar">
                    <div class="dots">
                      <span class="dot red"></span>
                      <span class="dot yellow"></span>
                      <span class="dot green"></span>
                    </div>
                    <div class="url-pill"><i class="fa-solid fa-lock"></i> hetxa.cloud/admin/settings/sms-email</div>
                  </div>
                  <div class="mod-dive-img-wrap">
                    <img src="assets/images/modules/admin-email-ui.png" alt="Hetxa BOS SMS and Email Server Connection, Document Email Automation and Branch Notification Settings">
                    <div class="mod-dive-float-tag">
                      <i class="fa-solid fa-paper-plane" style="color: #3b82f6;"></i>
                      <span>SMTP Relay &amp; Document Auto-Dispatch</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </section>

        <!-- ===================================================================
             5. SYSTEM GOVERNANCE & SECURITY MARQUEE
             =================================================================== -->
        <section class="mod-section-alt hw-compatibility-section">
          <div class="container">
            <div class="row justify-content-center mb-5">
              <div class="col-12 col-lg-8 text-center">
                <div class="sec-heading style-3">
                  <span class="sub-title wow fadeInUp space" data-wow-delay=".2s">
                    <i class="fa-solid fa-shield-halved text-orange" style="margin: 5px;"></i> SYSTEM GOVERNANCE &bull; SECURITY
                  </span>
                  <h2 class="sec-title wow fadeInUp" data-wow-delay=".3s">
                    Enterprise Governance &amp; <span class="text-orange">Data Protection</span>
                  </h2>
                  <p class="sec-desc wow fadeInUp" data-wow-delay=".4s" style="color: #64748B; max-width: 720px; margin: 15px auto 0;">
                    Bank-grade encryption, role-based boundary enforcement, and automatic cloud backups built for multi-branch organizations.
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- Full Width Right-to-Left Auto-Scrolling Admin Governance Marquee -->
          <div class="hw-marquee-outer">
            <div class="hw-marquee-track">
              <!-- Group 1 -->
              <div class="hw-marquee-group">
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-users-gear"></i></div>
                  <h5>Role-Based RBAC</h5>
                  <p>Granular action-level permissions per module, user, and role.</p>
                </div>
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-location-dot"></i></div>
                  <h5>Multi-Branch Locations</h5>
                  <p>Dedicated invoice prefixes, tax numbers &amp; receipt headers.</p>
                </div>
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-building-columns"></i></div>
                  <h5>RAMIS Tax Rules</h5>
                  <p>Inland Revenue VAT 18%, SSCL 2.5% &amp; WHT ledger mappings.</p>
                </div>
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-clock-rotate-left"></i></div>
                  <h5>Audit Trail Logs</h5>
                  <p>Immutable logging of bill edits, discounts, voids &amp; user logins.</p>
                </div>
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-shield-halved"></i></div>
                  <h5>Two-Factor Auth</h5>
                  <p>SMS OTP and Authenticator app protection for executive accounts.</p>
                </div>
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-credit-card"></i></div>
                  <h5>Payment Accounts</h5>
                  <p>Direct mapping of cash drawers, EDC card machines &amp; banks.</p>
                </div>
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-file-invoice"></i></div>
                  <h5>Document Schemes</h5>
                  <p>Branded invoice templates, header logos &amp; annual auto-resets.</p>
                </div>
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-cloud-arrow-up"></i></div>
                  <h5>Automated Cloud Backup</h5>
                  <p>Daily encrypted multi-region snapshots and rapid disaster recovery.</p>
                </div>
              </div>

              <!-- Group 2 (Duplicate for Seamless Infinite Loop) -->
              <div class="hw-marquee-group" aria-hidden="true">
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-users-gear"></i></div>
                  <h5>Role-Based RBAC</h5>
                  <p>Granular action-level permissions per module, user, and role.</p>
                </div>
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-location-dot"></i></div>
                  <h5>Multi-Branch Locations</h5>
                  <p>Dedicated invoice prefixes, tax numbers &amp; receipt headers.</p>
                </div>
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-building-columns"></i></div>
                  <h5>RAMIS Tax Rules</h5>
                  <p>Inland Revenue VAT 18%, SSCL 2.5% &amp; WHT ledger mappings.</p>
                </div>
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-clock-rotate-left"></i></div>
                  <h5>Audit Trail Logs</h5>
                  <p>Immutable logging of bill edits, discounts, voids &amp; user logins.</p>
                </div>
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-shield-halved"></i></div>
                  <h5>Two-Factor Auth</h5>
                  <p>SMS OTP and Authenticator app protection for executive accounts.</p>
                </div>
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-credit-card"></i></div>
                  <h5>Payment Accounts</h5>
                  <p>Direct mapping of cash drawers, EDC card machines &amp; banks.</p>
                </div>
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-file-invoice"></i></div>
                  <h5>Document Schemes</h5>
                  <p>Branded invoice templates, header logos &amp; annual auto-resets.</p>
                </div>
                <div class="hw-card">
                  <div class="hw-icon"><i class="fa-solid fa-cloud-arrow-up"></i></div>
                  <h5>Automated Cloud Backup</h5>
                  <p>Daily encrypted multi-region snapshots and rapid disaster recovery.</p>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ===================================================================
             6. EXPLORE OTHER ERP MODULES
             =================================================================== -->
        <section class="mod-section-light">
          <div class="container">
            <div class="row align-items-center mb-4">
              <div class="col-12 col-md-8">
                <div class="sec-heading style-3">
                  <span class="sub-title"><i class="tji-box"></i> SEAMLESS SUITE INTEGRATION</span>
                  <h3 class="sec-title" style="font-size: 28px;">Connect Administration With Other <span class="text-orange">Hetxa Modules</span></h3>
                </div>
              </div>
              <div class="col-12 col-md-4 text-md-end">
                <a href="index.php#modules" class="tj-primary-btn" style="padding: 9px 20px; font-size: 13px;">
                  <span class="btn-text"><span>All 9 Modules</span></span>
                  <span class="btn-icon"><i class="tji-arrow-right-long"></i></span>
                </a>
              </div>
            </div>

            <div class="other-modules-nav">
              
              <!-- Module 01: Sales & POS -->
              <a href="module-sales.php" class="mod-nav-item">
                <div class="mod-nav-icon">
                  <i class="fa-solid fa-cash-register"></i>
                </div>
                <div class="mod-nav-info">
                  <span class="name">Sales &amp; POS</span>
                  <span class="num">Module 01 &bull; Cashier Registers &amp; POS Terminals</span>
                </div>
                <div class="mod-nav-arrow"><i class="fa-solid fa-arrow-right"></i></div>
              </a>

              <!-- Module 04: Finance -->
              <a href="module-finance.php" class="mod-nav-item">
                <div class="mod-nav-icon">
                  <i class="fa-solid fa-money-check-dollar"></i>
                </div>
                <div class="mod-nav-info">
                  <span class="name">Finance &amp; Cheques</span>
                  <span class="num">Module 04 &bull; Payment Accounts &amp; Tax Ledgers</span>
                </div>
                <div class="mod-nav-arrow"><i class="fa-solid fa-arrow-right"></i></div>
              </a>

              <!-- Module 08: HR & Payroll -->
              <a href="module-hr.php" class="mod-nav-item">
                <div class="mod-nav-icon">
                  <i class="fa-solid fa-users-gear"></i>
                </div>
                <div class="mod-nav-info">
                  <span class="name">Human Resources</span>
                  <span class="num">Module 08 &bull; Employee Records &amp; Staff Roles</span>
                </div>
                <div class="mod-nav-arrow"><i class="fa-solid fa-arrow-right"></i></div>
              </a>

            </div>
          </div>
        </section>

        <!-- ===================================================================
             7. EXECUTIVE CALL TO ACTION (CTA)
             =================================================================== -->
        <section class="mod-section-light pt-10">
          <div class="container">
            <div class="mod-cta-banner wow fadeInUp" data-wow-delay=".3s">
              <h2 class="sec-title">Take Complete Control of Your Enterprise with <span class="text-orange">Hetxa Governance</span></h2>
              <p class="sec-desc">
                Schedule a consultation to see how Hetxa's centralized administration module streamlines user permissions, multi-branch locations, payment accounts, and tax settings in one secure system.
              </p>
              <div class="mod-cta-actions">
                <a href="contact.php" class="tj-primary-btn">
                  <span class="btn-text"><span>Request Live Demo</span></span>
                  <span class="btn-icon"><i class="tji-arrow-right-long"></i></span>
                </a>
                <a href="https://wa.me/94741588728?text=Hi%20Hetxa,%20I'd%20like%20to%20schedule%20a%20Live%20Demo%20of%20the%20Administration%20Module." target="_blank" class="btn-whatsapp-cta">
                  <i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp (Fast Reply)
                </a>
              </div>
            </div>
          </div>
        </section>

      </main>

      <?php include 'footer.php'; ?>
    </div>
  </div>

  <!-- JS here -->
  <script src="assets/js/jquery.min.js"></script>
  <script src="assets/js/bootstrap.bundle.min.js"></script>
  <script src="assets/js/gsap.min.js"></script>
  <script src="assets/js/gsap-scroll-to-plugin.min.js"></script>
  <script src="assets/js/gsap-scroll-trigger.min.js"></script>
  <script src="assets/js/gsap-split-text.min.js"></script>
  <script src="assets/js/jquery.nice-select.min.js"></script>
  <script src="assets/js/swiper.min.js"></script>
  <script src="assets/js/odometer.min.js"></script>
  <script src="assets/js/venobox.min.js"></script>
  <script src="assets/js/appear.min.js"></script>
  <script src="assets/js/wow.min.js"></script>
  <script src="assets/js/meanmenu.js"></script>
  <script src="assets/js/imagesloaded-pkgd.js"></script>
  <script src="assets/js/isotope.pkgd.min.js"></script>
  <script src="assets/js/magiccursor.js"></script>
  <script src="assets/js/main.js?v=<?php echo time(); ?>"></script>
</body>

</html>
