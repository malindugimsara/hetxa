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

# ==============================================================================
# 1. VISUAL KANBAN TASK BOARD MOCKUP (project-kanban-ui.png)
# ==============================================================================
print('Generating project-kanban-ui.png...')
im_kan, d_kan = create_base_canvas(
    'Interactive Kanban Board — Sprint 42',
    'Home  »  Projects & Tasks  »  Tasks  »  Kanban View',
    '+ Create Task',
    'Filter Assignees'
)

# 4 Columns for Kanban
cols_kan = [
    ("BACKLOG", "4 Tasks", (100, 116, 139), [
        ("Design Bluetooth Printer SDK Layout", "PRJ-0042", "High", (239, 68, 68), "Danushka M.", "3 Subtasks", "Nov 15"),
        ("Setup Barcode Scanner Webhook Endpoint", "PRJ-0041", "Medium", (217, 119, 6), "Sanduni P.", "2 Subtasks", "Nov 18"),
        ("Audit Item Variant Pricing Matrix", "PRJ-0040", "Low", (2, 132, 199), "Kasun T.", "1 Subtask", "Nov 20")
    ]),
    ("IN PROGRESS", "3 Active", (255, 94, 20), [
        ("Implement 80mm Thermal Receipt Layout", "PRJ-0042", "Urgent", (239, 68, 68), "Nuwan S.", "4/5 Checklist (80%)", "Nov 11"),
        ("Customer Loyalty QR Code Generator", "PRJ-0042", "High", (239, 68, 68), "Sanduni P.", "3/4 Checklist (75%)", "Nov 12"),
        ("Multi-Currency Split Payment Modal", "PRJ-0042", "Medium", (217, 119, 6), "Danushka M.", "5/6 Checklist (83%)", "Nov 10")
    ]),
    ("UNDER REVIEW", "2 QA Ready", (2, 132, 199), [
        ("Cash Drawer Kick-Out Relay Test", "PRJ-0041", "High", (239, 68, 68), "QA Lead", "3/3 Verified", "Nov 10"),
        ("Post-Dated Cheque Maturity Alert Logs", "PRJ-0040", "Medium", (217, 119, 6), "QA Lead", "5/5 Verified", "Nov 09")
    ]),
    ("COMPLETED", "8 Done", (22, 163, 74), [
        ("IRD RAMIS VAT Invoice XML Formatting", "PRJ-0040", "Urgent", (239, 68, 68), "Nuwan S.", "✔ Completed Nov 08", "Done"),
        ("LankaQR Dynamic Image Generator", "PRJ-0042", "High", (239, 68, 68), "Sanduni P.", "✔ Completed Nov 07", "Done"),
        ("Product Master 10,000 SKU Import Script", "PRJ-0041", "Medium", (217, 119, 6), "Danushka M.", "✔ Completed Nov 06", "Done")
    ])
]

