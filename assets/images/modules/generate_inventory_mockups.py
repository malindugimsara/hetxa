import os
from PIL import Image, ImageDraw, ImageFont

p_grn = r'C:/Users/MG/.gemini/antigravity/brain/387b0f7e-a7aa-4240-b23b-79b73f4876b3/.user_uploaded/media_1794222900673_d45976ff.png'
p_items = r'C:/Users/MG/.gemini/antigravity/brain/387b0f7e-a7aa-4240-b23b-79b73f4876b3/.user_uploaded/media_1794222938547_15769439.png'
p_adj = r'C:/Users/MG/.gemini/antigravity/brain/387b0f7e-a7aa-4240-b23b-79b73f4876b3/.user_uploaded/media_1794222990150_e8e757ca.png'

out_dir = r'c:/xampp/htdocs/hetxa/assets/images/modules'
os.makedirs(out_dir, exist_ok=True)

f_b_xl = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 16)
f_b_lg = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 13)
f_b_md = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 11)
f_b_sm = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 9.5)
f_b_xs = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 8.5)

f_r_md = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 11)
f_r_sm = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 9.5)
f_r_xs = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 8.5)

# ==============================================================================
# 1. PROCESS ADD NEW GRN
# ==============================================================================
print('Processing Add New GRN...')
im_grn = Image.open(p_grn).convert('RGBA')
d_grn = ImageDraw.Draw(im_grn)

# 1.1 Supplier dropdown fill
d_grn.rectangle([25, 182, 280, 203], fill=(255, 255, 255, 255))
d_grn.text((27, 185), 'Lanka Distributors (Pvt) Ltd', font=f_r_md, fill=(15, 23, 42, 255))

# 1.2 Delivery Date fill
d_grn.rectangle([25, 245, 150, 268], fill=(255, 255, 255, 255))
d_grn.text((27, 248), '2026-11-10', font=f_r_md, fill=(15, 23, 42, 255))

# 1.3 Notes fill
d_grn.rectangle([25, 305, 350, 325], fill=(255, 255, 255, 255))
d_grn.text((27, 307), 'Bulk inward: 80mm thermal rolls, 2D scanners & cash drawers', font=f_r_sm, fill=(71, 85, 105, 255))

# 1.4 GRN Items Table: Clear "No Items Added Yet"
# y=268..372, x=20..1005
d_grn.rectangle([20, 268, 1005, 372], fill=(255, 255, 255, 255))

grn_rows = [
    ('Thermal Paper Roll 80mm x 80m', 'Box (50)', 'LOT-2026-B12', 'N/A', '20', '2', '14,500.00', '18,000.00', '0%', '290,000.00'),
    ('Wireless 2D Barcode Scanner USB', 'Piece', 'LOT-SC-904', 'N/A', '15', '0', '12,800.00', '16,500.00', '0%', '192,000.00'),
    ('Heavy Duty Cash Drawer 5B/8C', 'Piece', 'LOT-CD-201', 'N/A', '10', '0', '18,500.00', '23,000.00', '0%', '185,000.00')
]

