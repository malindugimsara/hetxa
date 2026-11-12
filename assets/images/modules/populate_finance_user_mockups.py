import os
from PIL import Image, ImageDraw, ImageFont

p_exp = r'C:/Users/MG/.gemini/antigravity/brain/387b0f7e-a7aa-4240-b23b-79b73f4876b3/.user_uploaded/media_1794224128704_9dfc303f.png'
p_chq = r'C:/Users/MG/.gemini/antigravity/brain/387b0f7e-a7aa-4240-b23b-79b73f4876b3/.user_uploaded/media_1794224152033_6e6a980e.png'
p_acc = r'C:/Users/MG/.gemini/antigravity/brain/387b0f7e-a7aa-4240-b23b-79b73f4876b3/.user_uploaded/media_1794224221742_673dd227.png'

out_dir = r'c:/xampp/htdocs/hetxa/assets/images/modules'
os.makedirs(out_dir, exist_ok=True)

f_b_xl = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 16)
f_b_lg = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 13.5)
f_b_md = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 11)
f_b_sm = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 9.5)
f_b_xs = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 8.5)

f_r_md = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 11)
f_r_sm = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 9.5)
f_r_xs = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 8.5)

# ==============================================================================
# 1. PROCESS EXPENSES LIST (media_1794224128704_9dfc303f.png)
# ==============================================================================
print('Processing Expenses List...')
im_exp = Image.open(p_exp).convert('RGBA')
d_exp = ImageDraw.Draw(im_exp)

# Clear "No data available in table" and empty area from y=118 to y=480
# Table starts at y=118, width x=14 to 1010
d_exp.rectangle([14, 118, 1010, 480], fill=(255, 255, 255, 255))

exp_rows = [
    ("Diesel Fuel - Delivery Lorry WP-GA-4589", "2026-11-09", "28,500.00", "28,500.00", "Paid", "Kamal Perera", "Operations", "Petty Cash", "Logistics & Fuel", "Central WH", "EXP-0412"),
    ("CEB Commercial Electricity Bill - Stores", "2026-11-08", "145,200.00", "145,200.00", "Paid", "Finance Dept", "Main Hub", "HNB Corporate", "Utilities", "Head Office", "EXP-0411"),
    ("5-Ply Heavy Corrugated Boxes (500)", "2026-11-07", "95,000.00", "95,000.00", "Paid", "Stores Div", "Packaging", "Sampath CHQ", "Store Supplies", "Main Store", "EXP-0410"),
    ("Monthly AWS Production Cloud Hosting", "2026-11-06", "68,400.00", "68,400.00", "Paid", "Tech Team", "Cloud Infra", "Corporate Card", "IT Software", "All Branches", "EXP-0409"),
    ("Forklift Hydraulic Servicing & Oil", "2026-11-05", "36,000.00", "36,000.00", "Paid", "Stores Div", "Logistics", "Petty Cash", "Maintenance", "Central WH", "EXP-0408"),
    ("Staff Welfare Pantry & Drinking Water", "2026-11-04", "24,800.00", "24,800.00", "Paid", "HR Admin", "Welfare", "Petty Cash", "Staff Welfare", "Head Office", "EXP-0407"),
    ("Dialog Corporate Fiber Internet Bill", "2026-11-03", "42,800.00", "42,800.00", "Paid", "IT Dept", "Connectivity", "Commercial Bank", "Telecom", "Head Office", "EXP-0406"),
    ("Commercial Store Monthly Lease Rental", "2026-11-01", "280,000.00", "280,000.00", "Paid", "Management", "Corporate", "Comm CHQ", "Rent & Lease", "Colombo Hub", "EXP-0405")
]