col_w = (W - 40 - 36) // 4
for ci, (col_title, col_count, col_color, cards) in enumerate(cols_kan):
    col_x = 20 + ci * (col_w + 12)
    col_y = 66
    
    # Column Container
    d_kan.rounded_rectangle([col_x, col_y, col_x + col_w, H - 15], radius=6, fill=(241, 245, 249), outline=(226, 232, 240), width=1)
    
    # Column Header
    d_kan.rounded_rectangle([col_x, col_y, col_x + col_w, col_y + 36], radius=6, fill=(255, 255, 255))
    d_kan.rounded_rectangle([col_x, col_y, col_x + col_w, col_y + 3], radius=1, fill=col_color)
    d_kan.text((col_x + 12, col_y + 11), col_title, font=f_b_xs, fill=(15, 23, 42))
    
    # Count badge
    d_kan.rounded_rectangle([col_x + col_w - 65, col_y + 9, col_x + col_w - 10, col_y + 26], radius=10, fill=(241, 245, 249))
    d_kan.text((col_x + col_w - 58, col_y + 11), col_count, font=f_b_xs, fill=col_color)
    d_kan.line([col_x, col_y + 36, col_x + col_w, col_y + 36], fill=(226, 232, 240))
    
    # Task Cards
    card_y = col_y + 44
    for title, prj, prio, p_col, assignee, subtasks, due in cards:
        d_kan.rounded_rectangle([col_x + 8, card_y, col_x + col_w - 8, card_y + 105], radius=5, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
        
        # Priority Pill
        d_kan.rounded_rectangle([col_x + 16, card_y + 8, col_x + 65, card_y + 22], radius=3, fill=(254, 242, 242) if prio == "Urgent" or prio == "High" else (240, 249, 255))
        d_kan.text((col_x + 22, card_y + 9), prio, font=f_b_xs, fill=p_col)
        
        # Project tag
        d_kan.text((col_x + 72, card_y + 9), prj, font=f_r_xs, fill=(100, 116, 139))
        
        # Task Title (multiline wrap simulated)
        if len(title) > 34:
            d_kan.text((col_x + 16, card_y + 27), title[:33], font=f_b_xs, fill=(15, 23, 42))
            d_kan.text((col_x + 16, card_y + 41), title[33:], font=f_b_xs, fill=(15, 23, 42))
        else:
            d_kan.text((col_x + 16, card_y + 28), title, font=f_b_xs, fill=(15, 23, 42))
            
        d_kan.line([col_x + 16, card_y + 60, col_x + col_w - 16, card_y + 60], fill=(241, 245, 249))
        
        # Assignee & Subtasks
        d_kan.text((col_x + 16, card_y + 68), "👤 " + assignee, font=f_r_xs, fill=(71, 85, 105))
        d_kan.text((col_x + 16, card_y + 85), "☑ " + subtasks, font=f_b_xs, fill=(255, 94, 20) if "%" in subtasks else (100, 116, 139))
        d_kan.text((col_x + col_w - 65, card_y + 85), due, font=f_r_xs, fill=(22, 163, 74) if due == "Done" else (100, 116, 139))
        
        card_y += 114

im_kan.save(os.path.join(out_dir, 'project-kanban-ui.png'))
print('Saved project-kanban-ui.png!')


# ==============================================================================
# 2. ALL PROJECTS & MY PROJECTS REGISTER (project-list-ui.png)
# ==============================================================================
print('Generating project-list-ui.png...')
im_prj, d_prj = create_base_canvas(
    'All Projects Master Register',
    'Home  »  Projects & Tasks  »  Projects  »  All Projects',
    '+ New Project',
    'My Projects (4)'
)

# 4 KPI Cards
kpis_prj = [
    ('TOTAL PROJECTS', '24 Registered', 'All Enterprise Workflows', (255, 94, 20), (255, 247, 242)),
    ('ACTIVE PROJECTS', '12 In Progress', '5 Priority Deliverables', (2, 132, 199), (240, 249, 255)),
    ('COMPLETED PROJECTS', '10 Delivered', '100% Client Sign-Off', (22, 163, 74), (240, 253, 244)),
    ('ON-TIME DELIVERY', '96.8% Target', 'Ahead of Milestones', (217, 119, 6), (254, 243, 199))
]

card_w = (W - 40 - 36) // 4
for i, (label, val, sub, col, bg_col) in enumerate(kpis_prj):
    cx = 20 + i * (card_w + 12)
    cy = 64
    d_prj.rounded_rectangle([cx, cy, cx + card_w, cy + 62], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d_prj.rounded_rectangle([cx, cy, cx + card_w, cy + 3], radius=1, fill=col)
    d_prj.text((cx + 12, cy + 9), label, font=f_b_xs, fill=(100, 116, 139))
    d_prj.text((cx + 12, cy + 24), val, font=f_b_md, fill=(15, 23, 42))
    d_prj.rounded_rectangle([cx + 12, cy + 44, cx + card_w - 12, cy + 57], radius=3, fill=bg_col)
    d_prj.text((cx + 16, cy + 45), sub, font=f_b_xs, fill=col)

# Table Container
ty = 138
d_prj.rounded_rectangle([20, ty, W - 20, H - 15], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
d_prj.rounded_rectangle([20, ty, W - 20, ty + 34], radius=6, fill=(241, 245, 249))

headers_prj = [
    ('CODE', 35),
    ('PROJECT NAME', 115),
    ('CLIENT / ACCOUNT', 355),
    ('START DATE', 515),
    ('DEADLINE', 595),
    ('PROJECT LEAD', 680),
    ('PROGRESS', 785),
    ('STATUS', 875),
    ('ACTION', 945)
]
for h_text, hx in headers_prj:
    d_prj.text((hx, ty + 10), h_text, font=f_b_xs, fill=(71, 85, 105))
d_prj.line([20, ty + 34, W - 20, ty + 34], fill=(226, 232, 240))

rows_prj = [
    ('PRJ-0042', 'ERP Mobile POS Redesign & Tablet App', 'Ceylon Super Foods Hub', '2026-10-01', '2026-11-25', 'Nuwan S.', 72, 'In Progress', (255, 94, 20), (255, 247, 242)),
    ('PRJ-0041', 'Warehouse Barcoding & Scanner Matrix', 'Lanka Distributors (Pvt) Ltd', '2026-09-15', '2026-11-15', 'Danushka M.', 90, 'Review', (2, 132, 199), (240, 249, 255)),
    ('PRJ-0040', 'Cloud Accounting & Cheque PDC Engine', 'Royal Tea Traders (Pvt) Ltd', '2026-08-01', '2026-10-31', 'Nuwan S.', 100, 'Completed', (22, 163, 74), (240, 253, 244)),
    ('PRJ-0039', 'Omnichannel CRM & WhatsApp Bot Flow', 'Apex Global Logistics LK', '2026-10-10', '2026-12-10', 'Sanduni P.', 45, 'In Progress', (255, 94, 20), (255, 247, 242)),
    ('PRJ-0038', 'Supermarket Touchscreen POS Terminal', 'Lanka Retail Hub Supermart', '2026-10-20', '2026-12-20', 'Kasun T.', 35, 'In Progress', (255, 94, 20), (255, 247, 242)),
    ('PRJ-0037', 'Factory Batch & Expiry ERP Deployment', 'Greenfield Organic Spices', '2026-09-01', '2026-11-05', 'Nuwan S.', 100, 'Completed', (22, 163, 74), (240, 253, 244)),
    ('PRJ-0036', 'Central Logistics & Fleet Fuel Tracker', 'Metro Lanka Wholesale Dist.', '2026-08-15', '2026-10-15', 'Danushka M.', 100, 'Completed', (22, 163, 74), (240, 253, 244)),
    ('PRJ-0035', 'Hardware Mart Counter Multi-Price Setup', 'Sunlight Hardware Emporium', '2026-10-25', '2026-12-05', 'Sanduni P.', 50, 'In Progress', (255, 94, 20), (255, 247, 242)),
    ('PRJ-0034', 'Bakery POS & Weighing Scale Interface', 'Highland Bakers & Mart', '2026-09-10', '2026-11-02', 'Kasun T.', 100, 'Completed', (22, 163, 74), (240, 253, 244))
]

ry = ty + 35
for i, (code, name, client, s_dt, d_dt, lead, prog, st, st_col, st_bg) in enumerate(rows_prj):
    if i % 2 == 1:
        d_prj.rectangle([21, ry, W - 21, ry + 32], fill=(248, 250, 252))
        
    d_prj.text((35, ry + 8), code, font=f_b_sm, fill=(255, 94, 20))
    d_prj.text((115, ry + 8), name, font=f_b_sm, fill=(15, 23, 42))
    d_prj.text((355, ry + 8), client, font=f_r_sm, fill=(71, 85, 105))
    d_prj.text((515, ry + 8), s_dt, font=f_r_xs, fill=(100, 116, 139))
    d_prj.text((595, ry + 8), d_dt, font=f_r_xs, fill=(100, 116, 139))
    d_prj.text((680, ry + 8), "👤 " + lead, font=f_b_xs, fill=(15, 23, 42))
    
    # Progress Bar
    d_prj.rounded_rectangle([785, ry + 12, 835, ry + 19], radius=3, fill=(226, 232, 240))
    bar_fill = int(785 + (prog / 100) * 50)
    d_prj.rounded_rectangle([785, ry + 12, bar_fill, ry + 19], radius=3, fill=(22, 163, 74) if prog == 100 else (255, 94, 20))
    d_prj.text((842, ry + 8), f"{prog}%", font=f_b_xs, fill=(15, 23, 42))
    
    # Status badge
    d_prj.rounded_rectangle([870, ry + 6, 930, ry + 25], radius=4, fill=st_bg)
    d_prj.text((878, ry + 8), st, font=f_b_xs, fill=st_col)
    
    # Action button
    d_prj.rounded_rectangle([940, ry + 6, 985, ry + 25], radius=4, fill=(255, 255, 255), outline=(203, 213, 225), width=1)
    d_prj.text((950, ry + 8), 'View', font=f_b_xs, fill=(51, 65, 85))
    
    d_prj.line([21, ry + 32, W - 21, ry + 32], fill=(241, 245, 249))
    ry += 33

im_prj.save(os.path.join(out_dir, 'project-list-ui.png'))
print('Saved project-list-ui.png!')


# ==============================================================================
# 3. TASK MANAGEMENT & MY TASKS (project-tasks-ui.png)
# ==============================================================================
print('Generating project-tasks-ui.png...')
im_tsk, d_tsk = create_base_canvas(
    'Task Management & To-Do Queue',
    'Home  »  Projects & Tasks  »  Tasks  »  All Tasks',
    '+ New Task',
    'My Tasks Queue (7)'
)

# 4 KPI Cards
kpis_tsk = [
    ('ALL TASKS', '48 Open Tasks', 'Across All Active Projects', (255, 94, 20), (255, 247, 242)),
    ('MY TASKS', '7 Assigned To Me', '3 Priority To-Dos Today', (2, 132, 199), (240, 249, 255)),
    ('COMPLETED SPRINT', '32 Tasks Done', 'Sprint 42 Deliverables', (22, 163, 74), (240, 253, 244)),
    ('ON-TIME EXECUTION', '98.5% Rate', 'Zero Overdue Tasks', (217, 119, 6), (254, 243, 199))
]

for i, (label, val, sub, col, bg_col) in enumerate(kpis_tsk):
    cx = 20 + i * (card_w + 12)
    cy = 64
    d_tsk.rounded_rectangle([cx, cy, cx + card_w, cy + 62], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d_tsk.rounded_rectangle([cx, cy, cx + card_w, cy + 3], radius=1, fill=col)
    d_tsk.text((cx + 12, cy + 9), label, font=f_b_xs, fill=(100, 116, 139))
    d_tsk.text((cx + 12, cy + 24), val, font=f_b_md, fill=(15, 23, 42))
    d_tsk.rounded_rectangle([cx + 12, cy + 44, cx + card_w - 12, cy + 57], radius=3, fill=bg_col)
    d_tsk.text((cx + 16, cy + 45), sub, font=f_b_xs, fill=col)

# Table Container
d_tsk.rounded_rectangle([20, ty, W - 20, H - 15], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
d_tsk.rounded_rectangle([20, ty, W - 20, ty + 34], radius=6, fill=(241, 245, 249))

headers_tsk = [
    ('TASK REF', 35),
    ('TASK DESCRIPTION', 125),
    ('PROJECT NAME', 370),
    ('ASSIGNEE', 530),
    ('PRIORITY', 620),
    ('SUBTASKS', 700),
    ('DEADLINE', 795),
    ('STATUS', 875),
    ('ACTION', 945)
]
for h_text, hx in headers_tsk:
    d_tsk.text((hx, ty + 10), h_text, font=f_b_xs, fill=(71, 85, 105))
d_tsk.line([20, ty + 34, W - 20, ty + 34], fill=(226, 232, 240))

rows_tsk = [
    ('TSK-1082', 'Implement 80mm Thermal Receipt Layout', 'ERP Mobile POS Redesign', 'Nuwan S.', 'High', (239, 68, 68), '4/5 Done (80%)', '2026-11-11', 'In Progress', (255, 94, 20), (255, 247, 242)),
    ('TSK-1081', 'Dynamic LankaQR Payment Code Generator', 'ERP Mobile POS Redesign', 'Sanduni P.', 'High', (239, 68, 68), '3/4 Done (75%)', '2026-11-12', 'In Progress', (255, 94, 20), (255, 247, 242)),
    ('TSK-1080', 'Commercial Bank Statement CSV Auto-Parser', 'Cloud Accounting Sync', 'Danushka M.', 'Medium', (217, 119, 6), '4/4 Done (100%)', '2026-11-09', 'Completed', (22, 163, 74), (240, 253, 244)),
    ('TSK-1079', 'Barcode Scanner Driver Firmware Calibration', 'Warehouse Barcoding', 'Kasun T.', 'Medium', (217, 119, 6), '3/3 Done (100%)', '2026-11-08', 'Completed', (22, 163, 74), (240, 253, 244)),
    ('TSK-1078', 'Client WhatsApp Business Catalog Webhook', 'Omnichannel CRM Bot', 'Sanduni P.', 'Urgent', (239, 68, 68), '5/6 Done (83%)', '2026-11-14', 'In Progress', (255, 94, 20), (255, 247, 242)),
    ('TSK-1077', 'Multi-Currency Split Payment Modal Component', 'ERP Mobile POS Redesign', 'Danushka M.', 'Medium', (217, 119, 6), '3/3 Done (100%)', '2026-11-10', 'Review', (2, 132, 199), (240, 249, 255)),
    ('TSK-1076', 'RAMIS VAT Schedule Generation Automation', 'Cloud Accounting Sync', 'Nuwan S.', 'Urgent', (239, 68, 68), '6/6 Done (100%)', '2026-11-06', 'Completed', (22, 163, 74), (240, 253, 244)),
    ('TSK-1075', 'Weighing Scale Serial Port RS232 Driver', 'Supermarket Touchscreen POS', 'Kasun T.', 'High', (239, 68, 68), '2/4 Done (50%)', '2026-11-16', 'In Progress', (255, 94, 20), (255, 247, 242)),
    ('TSK-1074', 'User Role Permission Matrix for Cashiers', 'Factory Batch & Expiry ERP', 'Nuwan S.', 'Low', (2, 132, 199), '4/4 Done (100%)', '2026-11-04', 'Completed', (22, 163, 74), (240, 253, 244))
]

ry = ty + 35
for i, (ref, title, prj, assignee, prio, p_col, subtasks, dt, st, st_col, st_bg) in enumerate(rows_tsk):
    if i % 2 == 1:
        d_tsk.rectangle([21, ry, W - 21, ry + 32], fill=(248, 250, 252))
        
    d_tsk.text((35, ry + 8), ref, font=f_b_sm, fill=(255, 94, 20))
    d_tsk.text((125, ry + 8), title, font=f_b_sm, fill=(15, 23, 42))
    d_tsk.text((370, ry + 8), prj, font=f_r_xs, fill=(71, 85, 105))
    d_tsk.text((530, ry + 8), "👤 " + assignee, font=f_r_xs, fill=(15, 23, 42))
    
    # Priority badge
    d_tsk.rounded_rectangle([615, ry + 6, 670, ry + 25], radius=3, fill=(254, 242, 242) if prio in ["High", "Urgent"] else (240, 249, 255))
    d_tsk.text((622, ry + 8), prio, font=f_b_xs, fill=p_col)
    
    d_tsk.text((700, ry + 8), subtasks, font=f_b_xs, fill=(255, 94, 20) if "%" in subtasks and "100%" not in subtasks else (15, 23, 42))
    d_tsk.text((795, ry + 8), dt, font=f_r_xs, fill=(100, 116, 139))
    
    # Status badge
    d_tsk.rounded_rectangle([870, ry + 6, 930, ry + 25], radius=4, fill=st_bg)
    d_tsk.text((878, ry + 8), st, font=f_b_xs, fill=st_col)
    
    # Action button
    d_tsk.rounded_rectangle([942, ry + 6, 985, ry + 25], radius=4, fill=(255, 255, 255), outline=(203, 213, 225), width=1)
    d_tsk.text((952, ry + 8), 'View', font=f_b_xs, fill=(51, 65, 85))
    
    d_tsk.line([21, ry + 32, W - 21, ry + 32], fill=(241, 245, 249))
    ry += 33

im_tsk.save(os.path.join(out_dir, 'project-tasks-ui.png'))
print('Saved project-tasks-ui.png!')