gy = 274
for item, unit, lot, exp, qty, free, p_price, s_price, tax, l_total in grn_rows:
    # row background
    if (gy // 30) % 2 == 0:
        d_grn.rectangle([20, gy - 2, 1005, gy + 28], fill=(248, 250, 252, 255))
    d_grn.text((27, gy + 4), item, font=f_b_sm, fill=(15, 23, 42, 255))
    d_grn.text((180, gy + 4), unit, font=f_r_sm, fill=(71, 85, 105, 255))
    d_grn.text((245, gy + 4), lot, font=f_r_sm, fill=(100, 116, 139, 255))
    d_grn.text((330, gy + 4), exp, font=f_r_sm, fill=(100, 116, 139, 255))
    
    # Qty badge
    d_grn.text((440, gy + 4), qty, font=f_b_sm, fill=(15, 23, 42, 255))
    d_grn.text((505, gy + 4), free, font=f_r_sm, fill=(16, 185, 129, 255) if free != '0' else (100, 116, 139, 255))
    
    d_grn.text((565, gy + 4), p_price, font=f_r_sm, fill=(15, 23, 42, 255))
    d_grn.text((665, gy + 4), s_price, font=f_r_sm, fill=(15, 23, 42, 255))
    d_grn.text((760, gy + 4), tax, font=f_r_sm, fill=(100, 116, 139, 255))
    d_grn.text((835, gy + 4), l_total, font=f_b_sm, fill=(255, 94, 20, 255))
    
    # Action trash icon (simulated red dot)
    d_grn.text((955, gy + 4), '✕', font=f_b_sm, fill=(239, 68, 68, 255))
    
    d_grn.line([20, gy + 30, 1005, gy + 30], fill=(241, 245, 249, 255))
    gy += 32

# 1.5 Adjustments section values
# Discount Value: 15,000.00
d_grn.rectangle([232, 780//2, 330, 815//2], fill=(255, 255, 255, 255))
d_grn.text((236, 395), '15,000.00', font=f_r_sm, fill=(15, 23, 42, 255))

# Additional Expense: 8,000.00
d_grn.rectangle([445, 780//2, 545, 815//2], fill=(255, 255, 255, 255))
d_grn.text((450, 395), '8,000.00', font=f_r_sm, fill=(15, 23, 42, 255))

# Expense Note
d_grn.rectangle([25, 425, 450, 450], fill=(255, 255, 255, 255))
d_grn.text((28, 428), 'Transport & logistics handling fee by supplier truck', font=f_r_xs, fill=(71, 85, 105, 255))

# 1.6 Calculation Summary Box (x=930..1005)
bg_sum = (242, 244, 245, 255)
# Subtotal: 667,000.00
d_grn.rectangle([925, 360, 1005, 375], fill=bg_sum)
d_grn.text((930, 361), '667,000.00', font=f_b_sm, fill=(15, 23, 42, 255))

# Total Tax: 0.00 (leave)
# Discount: 15,000.00
d_grn.rectangle([925, 400, 1005, 415], fill=bg_sum)
d_grn.text((930, 401), '15,000.00', font=f_b_sm, fill=(239, 68, 68, 255))

# Additional Expense: 8,000.00
d_grn.rectangle([925, 423, 1005, 438], fill=bg_sum)
d_grn.text((945, 423), '8,000.00', font=f_b_sm, fill=(15, 23, 42, 255))

# Grand Total: 660,000.00
d_grn.rectangle([915, 460, 1005, 480], fill=bg_sum)
d_grn.text((922, 462), '660,000.00', font=f_b_lg, fill=(15, 23, 42, 255))

out_grn_path = os.path.join(out_dir, 'inventory-grn-ui.png')
im_grn.save(out_grn_path, 'PNG')
print('Saved Add New GRN to', out_grn_path)

# ==============================================================================
# 2. PROCESS ITEMS LIST
# ==============================================================================
print('Processing Items List...')
im_items = Image.open(p_items).convert('RGBA')
d_items = ImageDraw.Draw(im_items)

# Clear existing 3 rows (y=165..315, x=15..1005)
d_items.rectangle([15, 165, 1005, 335], fill=(255, 255, 255, 255))

items_data = [
    ('100g BOPF Tea Packed Pouch', 'SI-0001', 'Single', 'TEA-BOPF', 'Beverages', 'Ceylon Point', 'Pouch', 'N/A', '2027-10', '210.00', '290.00', '142', (59, 130, 246)),
    ('Ceylon Royal Tin Gift Caddy', 'SI-0002', 'Single', 'TEA-LUX', 'Gift Packs', 'Ceylon Point', 'Piece', 'N/A', '2027-12', '850.00', '1,283.25', '64', (59, 130, 246)),
    ('Thermal Receipt Roll 80x80mm', 'SI-0003', 'Single', 'POS-ROL', 'Hardware', 'Codecraft', 'Box', 'N/A', 'N/A', '14,500.00', '18,000.00', '28', (59, 130, 246)),
    ('Wireless 2D Barcode Scanner', 'SI-0004', 'Single', 'POS-SCN', 'Hardware', 'Codecraft', 'Piece', '1 Year', 'N/A', '12,800.00', '16,500.00', '5', (245, 158, 11)),
    ('Heavy Duty Cash Drawer RJ11', 'SI-0005', 'Single', 'POS-CDR', 'Hardware', 'Codecraft', 'Piece', '1 Year', 'N/A', '18,500.00', '23,000.00', '12', (59, 130, 246))
]

iy = 168
for name, bc, itype, sku, cat, brand, unit, war, exp, p_pr, s_pr, qty, qty_col in items_data:
    if (iy // 28) % 2 == 0:
        d_items.rectangle([15, iy - 2, 1005, iy + 28], fill=(248, 250, 252, 255))
    
    # Checkbox
    d_items.rectangle([27, iy + 6, 37, iy + 16], outline=(203, 213, 225, 255), width=1)
    
    # + icon and Item Name
    d_items.text((45, iy + 4), '+', font=f_b_sm, fill=(255, 94, 20, 255))
    d_items.text((58, iy + 4), name, font=f_b_sm, fill=(15, 23, 42, 255))
    
    # Barcode
    d_items.text((280, iy + 4), bc, font=f_r_sm, fill=(71, 85, 105, 255))
    
    # Type pill (Single - orange)
    d_items.rounded_rectangle([348, iy + 3, 385, iy + 18], radius=3, fill=(255, 94, 20, 255))
    d_items.text((353, iy + 4), itype, font=f_b_xs, fill=(255, 255, 255, 255))
    
    d_items.text((398, iy + 4), sku, font=f_r_sm, fill=(100, 116, 139, 255))
    d_items.text((445, iy + 4), cat, font=f_r_sm, fill=(15, 23, 42, 255))
    d_items.text((505, iy + 4), brand, font=f_r_sm, fill=(15, 23, 42, 255))
    d_items.text((552, iy + 4), unit, font=f_r_sm, fill=(71, 85, 105, 255))
    d_items.text((592, iy + 4), war, font=f_r_sm, fill=(100, 116, 139, 255))
    d_items.text((648, iy + 4), exp, font=f_r_sm, fill=(100, 116, 139, 255))
    d_items.text((698, iy + 4), p_pr, font=f_r_sm, fill=(15, 23, 42, 255))
    d_items.text((765, iy + 4), s_pr, font=f_b_sm, fill=(15, 23, 42, 255))
    
    # Remaining QTY pill
    d_items.rounded_rectangle([828, iy + 3, 852, iy + 18], radius=4, fill=(*qty_col, 255))
    d_items.text((832, iy + 4), qty, font=f_b_xs, fill=(255, 255, 255, 255))
    
    # Status pill (Active - green)
    d_items.rounded_rectangle([890, iy + 3, 922, iy + 18], radius=3, fill=(22, 163, 74, 255))
    d_items.text((894, iy + 4), 'Active', font=f_b_xs, fill=(255, 255, 255, 255))
    
    # Action dots
    d_items.text((945, iy + 4), 'Action :', font=f_r_xs, fill=(100, 116, 139, 255))
    
    d_items.line([15, iy + 30, 1005, iy + 30], fill=(241, 245, 249, 255))
    iy += 31

# Update "Showing 1 to 3 of 3 entries" -> "Showing 1 to 5 of 128 entries"
d_items.rectangle([15, 338, 250, 355], fill=(255, 255, 255, 255))
d_items.text((18, 340), 'Showing 1 to 5 of 128 entries (Filtered from master stock catalog)', font=f_r_xs, fill=(100, 116, 139, 255))

out_items_path = os.path.join(out_dir, 'inventory-items-ui.png')
im_items.save(out_items_path, 'PNG')
print('Saved Items List to', out_items_path)

# ==============================================================================
# 3. PROCESS STOCK ADJUSTMENT
# ==============================================================================
print('Processing Stock Adjustment...')
im_adj = Image.open(p_adj).convert('RGBA')
d_adj = ImageDraw.Draw(im_adj)

# 3.1 Fill General Reason (y=245..275)
d_adj.rectangle([25, 246, 500, 275], fill=(255, 255, 255, 255))
d_adj.text((28, 250), 'Monthly physical cycle count audit & damage write-off reconciliation (Branch #01)', font=f_r_sm, fill=(30, 41, 59, 255))

# 3.2 Clear "+/- No Items Added" in table (y=265..360, x=20..1005)
d_adj.rectangle([20, 265, 1005, 360], fill=(255, 255, 255, 255))

adj_rows = [
    ('100g BOPF Tea Packed Pouch', 'LOT-2026-A01', '2027-10-15', 'Pouch', '+ 12', (22, 163, 74), '210.00', '290.00', 'Surplus found during physical warehouse count'),
    ('Wireless 2D Barcode Scanner USB', 'LOT-SC-904', 'N/A', 'Piece', '- 1', (239, 68, 68), '12,800.00', '16,500.00', 'Damaged demo unit in retail counter showroom'),
    ('80mm Thermal Receipt Paper Roll', 'LOT-PR-11', 'N/A', 'Box', '+ 2', (22, 163, 74), '14,500.00', '18,000.00', 'Unrecorded vendor bonus sample shipment')
]

ay = 270
for item, lot, exp, unit, qty, q_col, p_pr, s_pr, reason in adj_rows:
    if (ay // 28) % 2 == 0:
        d_adj.rectangle([20, ay - 2, 1005, ay + 28], fill=(248, 250, 252, 255))
    d_adj.text((28, ay + 4), item, font=f_b_sm, fill=(15, 23, 42, 255))
    d_adj.text((215, ay + 4), lot, font=f_r_sm, fill=(71, 85, 105, 255))
    d_adj.text((408, ay + 4), exp, font=f_r_sm, fill=(100, 116, 139, 255))
    d_adj.text((502, ay + 4), unit, font=f_r_sm, fill=(71, 85, 105, 255))
    
    # Qty pill (+ 12 green, - 1 red)
    d_adj.text((615, ay + 4), qty, font=f_b_sm, fill=(*q_col, 255))
    
    d_adj.text((665, ay + 4), p_pr, font=f_r_sm, fill=(15, 23, 42, 255))
    d_adj.text((770, ay + 4), s_pr, font=f_r_sm, fill=(15, 23, 42, 255))
    d_adj.text((845, ay + 4), reason, font=f_r_xs, fill=(71, 85, 105, 255))
    
    # Action trash icon
    d_adj.text((958, ay + 4), '✕', font=f_b_sm, fill=(239, 68, 68, 255))
    
    d_adj.line([20, ay + 30, 1005, ay + 30], fill=(241, 245, 249, 255))
    ay += 31

out_adj_path = os.path.join(out_dir, 'inventory-adjustments-ui.png')
im_adj.save(out_adj_path, 'PNG')
print('Saved Stock Adjustment to', out_adj_path)

print('All 3 Inventory mockups successfully generated with rich data!')