# Exact header x centers:
# Title: 24, Date: 77, Amount: 165, Paid: 255, Status: 320, For: 420, Project: 516, Account: 585, Category: 720, Loc: 800, Ref: 874, Action: 955
ey = 120
for i, (title, dt, amt, paid, status, exp_for, proj, acc, cat, loc, ref) in enumerate(exp_rows):
    # Alternating row background
    if i % 2 == 1:
        d_exp.rectangle([14, ey - 2, 1010, ey + 30], fill=(248, 250, 252, 255))
        
    d_exp.text((24, ey + 6), title, font=f_b_xs, fill=(15, 23, 42, 255))
    d_exp.text((77, ey + 6), dt, font=f_r_xs, fill=(100, 116, 139, 255))
    d_exp.text((160, ey + 6), amt, font=f_b_xs, fill=(15, 23, 42, 255))
    d_exp.text((255, ey + 6), paid, font=f_r_xs, fill=(71, 85, 105, 255))
    
    # Status pill (Paid - green)
    d_exp.rounded_rectangle([318, ey + 5, 360, ey + 22], radius=3, fill=(240, 253, 244, 255), outline=(187, 247, 208, 255), width=1)
    d_exp.text((326, ey + 6), status, font=f_b_xs, fill=(22, 163, 74, 255))
    
    d_exp.text((420, ey + 6), exp_for, font=f_r_xs, fill=(15, 23, 42, 255))
    d_exp.text((516, ey + 6), proj, font=f_r_xs, fill=(100, 116, 139, 255))
    d_exp.text((582, ey + 6), acc, font=f_r_xs, fill=(71, 85, 105, 255))
    
    # Category badge
    d_exp.text((715, ey + 6), cat, font=f_b_xs, fill=(255, 94, 20, 255))
    d_exp.text((800, ey + 6), loc, font=f_r_xs, fill=(100, 116, 139, 255))
    d_exp.text((874, ey + 6), ref, font=f_b_xs, fill=(15, 23, 42, 255))
    
    # Action button
    d_exp.rounded_rectangle([948, ey + 5, 995, ey + 22], radius=3, fill=(255, 255, 255, 255), outline=(203, 213, 225, 255), width=1)
    d_exp.text((955, ey + 6), "Action ▾", font=f_b_xs, fill=(51, 65, 85, 255))
    
    # Row bottom border
    d_exp.line([14, ey + 30, 1010, ey + 30], fill=(241, 245, 249, 255))
    ey += 32

# Table Footer (Showing 1 to 8 of 8 entries and pagination)
fy = ey + 10
d_exp.text((18, fy + 4), "Showing 1 to 8 of 8 entries", font=f_r_xs, fill=(100, 116, 139, 255))

# Previous button
d_exp.rounded_rectangle([875, fy, 930, fy + 24], radius=3, fill=(255, 255, 255, 255), outline=(226, 232, 240, 255), width=1)
d_exp.text((885, fy + 4), "Previous", font=f_r_xs, fill=(148, 163, 184, 255))

# Page 1 button (Active orange)
d_exp.rounded_rectangle([936, fy, 958, fy + 24], radius=3, fill=(255, 94, 20, 255))
d_exp.text((944, fy + 4), "1", font=f_b_xs, fill=(255, 255, 255, 255))

# Next button
d_exp.rounded_rectangle([964, fy, 1005, fy + 24], radius=3, fill=(255, 255, 255, 255), outline=(226, 232, 240, 255), width=1)
d_exp.text((974, fy + 4), "Next", font=f_r_xs, fill=(148, 163, 184, 255))

im_exp.save(os.path.join(out_dir, 'finance-expenses-ui.png'))
print('Saved finance-expenses-ui.png!')


# ==============================================================================
# 2. PROCESS RECEIVABLE CHEQUES (media_1794224152033_6e6a980e.png)
# ==============================================================================
print('Processing Receivable Cheques...')
im_chq = Image.open(p_chq).convert('RGBA')
d_chq = ImageDraw.Draw(im_chq)

# Clear "No data available in table" from y=162 to y=480
d_chq.rectangle([14, 162, 1010, 480], fill=(255, 255, 255, 255))

