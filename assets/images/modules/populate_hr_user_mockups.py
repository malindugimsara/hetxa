import os
from PIL import Image, ImageDraw, ImageFont

p1 = r'C:/Users/MG/.gemini/antigravity/brain/a68b6681-cdc2-4b67-b620-e6b76a258d07/.user_uploaded/media_1794456592505_944f0d95.png'
p2 = r'C:/Users/MG/.gemini/antigravity/brain/a68b6681-cdc2-4b67-b620-e6b76a258d07/.user_uploaded/media_1794456631833_ee0adc43.png'
p3 = r'C:/Users/MG/.gemini/antigravity/brain/a68b6681-cdc2-4b67-b620-e6b76a258d07/.user_uploaded/media_1794456673633_7aa60c4a.png'

out_dir = r'c:/xampp/htdocs/hetxa/assets/images/modules'
os.makedirs(out_dir, exist_ok=True)

# Standard Fonts
f_b_xl = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 19)
f_b_lg = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 14)
f_b_md = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 11.5)
f_b_sm = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 9.5)
f_b_xs = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 8.5)

f_r_md = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 11)
f_r_sm = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 9.5)
f_r_xs = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 8)

# ==============================================================================
# 1. PROCESS HR DASHBOARD (media_1794456592505_944f0d95.png)
# ==============================================================================
print('Processing HR Dashboard...')
im1 = Image.open(p1).convert('RGBA')
d1 = ImageDraw.Draw(im1)

# Card 1: Headcount (x: 14 to 256, y: 196 to 260)
# Replace "0" and "Active and on leave in range"
d1.rectangle([16, 218, 120, 248], fill=(255, 255, 255, 255))
d1.text((22, 218), '88', font=f_b_xl, fill=(15, 23, 42, 255))
d1.rectangle([16, 248, 180, 260], fill=(255, 255, 255, 255))
d1.text((22, 248), '84 Active • 4 On leave', font=f_r_xs, fill=(100, 116, 139, 255))

# Card 2: Attendance rate (x: 266 to 509)
d1.rectangle([270, 218, 380, 248], fill=(255, 255, 255, 255))
d1.text((272, 218), '96.4%', font=f_b_xl, fill=(15, 23, 42, 255))
d1.rectangle([270, 248, 420, 260], fill=(255, 255, 255, 255))
d1.text((272, 248), '2 late arrivals (within grace)', font=f_r_xs, fill=(100, 116, 139, 255))
# Top right badge "0 present" -> "84 present"
d1.rectangle([440, 196, 500, 210], fill=(255, 255, 255, 255))
d1.text((442, 198), '84 present', font=f_r_xs, fill=(22, 101, 52, 255))

# Card 3: Leave used (x: 518 to 761)
d1.rectangle([522, 218, 620, 248], fill=(255, 255, 255, 255))
d1.text((524, 218), '14 days', font=f_b_xl, fill=(15, 23, 42, 255))
d1.rectangle([522, 248, 680, 260], fill=(255, 255, 255, 255))
d1.text((524, 248), 'Approved leave in period', font=f_r_xs, fill=(100, 116, 139, 255))
# Top right "0 pending" -> "2 pending"
d1.rectangle([695, 196, 755, 210], fill=(255, 255, 255, 255))
d1.text((697, 198), '2 pending', font=f_r_xs, fill=(234, 88, 12, 255))

# Card 4: Attendance gaps (x: 770 to 1014)
d1.rectangle([774, 218, 850, 248], fill=(255, 255, 255, 255))
d1.text((776, 218), '1', font=f_b_xl, fill=(15, 23, 42, 255))
d1.rectangle([774, 248, 920, 260], fill=(255, 255, 255, 255))
d1.text((776, 248), '1 missing out • 0 missing in', font=f_r_xs, fill=(100, 116, 139, 255))

# Mini chips (y: 268 to 290)
# Chip 1: Unmarked absence cost LKR 0 -> LKR 12,400
d1.rectangle([105, 271, 150, 287], fill=(255, 255, 255, 255))
d1.text((106, 273), 'LKR 12,400', font=f_b_xs, fill=(220, 38, 38, 255))

# Chip 3: Open notices 0 -> 3
d1.rectangle([570, 271, 595, 287], fill=(255, 255, 255, 255))
d1.text((571, 273), '3', font=f_b_xs, fill=(37, 99, 235, 255))

