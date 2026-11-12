import os
from PIL import Image, ImageDraw, ImageFont

out_dir = r'c:/xampp/htdocs/hetxa/assets/images/modules'
os.makedirs(out_dir, exist_ok=True)

# Fonts
f_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 16)
f_sub = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 10.5)
f_b_lg = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 14)
f_b_md = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 11.5)
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
    
    # Action buttons
    if btn2_text:
        d.rounded_rectangle([W - 275, 12, W - 145, 40], radius=5, fill=(255, 255, 255), outline=(203, 213, 225), width=1)
        d.text((W - 263, 19), btn2_text, font=f_b_xs, fill=(51, 65, 85))
        
    if btn1_text:
        d.rounded_rectangle([W - 135, 12, W - 20, 40], radius=5, fill=(255, 94, 20))
        d.text((W - 123, 19), btn1_text, font=f_b_xs, fill=(255, 255, 255))
        
    return im, d

card_w = (W - 40 - 36) // 4
ty = 138

# ==============================================================================
# 1. SALES & REVENUE BI REPORT (report-sales-ui.png)
# ==============================================================================
print('Generating report-sales-ui.png...')
im_sal, d_sal = create_base_canvas(
    'Sales & Revenue BI Analytics Report',
    'Home  »  Reports  »  Sales Reports  »  Monthly Revenue Breakdown',
    'Export XLSX',
    'Filter Outlets'
)

kpis_sal = [
    ('TOTAL REVENUE (NOV)', 'LKR 18,450,200.00', '+14.8% vs October', (255, 94, 20), (255, 247, 242)),
    ('GROSS PROFIT', 'LKR 6,310,000.00', '34.2% Gross Margin', (2, 132, 199), (240, 249, 255)),
    ('TOTAL INVOICES', '1,428 Invoices', 'Avg LKR 12,920 / Sale', (22, 163, 74), (240, 253, 244)),
    ('PAYMENT SETTLED', '98.6% Realized', 'LKR 260K Pending AR', (217, 119, 6), (254, 243, 199))
]

