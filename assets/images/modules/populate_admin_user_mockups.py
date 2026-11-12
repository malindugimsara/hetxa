import os
from PIL import Image, ImageDraw, ImageFont

p1 = r'C:/Users/MG/.gemini/antigravity/brain/a68b6681-cdc2-4b67-b620-e6b76a258d07/.user_uploaded/media_1794457069840_4fa7d87d.png'
p2 = r'C:/Users/MG/.gemini/antigravity/brain/a68b6681-cdc2-4b67-b620-e6b76a258d07/.user_uploaded/media_1794457093708_49a836a5.png'
p3 = r'C:/Users/MG/.gemini/antigravity/brain/a68b6681-cdc2-4b67-b620-e6b76a258d07/.user_uploaded/media_1794457152277_b9d26258.png'

out_dir = r'c:/xampp/htdocs/hetxa/assets/images/modules'
os.makedirs(out_dir, exist_ok=True)

# Standard Fonts
f_b_lg = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 13)
f_b_md = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 11)
f_b_sm = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 9.5)
f_b_xs = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 8.5)

f_r_md = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 11)
f_r_sm = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 9.5)
f_r_xs = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 8.5)

# ==============================================================================
# 1. PROCESS USER ROLES LIST (media_1794457069840_4fa7d87d.png)
# ==============================================================================
print('Processing User Roles List...')
im1 = Image.open(p1).convert('RGBA')

# The card currently ends at y=187.
# Card horizontal bounds: x=10 to x=1014.
# We will expand the white card down to y=435, leaving room for pagination and bottom footer.
# Background color of the page: (248, 250, 251, 255)
# Card border color: (226, 232, 240, 255)

# Extract green pill and action button from Row 1
pill_crop = im1.crop((514, 133, 545, 146))
action_crop = im1.crop((758, 134, 796, 145))

# Row 1 is at y=128 to 150.
# Let's clean up from y=148 downwards up to y=450 to redraw extended card and rows
d1 = ImageDraw.Draw(im1)

# Card dimensions
card_left = 10
card_right = 1014
card_bottom = 430

# Fill card area with white
d1.rectangle([card_left, 148, card_right, card_bottom], fill=(255, 255, 255, 255))
# Draw card side borders
d1.line([(card_left, 148), (card_left, card_bottom)], fill=(226, 232, 240, 255), width=1)
d1.line([(card_right, 148), (card_right, card_bottom)], fill=(226, 232, 240, 255), width=1)
d1.line([(card_left, card_bottom), (card_right, card_bottom)], fill=(226, 232, 240, 255), width=1)

# Roles to add
roles = [
    (1, "Super Admin", True),
    (2, "Branch / Outlet General Manager", False),
    (3, "Finance Head & Senior Accountant", True),
    (4, "Sales Executive & Billing Officer", False),
    (5, "Inventory & Warehouse Controller", True),
    (6, "HR & Payroll Administrator", False),
    (7, "POS Cashier & Shift Operator", True),
]

# Row parameters
row_h = 32
start_y = 126

# Re-render rows 2 to 7 (Row 1 is already at y=126..148, but let's make the table uniform from y=126 to y=350)
d1.rectangle([18, 126, 1006, 126 + 7 * row_h], fill=(255, 255, 255, 255))

for idx, (r_id, r_name, is_even) in enumerate(roles):
    ry = start_y + idx * row_h
    row_bg = (248, 250, 252, 255) if is_even else (255, 255, 255, 255)
    
    # Fill row background
    d1.rectangle([18, ry, 1006, ry + row_h], fill=row_bg)
    # Bottom border of row
    d1.line([(18, ry + row_h), (1006, ry + row_h)], fill=(241, 245, 249, 255), width=1)
    
    # ID column (x ~ 28)
    d1.text((28, ry + 9), str(r_id), font=f_r_sm, fill=(51, 65, 85, 255))
    
    # Role Name column (x ~ 185)
    # Make Super Admin stand out slightly or uniform
    f_role = f_b_sm if r_id == 1 else f_r_sm
    d1.text((185, ry + 9), r_name, font=f_role, fill=(30, 41, 59, 255))
    
    # Status column (x ~ 516) - paste exact green pill
    im1.paste(pill_crop, (515, ry + 8), pill_crop)
    
    # Action column (x ~ 760) - paste exact action dropdown
    im1.paste(action_crop, (759, ry + 9), action_crop)

# Draw Table bottom subtle line
table_end_y = start_y + len(roles) * row_h
d1.line([(18, table_end_y), (1006, table_end_y)], fill=(226, 232, 240, 255), width=1)

# Pagination row at y = 370
d1.text((24, 385), "Showing 1 to 7 of 7 entries", font=f_r_sm, fill=(100, 116, 139, 255))

# Pagination buttons on right (Previous, 1, Next)
# Previous
d1.rectangle([900, 378, 945, 400], fill=(255, 255, 255, 255), outline=(226, 232, 240, 255))
d1.text((908, 383), "Prev", font=f_r_xs, fill=(148, 163, 184, 255))

# Page 1 active button (Orange)
d1.rectangle([950, 378, 972, 400], fill=(255, 94, 20, 255), outline=(255, 94, 20, 255))
d1.text((958, 383), "1", font=f_b_xs, fill=(255, 255, 255, 255))