# Attendance by week graph area (y: 350 to 500, x: 25 to 620)
# Draw realistic bar columns for Week 1, Week 2, Week 3, Week 4
d1.rectangle([35, 360, 620, 500], fill=(255, 255, 255, 255))
weeks = [
    ('Week 1 (Nov 1-7)', 82, 3, 1),
    ('Week 2 (Nov 8-14)', 84, 2, 0),
    ('Week 3 (Nov 15-21)', 85, 1, 1),
    ('Week 4 (Nov 22-28)', 83, 2, 1)
]
for w_idx, (w_label, pres, late, miss) in enumerate(weeks):
    wx = 55 + w_idx * 140
    # Bar for present
    h_pres = int((pres / 88) * 95)
    d1.rounded_rectangle([wx, 470 - h_pres, wx + 40, 470], radius=4, fill=(59, 130, 246, 230))
    d1.text((wx + 8, 470 - h_pres - 14), f'{pres}', font=f_b_xs, fill=(37, 99, 235, 255))
    
    # Small bar for late
    h_late = int((late / 88) * 95)
    d1.rounded_rectangle([wx + 44, 470 - max(8, h_late), wx + 62, 470], radius=3, fill=(245, 158, 11, 230))
    
    # Label
    d1.text((wx, 476), w_label.split(' ')[0], font=f_r_xs, fill=(100, 116, 139, 255))

# Team Status: Workforce (x: 645 to 1010, y: 350 to 500)
d1.rectangle([645, 350, 1010, 500], fill=(255, 255, 255, 255))
depts = [
    ('Retail POS & Counters', '34 Staff', '100% Present', (16, 185, 129)),
    ('Warehouse & Inventory', '22 Staff', '95.5% (1 On Leave)', (16, 185, 129)),
    ('Sales & Wholesale Reps', '18 Staff', '94.4% (1 On Leave)', (16, 185, 129)),
    ('Finance & Administration', '14 Staff', '100% Present', (16, 185, 129))
]
for d_idx, (dname, dstaff, dstat, dcol) in enumerate(depts):
    dy = 356 + d_idx * 33
    d1.text((652, dy), dname, font=f_b_xs, fill=(15, 23, 42, 255))
    d1.text((652, dy + 14), dstaff, font=f_r_xs, fill=(100, 116, 139, 255))
    d1.text((915, dy + 6), dstat, font=f_b_xs, fill=dcol)
    d1.line([652, dy + 28, 1000, dy + 28], fill=(241, 245, 249, 255))

im1.save(os.path.join(out_dir, 'hr-dashboard-ui.png'), 'PNG')
print('Saved hr-dashboard-ui.png')

# ==============================================================================
# 2. PROCESS ATTENDANCE TABLE (media_1794456631833_ee0adc43.png)
# ==============================================================================
print('Processing HR Attendance...')
im2 = Image.open(p2).convert('RGBA')
d2 = ImageDraw.Draw(im2)

# Stat cards at top
# Card 1: Rows 0 -> 88
d2.rectangle([14, 115, 60, 138], fill=(255, 255, 255, 255))
d2.text((16, 117), '88', font=f_b_xl, fill=(15, 23, 42, 255))

# Card 2: Missing out 0 -> 1
d2.rectangle([264, 115, 310, 138], fill=(255, 255, 255, 255))
d2.text((266, 117), '1', font=f_b_xl, fill=(220, 38, 38, 255))

# Card 3: Late 0 -> 2
d2.rectangle([518, 115, 560, 138], fill=(255, 255, 255, 255))
d2.text((520, 117), '2', font=f_b_xl, fill=(234, 88, 12, 255))

# Card 4: Self punches 0 -> 18
d2.rectangle([770, 115, 820, 138], fill=(255, 255, 255, 255))
d2.text((772, 117), '18', font=f_b_xl, fill=(37, 99, 235, 255))

# Table area: Clear from y=260 to y=490
d2.rectangle([14, 260, 1007, 490], fill=(255, 255, 255, 255))

# Table Header
th_y = 262
d2.rectangle([14, th_y, 1007, th_y + 26], fill=(248, 250, 252, 255))
d2.line([14, th_y + 26, 1007, th_y + 26], fill=(226, 232, 240, 255))

cols_att = [
    (24, 'DATE'),
    (100, 'EMPLOYEE'),
    (235, 'DEPARTMENT'),
    (385, 'IN'),
    (455, 'OUT'),
    (525, 'WORKED'),
    (595, 'LATE'),
    (655, 'OT MIN'),
    (725, 'SOURCE'),
    (835, 'LOCATION'),
    (945, 'STATUS')
]
for x, cname in cols_att:
    d2.text((x, th_y + 7), cname, font=f_b_xs, fill=(100, 116, 139, 255))