chq_rows = [
    ("1", "CHQ-REC-0014", "Royal Tea Traders (Pvt) Ltd", "CHQ-748921", "Commercial Bank (Kollupitiya)", "2026-11-01", "2026-11-12", "2026-11-12", "In 3 Days", "450,000.00", "Comm Bank Current", "In Hand", (255, 94, 20), (255, 247, 242)),
    ("2", "CHQ-REC-0013", "Ceylon Super Foods Hub", "CHQ-104928", "Sampath Bank (Borella)", "2026-10-28", "2026-11-10", "2026-11-10", "In 1 Day", "1,280,000.00", "Sampath Enterprise", "Deposited", (2, 132, 199), (240, 249, 255)),
    ("3", "CHQ-REC-0012", "Apex Global Logistics LK", "CHQ-559102", "Hatton National Bank (Pettah)", "2026-10-25", "2026-11-08", "2026-11-08", "Matured", "650,000.00", "HNB Corporate", "Realized", (22, 163, 74), (240, 253, 244)),
    ("4", "CHQ-REC-0011", "Metro Lanka Wholesale Dist.", "CHQ-338291", "Bank of Ceylon (Fort)", "2026-10-22", "2026-11-05", "2026-11-05", "Cleared", "820,000.00", "BOC Corporate", "Realized", (22, 163, 74), (240, 253, 244)),
    ("5", "CHQ-REC-0010", "Lanka Retail Hub Supermart", "CHQ-882103", "Nations Trust (Nugegoda)", "2026-11-04", "2026-11-15", "2026-11-15", "In 6 Days", "250,000.00", "Comm Bank Current", "In Hand", (255, 94, 20), (255, 247, 242)),
    ("6", "CHQ-REC-0009", "Greenfield Organic Spices", "CHQ-420915", "Seylan Bank (Maharagama)", "2026-10-18", "2026-11-02", "2026-11-02", "Cleared", "385,000.00", "Sampath Enterprise", "Realized", (22, 163, 74), (240, 253, 244)),
    ("7", "CHQ-REC-0008", "Highland Bakers & Mart", "CHQ-910482", "People's Bank (Kandy)", "2026-11-05", "2026-11-18", "2026-11-18", "In 9 Days", "510,000.00", "Comm Bank Current", "In Hand", (255, 94, 20), (255, 247, 242)),
    ("8", "CHQ-REC-0007", "Sunlight Hardware Emporium", "CHQ-294017", "Commercial Bank (Wattala)", "2026-10-15", "2026-11-01", "2026-11-01", "Cleared", "195,000.00", "HNB Corporate", "Realized", (22, 163, 74), (240, 253, 244))
]

# Exact header x centers:
# ID: 26, Ref: 60, Contact: 125, Cheque: 190, Bank: 266, PayDate: 395, ChqDate: 475, PDDate: 550, DueMon: 615, Amt: 710, Acc: 785, Status: 900, Action: 960
cy = 164
for i, (cid, ref, contact, chq_no, bank, p_dt, c_dt, pd_dt, due, amt, acc, st, st_col, st_bg) in enumerate(chq_rows):
    if i % 2 == 1:
        d_chq.rectangle([14, cy - 2, 1010, cy + 30], fill=(248, 250, 252, 255))
        
    d_chq.text((26, cy + 6), cid, font=f_r_xs, fill=(100, 116, 139, 255))
    d_chq.text((50, cy + 6), ref, font=f_b_xs, fill=(15, 23, 42, 255))
    d_chq.text((125, cy + 6), contact, font=f_b_xs, fill=(15, 23, 42, 255))
    d_chq.text((205, cy + 6), chq_no, font=f_b_xs, fill=(255, 94, 20, 255))
    d_chq.text((275, cy + 6), bank, font=f_r_xs, fill=(51, 65, 85, 255))
    d_chq.text((400, cy + 6), p_dt, font=f_r_xs, fill=(100, 116, 139, 255))
    d_chq.text((475, cy + 6), c_dt, font=f_r_xs, fill=(100, 116, 139, 255))
    d_chq.text((550, cy + 6), pd_dt, font=f_b_xs, fill=(15, 23, 42, 255))
    
    # Due monitor pill
    d_chq.rounded_rectangle([615, cy + 5, 665, cy + 22], radius=3, fill=(254, 243, 199, 255) if "In" in due else (240, 253, 244, 255))
    d_chq.text((620, cy + 6), due, font=f_b_xs, fill=(217, 119, 6, 255) if "In" in due else (22, 163, 74, 255))
    
    d_chq.text((710, cy + 6), amt, font=f_b_xs, fill=(15, 23, 42, 255))
    d_chq.text((785, cy + 6), acc, font=f_r_xs, fill=(71, 85, 105, 255))
    
    # Status badge
    d_chq.rounded_rectangle([895, cy + 5, 940, cy + 22], radius=3, fill=st_bg)
    d_chq.text((902, cy + 6), st, font=f_b_xs, fill=st_col)
    
    # Action button
    d_chq.rounded_rectangle([955, cy + 5, 1000, cy + 22], radius=3, fill=(255, 255, 255, 255), outline=(203, 213, 225, 255), width=1)
    d_chq.text((960, cy + 6), "Action ▾", font=f_b_xs, fill=(51, 65, 85, 255))
    
    d_chq.line([14, cy + 30, 1010, cy + 30], fill=(241, 245, 249, 255))
    cy += 32

