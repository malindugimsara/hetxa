import os
from PIL import Image, ImageDraw, ImageFont

p_dash = r'C:/Users/MG/.gemini/antigravity/brain/387b0f7e-a7aa-4240-b23b-79b73f4876b3/.user_uploaded/media_1794221803813_18c113b9.png'
p_pipe = r'C:/Users/MG/.gemini/antigravity/brain/387b0f7e-a7aa-4240-b23b-79b73f4876b3/.user_uploaded/media_1794221844830_aeeee1af.png'
p_lead = r'C:/Users/MG/.gemini/antigravity/brain/387b0f7e-a7aa-4240-b23b-79b73f4876b3/.user_uploaded/media_1794221920516_7a0f7f97.png'

out_dir = r'c:/xampp/htdocs/hetxa/assets/images/modules'
os.makedirs(out_dir, exist_ok=True)

f_b_xl = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 20)
f_b_lg = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 16)
f_b_md = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 13)
f_b_sm = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 11)
f_b_xs = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 9)

f_r_md = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 12)
f_r_sm = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 10)
f_r_xs = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 8.5)

# ==============================================================================
# 1. PROCESS DASHBOARD
# ==============================================================================
print('Processing Dashboard...')
im_dash = Image.open(p_dash).convert('RGBA')
d_dash = ImageDraw.Draw(im_dash)

# 1.1 Cover and update Stat Cards
# Card 1: OPEN LEADS (0 -> 28)
d_dash.rectangle([58, 68, 120, 93], fill=(255, 255, 255, 255))
d_dash.text((60, 68), '28', font=f_b_xl, fill=(15, 23, 42, 255))

# Card 2: PIPELINE VALUE (LKR 0 -> LKR 4,850,000)
d_dash.rectangle([252, 68, 380, 93], fill=(255, 255, 255, 255))
d_dash.text((254, 69), 'LKR 4,850,000', font=f_b_lg, fill=(15, 23, 42, 255))

# Card 3: WON VALUE (LKR 0, 0 won -> LKR 1,620,000, 12 won)
d_dash.rectangle([452, 68, 590, 105], fill=(255, 255, 255, 255))
d_dash.text((454, 69), 'LKR 1,620,000', font=f_b_lg, fill=(15, 23, 42, 255))
# pill for won
d_dash.rounded_rectangle([454, 91, 510, 104], radius=3, fill=(240, 253, 244, 255))
d_dash.text((458, 91), '✔ 12 won', font=f_b_xs, fill=(22, 163, 74, 255))

# Card 4: WIN RATE (0% -> 68%)
d_dash.rectangle([650, 68, 730, 93], fill=(255, 255, 255, 255))
d_dash.text((652, 68), '68%', font=f_b_xl, fill=(15, 23, 42, 255))

# Card 5: NEW THIS MONTH (0 -> 14)
d_dash.rectangle([848, 68, 920, 93], fill=(255, 255, 255, 255))
d_dash.text((850, 68), '14', font=f_b_xl, fill=(15, 23, 42, 255))

# 1.2 Leads by Source (replace "No leads recorded yet" at x=20..335, y=145..315)
d_dash.rectangle([25, 145, 335, 315], fill=(255, 255, 255, 255))

sources = [
    ('WhatsApp Business', 42, (34, 197, 94), '12 leads'),
    ('Website Inquiry Form', 28, (59, 130, 246), '8 leads'),
    ('Showroom Walk-in', 18, (255, 94, 20), '5 leads'),
    ('Meta & Social Ads', 12, (168, 85, 247), '3 leads')
]

sy = 152
for name, pct, col, count in sources:
    # label & count
    d_dash.text((36, sy), name, font=f_b_sm, fill=(30, 41, 59, 255))
    d_dash.text((275, sy), f'{pct}% ({count})', font=f_r_xs, fill=(100, 116, 139, 255))
    # progress bar background
    bar_w = 275
    d_dash.rounded_rectangle([36, sy + 18, 36 + bar_w, sy + 25], radius=3, fill=(241, 245, 249, 255))
    # filled progress bar
    fill_w = int(bar_w * (pct / 100))
    d_dash.rounded_rectangle([36, sy + 18, 36 + fill_w, sy + 25], radius=3, fill=(*col, 255))
    sy += 39

