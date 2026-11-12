import os
from PIL import Image, ImageDraw, ImageFont

out_dir = r'c:/xampp/htdocs/hetxa/assets/images/modules'
os.makedirs(out_dir, exist_ok=True)

# Fonts
f_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 17)
f_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 10.5)
f_b_lg = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 15)
f_b_md = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 12)
f_b_sm = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 10)
f_b_xs = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 8.5)

f_r_md = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 11)
f_r_sm = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 9.5)
f_r_xs = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 8.5)

W, H = 1024, 520

def create_base_canvas(title, breadcrumb, btn1_text, btn2_text):
    im = Image.new('RGB', (W, H), (248, 250, 252))
    d = ImageDraw.Draw(im)
    
    # Top Bar Header
    d.rectangle([0, 0, W, 52], fill=(255, 255, 255))
    d.line([0, 52, W, 52], fill=(226, 232, 240))
    
    d.text((20, 10), title, font=f_title, fill=(15, 23, 42))
    d.text((22, 33), breadcrumb, font=f_sub, fill=(100, 116, 139))
    
    # Top action buttons
    if btn2_text:
        d.rounded_rectangle([W - 275, 12, W - 145, 40], radius=5, fill=(255, 255, 255), outline=(203, 213, 225), width=1)
        d.text((W - 263, 19), btn2_text, font=f_b_xs, fill=(51, 65, 85))
        
    if btn1_text:
        d.rounded_rectangle([W - 135, 12, W - 20, 40], radius=5, fill=(255, 94, 20))
        d.text((W - 123, 19), btn1_text, font=f_b_xs, fill=(255, 255, 255))
        
    return im, d

# ==============================================================================
# 1. USER MANAGEMENT & RBAC PERMISSIONS MOCKUP
# ==============================================================================
print('Generating admin-users-ui.png...')
im_usr, d_usr = create_base_canvas(
    'User Management & Role-Based Access Control (RBAC)',
    'Home  »  Administration  »  User Management  »  Users & Permissions',
    'Manage Roles (6)',
    '+ Add New User'
)

# Stat Cards
card_w = (W - 40 - 36) // 4
card_h = 74
top_y = 66
stats_usr = [
    ('ACTIVE USERS', '24 Staff Members', 'Across 4 Branch Outlets', (255, 94, 20)),
    ('SYSTEM ROLES', '6 Configured Roles', 'Admin, Cashier, Auditor', (37, 99, 235)),
    ('TWO-FACTOR AUTH', '100% Enforced', 'All Management Accounts', (16, 185, 129)),
    ('SECURITY AUDIT LOG', 'Tamper-Evident', 'All Actions Recorded', (15, 23, 42))
]

