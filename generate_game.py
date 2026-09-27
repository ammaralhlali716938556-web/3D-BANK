import json

# Let's define the 40 tiles of Egyptian Bank El Hazz
TILES = [
    {
        "id": 0, "name": "انطلق", "subtitle": "البداية (+200 ج.م)", "type": "go", 
        "color": "#10b981", "icon": "🚀", "price": 0
    },
    {
        "id": 1, "name": "العريش", "subtitle": "شمال سيناء", "type": "property", 
        "group": "brown", "groupName": "بني", "color": "#8b5a2b", "icon": "🌴",
        "price": 60, "rent": [2, 10, 30, 90, 160, 250], "houseCost": 50, "mortgage": 30
    },
    {
        "id": 2, "name": "صندوق الدنيا", "subtitle": "محفظة الشعب", "type": "chest", 
        "color": "#f59e0b", "icon": "🎁", "price": 0
    },
    {
        "id": 3, "name": "بورسعيد", "subtitle": "المدينة الباسلة", "type": "property", 
        "group": "brown", "groupName": "بني", "color": "#8b5a2b", "icon": "⚓",
        "price": 60, "rent": [4, 20, 60, 180, 320, 450], "houseCost": 50, "mortgage": 30
    },
    {
        "id": 4, "name": "ضريبة الدخل", "subtitle": "ادفع 200 ج.م", "type": "tax", 
        "color": "#ef4444", "icon": "💸", "price": 200
    },
    {
        "id": 5, "name": "محطة رمسيس", "subtitle": "سكك حديد مصر", "type": "station", 
        "group": "station", "groupName": "محطة", "color": "#334155", "icon": "🚂",
        "price": 200, "rent": [25, 50, 100, 200], "mortgage": 100
    },
    {
        "id": 6, "name": "طنطا", "subtitle": "عاصمة الغربية", "type": "property", 
        "group": "lightblue", "groupName": "سماوي", "color": "#38bdf8", "icon": "🕌",
        "price": 100, "rent": [6, 30, 90, 270, 400, 550], "houseCost": 50, "mortgage": 50
    },
    {
        "id": 7, "name": "كارت الحظ", "subtitle": "جرب حظك اليوم", "type": "chance", 
        "color": "#ec4899", "icon": "❓", "price": 0
    },
    {
        "id": 8, "name": "شبين الكوم", "subtitle": "المنوفية", "type": "property", 
        "group": "lightblue", "groupName": "سماوي", "color": "#38bdf8", "icon": "🌾",
        "price": 100, "rent": [6, 30, 90, 270, 400, 550], "houseCost": 50, "mortgage": 50
    },
    {
        "id": 9, "name": "المنصورة", "subtitle": "عروس النيل والدلتا", "type": "property", 
        "group": "lightblue", "groupName": "سماوي", "color": "#38bdf8", "icon": "🌸",
        "price": 120, "rent": [8, 40, 100, 300, 450, 600], "houseCost": 50, "mortgage": 60
    },
    {
        "id": 10, "name": "سجن القلعة", "subtitle": "زيارة بريئة / حبس", "type": "jail", 
        "color": "#64748b", "icon": "⛓️", "price": 0
    },
    {
        "id": 11, "name": "دمنهور", "subtitle": "البحيرة", "type": "property", 
        "group": "pink", "groupName": "وردي", "color": "#d946ef", "icon": "🏛️",
        "price": 140, "rent": [10, 50, 150, 450, 625, 750], "houseCost": 100, "mortgage": 70
    },
    {
        "id": 12, "name": "شركة الكهرباء", "subtitle": "مرفق عام", "type": "utility", 
        "group": "utility", "groupName": "مرفق", "color": "#eab308", "icon": "⚡",
        "price": 150, "mortgage": 75
    },
    {
        "id": 13, "name": "كفر الشيخ", "subtitle": "أرض الأمل", "type": "property", 
        "group": "pink", "groupName": "وردي", "color": "#d946ef", "icon": "🌊",
        "price": 140, "rent": [10, 50, 150, 450, 625, 750], "houseCost": 100, "mortgage": 70
    },
    {
        "id": 14, "name": "الزقازيق", "subtitle": "الشرقية والحضارة", "type": "property", 
        "group": "pink", "groupName": "وردي", "color": "#d946ef", "icon": "🐎",
        "price": 160, "rent": [12, 60, 180, 500, 700, 900], "houseCost": 100, "mortgage": 80
    },
    {
        "id": 15, "name": "محطة سيدي جابر", "subtitle": "سكك حديد الإسكندرية", "type": "station", 
        "group": "station", "groupName": "محطة", "color": "#334155", "icon": "🚆",
        "price": 200, "rent": [25, 50, 100, 200], "mortgage": 100
    },
    {
        "id": 16, "name": "بني سويف", "subtitle": "بوابة الصعيد", "type": "property", 
        "group": "orange", "groupName": "برتقالي", "color": "#f97316", "icon": "🏺",
        "price": 180, "rent": [14, 70, 200, 550, 750, 950], "houseCost": 100, "mortgage": 90
    },
    {
        "id": 17, "name": "صندوق الدنيا", "subtitle": "محفظة الشعب", "type": "chest", 
        "color": "#f59e0b", "icon": "🎁", "price": 0
    },
    {
        "id": 18, "name": "الفيوم", "subtitle": "بلاد السواقي وقارون", "type": "property", 
        "group": "orange", "groupName": "برتقالي", "color": "#f97316", "icon": "🎡",
        "price": 180, "rent": [14, 70, 200, 550, 750, 950], "houseCost": 100, "mortgage": 90
    },
    {
        "id": 19, "name": "المنيا", "subtitle": "عروس الصعيد", "type": "property", 
        "group": "orange", "groupName": "برتقالي", "color": "#f97316", "icon": "👑",
        "price": 200, "rent": [16, 80, 220, 600, 800, 1000], "houseCost": 100, "mortgage": 100
    },
    {
        "id": 20, "name": "الاستراحة المجانية", "subtitle": "الموقف والجائزة الكبرى", "type": "parking", 
        "color": "#6366f1", "icon": "🚗", "price": 0
    },
    {
        "id": 21, "name": "أسيوط", "subtitle": "قلب الوادي", "type": "property", 
        "group": "red", "groupName": "أحمر", "color": "#ef4444", "icon": "🦁",
        "price": 220, "rent": [18, 90, 250, 700, 875, 1050], "houseCost": 150, "mortgage": 110
    },
    {
        "id": 22, "name": "كارت الحظ", "subtitle": "جرب حظك اليوم", "type": "chance", 
        "color": "#ec4899", "icon": "❓", "price": 0
    },
    {
        "id": 23, "name": "سوهاج", "subtitle": "أرض الأجداد والأديرة", "type": "property", 
        "group": "red", "groupName": "أحمر", "color": "#ef4444", "icon": "☀️",
        "price": 220, "rent": [18, 90, 250, 700, 875, 1050], "houseCost": 150, "mortgage": 110
    },
    {
        "id": 24, "name": "قنا", "subtitle": "دندرة وحضارة الصعيد", "type": "property", 
        "group": "red", "groupName": "أحمر", "color": "#ef4444", "icon": "🦅",
        "price": 240, "rent": [20, 100, 300, 750, 925, 1100], "houseCost": 150, "mortgage": 120
    },
    {
        "id": 25, "name": "محطة الأقصر", "subtitle": "سكك حديد الصعيد", "type": "station", 
        "group": "station", "groupName": "محطة", "color": "#334155", "icon": "🚊",
        "price": 200, "rent": [25, 50, 100, 200], "mortgage": 100
    },
    {
        "id": 26, "name": "الغردقة", "subtitle": "لؤلؤة البحر الأحمر", "type": "property", 
        "group": "yellow", "groupName": "أصفر", "color": "#eab308", "icon": "🤿",
        "price": 260, "rent": [22, 110, 330, 800, 975, 1150], "houseCost": 150, "mortgage": 130
    },
    {
        "id": 27, "name": "شرم الشيخ", "subtitle": "مدينة السلام العالمية", "type": "property", 
        "group": "yellow", "groupName": "أصفر", "color": "#eab308", "icon": "🏖️",
        "price": 260, "rent": [22, 110, 330, 800, 975, 1150], "houseCost": 150, "mortgage": 130
    },
    {
        "id": 28, "name": "شركة المياه", "subtitle": "مرفق عام وشريان النيل", "type": "utility", 
        "group": "utility", "groupName": "مرفق", "color": "#06b6d4", "icon": "🚰",
        "price": 150, "mortgage": 75
    },
    {
        "id": 29, "name": "مرسى مطروح", "subtitle": "شواطئ الفيروز وعجيبة", "type": "property", 
        "group": "yellow", "groupName": "أصفر", "color": "#eab308", "icon": "🐚",
        "price": 280, "rent": [24, 120, 360, 850, 1025, 1200], "houseCost": 150, "mortgage": 140
    },
    {
        "id": 30, "name": "ادخل السجن!", "subtitle": "اذهب فوراً دون مرور بالبداية", "type": "gotojail", 
        "color": "#991b1b", "icon": "👮‍♂️", "price": 0
    },
    {
        "id": 31, "name": "الأقصر", "subtitle": "معبد الكرنك والملوك", "type": "property", 
        "group": "green", "groupName": "أخضر", "color": "#22c55e", "icon": "🏛️",
        "price": 300, "rent": [26, 130, 390, 900, 1100, 1275], "houseCost": 200, "mortgage": 150
    },
    {
        "id": 32, "name": "أسوان", "subtitle": "بلاد الذهب وفيلة والسد", "type": "property", 
        "group": "green", "groupName": "أخضر", "color": "#22c55e", "icon": "⛵",
        "price": 300, "rent": [26, 130, 390, 900, 1100, 1275], "houseCost": 200, "mortgage": 150
    },
    {
        "id": 33, "name": "صندوق الدنيا", "subtitle": "محفظة الشعب", "type": "chest", 
        "color": "#f59e0b", "icon": "🎁", "price": 0
    },
    {
        "id": 34, "name": "الإسكندرية", "subtitle": "عروس البحر المتوسط", "type": "property", 
        "group": "green", "groupName": "أخضر", "color": "#22c55e", "icon": "🏰",
        "price": 320, "rent": [28, 150, 450, 1000, 1200, 1400], "houseCost": 200, "mortgage": 160
    },
    {
        "id": 35, "name": "محطة أسوان", "subtitle": "بوابة النوبة والجنوب", "type": "station", 
        "group": "station", "groupName": "محطة", "color": "#334155", "icon": "🚉",
        "price": 200, "rent": [25, 50, 100, 200], "mortgage": 100
    },
    {
        "id": 36, "name": "كارت الحظ", "subtitle": "جرب حظك اليوم", "type": "chance", 
        "color": "#ec4899", "icon": "❓", "price": 0
    },
    {
        "id": 37, "name": "الجيزة", "subtitle": "الأهرامات العظيمة وأبو الهول", "type": "property", 
        "group": "darkblue", "groupName": "أزرق ملكي", "color": "#2563eb", "icon": "🐫",
        "price": 350, "rent": [35, 175, 500, 1100, 1300, 1500], "houseCost": 200, "mortgage": 175
    },
    {
        "id": 38, "name": "ضريبة الرفاهية", "subtitle": "ادفع 100 ج.م", "type": "tax", 
        "color": "#ef4444", "icon": "💎", "price": 100
    },
    {
        "id": 39, "name": "القاهرة", "subtitle": "برج القاهرة وقصر النيل", "type": "property", 
        "group": "darkblue", "groupName": "أزرق ملكي", "color": "#2563eb", "icon": "🗼",
        "price": 400, "rent": [50, 200, 600, 1400, 1700, 2000], "houseCost": 200, "mortgage": 200
    }
]

print(f"Total tiles configured: {len(TILES)}")