# 1.3 Pipeline by Stage (add colorful bars above each stage)
# Stage X coordinates roughly:
# New Lead: 412, Contacted: 485, Requirements: 557, Solution: 628, Proposal: 700, Quotation: 772, Won: 844, Lost: 916
# baseline y = 265
stage_data = [
    (412, 65, (148, 163, 184), '8'),      # New Lead
    (485, 55, (59, 130, 246), '6'),       # Contacted
    (557, 45, (6, 182, 212), '4'),        # Requirements
    (628, 38, (14, 165, 233), '3'),       # Solution
    (700, 38, (236, 72, 153), '3'),       # Proposal
    (772, 30, (249, 115, 22), '2'),       # Quotation
    (844, 95, (16, 185, 129), '12'),      # Won
    (916, 22, (239, 68, 68), '2'),        # Lost
]

base_y = 265
for sx, h_bar, col, val in stage_data:
    bx1 = sx - 16
    bx2 = sx + 16
    by1 = base_y - h_bar
    by2 = base_y
    # subtle gradient/bar
    d_dash.rounded_rectangle([bx1, by1, bx2, by2], radius=4, fill=(*col, 235))
    # text value on top
    d_dash.text((sx - 4, by1 - 14), val, font=f_b_xs, fill=(30, 41, 59, 255))

# 1.4 Recent Activity (x=680..1005, y=365..510)
d_dash.rectangle([680, 365, 1005, 510], fill=(255, 255, 255, 255))

activities = [
    ('●', (34, 197, 94), 'New Lead: Colombo Textiles Ltd', 'WhatsApp • 10m ago', 'LKR 450,000'),
    ('●', (59, 130, 246), 'Stage Move: Lanka Fresh Mart', 'Moved to Quotation • 1h ago', 'LKR 1,250,000'),
    ('●', (255, 94, 20), 'Deal Won: Royal Tea Exports', 'Closed by Super Admin • Today', 'LKR 1,620,000')
]

ay = 372
for bullet, b_col, title, sub, amt in activities:
    d_dash.ellipse([690, ay + 3, 698, ay + 11], fill=(*b_col, 255))
    d_dash.text((708, ay), title, font=f_b_sm, fill=(15, 23, 42, 255))
    d_dash.text((708, ay + 17), sub, font=f_r_xs, fill=(100, 116, 139, 255))
    d_dash.text((915, ay + 4), amt, font=f_b_xs, fill=(15, 23, 42, 255))
    # divider
    d_dash.line([690, ay + 38, 995, ay + 38], fill=(241, 245, 249, 255))
    ay += 44

out_dash_path = os.path.join(out_dir, 'crm-dashboard-ui.png')
im_dash.save(out_dash_path, 'PNG')
print('Saved Dashboard to', out_dash_path)

# ==============================================================================
# 2. PROCESS PIPELINE
# ==============================================================================
print('Processing Pipeline...')
im_pipe = Image.open(p_pipe).convert('RGBA')
d_pipe = ImageDraw.Draw(im_pipe)

# Columns approximate x starts:
# 0: 12..136 (New Lead)
# 1: 137..261 (Contacted)
# 2: 262..386 (Requirements)
# 3: 387..511 (Solution)
# 4: 512..636 (Proposal)
# 5: 637..761 (Quotation)
# 6: 762..886 (Won)
# 7: 887..1011 (Lost)

col_x = [12, 137, 262, 387, 512, 637, 762, 887]
col_w = 124

# 2.1 Update Headers (count & values)
headers_info = [
    (0, '3', 'LKR 850k'),
    (1, '2', 'LKR 720k'),
    (2, '2', 'LKR 950k'),
    (3, '1', 'LKR 680k'),
    (4, '2', 'LKR 550k'),
    (5, '2', 'LKR 600k'),
    (6, '4', 'LKR 1.62M'),
    (7, '1', 'LKR 280k')
]