# Table Footer
cfy = cy + 10
d_chq.text((18, cfy + 4), "Showing 1 to 8 of 8 entries", font=f_r_xs, fill=(100, 116, 139, 255))

d_chq.rounded_rectangle([875, cfy, 930, cfy + 24], radius=3, fill=(255, 255, 255, 255), outline=(226, 232, 240, 255), width=1)
d_chq.text((885, cfy + 4), "Previous", font=f_r_xs, fill=(148, 163, 184, 255))

d_chq.rounded_rectangle([936, cfy, 958, cfy + 24], radius=3, fill=(255, 94, 20, 255))
d_chq.text((944, cfy + 4), "1", font=f_b_xs, fill=(255, 255, 255, 255))

d_chq.rounded_rectangle([964, cfy, 1005, cfy + 24], radius=3, fill=(255, 255, 255, 255), outline=(226, 232, 240, 255), width=1)
d_chq.text((974, cfy + 4), "Next", font=f_r_xs, fill=(148, 163, 184, 255))

im_chq.save(os.path.join(out_dir, 'finance-cheques-ui.png'))
print('Saved finance-cheques-ui.png!')


# ==============================================================================
# 3. PROCESS ACCOUNTING DASHBOARD (media_1794224221742_673dd227.png)
# ==============================================================================
print('Processing Accounting Dashboard...')
im_acc = Image.open(p_acc).convert('RGBA')
d_acc = ImageDraw.Draw(im_acc)

# 3.1 Update top-right badges
# Replace "Accounting Off" (at x=893..938, y=23..38) with "Accounting Active" (Green)
d_acc.rounded_rectangle([860, 23, 936, 38], radius=3, fill=(22, 163, 74, 255))
d_acc.text((865, 25), "Accounting Active", font=f_b_xs, fill=(255, 255, 255, 255))

# 3.2 Update Row 1 KPI cards:
# Card 1: CASH & BANK (GL) (x ~ 10..255, y ~ 48..102) -> LKR 9,840,250.00
d_acc.rectangle([50, 70, 250, 95], fill=(255, 255, 255, 255))
d_acc.text((52, 70), "LKR 9,840,250.00", font=f_b_md, fill=(15, 23, 42, 255))

# Card 2: AR OUTSTANDING (x ~ 263..508) -> LKR 4,680,100.00
d_acc.rectangle([298, 70, 480, 95], fill=(255, 255, 255, 255))
d_acc.text((300, 70), "LKR 4,680,100.00", font=f_b_md, fill=(15, 23, 42, 255))

# Card 3: AP OUTSTANDING (x ~ 516..761) -> LKR 3,420,000.00
d_acc.rectangle([548, 70, 740, 95], fill=(255, 255, 255, 255))
d_acc.text((550, 70), "LKR 3,420,000.00", font=f_b_md, fill=(15, 23, 42, 255))

# Card 4: NET PROFIT (MTD) (x ~ 769..1014) -> LKR 2,450,800.00
d_acc.rectangle([798, 68, 1008, 98], fill=(255, 255, 255, 255))
d_acc.text((800, 68), "LKR 2,450,800.00", font=f_b_md, fill=(22, 163, 74, 255))
d_acc.text((800, 85), "Revenue LKR 6.28M - Expenses LKR 3.83M", font=f_r_xs, fill=(100, 116, 139, 255))

# 3.3 Update Row 2 KPI cards:
# Card 5: DRAFT JOURNALS -> 2
d_acc.rectangle([50, 130, 240, 155], fill=(255, 255, 255, 255))
d_acc.text((52, 130), "2", font=f_b_lg, fill=(15, 23, 42, 255))

# Card 6: POSTED JOURNALS (MTD) -> 48
d_acc.rectangle([298, 130, 480, 155], fill=(255, 255, 255, 255))
d_acc.text((300, 130), "48", font=f_b_lg, fill=(15, 23, 42, 255))

