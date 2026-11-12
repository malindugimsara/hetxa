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
# 1. PAYROLL & STATUTORY EPF/ETF MOCKUP
# ==============================================================================
print('Generating hr-payroll-ui.png...')
im_pay, d_pay = create_base_canvas(
    'Monthly Statutory Payroll & EPF/ETF Processing',
    'Home  »  HR  »  Pay  »  Monthly Payroll Processing (Nov 2026)',
    'Export Bank Upload',
    '+ Process Month End'
)

# Stat Cards
card_w = (W - 40 - 36) // 4
card_h = 74
top_y = 66
stats_pay = [
    ('TOTAL GROSS SALARIES', 'LKR 4,820,000', '88 Active Employees', (255, 94, 20)),
    ('EPF POOL (8% + 12%)', 'LKR 964,000', '100% C-Form Compliant', (37, 99, 235)),
    ('ETF POOL (3%)', 'LKR 144,600', 'Form II Schedule Ready', (16, 185, 129)),
    ('NET BANK DISBURSEMENT', 'LKR 4,120,400', 'BOC, COMB, HNB Ready', (15, 23, 42))
]

for i, (label, val, sub, col) in enumerate(stats_pay):
    cx = 20 + i * (card_w + 12)
    d_pay.rounded_rectangle([cx, top_y, cx + card_w, top_y + card_h], radius=7, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d_pay.rectangle([cx + 1, top_y + 1, cx + 4, top_y + card_h - 1], fill=col)
    d_pay.text((cx + 14, top_y + 10), label, font=f_b_xs, fill=(100, 116, 139))
    d_pay.text((cx + 14, top_y + 25), val, font=f_b_lg, fill=(15, 23, 42))
    d_pay.text((cx + 14, top_y + 49), sub, font=f_r_xs, fill=(100, 116, 139))

# Table Card
tbl_y = top_y + card_h + 14
tbl_h = H - tbl_y - 15
d_pay.rounded_rectangle([20, tbl_y, W - 20, tbl_y + tbl_h], radius=7, fill=(255, 255, 255), outline=(226, 232, 240), width=1)

# Filter Bar inside Table
d_pay.text((36, tbl_y + 14), 'Employee Payroll Register (88 Records)', font=f_b_md, fill=(15, 23, 42))
d_pay.rounded_rectangle([W - 380, tbl_y + 10, W - 180, tbl_y + 34], radius=4, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
d_pay.text((W - 370, tbl_y + 16), 'Search by Name or NIC...', font=f_r_xs, fill=(148, 163, 184))
d_pay.rounded_rectangle([W - 170, tbl_y + 10, W - 36, tbl_y + 34], radius=4, fill=(255, 255, 255), outline=(203, 213, 225), width=1)
d_pay.text((W - 158, tbl_y + 16), 'Filter: All Branches', font=f_b_xs, fill=(71, 85, 105))

# Table Header
th_y = tbl_y + 44
d_pay.rectangle([20, th_y, W - 20, th_y + 28], fill=(241, 245, 249))
d_pay.line([20, th_y + 28, W - 20, th_y + 28], fill=(226, 232, 240))

cols_pay = [
    (36, 'EMP ID & NAME'),
    (240, 'DEPARTMENT'),
    (370, 'BASIC (LKR)'),
    (475, 'EPF 8%'),
    (560, 'EPF 12%'),
    (650, 'ETF 3%'),
    (740, 'APIT TAX'),
    (835, 'NET SALARY'),
    (935, 'BANK FILE')
]
for x, name in cols_pay:
    d_pay.text((x, th_y + 8), name, font=f_b_xs, fill=(100, 116, 139))

rows_pay = [
    ('EMP-1042', 'Kasun Perera', 'Warehouse / Colombo', '125,000.00', '10,000.00', '15,000.00', '3,750.00', '0.00', '132,450.00', 'COMB Ready', (16, 185, 129)),
    ('EMP-1043', 'Nadeesha Silva', 'Finance & Accounts', '185,000.00', '14,800.00', '22,200.00', '5,550.00', '3,500.00', '188,700.00', 'BOC Ready', (16, 185, 129)),
    ('EMP-1044', 'Mohamed Farhan', 'Retail POS / Kandy', '95,000.00', '7,600.00', '11,400.00', '2,850.00', '0.00', '104,200.00', 'Sampath Ready', (16, 185, 129)),
    ('EMP-1045', 'Dilini Jayawardena', 'Human Resources', '140,000.00', '11,200.00', '16,800.00', '4,200.00', '1,200.00', '148,600.00', 'HNB Ready', (16, 185, 129)),
    ('EMP-1046', 'Nuwan Wickramasinghe', 'Sales & Distribution', '160,000.00', '12,800.00', '19,200.00', '4,800.00', '2,400.00', '174,300.00', 'COMB Ready', (16, 185, 129)),
    ('EMP-1047', 'Chamari Fernando', 'Procurement & Stock', '110,000.00', '8,800.00', '13,200.00', '3,300.00', '0.00', '119,400.00', 'BOC Ready', (16, 185, 129)),
    ('EMP-1048', 'Ravindu Bandara', 'IT & Infrastructure', '175,000.00', '14,000.00', '21,000.00', '5,250.00', '3,000.00', '186,000.00', 'HNB Ready', (16, 185, 129)),
]

for r_idx, (eid, name, dept, basic, epf8, epf12, etf3, apit, net, bstatus, bcol) in enumerate(rows_pay):
    ry = th_y + 29 + r_idx * 38
    d_pay.line([20, ry + 37, W - 20, ry + 37], fill=(241, 245, 249))
    d_pay.text((36, ry + 6), name, font=f_b_sm, fill=(15, 23, 42))
    d_pay.text((36, ry + 20), eid, font=f_r_xs, fill=(148, 163, 184))
    d_pay.text((240, ry + 12), dept, font=f_r_sm, fill=(71, 85, 105))
    d_pay.text((370, ry + 12), basic, font=f_r_sm, fill=(15, 23, 42))
    d_pay.text((475, ry + 12), epf8, font=f_r_sm, fill=(220, 38, 38))
    d_pay.text((560, ry + 12), epf12, font=f_r_sm, fill=(37, 99, 235))
    d_pay.text((650, ry + 12), etf3, font=f_r_sm, fill=(16, 185, 129))
    d_pay.text((740, ry + 12), apit, font=f_r_sm, fill=(100, 116, 139))
    d_pay.text((835, ry + 12), net, font=f_b_sm, fill=(15, 23, 42))
    
    # Bank pill
    d_pay.rounded_rectangle([930, ry + 9, 1005, ry + 27], radius=3, fill=(240, 253, 244), outline=(187, 247, 208), width=1)
    d_pay.text((937, ry + 13), bstatus, font=f_b_xs, fill=(22, 101, 52))

im_pay.save(os.path.join(out_dir, 'hr-payroll-ui.png'), 'PNG')
print('Saved hr-payroll-ui.png')

# ==============================================================================
# 2. TIME & BIOMETRIC ATTENDANCE MOCKUP
# ==============================================================================
print('Generating hr-attendance-ui.png...')
im_att, d_att = create_base_canvas(
    'Time & Multi-Branch Biometric Attendance Log',
    'Home  »  HR  »  Time  »  Live Biometric Device Feeds & Shifts',
    'Sync All Devices',
    'Generate Roster'
)

# Stat Cards
stats_att = [
    ('ON-DUTY STAFF TODAY', '84 / 88 (95.4%)', 'Across 4 Main Branches', (16, 185, 129)),
    ('LATE ARRIVALS', '2 Staff', 'Within 15-min Grace Period', (234, 179, 8)),
    ('APPROVED LEAVES', '4 Staff', '3 Annual, 1 Medical Leave', (59, 130, 246)),
    ('BIOMETRIC TERMINALS', '6 / 6 Connected', 'ZKTeco & Hikvision Live', (255, 94, 20))
]

for i, (label, val, sub, col) in enumerate(stats_att):
    cx = 20 + i * (card_w + 12)
    d_att.rounded_rectangle([cx, top_y, cx + card_w, top_y + card_h], radius=7, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d_att.rectangle([cx + 1, top_y + 1, cx + 4, top_y + card_h - 1], fill=col)
    d_att.text((cx + 14, top_y + 10), label, font=f_b_xs, fill=(100, 116, 139))
    d_att.text((cx + 14, top_y + 25), val, font=f_b_lg, fill=(15, 23, 42))
    d_att.text((cx + 14, top_y + 49), sub, font=f_r_xs, fill=(100, 116, 139))

# Table Card
d_att.rounded_rectangle([20, tbl_y, W - 20, tbl_y + tbl_h], radius=7, fill=(255, 255, 255), outline=(226, 232, 240), width=1)

d_att.text((36, tbl_y + 14), 'Live Biometric In/Out Feed — Real Time Sync', font=f_b_md, fill=(15, 23, 42))
d_att.rounded_rectangle([W - 380, tbl_y + 10, W - 180, tbl_y + 34], radius=4, fill=(248, 250, 252), outline=(226, 232, 240), width=1)
d_att.text((W - 370, tbl_y + 16), 'Search Employee or Punch ID...', font=f_r_xs, fill=(148, 163, 184))
d_att.rounded_rectangle([W - 170, tbl_y + 10, W - 36, tbl_y + 34], radius=4, fill=(255, 255, 255), outline=(203, 213, 225), width=1)
d_att.text((W - 158, tbl_y + 16), 'Status: All Logs', font=f_b_xs, fill=(71, 85, 105))

# Table Header
d_att.rectangle([20, th_y, W - 20, th_y + 28], fill=(241, 245, 249))
d_att.line([20, th_y + 28, W - 20, th_y + 28], fill=(226, 232, 240))

cols_att = [
    (36, 'EMPLOYEE & ID'),
    (240, 'BRANCH OUTLET'),
    (390, 'ROSTER SHIFT'),
    (520, 'CHECK-IN (BIOMETRIC)'),
    (670, 'CHECK-OUT'),
    (790, 'WORKED / OT'),
    (925, 'PUNCH STATUS')
]
for x, name in cols_att:
    d_att.text((x, th_y + 8), name, font=f_b_xs, fill=(100, 116, 139))

rows_att = [
    ('EMP-1042', 'Kasun Perera', 'Warehouse / Colombo', 'Morning (08:30 - 17:30)', '08:24 AM (Fingerprint)', '17:35 PM', '8h 11m / +0.5h OT', 'Present (On-Time)', (16, 185, 129)),
    ('EMP-1043', 'Nadeesha Silva', 'Head Office / Colombo', 'Standard (09:00 - 18:00)', '08:52 AM (Face Scan)', 'In Progress', 'Running...', 'Present (On-Time)', (16, 185, 129)),
    ('EMP-1044', 'Mohamed Farhan', 'Retail Outlet / Kandy', 'Counter A (09:30 - 19:30)', '09:41 AM (Fingerprint)', 'In Progress', 'Running...', 'Late (Grace 11m)', (234, 179, 8)),
    ('EMP-1045', 'Dilini Jayawardena', 'Head Office / Colombo', 'Standard (09:00 - 18:00)', '08:55 AM (Face Scan)', 'In Progress', 'Running...', 'Present (On-Time)', (16, 185, 129)),
    ('EMP-1046', 'Nuwan Wickramasinghe', 'Galle Distribution Hub', 'Logistics (08:00 - 17:00)', '07:58 AM (RFID Card)', 'In Progress', 'Running...', 'Present (On-Time)', (16, 185, 129)),
    ('EMP-1047', 'Chamari Fernando', 'Warehouse / Colombo', 'Morning (08:30 - 17:30)', '-- On Approved Leave --', '--', '0h 00m (Annual)', 'Approved Leave', (59, 130, 246)),
    ('EMP-1048', 'Ravindu Bandara', 'Head Office / Colombo', 'Tech Shift (10:00 - 19:00)', '09:50 AM (Face Scan)', 'In Progress', 'Running...', 'Present (On-Time)', (16, 185, 129)),
]

for r_idx, (eid, name, branch, shift, cin, cout, wot, status, scol) in enumerate(rows_att):
    ry = th_y + 29 + r_idx * 38
    d_att.line([20, ry + 37, W - 20, ry + 37], fill=(241, 245, 249))
    d_att.text((36, ry + 6), name, font=f_b_sm, fill=(15, 23, 42))
    d_att.text((36, ry + 20), eid, font=f_r_xs, fill=(148, 163, 184))
    d_att.text((240, ry + 12), branch, font=f_r_sm, fill=(71, 85, 105))
    d_att.text((390, ry + 12), shift, font=f_r_sm, fill=(15, 23, 42))
    d_att.text((520, ry + 12), cin, font=f_r_sm, fill=(22, 101, 52) if '0' in cin else (100, 116, 139))
    d_att.text((670, ry + 12), cout, font=f_r_sm, fill=(71, 85, 105))
    d_att.text((790, ry + 12), wot, font=f_b_sm, fill=(15, 23, 42))
    
    # Status pill
    if 'Late' in status:
        bg, border, tc = (254, 252, 232), (254, 240, 138), (161, 98, 7)
    elif 'Leave' in status:
        bg, border, tc = (239, 246, 255), (191, 219, 254), (29, 78, 216)
    else:
        bg, border, tc = (240, 253, 244), (187, 247, 208), (22, 101, 52)
        
    d_att.rounded_rectangle([920, ry + 9, 1010, ry + 27], radius=3, fill=bg, outline=border, width=1)
    d_att.text((927, ry + 13), status, font=f_b_xs, fill=tc)

im_att.save(os.path.join(out_dir, 'hr-attendance-ui.png'), 'PNG')
print('Saved hr-attendance-ui.png')
print('All HR mockups generated successfully!')