for idx, cnt, val in headers_info:
    cx = col_x[idx]
    # count badge at top right of column header: cx + 105, y=62
    d_pipe.rectangle([cx + 96, 61, cx + 118, 77], fill=(255, 255, 255, 0)) # transparent clear
    # value text at cx + 18, y=80..95
    d_pipe.rectangle([cx + 8, 80, cx + 115, 96], fill=(255, 255, 255, 255))
    d_pipe.text((cx + 10, 81), val, font=f_b_xs, fill=(71, 85, 105, 255))

# 2.2 Clear "Nothing here yet" in columns (y=105..490)
for cx in col_x:
    d_pipe.rectangle([cx + 2, 105, cx + col_w - 4, 480], fill=(244, 248, 253, 255))

# Helper to draw a rich Kanban card inside a column
def draw_card(draw, cx, cy, title, client, amt, tag, tag_col):
    cw = col_w - 12
    x1 = cx + 6
    x2 = x1 + cw
    y1 = cy
    y2 = cy + 78
    # card background with border
    draw.rounded_rectangle([x1, y1, x2, y2], radius=8, fill=(255, 255, 255, 255), outline=(226, 232, 240, 255), width=1)
    # top accent tag
    draw.rounded_rectangle([x1 + 8, y1 + 8, x1 + 8 + len(tag)*6 + 10, y1 + 20], radius=3, fill=(*tag_col, 20))
    draw.text((x1 + 12, y1 + 8), tag, font=f_b_xs, fill=(*tag_col, 255))
    # title / client
    draw.text((x1 + 8, y1 + 24), title, font=f_b_sm, fill=(15, 23, 42, 255))
    draw.text((x1 + 8, y1 + 40), client, font=f_r_xs, fill=(100, 116, 139, 255))
    # bottom row: amount and avatar
    draw.text((x1 + 8, y1 + 58), amt, font=f_b_xs, fill=(255, 94, 20, 255))
    # mini avatar icon
    draw.ellipse([x2 - 20, y1 + 56, x2 - 8, y1 + 68], fill=(224, 231, 255, 255))
    draw.text((x2 - 17, y1 + 57), 'SA', font=f_b_xs, fill=(67, 56, 202, 255))

# Add cards to stages
# Col 0: New Lead
draw_card(d_pipe, col_x[0], 115, 'POS Hardware', 'Ceylon Spices', 'LKR 450,000', 'WhatsApp', (34, 197, 94))
draw_card(d_pipe, col_x[0], 200, 'Retail Barcode', 'Apex Hardware', 'LKR 400,000', 'Website', (59, 130, 246))

# Col 1: Contacted
draw_card(d_pipe, col_x[1], 115, 'Multi-Branch', 'Royal Bakery', 'LKR 720,000', 'Showroom', (255, 94, 20))

# Col 2: Requirements
draw_card(d_pipe, col_x[2], 115, 'ERP + RAMIS', 'Sunlight Mart', 'LKR 950,000', 'Hot Lead', (239, 68, 68))

# Col 3: Solution
draw_card(d_pipe, col_x[3], 115, 'Cloud Server', 'Prime Traders', 'LKR 680,000', 'In Review', (14, 165, 233))

# Col 4: Proposal
draw_card(d_pipe, col_x[4], 115, '5 Counter POS', 'City Grocers', 'LKR 550,000', 'Shared', (236, 72, 153))

# Col 5: Quotation
draw_card(d_pipe, col_x[5], 115, 'Quote #QT-104', 'Lanka Auto', 'LKR 600,000', 'Sent', (249, 115, 22))

# Col 6: Won (Green accent)
draw_card(d_pipe, col_x[6], 115, 'Enterprise ERP', 'Dilmah Tea Shop', 'LKR 850,000', 'Won ✔', (16, 185, 129))
draw_card(d_pipe, col_x[6], 200, '3 Mart Outlets', 'Kandy City Mart', 'LKR 770,000', 'Won ✔', (16, 185, 129))

# Col 7: Lost
draw_card(d_pipe, col_x[7], 115, 'Single Tablet', 'Local Kiosk', 'LKR 280,000', 'Postponed', (239, 68, 68))

out_pipe_path = os.path.join(out_dir, 'crm-pipeline-ui.png')
im_pipe.save(out_pipe_path, 'PNG')
print('Saved Pipeline to', out_pipe_path)