# Card 7: POS SALES TODAY -> 142
d_acc.rectangle([548, 130, 740, 155], fill=(255, 255, 255, 255))
d_acc.text((550, 130), "142", font=f_b_lg, fill=(15, 23, 42, 255))

# 3.4 Populate the Chart area (x=20..1005, y=200..450)
# Clear flat line area
d_acc.rectangle([25, 215, 1000, 455], fill=(255, 255, 255, 255))

# Update Y-axis labels at x=20..48
d_acc.rectangle([20, 210, 50, 455], fill=(255, 255, 255, 255))
d_acc.text((22, 230), "LKR 6M", font=f_r_xs, fill=(148, 163, 184, 255))
d_acc.text((22, 290), "LKR 4M", font=f_r_xs, fill=(148, 163, 184, 255))
d_acc.text((22, 350), "LKR 2M", font=f_r_xs, fill=(148, 163, 184, 255))
d_acc.text((22, 420), "LKR 0", font=f_r_xs, fill=(148, 163, 184, 255))

# Subtle grid lines
for gy in [238, 298, 358, 428]:
    d_acc.line([55, gy, 990, gy], fill=(241, 245, 249, 255), width=1)

# X coordinates for months:
# Jun 2026: 125, Jul 2026: 275, Aug 2026: 425, Sep 2026: 580, Oct 2026: 730, Nov 2026: 885
x_months = [125, 275, 425, 580, 730, 885]

# Data points:
# Revenue: 3.8M, 4.2M, 4.5M, 5.1M, 5.8M, 6.28M
# y mapping: 0 -> 428, 2M -> 358, 4M -> 298, 6M -> 238
# dy = (428 - 238) / 6 = 31.67 px per 1M
# y = 428 - val * 31.67
rev_vals = [3.8, 4.2, 4.5, 5.1, 5.8, 6.28]
exp_vals = [2.4, 2.7, 2.8, 3.1, 3.4, 3.83]

rev_pts = [(x, int(428 - v * 31.67)) for x, v in zip(x_months, rev_vals)]
exp_pts = [(x, int(428 - v * 31.67)) for x, v in zip(x_months, exp_vals)]

# Draw Revenue Line (Blue #2563EB)
for i in range(len(rev_pts) - 1):
    d_acc.line([rev_pts[i], rev_pts[i+1]], fill=(37, 99, 235, 255), width=3)
    
# Draw Expenses Line (Orange #FF5E14)
for i in range(len(exp_pts) - 1):
    d_acc.line([exp_pts[i], exp_pts[i+1]], fill=(255, 94, 20, 255), width=3)

# Draw points on Revenue
for x, y in rev_pts:
    d_acc.ellipse([x - 4, y - 4, x + 4, y + 4], fill=(255, 255, 255, 255), outline=(37, 99, 235, 255), width=2)

# Draw points on Expenses
for x, y in exp_pts:
    d_acc.ellipse([x - 4, y - 4, x + 4, y + 4], fill=(255, 255, 255, 255), outline=(255, 94, 20, 255), width=2)

# Draw high-impact interactive tooltip over November point (x=885)
tooltip_x = 810
tooltip_y = 195
d_acc.rounded_rectangle([tooltip_x, tooltip_y, tooltip_x + 175, tooltip_y + 60], radius=5, fill=(15, 23, 42, 245))
d_acc.text((tooltip_x + 10, tooltip_y + 6), "November 2026 Fiscal", font=f_b_xs, fill=(255, 255, 255, 255))
d_acc.text((tooltip_x + 10, tooltip_y + 22), "● Revenue: LKR 6,280,000", font=f_r_xs, fill=(147, 197, 253, 255))
d_acc.text((tooltip_x + 10, tooltip_y + 36), "● Expenses: LKR 3,829,200", font=f_r_xs, fill=(254, 215, 170, 255))
d_acc.text((tooltip_x + 10, tooltip_y + 49), "✔ Net Margin: +39.0%", font=f_b_xs, fill=(134, 239, 172, 255))

# Tooltip pointer down to Nov rev point
d_acc.line([885, tooltip_y + 60, 885, rev_pts[-1][1] - 4], fill=(15, 23, 42, 180), width=1)

im_acc.save(os.path.join(out_dir, 'finance-accounting-ui.png'))
print('Saved finance-accounting-ui.png!')