att_rows = [
    ('2026-11-12', 'Kasun Perera (EMP-1042)', 'Warehouse / Col', '08:24 AM', '17:35 PM', '8h 11m', '0m', '+30m', 'Fingerprint', 'Central WH', 'Present', (22, 101, 52)),
    ('2026-11-12', 'Nadeesha Silva (EMP-1043)', 'Finance & Accounts', '08:52 AM', '18:05 PM', '8h 13m', '0m', '0m', 'Face Scan', 'Head Office', 'Present', (22, 101, 52)),
    ('2026-11-12', 'Mohamed Farhan (EMP-1044)', 'Retail POS / Kandy', '09:41 AM', '19:30 PM', '8h 49m', '11m', '0m', 'Biometric', 'Kandy Outlet', 'Late (Grace)', (180, 83, 9)),
    ('2026-11-12', 'Dilini Jayawardena (EMP-1045)', 'Human Resources', '08:55 AM', '18:00 PM', '8h 05m', '0m', '0m', 'Face Scan', 'Head Office', 'Present', (22, 101, 52)),
    ('2026-11-12', 'Nuwan Wickrama (EMP-1046)', 'Sales & Distribution', '07:58 AM', '17:15 PM', '8h 17m', '0m', '+15m', 'RFID Card', 'Galle Hub', 'Present', (22, 101, 52)),
    ('2026-11-12', 'Chamari Fernando (EMP-1047)', 'Procurement & Stock', '--:--', '--:--', '0h 00m', '--', '--', 'Portal', 'Colombo', 'On Leave', (29, 78, 216)),
    ('2026-11-12', 'Ravindu Bandara (EMP-1048)', 'IT Infrastructure', '09:50 AM', '19:10 PM', '8h 20m', '0m', '+10m', 'Face Scan', 'Head Office', 'Present', (22, 101, 52))
]

for r_idx, (dt, emp, dept, t_in, t_out, wrk, lte, ot, src, loc, st, scol) in enumerate(att_rows):
    ry = th_y + 27 + r_idx * 31
    if r_idx % 2 == 1:
        d2.rectangle([14, ry, 1007, ry + 30], fill=(248, 250, 252, 255))
    d2.line([14, ry + 30, 1007, ry + 30], fill=(241, 245, 249, 255))
    
    d2.text((24, ry + 8), dt, font=f_r_xs, fill=(71, 85, 105, 255))
    d2.text((100, ry + 8), emp, font=f_b_xs, fill=(15, 23, 42, 255))
    d2.text((235, ry + 8), dept, font=f_r_xs, fill=(71, 85, 105, 255))
    d2.text((385, ry + 8), t_in, font=f_b_xs, fill=(22, 101, 52, 255) if 'AM' in t_in else (100, 116, 139, 255))
    d2.text((455, ry + 8), t_out, font=f_r_xs, fill=(71, 85, 105, 255))
    d2.text((525, ry + 8), wrk, font=f_b_xs, fill=(15, 23, 42, 255))
    d2.text((595, ry + 8), lte, font=f_r_xs, fill=(220, 38, 38, 255) if lte != '0m' and lte != '--' else (100, 116, 139, 255))
    d2.text((655, ry + 8), ot, font=f_r_xs, fill=(37, 99, 235, 255) if '+' in ot else (100, 116, 139, 255))
    d2.text((725, ry + 8), src, font=f_r_xs, fill=(71, 85, 105, 255))
    d2.text((835, ry + 8), loc, font=f_r_xs, fill=(71, 85, 105, 255))
    
    # Status pill
    if 'Present' in st:
        p_bg, p_border, p_col = (240, 253, 244, 255), (187, 247, 208, 255), (22, 101, 52, 255)
    elif 'Late' in st:
        p_bg, p_border, p_col = (254, 252, 232, 255), (254, 240, 138, 255), (180, 83, 9, 255)
    else:
        p_bg, p_border, p_col = (239, 246, 255, 255), (191, 219, 254, 255), (29, 78, 216, 255)
    d2.rounded_rectangle([940, ry + 6, 1000, ry + 24], radius=3, fill=p_bg, outline=p_border, width=1)
    d2.text((945, ry + 8), st.split(' ')[0], font=f_b_xs, fill=p_col)

# Bottom info text
d2.rectangle([14, 490, 400, 520], fill=(255, 255, 255, 255))
d2.text((16, 496), 'Showing 1 to 7 of 88 entries (Real-Time Biometric Cloud)', font=f_r_xs, fill=(100, 116, 139, 255))