# ==============================================================================
# 3. PROCESS LEADS
# ==============================================================================
print('Processing Leads...')
im_lead = Image.open(p_lead).convert('RGBA')
d_lead = ImageDraw.Draw(im_lead)

# 3.1 Clear "No data available in table" (x=20..685, y=180..380)
d_lead.rectangle([20, 180, 685, 380], fill=(255, 255, 255, 255))

leads_rows = [
    ('#101', 'Colombo Textiles Ltd', 'Requirements', 'Hot', 'Open', 'WhatsApp', 'Retail, POS', 'Default', 'Super Admin', '450,000'),
    ('#102', 'Lanka Fresh Mart', 'Quotation', 'High', 'Open', 'Website', 'Multi-Branch', 'Default', 'Kamal P.', '1,250,000'),
    ('#103', 'Royal Tea Exports', 'Won', 'Closed', 'Won', 'Showroom', 'ERP, RAMIS', 'Default', 'Super Admin', '1,620,000'),
    ('#104', 'Apex Hardware Mart', 'Contacted', 'Medium', 'Open', 'Meta Ads', 'POS Terminal', 'Default', 'Nimal S.', '400,000')
]

ly = 185
for lid, l_name, stage, fit, outc, src, tags, loc, own, bud in leads_rows:
    # row background alternating
    if ly % 2 == 0:
        d_lead.rectangle([20, ly - 3, 685, ly + 28], fill=(248, 250, 252, 255))
    d_lead.text((26, ly + 4), lid, font=f_b_xs, fill=(100, 116, 139, 255))
    d_lead.text((62, ly + 4), l_name, font=f_b_xs, fill=(15, 23, 42, 255))
    
    # stage pill
    d_lead.rounded_rectangle([185, ly + 2, 245, ly + 18], radius=3, fill=(238, 242, 255, 255))
    d_lead.text((190, ly + 4), stage, font=f_r_xs, fill=(79, 70, 229, 255))
    
    d_lead.text((258, ly + 4), fit, font=f_r_xs, fill=(100, 116, 139, 255))
    d_lead.text((298, ly + 4), outc, font=f_r_xs, fill=(15, 23, 42, 255))
    d_lead.text((352, ly + 4), src, font=f_r_xs, fill=(15, 23, 42, 255))
    d_lead.text((410, ly + 4), tags, font=f_r_xs, fill=(100, 116, 139, 255))
    d_lead.text((485, ly + 4), loc, font=f_r_xs, fill=(100, 116, 139, 255))
    d_lead.text((550, ly + 4), own, font=f_r_xs, fill=(15, 23, 42, 255))
    d_lead.text((620, ly + 4), f'LKR {bud}', font=f_b_xs, fill=(255, 94, 20, 255))
    
    # line
    d_lead.line([20, ly + 28, 685, ly + 28], fill=(241, 245, 249, 255))
    ly += 33

# 3.2 Right Drawer "New lead" input fields
# Company: x=710, y=182..215
d_lead.text((715, 187), 'Ceylon Distribution Hub', font=f_r_md, fill=(15, 23, 42, 255))

# First name: x=710, y=253..285
d_lead.text((715, 258), 'Saman', font=f_r_md, fill=(15, 23, 42, 255))

# Last name: x=855, y=253..285
d_lead.text((860, 258), 'Perera', font=f_r_md, fill=(15, 23, 42, 255))

# Phone: x=710, y=320..350
d_lead.text((715, 323), '077 415 8872', font=f_r_md, fill=(15, 23, 42, 255))

# Email: x=855, y=320..350
d_lead.text((860, 323), 'saman@ceylondh.lk', font=f_r_md, fill=(15, 23, 42, 255))

# Source dropdown text at y=565
d_lead.text((715, 565), 'WhatsApp Business', font=f_r_md, fill=(15, 23, 42, 255))

# Tags at y=640
d_lead.text((715, 640), 'Retail POS, Wholesale, RAMIS VAT', font=f_r_md, fill=(15, 23, 42, 255))

out_lead_path = os.path.join(out_dir, 'crm-leads-ui.png')
im_lead.save(out_lead_path, 'PNG')
print('Saved Leads to', out_lead_path)

print('All 3 CRM mockups generated successfully with realistic corporate data!')