# Next
d1.rectangle([977, 378, 1006, 400], fill=(255, 255, 255, 255), outline=(226, 232, 240, 255))
d1.text((984, 383), "Next", font=f_r_xs, fill=(148, 163, 184, 255))

# Save Image 1
out_p1 = os.path.join(out_dir, 'admin-roles-ui.png')
im1.save(out_p1, 'PNG', quality=95)
print(f'Saved {out_p1}')

# Also save copy as admin-users-ui.png for compatibility
out_p1_compat = os.path.join(out_dir, 'admin-users-ui.png')
im1.save(out_p1_compat, 'PNG', quality=95)


# ==============================================================================
# 2. PROCESS GENERAL SETTINGS (media_1794457093708_49a836a5.png)
# ==============================================================================
print('Processing General Settings...')
im2 = Image.open(p2).convert('RGBA')
d2 = ImageDraw.Draw(im2)

# Box 1: Business Name (x: 24 to 495, y: 130 to 151)
d2.rectangle([25, 131, 495, 151], fill=(255, 255, 255, 255))
d2.text((32, 134), "Hetxa Technologies (Pvt) Ltd", font=f_r_sm, fill=(30, 41, 59, 255))

# Box 2: Browser Tab Title (x: 512 to 983, y: 130 to 151)
d2.rectangle([513, 131, 983, 151], fill=(255, 255, 255, 255))
d2.text((520, 134), "Hetxa BOS | AI Business Operating System", font=f_r_sm, fill=(30, 41, 59, 255))

# Box 3: Business TAX/VAT No (x: 24 to 495, y: 177 to 199)
d2.rectangle([25, 178, 495, 199], fill=(255, 255, 255, 255))
d2.text((32, 182), "RAMIS-104928172 (IRD Sri Lanka Registered)", font=f_r_sm, fill=(30, 41, 59, 255))

# Save Image 2
out_p2 = os.path.join(out_dir, 'admin-settings-ui.png')
im2.save(out_p2, 'PNG', quality=95)
print(f'Saved {out_p2}')


# ==============================================================================
# 3. PROCESS SMS & EMAIL SETTINGS (media_1794457152277_b9d26258.png)
# ==============================================================================
print('Processing SMS & Email Settings...')
im3 = Image.open(p3).convert('RGBA')
d3 = ImageDraw.Draw(im3)

# Row 1: Server Connection
# SMTP Host (x: 23 to 495, y: 154 to 174)
d3.rectangle([24, 154, 495, 174], fill=(255, 255, 255, 255))
d3.text((32, 158), "smtp.hetxa.cloud", font=f_r_sm, fill=(30, 41, 59, 255))

# Row 2: Authentication
# SMTP Username (x: 23 to 495, y: 222 to 242)
d3.rectangle([24, 222, 495, 242], fill=(255, 255, 255, 255))
d3.text((32, 226), "notifications@hetxa.cloud", font=f_r_sm, fill=(30, 41, 59, 255))

# SMTP Password (x: 507 to 983, y: 222 to 242)
d3.rectangle([508, 222, 980, 242], fill=(255, 255, 255, 255))
d3.text((516, 225), "••••••••••••••••••••", font=f_b_md, fill=(71, 85, 105, 255))

# Row 3: Sender Details
# From Name (x: 23 to 330, y: 284 to 304)
d3.rectangle([24, 284, 330, 304], fill=(255, 255, 255, 255))
d3.text((32, 288), "Hetxa Business Cloud", font=f_r_sm, fill=(30, 41, 59, 255))

# From / Reply-To (x: 340 to 655, y: 284 to 304)
d3.rectangle([342, 284, 655, 304], fill=(255, 255, 255, 255))
d3.text((350, 288), "billing@hetxa.cloud", font=f_r_sm, fill=(30, 41, 59, 255))

# Default System Email (x: 665 to 983, y: 284 to 304)
d3.rectangle([667, 284, 980, 304], fill=(255, 255, 255, 255))
d3.text((675, 288), "admin@hetxa.cloud", font=f_r_sm, fill=(30, 41, 59, 255))

# Document Email Automation Cards (y: 432 to 445)
# Card 1: Invoices Auto-Email (around x=71)
d3.rectangle([68, 434, 180, 447], fill=(255, 255, 255, 255))
d3.text((68, 434), "3 / 3 Branches Active", font=f_b_xs, fill=(22, 101, 52, 255))

# Card 2: Quotations Auto-Email (around x=305)
d3.rectangle([300, 434, 430, 447], fill=(255, 255, 255, 255))
d3.text((300, 434), "3 / 3 Branches Active", font=f_b_xs, fill=(22, 101, 52, 255))

# Card 3: Proforma Auto-Email (around x=545)
d3.rectangle([540, 434, 670, 447], fill=(255, 255, 255, 255))
d3.text((540, 434), "3 / 3 Branches Active", font=f_b_xs, fill=(22, 101, 52, 255))

# Card 4: Purchase Orders Auto-Email (around x=785)
d3.rectangle([780, 434, 910, 447], fill=(255, 255, 255, 255))
d3.text((780, 434), "3 / 3 Branches Active", font=f_b_xs, fill=(22, 101, 52, 255))

# Save Image 3
out_p3 = os.path.join(out_dir, 'admin-email-ui.png')
im3.save(out_p3, 'PNG', quality=95)
print(f'Saved {out_p3}')

print('All 3 Admin mockups generated successfully!')