im2.save(os.path.join(out_dir, 'hr-attendance-ui.png'), 'PNG')
print('Saved hr-attendance-ui.png')

# ==============================================================================
# 3. PROCESS PAYROLL RECENT RUNS (media_1794456673633_7aa60c4a.png)
# ==============================================================================
print('Processing HR Payroll...')
im3 = Image.open(p3).convert('RGBA')
d3 = ImageDraw.Draw(im3)

# Clear right card "No data available in table"
# Right card table body: from x: 345 to 1010, y: 220 to 480
d3.rectangle([346, 220, 1010, 480], fill=(255, 255, 255, 255))

# Table Header
th_y = 195
d3.rectangle([346, th_y, 1010, th_y + 24], fill=(248, 250, 252, 255))
d3.line([346, th_y + 24, 1010, th_y + 24], fill=(226, 232, 240, 255))

cols_pay = [
    (360, 'PAYROLL PERIOD'),
    (495, 'RUN STATUS'),
    (645, 'EMPLOYEES'),
    (740, 'GROSS DISBURSEMENT'),
    (910, 'BANK FILE')
]
for x, cname in cols_pay:
    d3.text((x, th_y + 6), cname, font=f_b_xs, fill=(100, 116, 139, 255))

pay_runs = [
    ('November 2026', 'In Progress (Draft)', '88 Staff', 'LKR 4,820,000.00', 'Pending Freeze', (234, 88, 12)),
    ('October 2026', 'Finalized & Paid', '88 Staff', 'LKR 4,785,000.00', 'COMB/BOC Uploaded', (22, 101, 52)),
    ('September 2026', 'Finalized & Paid', '86 Staff', 'LKR 4,680,000.00', 'C-Form Submitted', (22, 101, 52)),
    ('August 2026', 'Finalized & Paid', '85 Staff', 'LKR 4,610,000.00', 'Form II Remitted', (22, 101, 52)),
    ('July 2026', 'Finalized & Paid', '84 Staff', 'LKR 4,550,000.00', 'EPF/ETF Cleared', (22, 101, 52)),
    ('June 2026', 'Finalized & Paid', '83 Staff', 'LKR 4,490,000.00', 'Bank Transferred', (22, 101, 52)),
    ('May 2026', 'Finalized & Paid', '82 Staff', 'LKR 4,420,000.00', 'Archived', (100, 116, 139))
]

for r_idx, (prd, r_st, emps, amt, bfile, rcol) in enumerate(pay_runs):
    ry = th_y + 25 + r_idx * 35
    if r_idx % 2 == 1:
        d3.rectangle([346, ry, 1010, ry + 34], fill=(248, 250, 252, 255))
    d3.line([346, ry + 34, 1010, ry + 34], fill=(241, 245, 249, 255))
    
    d3.text((360, ry + 9), prd, font=f_b_sm, fill=(15, 23, 42, 255))
    
    # Status pill
    if 'Finalized' in r_st:
        p_bg, p_border, p_col = (240, 253, 244, 255), (187, 247, 208, 255), (22, 101, 52, 255)
    else:
        p_bg, p_border, p_col = (255, 247, 237, 255), (254, 215, 170, 255), (194, 65, 12, 255)
    d3.rounded_rectangle([490, ry + 7, 615, ry + 26], radius=3, fill=p_bg, outline=p_border, width=1)
    d3.text((498, ry + 9), r_st, font=f_b_xs, fill=p_col)
    
    d3.text((645, ry + 9), emps, font=f_r_sm, fill=(71, 85, 105, 255))
    d3.text((740, ry + 9), amt, font=f_b_sm, fill=(15, 23, 42, 255))
    
    # Bank file pill
    d3.rounded_rectangle([905, ry + 7, 1000, ry + 26], radius=3, fill=(241, 245, 249, 255), outline=(203, 213, 225, 255), width=1)
    d3.text((912, ry + 9), bfile, font=f_b_xs, fill=(51, 65, 85, 255))

# Bottom info text
d3.rectangle([346, 480, 600, 520], fill=(255, 255, 255, 255))
d3.text((350, 488), 'Showing 1 to 7 of 24 monthly runs (Statutory History)', font=f_r_xs, fill=(100, 116, 139, 255))

im3.save(os.path.join(out_dir, 'hr-payroll-ui.png'), 'PNG')
print('Saved hr-payroll-ui.png')
print('ALL 3 HR MOCKUPS POPULATED AND SAVED CLEANLY!')