for i, (label, val, sub, col, bg_col) in enumerate(kpis_sal):
    cx = 20 + i * (card_w + 12)
    cy = 64
    d_sal.rounded_rectangle([cx, cy, cx + card_w, cy + 62], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d_sal.rounded_rectangle([cx, cy, cx + card_w, cy + 3], radius=1, fill=col)
    d_sal.text((cx + 12, cy + 9), label, font=f_b_xs, fill=(100, 116, 139))
    d_sal.text((cx + 12, cy + 24), val, font=f_b_md, fill=(15, 23, 42))
    d_sal.rounded_rectangle([cx + 12, cy + 44, cx + card_w - 12, cy + 57], radius=3, fill=bg_col)
    d_sal.text((cx + 16, cy + 45), sub, font=f_b_xs, fill=col)

d_sal.rounded_rectangle([20, ty, W - 20, H - 15], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
d_sal.rounded_rectangle([20, ty, W - 20, ty + 34], radius=6, fill=(241, 245, 249))

headers_sal = [
    ('INVOICE #', 35),
    ('DATE & TIME', 135),
    ('CUSTOMER / ACCOUNT', 265),
    ('BRANCH / OUTLET', 475),
    ('PAY METHOD', 605),
    ('SUBTOTAL (LKR)', 710),
    ('TAX (RAMIS)', 815),
    ('TOTAL (LKR)', 900)
]
for h_text, hx in headers_sal:
    d_sal.text((hx, ty + 10), h_text, font=f_b_xs, fill=(71, 85, 105))
d_sal.line([20, ty + 34, W - 20, ty + 34], fill=(226, 232, 240))

rows_sal = [
    ('INV-2026-8492', '2026-11-09 14:22', 'Ceylon Super Foods Hub', 'Colombo Central Store', 'Bank Transfer', '384,500.00', '18% VAT', '453,710.00'),
    ('INV-2026-8491', '2026-11-09 13:45', 'Royal Tea Traders (Pvt) Ltd', 'Wholesale Depot LK', 'Cheque PDC', '540,000.00', '18% VAT', '637,200.00'),
    ('INV-2026-8490', '2026-11-09 12:10', 'Walk-in Retail Customer', 'Kandy Super Store', 'LankaQR', '18,450.00', 'Included', '18,450.00'),
    ('INV-2026-8489', '2026-11-09 11:30', 'Apex Global Logistics LK', 'Colombo Central Store', 'Card (Visa)', '86,200.00', '18% VAT', '101,716.00'),
    ('INV-2026-8488', '2026-11-09 10:15', 'Sunlight Hardware Emporium', 'Galle Branch Outlet', 'Cash', '42,500.00', 'None', '42,500.00'),
    ('INV-2026-8487', '2026-11-09 09:50', 'Lanka Distributors (Pvt) Ltd', 'Wholesale Depot LK', 'Bank Transfer', '920,000.00', '18% VAT', '1,085,600.00'),
    ('INV-2026-8486', '2026-11-08 17:30', 'Highland Bakers & Mart', 'Colombo Central Store', 'Cheque PDC', '165,000.00', '18% VAT', '194,700.00'),
    ('INV-2026-8485', '2026-11-08 16:15', 'Greenfield Organic Spices', 'Kurunegala Depot', 'Card (Master)', '124,000.00', '18% VAT', '146,320.00'),
    ('INV-2026-8484', '2026-11-08 15:00', 'Metro Lanka Wholesale Dist.', 'Wholesale Depot LK', 'Bank Transfer', '480,000.00', '18% VAT', '566,400.00')
]

ry = ty + 35
for i, (inv, dt, cust, branch, pay, sub, tax, tot) in enumerate(rows_sal):
    if i % 2 == 1:
        d_sal.rectangle([21, ry, W - 21, ry + 32], fill=(248, 250, 252))
        
    d_sal.text((35, ry + 8), inv, font=f_b_sm, fill=(255, 94, 20))
    d_sal.text((135, ry + 8), dt, font=f_r_xs, fill=(100, 116, 139))
    d_sal.text((265, ry + 8), cust, font=f_b_xs, fill=(15, 23, 42))
    d_sal.text((475, ry + 8), branch, font=f_r_xs, fill=(71, 85, 105))
    
    # Pay badge
    pay_col = (22, 163, 74) if 'Cash' in pay or 'LankaQR' in pay else ((2, 132, 199) if 'Bank' in pay or 'Card' in pay else (217, 119, 6))
    pay_bg = (240, 253, 244) if 'Cash' in pay or 'LankaQR' in pay else ((240, 249, 255) if 'Bank' in pay or 'Card' in pay else (254, 243, 199))
    d_sal.rounded_rectangle([605, ry + 6, 685, ry + 25], radius=3, fill=pay_bg)
    d_sal.text((612, ry + 8), pay, font=f_b_xs, fill=pay_col)
    
    d_sal.text((710, ry + 8), sub, font=f_r_xs, fill=(100, 116, 139))
    d_sal.text((815, ry + 8), tax, font=f_r_xs, fill=(100, 116, 139))
    d_sal.text((900, ry + 8), tot, font=f_b_xs, fill=(15, 23, 42))
    
    d_sal.line([21, ry + 32, W - 21, ry + 32], fill=(241, 245, 249))
    ry += 33

im_sal.save(os.path.join(out_dir, 'report-sales-ui.png'))
print('Saved report-sales-ui.png!')


# ==============================================================================
# 2. STOCK VALUATION & ITEM VELOCITY REPORT (report-stock-ui.png)
# ==============================================================================
print('Generating report-stock-ui.png...')
im_stk, d_stk = create_base_canvas(
    'Inventory Valuation & Stock Velocity Report',
    'Home  »  Reports  »  Stock Reports  »  Warehouse Valuation & Reorder Audit',
    'Export XLSX',
    'Filter Fast Movers'
)

kpis_stk = [
    ('TOTAL STOCK VALUE', 'LKR 42,650,800.00', 'At Cost Valuation', (255, 94, 20), (255, 247, 242)),
    ('ACTIVE INVENTORY', '8,450 SKUs', 'Across 3 Warehouses', (2, 132, 199), (240, 249, 255)),
    ('LOW STOCK ALERTS', '14 SKUs Below Min', 'Reorder Triggers Active', (239, 68, 68), (254, 242, 242)),
    ('STOCK TURNOVER', '6.8x Annual Velocity', 'Optimal Working Capital', (22, 163, 74), (240, 253, 244))
]

for i, (label, val, sub, col, bg_col) in enumerate(kpis_stk):
    cx = 20 + i * (card_w + 12)
    cy = 64
    d_stk.rounded_rectangle([cx, cy, cx + card_w, cy + 62], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d_stk.rounded_rectangle([cx, cy, cx + card_w, cy + 3], radius=1, fill=col)
    d_stk.text((cx + 12, cy + 9), label, font=f_b_xs, fill=(100, 116, 139))
    d_stk.text((cx + 12, cy + 24), val, font=f_b_md, fill=(15, 23, 42))
    d_stk.rounded_rectangle([cx + 12, cy + 44, cx + card_w - 12, cy + 57], radius=3, fill=bg_col)
    d_stk.text((cx + 16, cy + 45), sub, font=f_b_xs, fill=col)

d_stk.rounded_rectangle([20, ty, W - 20, H - 15], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
d_stk.rounded_rectangle([20, ty, W - 20, ty + 34], radius=6, fill=(241, 245, 249))

headers_stk = [
    ('SKU CODE', 35),
    ('PRODUCT / ITEM NAME', 125),
    ('CATEGORY', 360),
    ('IN STOCK', 475),
    ('UNIT COST (LKR)', 565),
    ('TOTAL VAL (LKR)', 675),
    ('REORDER LEVEL', 785),
    ('VELOCITY STATUS', 885)
]
for h_text, hx in headers_stk:
    d_stk.text((hx, ty + 10), h_text, font=f_b_xs, fill=(71, 85, 105))
d_stk.line([20, ty + 34, W - 20, ty + 34], fill=(226, 232, 240))

rows_stk = [
    ('SKU-TEA-001', 'Dilmah Premium Ceylon Tea 500g', 'Beverages', '2,450 Pcs', '780.00', '1,911,000.00', '500 Pcs', 'Fast-Moving', (22, 163, 74), (240, 253, 244)),
    ('SKU-MLK-002', 'Anchor Full Cream Milk Powder 1kg', 'Dairy & Baby Food', '1,820 Pcs', '1,320.00', '2,402,400.00', '400 Pcs', 'Fast-Moving', (22, 163, 74), (240, 253, 244)),
    ('SKU-RCE-003', 'Araliya Keeri Samba Rice 5kg Pack', 'Grains & Flours', '940 Bags', '1,450.00', '1,363,000.00', '200 Bags', 'Fast-Moving', (22, 163, 74), (240, 253, 244)),
    ('SKU-OIL-004', 'Fortune Coconut Cooking Oil 1L Bottle', 'Cooking Oils', '48 Pcs', '820.00', '39,360.00', '100 Pcs', 'Low Stock Alert', (239, 68, 68), (254, 242, 242)),
    ('SKU-BSC-005', 'Munchee Super Cream Cracker 490g', 'Biscuits & Snacks', '3,100 Pcs', '290.00', '899,000.00', '600 Pcs', 'Fast-Moving', (22, 163, 74), (240, 253, 244)),
    ('SKU-DRY-006', 'Highland Salted Butter 200g Tub', 'Dairy & Chilled', '32 Pcs', '720.00', '23,040.00', '50 Pcs', 'Low Stock Alert', (239, 68, 68), (254, 242, 242)),
    ('SKU-SPP-007', 'Harischandra Pure Coffee 200g Pack', 'Beverages', '1,250 Pcs', '420.00', '525,000.00', '250 Pcs', 'Steady Velocity', (2, 132, 199), (240, 249, 255)),
    ('SKU-BVR-008', 'Elephant House Ginger Beer 1.5L PET', 'Soft Drinks', '1,890 Btls', '380.00', '718,200.00', '400 Btls', 'Fast-Moving', (22, 163, 74), (240, 253, 244)),
    ('SKU-CLN-009', 'Sunlight Washing Powder Lemon 1kg', 'Home Cleaning', '1,100 Pcs', '480.00', '528,000.00', '300 Pcs', 'Steady Velocity', (2, 132, 199), (240, 249, 255))
]

ry = ty + 35
for i, (sku, name, cat, qty, u_cost, tot_val, ro, status, st_col, st_bg) in enumerate(rows_stk):
    if i % 2 == 1:
        d_stk.rectangle([21, ry, W - 21, ry + 32], fill=(248, 250, 252))
        
    d_stk.text((35, ry + 8), sku, font=f_b_sm, fill=(255, 94, 20))
    d_stk.text((125, ry + 8), name, font=f_b_sm, fill=(15, 23, 42))
    d_stk.text((360, ry + 8), cat, font=f_r_xs, fill=(71, 85, 105))
    d_stk.text((475, ry + 8), qty, font=f_b_xs, fill=(15, 23, 42))
    d_stk.text((565, ry + 8), u_cost, font=f_r_xs, fill=(100, 116, 139))
    d_stk.text((675, ry + 8), tot_val, font=f_b_xs, fill=(15, 23, 42))
    d_stk.text((785, ry + 8), ro, font=f_r_xs, fill=(100, 116, 139))
    
    # Status badge
    d_stk.rounded_rectangle([880, ry + 6, 975, ry + 25], radius=3, fill=st_bg)
    d_stk.text((888, ry + 8), status, font=f_b_xs, fill=st_col)
    
    d_stk.line([21, ry + 32, W - 21, ry + 32], fill=(241, 245, 249))
    ry += 33

im_stk.save(os.path.join(out_dir, 'report-stock-ui.png'))
print('Saved report-stock-ui.png!')


# ==============================================================================
# 3. CHEQUE & PAYMENT RECONCILIATION REPORT (report-cheque-ui.png)
# ==============================================================================
print('Generating report-cheque-ui.png...')
im_chq, d_chq = create_base_canvas(
    'Post-Dated Cheques & Payment Audit Report',
    'Home  »  Reports  »  Cheque Reports  »  In-Hand & Issued PDC Registry',
    'Export XLSX',
    'Maturity Calendar'
)

kpis_chq = [
    ('IN-HAND CHEQUES', 'LKR 8,420,500.00', '18 Customer PDCs', (255, 94, 20), (255, 247, 242)),
    ('ISSUED CHEQUES', 'LKR 4,150,000.00', '9 Supplier PDCs Out', (2, 132, 199), (240, 249, 255)),
    ('REALIZED (NOV)', 'LKR 14,890,000.00', '100% Cleared On-Time', (22, 163, 74), (240, 253, 244)),
    ('BOUNCED / RETURNED', '0 Cheques', 'Zero Default Risk', (217, 119, 6), (254, 243, 199))
]

for i, (label, val, sub, col, bg_col) in enumerate(kpis_chq):
    cx = 20 + i * (card_w + 12)
    cy = 64
    d_chq.rounded_rectangle([cx, cy, cx + card_w, cy + 62], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d_chq.rounded_rectangle([cx, cy, cx + card_w, cy + 3], radius=1, fill=col)
    d_chq.text((cx + 12, cy + 9), label, font=f_b_xs, fill=(100, 116, 139))
    d_chq.text((cx + 12, cy + 24), val, font=f_b_md, fill=(15, 23, 42))
    d_chq.rounded_rectangle([cx + 12, cy + 44, cx + card_w - 12, cy + 57], radius=3, fill=bg_col)
    d_chq.text((cx + 16, cy + 45), sub, font=f_b_xs, fill=col)

d_chq.rounded_rectangle([20, ty, W - 20, H - 15], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
d_chq.rounded_rectangle([20, ty, W - 20, ty + 34], radius=6, fill=(241, 245, 249))

headers_chq = [
    ('CHQ #', 35),
    ('BANK & BRANCH', 115),
    ('DRAWER / PAYEE', 285),
    ('ISSUE DATE', 465),
    ('MATURITY DATE', 545),
    ('AMOUNT (LKR)', 635),
    ('TYPE', 745),
    ('STATUS', 840),
    ('ACTION', 940)
]
for h_text, hx in headers_chq:
    d_chq.text((hx, ty + 10), h_text, font=f_b_xs, fill=(71, 85, 105))
d_chq.line([20, ty + 34, W - 20, ty + 34], fill=(226, 232, 240))

rows_chq = [
    ('CHQ-849201', 'Commercial Bank - Kollupitiya', 'Royal Tea Traders (Pvt) Ltd', '2026-10-15', '2026-11-10', '850,000.00', 'In-Hand', 'Due Tomorrow', (255, 94, 20), (255, 247, 242)),
    ('CHQ-402918', 'Hatton National Bank - Pettah', 'Lanka Distributors (Pvt) Ltd', '2026-10-20', '2026-11-12', '1,200,000.00', 'In-Hand', 'In Hand', (2, 132, 199), (240, 249, 255)),
    ('CHQ-192840', 'Sampath Bank - Nugegoda', 'Ceylon Super Foods Hub', '2026-10-10', '2026-11-08', '450,000.00', 'In-Hand', 'Deposited', (22, 163, 74), (240, 253, 244)),
    ('CHQ-772819', 'Bank of Ceylon - Fort Corporate', 'Greenfield Spices Supply', '2026-10-25', '2026-11-15', '680,000.00', 'Issued', 'Issued Out', (100, 116, 139), (241, 245, 249)),
    ('CHQ-661920', 'Seylan Bank - Rajagiriya', 'Highland Bakers & Mart', '2026-10-05', '2026-11-05', '320,000.00', 'In-Hand', 'Realized', (22, 163, 74), (240, 253, 244)),
    ('CHQ-551029', 'Nations Trust Bank - Nawala', 'Apex Global Logistics LK', '2026-10-28', '2026-11-18', '950,000.00', 'In-Hand', 'In Hand', (2, 132, 199), (240, 249, 255)),
    ('CHQ-339201', 'Commercial Bank - Piliyandala', 'Metro Wholesale Packaging', '2026-10-30', '2026-11-20', '520,000.00', 'Issued', 'Issued Out', (100, 116, 139), (241, 245, 249)),
    ('CHQ-220194', 'People\'s Bank - Kandy City', 'Sunlight Hardware Emporium', '2026-10-12', '2026-11-06', '280,000.00', 'In-Hand', 'Realized', (22, 163, 74), (240, 253, 244)),
    ('CHQ-991823', 'Hatton National Bank - Cinnamon Gdns', 'Araliya Rice Mills Polonnaruwa', '2026-11-01', '2026-11-25', '1,450,000.00', 'Issued', 'Issued Out', (100, 116, 139), (241, 245, 249))
]

ry = ty + 35
for i, (chq, bank, party, iss, mat, amt, t_type, st, st_col, st_bg) in enumerate(rows_chq):
    if i % 2 == 1:
        d_chq.rectangle([21, ry, W - 21, ry + 32], fill=(248, 250, 252))
        
    d_chq.text((35, ry + 8), chq, font=f_b_sm, fill=(255, 94, 20))
    d_chq.text((115, ry + 8), bank, font=f_r_xs, fill=(71, 85, 105))
    d_chq.text((285, ry + 8), party, font=f_b_xs, fill=(15, 23, 42))
    d_chq.text((465, ry + 8), iss, font=f_r_xs, fill=(100, 116, 139))
    d_chq.text((545, ry + 8), mat, font=f_b_xs, fill=(255, 94, 20) if 'Tomorrow' in st else (100, 116, 139))
    d_chq.text((635, ry + 8), amt, font=f_b_xs, fill=(15, 23, 42))
    d_chq.text((745, ry + 8), t_type, font=f_r_xs, fill=(71, 85, 105))
    
    # Status badge
    d_chq.rounded_rectangle([835, ry + 6, 920, ry + 25], radius=3, fill=st_bg)
    d_chq.text((843, ry + 8), st, font=f_b_xs, fill=st_col)
    
    # Action button
    d_chq.rounded_rectangle([935, ry + 6, 985, ry + 25], radius=4, fill=(255, 255, 255), outline=(203, 213, 225), width=1)
    d_chq.text((945, ry + 8), 'View', font=f_b_xs, fill=(51, 65, 85))
    
    d_chq.line([21, ry + 32, W - 21, ry + 32], fill=(241, 245, 249))
    ry += 33

im_chq.save(os.path.join(out_dir, 'report-cheque-ui.png'))
print('Saved report-cheque-ui.png!')