for i, (label, val, sub, col) in enumerate(stats_usr):
    cx = 20 + i * (card_w + 12)
    d_usr.rounded_rectangle([cx, top_y, cx + card_w, top_y + card_h], radius=7, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d_usr.rectangle([cx + 1, top_y + 1, cx + 4, top_y + card_h - 1], fill=col)
    d_usr.text((cx + 14, top_y + 10), label, font=f_b_xs, fill=(100, 116, 139))
    d_usr.text((cx + 14, top_y + 25), val, font=f_b_lg, fill=(15, 23, 42))
    d_usr.text((cx + 14, top_y + 49), sub, font=f_r_xs, fill=(100, 116, 139))

# Table Card
tbl_y = top_y + card_h + 14
tbl_h = H - tbl_y - 15
d_usr.rounded_rectangle([20, tbl_y, W - 20, tbl_y + tbl_h], radius=7, fill=(255, 255, 255), outline=(226, 232, 240), width=1)

# Filter Bar inside Table
d_usr.text((36, tbl_y + 14), 'System User Directory & Access Matrix (24 Users)', font=f_b_md, fill=(15, 23, 42))
d_usr.rounded_rectangle([W - 380, tbl_y + 10, W - 180, tbl_y + 34], radius=4, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
d_usr.text((W - 370, tbl_y + 16), 'Search User, Role or Branch...', font=f_r_xs, fill=(148, 163, 184))
d_usr.rounded_rectangle([W - 170, tbl_y + 10, W - 36, tbl_y + 34], radius=4, fill=(255, 255, 255), outline=(203, 213, 225), width=1)
d_usr.text((W - 158, tbl_y + 16), 'Role: All Roles', font=f_b_xs, fill=(71, 85, 105))

# Table Header
th_y = tbl_y + 44
d_usr.rectangle([20, th_y, W - 20, th_y + 28], fill=(241, 245, 249))
d_usr.line([20, th_y + 28, W - 20, th_y + 28], fill=(226, 232, 240))

cols_usr = [
    (36, 'USER & EMAIL'),
    (245, 'ASSIGNED ROLE'),
    (390, 'ASSIGNED BRANCH'),
    (530, 'POS TERMINAL'),
    (660, '2FA STATUS'),
    (775, 'LAST ACTIVE'),
    (910, 'ACCOUNT STATUS')
]
for x, name in cols_usr:
    d_usr.text((x, th_y + 8), name, font=f_b_xs, fill=(100, 116, 139))

rows_usr = [
    ('Dhanushka Perera', 'dhanushka@hetxa.com', 'Super Admin', 'All Locations (Central)', 'Full Override', 'Enabled (App)', 'Just Now', 'Active', (16, 185, 129)),
    ('Kavinda Silva', 'kavinda.s@hetxa.com', 'Branch Manager', 'Colombo Main Outlet', 'Terminal A, B', 'Enabled (SMS)', '12 mins ago', 'Active', (16, 185, 129)),
    ('Sachini Fernando', 'sachini@hetxa.com', 'Senior Accountant', 'Head Office Finance', 'View Only', 'Enabled (App)', '28 mins ago', 'Active', (16, 185, 129)),
    ('Mohamed Imran', 'imran.pos@hetxa.com', 'Cashier Terminal', 'Kandy Retail Outlet', 'Register K-01', 'Password Only', '1 hour ago', 'Active', (16, 185, 129)),
    ('Chathurika Jayasuriya', 'chathuri@hetxa.com', 'Inventory Officer', 'Central Warehouse', 'Restricted', 'Enabled (SMS)', '2 hours ago', 'Active', (16, 185, 129)),
    ('Ruwan Jayawardena', 'ruwan.pos@hetxa.com', 'Cashier Terminal', 'Galle Retail Branch', 'Register G-02', 'Password Only', '3 hours ago', 'Active', (16, 185, 129)),
    ('Pradeep Kumara', 'pradeep@hetxa.com', 'Wholesale Sales Rep', 'Negombo Distribution', 'Mobile App', 'Enabled (App)', 'Yesterday', 'Active', (16, 185, 129)),
]

for r_idx, (name, email, role, branch, pos, twofa, last, status, scol) in enumerate(rows_usr):
    ry = th_y + 29 + r_idx * 38
    d_usr.line([20, ry + 37, W - 20, ry + 37], fill=(241, 245, 249))
    d_usr.text((36, ry + 6), name, font=f_b_sm, fill=(15, 23, 42))
    d_usr.text((36, ry + 20), email, font=f_r_xs, fill=(148, 163, 184))
    
    # Role pill
    if 'Admin' in role:
        d_usr.rounded_rectangle([240, ry + 9, 340, ry + 27], radius=3, fill=(255, 247, 237), outline=(254, 215, 170), width=1)
        d_usr.text((246, ry + 13), role, font=f_b_xs, fill=(194, 65, 12))
    else:
        d_usr.text((245, ry + 12), role, font=f_b_sm, fill=(30, 41, 59))
        
    d_usr.text((390, ry + 12), branch, font=f_r_sm, fill=(71, 85, 105))
    d_usr.text((530, ry + 12), pos, font=f_r_sm, fill=(15, 23, 42))
    
    # 2FA
    if 'Enabled' in twofa:
        d_usr.text((660, ry + 12), '✓ ' + twofa, font=f_r_sm, fill=(16, 185, 129))
    else:
        d_usr.text((660, ry + 12), twofa, font=f_r_sm, fill=(100, 116, 139))
        
    d_usr.text((775, ry + 12), last, font=f_r_sm, fill=(100, 116, 139))
    
    # Status pill
    d_usr.rounded_rectangle([905, ry + 9, 980, ry + 27], radius=3, fill=(240, 253, 244), outline=(187, 247, 208), width=1)
    d_usr.text((923, ry + 13), status, font=f_b_xs, fill=(22, 101, 52))

im_usr.save(os.path.join(out_dir, 'admin-users-ui.png'), 'PNG')
print('Saved admin-users-ui.png')

# ==============================================================================
# 2. BUSINESS LOCATIONS & SYSTEM SETTINGS MOCKUP
# ==============================================================================
print('Generating admin-settings-ui.png...')
im_set, d_set = create_base_canvas(
    'Organization Locations, Payment Methods & Tax Settings',
    'Home  »  Administration  »  Settings  »  Business Locations & Financial Taxes',
    'Configure Taxes (VAT)',
    '+ Add Location'
)

# Stat Cards
stats_set = [
    ('BUSINESS LOCATIONS', '4 Active Branches', 'Colombo, Kandy, Galle, Negombo', (16, 185, 129)),
    ('PAYMENT METHODS', '5 Methods Active', 'Cash, Card, LankaQR, Transfer', (255, 94, 20)),
    ('RAMIS TAX RULES', 'VAT 18% & SSCL 2.5%', 'IRD Invoicing Active', (37, 99, 235)),
    ('DOC SCHEMES', 'Custom Numbering', 'Auto-Reset Annual Sequences', (15, 23, 42))
]

for i, (label, val, sub, col) in enumerate(stats_set):
    cx = 20 + i * (card_w + 12)
    d_set.rounded_rectangle([cx, top_y, cx + card_w, top_y + card_h], radius=7, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d_set.rectangle([cx + 1, top_y + 1, cx + 4, top_y + card_h - 1], fill=col)
    d_set.text((cx + 14, top_y + 10), label, font=f_b_xs, fill=(100, 116, 139))
    d_set.text((cx + 14, top_y + 25), val, font=f_b_lg, fill=(15, 23, 42))
    d_set.text((cx + 14, top_y + 49), sub, font=f_r_xs, fill=(100, 116, 139))

# Table Card
d_set.rounded_rectangle([20, tbl_y, W - 20, tbl_y + tbl_h], radius=7, fill=(255, 255, 255), outline=(226, 232, 240), width=1)

d_set.text((36, tbl_y + 14), 'Multi-Branch Business Locations & Invoice Schemes', font=f_b_md, fill=(15, 23, 42))
d_set.rounded_rectangle([W - 380, tbl_y + 10, W - 180, tbl_y + 34], radius=4, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
d_set.text((W - 370, tbl_y + 16), 'Search Location or Code...', font=f_r_xs, fill=(148, 163, 184))
d_set.rounded_rectangle([W - 170, tbl_y + 10, W - 36, tbl_y + 34], radius=4, fill=(255, 255, 255), outline=(203, 213, 225), width=1)
d_set.text((W - 158, tbl_y + 16), 'View: All Branches', font=f_b_xs, fill=(71, 85, 105))

# Table Header
d_set.rectangle([20, th_y, W - 20, th_y + 28], fill=(241, 245, 249))
d_set.line([20, th_y + 28, W - 20, th_y + 28], fill=(226, 232, 240))

cols_set = [
    (36, 'LOCATION & CODE'),
    (230, 'CITY / ADDRESS'),
    (390, 'INVOICE PREFIX'),
    (520, 'RAMIS VAT NUMBER'),
    (670, 'DEFAULT CASH ACCOUNT'),
    (815, 'POS REGISTERS'),
    (925, 'SYNC STATUS')
]
for x, name in cols_set:
    d_set.text((x, th_y + 8), name, font=f_b_xs, fill=(100, 116, 139))

rows_set = [
    ('Colombo Head Office & Store', 'LOC-01', 'Moratuwa Road, Piliyandala', 'INV-CMB-', 'RAMIS-104928172', 'Commercial Bank Main (012)', '3 Active Terminals', 'Live Synced', (16, 185, 129)),
    ('Kandy Retail Supermarket', 'LOC-02', 'Peradeniya Road, Kandy', 'INV-KDY-', 'RAMIS-104928172', 'BOC Kandy Branch (782)', '2 Active Terminals', 'Live Synced', (16, 185, 129)),
    ('Galle Showroom & Outlet', 'LOC-03', 'Main Street, Galle Fort', 'INV-GAL-', 'RAMIS-104928172', 'Sampath Bank Galle (341)', '2 Active Terminals', 'Live Synced', (16, 185, 129)),
    ('Negombo Distribution Hub', 'LOC-04', 'Colombo Road, Negombo', 'INV-NEG-', 'RAMIS-104928172', 'HNB Negombo Branch (901)', '1 Back-Office POS', 'Live Synced', (16, 185, 129)),
    ('Central Storage Warehouse', 'WAR-01', 'Industrial Zone, Piliyandala', 'GRN-WH-', 'RAMIS-104928172', 'Petty Cash - Piliyandala', 'Warehouse Dispatch', 'Live Synced', (16, 185, 129)),
    ('Online E-Commerce Store', 'WEB-01', 'hetxa.com Cloud Storefront', 'INV-WEB-', 'RAMIS-104928172', 'IPG Payment Gateway Acc', 'Virtual Terminal', 'Live Synced', (16, 185, 129)),
    ('Bambalapitiya Outlet (Upcoming)', 'LOC-05', 'Galle Road, Colombo 04', 'INV-BAM-', 'RAMIS-104928172', 'Pending Setup', '-- Inactive --', 'Staging Mode', (234, 179, 8)),
]

for r_idx, (loc, code, addr, pfx, vat, acc, pos, sync, scol) in enumerate(rows_set):
    ry = th_y + 29 + r_idx * 38
    d_set.line([20, ry + 37, W - 20, ry + 37], fill=(241, 245, 249))
    d_set.text((36, ry + 6), loc, font=f_b_sm, fill=(15, 23, 42))
    d_set.text((36, ry + 20), code, font=f_r_xs, fill=(148, 163, 184))
    d_set.text((230, ry + 12), addr, font=f_r_sm, fill=(71, 85, 105))
    
    # Prefix pill
    d_set.rounded_rectangle([385, ry + 9, 465, ry + 27], radius=3, fill=(241, 245, 249), outline=(203, 213, 225), width=1)
    d_set.text((392, ry + 13), pfx, font=f_b_xs, fill=(51, 65, 85))
    
    d_set.text((520, ry + 12), vat, font=f_r_sm, fill=(100, 116, 139))
    d_set.text((670, ry + 12), acc, font=f_r_sm, fill=(15, 23, 42))
    d_set.text((815, ry + 12), pos, font=f_r_sm, fill=(71, 85, 105))
    
    # Sync pill
    if 'Staging' in sync:
        bg, border, tc = (254, 252, 232), (254, 240, 138), (161, 98, 7)
    else:
        bg, border, tc = (240, 253, 244), (187, 247, 208), (22, 101, 52)
        
    d_set.rounded_rectangle([920, ry + 9, 1005, ry + 27], radius=3, fill=bg, outline=border, width=1)
    d_set.text((927, ry + 13), sync, font=f_b_xs, fill=tc)

im_set.save(os.path.join(out_dir, 'admin-settings-ui.png'), 'PNG')
print('Saved admin-settings-ui.png')
print('All Admin mockups generated successfully!')

