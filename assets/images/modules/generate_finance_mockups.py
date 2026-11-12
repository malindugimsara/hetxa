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
# 1. CHEQUE MANAGEMENT MOCKUP
# ==============================================================================
print('Generating finance-cheques-ui.png...')
im_chq, d_chq = create_base_canvas(
    'Receivable Cheques Management',
    'Home  »  Finance  »  Cheque Management  »  Receivable Cheques',
    '+ Add New Cheque',
    'Deposit Slip Batch'
)

# 4 KPI Cards
kpis_chq = [
    ('TOTAL IN HAND', 'LKR 3,450,000.00', '14 Active Cheques', (255, 94, 20), (255, 247, 242)),
    ('DUE THIS WEEK', 'LKR 820,000.00', '3 Maturity Alerts', (2, 132, 199), (240, 249, 255)),
    ('DEPOSITED / TRANSIT', 'LKR 1,280,000.00', '4 Pending Clearance', (217, 119, 6), (254, 243, 199)),
    ('REALIZED (THIS MONTH)', 'LKR 8,940,000.00', '28 Cleared Cheques', (22, 163, 74), (240, 253, 244))
]

card_w = (W - 40 - 36) // 4
for i, (label, val, sub, col, bg_col) in enumerate(kpis_chq):
    cx = 20 + i * (card_w + 12)
    cy = 64
    d_chq.rounded_rectangle([cx, cy, cx + card_w, cy + 62], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    # top accent stripe
    d_chq.rounded_rectangle([cx, cy, cx + card_w, cy + 3], radius=1, fill=col)
    d_chq.text((cx + 12, cy + 9), label, font=f_b_xs, fill=(100, 116, 139))
    d_chq.text((cx + 12, cy + 24), val, font=f_b_md, fill=(15, 23, 42))
    # pill
    d_chq.rounded_rectangle([cx + 12, cy + 44, cx + card_w - 12, cy + 57], radius=3, fill=bg_col)
    d_chq.text((cx + 16, cy + 45), sub, font=f_b_xs, fill=col)

# Table Container
ty = 138
d_chq.rounded_rectangle([20, ty, W - 20, H - 15], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)

# Table Header
d_chq.rounded_rectangle([20, ty, W - 20, ty + 34], radius=6, fill=(241, 245, 249))
headers_chq = [
    ('CHEQUE NO', 35),
    ('ISSUING BANK', 140),
    ('DRAWER / CUSTOMER', 315),
    ('DUE DATE', 495),
    ('AMOUNT (LKR)', 585),
    ('TARGET ACCOUNT', 705),
    ('STATUS', 850),
    ('ACTION', 940)
]
for h_text, hx in headers_chq:
    d_chq.text((hx, ty + 10), h_text, font=f_b_xs, fill=(71, 85, 105))
d_chq.line([20, ty + 34, W - 20, ty + 34], fill=(226, 232, 240))

rows_chq = [
    ('CHQ-748921', 'Commercial Bank - Kollupitiya', 'Royal Tea Traders (Pvt) Ltd', '2026-11-12', '450,000.00', 'Comm Bank Current (A/C: 1048)', 'In Hand', (255, 94, 20), (255, 247, 242)),
    ('CHQ-104928', 'Sampath Bank - Borella Metro', 'Ceylon Super Foods Hub', '2026-11-10', '1,280,000.00', 'Sampath Enterprise (A/C: 8812)', 'Deposited', (2, 132, 199), (240, 249, 255)),
    ('CHQ-559102', 'Hatton National Bank - Pettah', 'Apex Global Logistics LK', '2026-11-08', '650,000.00', 'HNB Corporate (A/C: 3390)', 'Realized', (22, 163, 74), (240, 253, 244)),
    ('CHQ-338291', 'Bank of Ceylon - Colombo Fort', 'Metro Lanka Wholesale Dist.', '2026-11-05', '820,000.00', 'BOC Operation (A/C: 5541)', 'Realized', (22, 163, 74), (240, 253, 244)),
    ('CHQ-882103', 'Nations Trust Bank - Nugegoda', 'Lanka Retail Hub Supermart', '2026-11-15', '250,000.00', 'Comm Bank Current (A/C: 1048)', 'In Hand', (255, 94, 20), (255, 247, 242)),
    ('CHQ-420915', 'Seylan Bank - Maharagama', 'Greenfield Organic Spices', '2026-11-02', '385,000.00', 'Sampath Enterprise (A/C: 8812)', 'Realized', (22, 163, 74), (240, 253, 244)),
    ('CHQ-910482', 'People\'s Bank - Kandy City', 'Highland Bakers & Mart', '2026-11-18', '510,000.00', 'Comm Bank Current (A/C: 1048)', 'In Hand', (255, 94, 20), (255, 247, 242)),
    ('CHQ-294017', 'Commercial Bank - Wattala', 'Sunlight Hardware Emporium', '2026-11-01', '195,000.00', 'HNB Corporate (A/C: 3390)', 'Realized', (22, 163, 74), (240, 253, 244)),
    ('CHQ-671204', 'DFCC Bank - Colombo 03', 'Silverline Electronics Ltd', '2026-11-20', '740,000.00', 'Comm Bank Current (A/C: 1048)', 'In Hand', (255, 94, 20), (255, 247, 242))
]

ry = ty + 35
for i, (c_no, bank, cust, dt, amt, acc, st, st_col, st_bg) in enumerate(rows_chq):
    if i % 2 == 1:
        d_chq.rectangle([21, ry, W - 21, ry + 32], fill=(248, 250, 252))
        
    d_chq.text((35, ry + 8), c_no, font=f_b_sm, fill=(15, 23, 42))
    d_chq.text((140, ry + 8), bank, font=f_r_sm, fill=(51, 65, 85))
    d_chq.text((315, ry + 8), cust, font=f_r_sm, fill=(15, 23, 42))
    d_chq.text((495, ry + 8), dt, font=f_r_sm, fill=(100, 116, 139))
    d_chq.text((585, ry + 8), amt, font=f_b_sm, fill=(15, 23, 42))
    d_chq.text((705, ry + 8), acc, font=f_r_xs, fill=(71, 85, 105))
    
    # Status badge
    d_chq.rounded_rectangle([846, ry + 6, 915, ry + 25], radius=4, fill=st_bg)
    d_chq.text((854, ry + 8), st, font=f_b_xs, fill=st_col)
    
    # Action button
    d_chq.rounded_rectangle([936, ry + 6, 985, ry + 25], radius=4, fill=(255, 255, 255), outline=(203, 213, 225), width=1)
    d_chq.text((945, ry + 8), 'View', font=f_b_xs, fill=(51, 65, 85))
    
    d_chq.line([21, ry + 32, W - 21, ry + 32], fill=(241, 245, 249))
    ry += 33

im_chq.save(os.path.join(out_dir, 'finance-cheques-ui.png'))
print('Saved finance-cheques-ui.png!')

# ==============================================================================
# 2. EXPENSES & PETTY CASH MOCKUP
# ==============================================================================
print('Generating finance-expenses-ui.png...')
im_exp, d_exp = create_base_canvas(
    'Company Expenses & Petty Cash',
    'Home  »  Finance  »  Expenses  »  Expenses List',
    '+ Record Expense',
    'Categories Setup'
)

# 4 KPI Cards
kpis_exp = [
    ('TOTAL EXPENSES (NOV)', 'LKR 1,485,200.00', '42 Active Vouchers', (255, 94, 20), (255, 247, 242)),
    ('PETTY CASH FLOAT', 'LKR 124,500.00', 'Ready Counter Balance', (22, 163, 74), (240, 253, 244)),
    ('PENDING APPROVAL', '2 Vouchers', 'LKR 84,000.00 Total', (217, 119, 6), (254, 243, 199)),
    ('INPUT TAX DEDUCTIBLE', 'LKR 214,800.00', 'IRD RAMIS VAT Eligible', (2, 132, 199), (240, 249, 255))
]

for i, (label, val, sub, col, bg_col) in enumerate(kpis_exp):
    cx = 20 + i * (card_w + 12)
    cy = 64
    d_exp.rounded_rectangle([cx, cy, cx + card_w, cy + 62], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d_exp.rounded_rectangle([cx, cy, cx + card_w, cy + 3], radius=1, fill=col)
    d_exp.text((cx + 12, cy + 9), label, font=f_b_xs, fill=(100, 116, 139))
    d_exp.text((cx + 12, cy + 24), val, font=f_b_md, fill=(15, 23, 42))
    d_exp.rounded_rectangle([cx + 12, cy + 44, cx + card_w - 12, cy + 57], radius=3, fill=bg_col)
    d_exp.text((cx + 16, cy + 45), sub, font=f_b_xs, fill=col)

# Table Container
d_exp.rounded_rectangle([20, ty, W - 20, H - 15], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
d_exp.rounded_rectangle([20, ty, W - 20, ty + 34], radius=6, fill=(241, 245, 249))

headers_exp = [
    ('EXPENSE REF', 35),
    ('DATE', 140),
    ('CATEGORY', 225),
    ('DESCRIPTION & PARTICULARS', 375),
    ('PAID THROUGH', 640),
    ('TAX / VAT', 770),
    ('AMOUNT (LKR)', 840),
    ('STATUS', 940)
]
for h_text, hx in headers_exp:
    d_exp.text((hx, ty + 10), h_text, font=f_b_xs, fill=(71, 85, 105))
d_exp.line([20, ty + 34, W - 20, ty + 34], fill=(226, 232, 240))

rows_exp = [
    ('EXP-2026-0412', '2026-11-09', 'Logistics & Fuel', 'Diesel Fuel - Delivery Lorry WP-GA-4589', 'Petty Cash Counter', '0%', '28,500.00', 'Approved', (22, 163, 74), (240, 253, 244)),
    ('EXP-2026-0411', '2026-11-08', 'Utilities & Power', 'CEB Commercial Electricity - Central Warehouse', 'Bank Transfer (HNB)', '18% VAT', '145,200.00', 'Approved', (22, 163, 74), (240, 253, 244)),
    ('EXP-2026-0410', '2026-11-07', 'Packing & Store', '5-Ply Corrugated Packing Carton Boxes (500)', 'Cheque (CHQ-9901)', '0%', '95,000.00', 'Approved', (22, 163, 74), (240, 253, 244)),
    ('EXP-2026-0409', '2026-11-06', 'Cloud & IT Systems', 'Monthly Cloud ERP Server Hosting & Daily Backups', 'Corporate Visa Card', '0%', '68,400.00', 'Approved', (22, 163, 74), (240, 253, 244)),
    ('EXP-2026-0408', '2026-11-05', 'Warehouse Maint.', 'Hydraulic Forklift Servicing & Oil Replacements', 'Petty Cash Counter', '18% VAT', '36,000.00', 'Approved', (22, 163, 74), (240, 253, 244)),
    ('EXP-2026-0407', '2026-11-04', 'Staff Welfare', 'Monthly Refreshments, Drinking Water & Tea Pantry', 'Petty Cash Counter', '0%', '24,800.00', 'Approved', (22, 163, 74), (240, 253, 244)),
    ('EXP-2026-0406', '2026-11-03', 'Office Stationery', 'A4 Printing Paper reams & Thermal Receipt rolls', 'Petty Cash Counter', '0%', '19,500.00', 'Approved', (22, 163, 74), (240, 253, 244)),
    ('EXP-2026-0405', '2026-11-02', 'Telecommunication', 'Dialog Fiber Internet & Corporate Mobile Lines', 'Bank Transfer (Comm)', '18% VAT', '42,800.00', 'Approved', (22, 163, 74), (240, 253, 244)),
    ('EXP-2026-0404', '2026-11-01', 'Facility Lease', 'Commercial Warehouse Monthly Lease Rental', 'Cheque (CHQ-9884)', '0%', '280,000.00', 'Approved', (22, 163, 74), (240, 253, 244))
]

ry = ty + 35
for i, (ref, dt, cat, desc, paid, tax, amt, st, st_col, st_bg) in enumerate(rows_exp):
    if i % 2 == 1:
        d_exp.rectangle([21, ry, W - 21, ry + 32], fill=(248, 250, 252))
        
    d_exp.text((35, ry + 8), ref, font=f_b_sm, fill=(15, 23, 42))
    d_exp.text((140, ry + 8), dt, font=f_r_sm, fill=(100, 116, 139))
    d_exp.text((225, ry + 8), cat, font=f_b_xs, fill=(255, 94, 20))
    d_exp.text((375, ry + 8), desc, font=f_r_sm, fill=(15, 23, 42))
    d_exp.text((640, ry + 8), paid, font=f_r_xs, fill=(71, 85, 105))
    d_exp.text((770, ry + 8), tax, font=f_r_xs, fill=(100, 116, 139))
    d_exp.text((840, ry + 8), amt, font=f_b_sm, fill=(15, 23, 42))
    
    # Status badge
    d_exp.rounded_rectangle([936, ry + 6, 995, ry + 25], radius=4, fill=st_bg)
    d_exp.text((945, ry + 8), st, font=f_b_xs, fill=st_col)
    
    d_exp.line([21, ry + 32, W - 21, ry + 32], fill=(241, 245, 249))
    ry += 33

im_exp.save(os.path.join(out_dir, 'finance-expenses-ui.png'))
print('Saved finance-expenses-ui.png!')

# ==============================================================================
# 3. ACCOUNTING DASHBOARD & GENERAL LEDGER MOCKUP
# ==============================================================================
print('Generating finance-accounting-ui.png...')
im_acc, d_acc = create_base_canvas(
    'Accounting Dashboard & Trial Balance',
    'Home  »  Finance  »  Accounting  »  General Ledger & Reports',
    '+ Journal Voucher',
    'Financial Reports'
)

# 4 KPI Cards
kpis_acc = [
    ('NET REVENUE (MTD)', 'LKR 18,450,000.00', '+14.2% Growth vs Oct', (22, 163, 74), (240, 253, 244)),
    ('GROSS PROFIT', 'LKR 6,280,000.00', '34.0% Gross Margin', (2, 132, 199), (240, 249, 255)),
    ('TOTAL CASH & BANK', 'LKR 9,840,250.00', '6 Commercial Accounts', (255, 94, 20), (255, 247, 242)),
    ('TRIAL BALANCE', 'BALANCED (0.00)', 'Debits Equal Credits', (22, 163, 74), (240, 253, 244))
]

for i, (label, val, sub, col, bg_col) in enumerate(kpis_acc):
    cx = 20 + i * (card_w + 12)
    cy = 64
    d_acc.rounded_rectangle([cx, cy, cx + card_w, cy + 62], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d_acc.rounded_rectangle([cx, cy, cx + card_w, cy + 3], radius=1, fill=col)
    d_acc.text((cx + 12, cy + 9), label, font=f_b_xs, fill=(100, 116, 139))
    d_acc.text((cx + 12, cy + 24), val, font=f_b_md, fill=(15, 23, 42))
    d_acc.rounded_rectangle([cx + 12, cy + 44, cx + card_w - 12, cy + 57], radius=3, fill=bg_col)
    d_acc.text((cx + 16, cy + 45), sub, font=f_b_xs, fill=col)

# Table Container (Trial Balance View)
d_acc.rounded_rectangle([20, ty, W - 20, H - 45], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
d_acc.rounded_rectangle([20, ty, W - 20, ty + 34], radius=6, fill=(241, 245, 249))

headers_acc = [
    ('ACCOUNT CODE', 35),
    ('ACCOUNT HEAD & DESCRIPTION', 140),
    ('ACCOUNT TYPE', 410),
    ('BRANCH / ENTITY', 560),
    ('DEBIT BALANCE (LKR)', 700),
    ('CREDIT BALANCE (LKR)', 860)
]
for h_text, hx in headers_acc:
    d_acc.text((hx, ty + 10), h_text, font=f_b_xs, fill=(71, 85, 105))
d_acc.line([20, ty + 34, W - 20, ty + 34], fill=(226, 232, 240))

rows_acc = [
    ('1010', 'Cash at Bank - Commercial Bank Current (A/C: 1048)', 'Current Asset', 'Head Office', '5,820,400.00', '-', (15, 23, 42)),
    ('1020', 'Cash at Bank - Sampath Bank Enterprise (A/C: 8812)', 'Current Asset', 'Head Office', '2,445,350.00', '-', (15, 23, 42)),
    ('1030', 'Petty Cash Counter Floats', 'Current Asset', 'All Branches', '124,500.00', '-', (15, 23, 42)),
    ('1040', 'Post-Dated Cheques in Hand (PDC)', 'Current Asset', 'Colombo Main', '3,450,000.00', '-', (15, 23, 42)),
    ('1050', 'Trade Debtors / Accounts Receivable', 'Current Asset', 'Corporate Clients', '4,680,100.00', '-', (15, 23, 42)),
    ('1080', 'Warehouse Merchandise Inventory', 'Current Asset', 'Central Store', '9,600,150.00', '-', (15, 23, 42)),
    ('2010', 'Trade Creditors / Accounts Payable', 'Current Liability', 'Suppliers Matrix', '-', '3,420,000.00', (15, 23, 42)),
    ('4010', 'Operating Sales Revenue - Wholesale & Retail', 'Operating Income', 'Enterprise', '-', '18,450,000.00', (15, 23, 42)),
    ('5010', 'Cost of Goods Sold (COGS)', 'Direct Expense', 'Operations', '12,170,000.00', '-', (15, 23, 42))
]

ry = ty + 35
for i, (code, title, act_type, entity, dr, cr, text_col) in enumerate(rows_acc):
    if i % 2 == 1:
        d_acc.rectangle([21, ry, W - 21, ry + 32], fill=(248, 250, 252))
        
    d_acc.text((35, ry + 8), code, font=f_b_sm, fill=(255, 94, 20))
    d_acc.text((140, ry + 8), title, font=f_r_sm, fill=(15, 23, 42))
    d_acc.text((410, ry + 8), act_type, font=f_r_xs, fill=(71, 85, 105))
    d_acc.text((560, ry + 8), entity, font=f_r_xs, fill=(100, 116, 139))
    d_acc.text((700, ry + 8), dr, font=f_b_sm if dr != '-' else f_r_sm, fill=(15, 23, 42) if dr != '-' else (148, 163, 184))
    d_acc.text((860, ry + 8), cr, font=f_b_sm if cr != '-' else f_r_sm, fill=(15, 23, 42) if cr != '-' else (148, 163, 184))
    
    d_acc.line([21, ry + 32, W - 21, ry + 32], fill=(241, 245, 249))
    ry += 33

# Trial Balance Balanced Footer Strip
d_acc.rounded_rectangle([20, H - 42, W - 20, H - 12], radius=5, fill=(240, 253, 244), outline=(187, 247, 208), width=1)
d_acc.text((35, H - 32), 'TOTAL TRIAL BALANCE:', font=f_b_xs, fill=(22, 163, 74))
d_acc.text((200, H - 32), 'Debits: LKR 38,290,500.00', font=f_b_xs, fill=(15, 23, 42))
d_acc.text((420, H - 32), 'Credits: LKR 38,290,500.00', font=f_b_xs, fill=(15, 23, 42))
d_acc.text((640, H - 32), 'Variance: LKR 0.00 (Balanced)', font=f_b_xs, fill=(22, 163, 74))
d_acc.text((860, H - 32), '✔ Strict Double-Entry Verified', font=f_b_xs, fill=(22, 163, 74))

im_acc.save(os.path.join(out_dir, 'finance-accounting-ui.png'))
print('Saved finance-accounting-ui.png!')

