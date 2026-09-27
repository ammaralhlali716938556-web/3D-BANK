import json

TILES = [
    {
        "id": 0, "name": "انطلق", "subtitle": "البداية (+200 $)", "type": "go",
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
        "id": 4, "name": "ضريبة الدخل", "subtitle": "ادفع 200 $", "type": "tax",
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
        "id": 13, "name": "كفر الشيخ", "subtitle": "أرض الأمل والخير", "type": "property",
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
        "id": 32, "name": "أسوان", "subtitle": "بلاد الذهب والسد العالي", "type": "property",
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
        "id": 37, "name": "الجيزة", "subtitle": "الأهرامات وأبو الهول", "type": "property",
        "group": "darkblue", "groupName": "أزرق ملكي", "color": "#2563eb", "icon": "🐫",
        "price": 350, "rent": [35, 175, 500, 1100, 1300, 1500], "houseCost": 200, "mortgage": 175
    },
    {
        "id": 38, "name": "ضريبة الرفاهية", "subtitle": "ادفع 100 $", "type": "tax",
        "color": "#ef4444", "icon": "💎", "price": 100
    },
    {
        "id": 39, "name": "القاهرة", "subtitle": "برج القاهرة وقصر النيل", "type": "property",
        "group": "darkblue", "groupName": "أزرق ملكي", "color": "#2563eb", "icon": "🗼",
        "price": 400, "rent": [50, 200, 600, 1400, 1700, 2000], "houseCost": 200, "mortgage": 200
    }
]

CHANCE_CARDS = [
    {
        "title": "عملية سطو على البنك! 💰",
        "desc": "فرصة ذهبية لاقتحام خزينة البنك الكبرى! خض جولة السطو على البنك وافتح الخزائن لتفوز بثروة طائلة!",
        "action": "heist", "icon": "💰"
    },
    {
        "title": "هجوم وتعطيل معالم الخصم! 🔨",
        "desc": "أطلق المطرقة الكرتونية المدمرة على معالم أحد الخصوم واحصل على غنائم ضخمة إن لم يحمها بالدرع!",
        "action": "shutdown", "icon": "🔨"
    },
    {
        "title": "تقدم إلى نقطة البداية (انطلق) 🚀",
        "desc": "تحرك فوراً إلى مربع انطلق واستلم مكافأة 200 $ !",
        "action": "move_to", "target": 0, "icon": "🚀"
    },
    {
        "title": "رحلة إلى قلب العاصمة: القاهرة! 🗼",
        "desc": "تقدم فوراً إلى عقار القاهرة الفاخر. إذا كان متاحاً يمكنك شراؤه، وإذا كان لخصمك ادفع الإيجار!",
        "action": "move_to", "target": 39, "icon": "🗼"
    },
    {
        "title": "أرباح أسهم البورصة المصرية 📈",
        "desc": "حققت استثماراتك في البورصة عوائد ممتازة! احصل على 150 $ نقداً من البنك!",
        "action": "cash", "amount": 150, "icon": "📈"
    },
    {
        "title": "كارت الخروج من السجن مجاناً 🗝️",
        "desc": "احتفظ بهذا الكارت السري لتخرج به من السجن مجاناً في أي وقت تحتاجه دون دفع غرامة الكفالة!",
        "action": "jail_free", "icon": "🗝️"
    },
    {
        "title": "غرامة رادار على كوبري 6 أكتوبر 🚓",
        "desc": "تجاوزت السرعة القانونية أثناء قيادة سيارتك الفارهة! ادفع غرامة قدرها 50 $ لحصيلة الاستراحة المجانية!",
        "action": "pay_tax", "amount": 50, "icon": "🚓"
    },
    {
        "title": "شحن دروع الحماية الأسطورية 🛡️",
        "desc": "مكافأة دفاعية ممتازة! تم شحن دروعك بالكامل لحماية معالمك من أي هجوم مباغت!",
        "action": "shield", "icon": "🛡️"
    },
    {
        "title": "ترميم وتجديد عقاراتك 🛠️",
        "desc": "أعمال صيانة شاملة: ادفع 25 $ عن كل منزل تمتلكه و 100 $ عن كل فندق!",
        "action": "repair", "house": 25, "hotel": 100, "icon": "🛠️"
    },
    {
        "title": "لفة مجانية في عجلة الحظ الدوارة 🎡",
        "desc": "أدر عجلة الحظ الكرتونية الآن واربح جوائز نرد وأموال ودروع قيّمة!",
        "action": "wheel", "icon": "🎡"
    },
    {
        "title": "ادخل السجن فوراً! ⛓️",
        "desc": "تم رصد مخالفات مالية كبرى! اذهب مباشرة إلى سجن القلعة دون أن تمر بنقطة انطلق ولا تقبض 200 $!",
        "action": "jail", "icon": "⛓️"
    }
]

CHEST_CARDS = [
    {
        "title": "استرداد ضريبي من وزارة المالية 💵",
        "desc": "مراجعة الحسابات أسفرت عن استرداد ضريبي لصالحك! احصل على 100 $ فوراً من البنك!",
        "action": "cash", "amount": 100, "icon": "💵"
    },
    {
        "title": "عيد ميلادك السعيد! 🎂",
        "desc": "احتفل مع منافسيك! يدفع كل لاعب لك هدية نقدية قدرها 25 $ تعبيراً عن المودة!",
        "action": "birthday", "amount": 25, "icon": "🎂"
    },
    {
        "title": "عائد استثمار قناة السويس 🚢",
        "desc": "استثمارك في شهادات الاستثمار الوطنية حقق أرباحاً هائلة! احصل على 200 $!",
        "action": "cash", "amount": 200, "icon": "🚢"
    },
    {
        "title": "تكاليف الفحص الطبي بالمستشفى 🏥",
        "desc": "أجريت فحوصاتك الدورية في أرقى المراكز الطبية! ادفع 50 $ للمحفظة العامة!",
        "action": "pay_tax", "amount": 50, "icon": "🏥"
    },
    {
        "title": "عملية سطو على البنك! 💰",
        "desc": "فتحت الأبواب السرية لخزنة البنك! حان وقت السطو على البنك وجمع سبائك الذهب!",
        "action": "heist", "icon": "💰"
    },
    {
        "title": "بيع محصول القمح والخير 🌾",
        "desc": "موسم حصاد وفير ومبارك في ريف مصر! احصل على 120 $ أرباح مبيعات المحصول!",
        "action": "cash", "amount": 120, "icon": "🌾"
    },
    {
        "title": "فاتورة خدمات متأخرة 💡",
        "desc": "سدد مستحقات الكهرباء والمياه لشركات المرافق العامة! ادفع 40 $!",
        "action": "pay_tax", "amount": 40, "icon": "💡"
    },
    {
        "title": "تقدم إلى الإسكندرية عروس المتوسط 🌊",
        "desc": "رحلة استجمام ساحلية! تحرك فوراً إلى مربع الإسكندرية الجميل!",
        "action": "move_to", "target": 34, "icon": "🌊"
    },
    {
        "title": "درع طاقة ملكي إضافي 🛡️",
        "desc": "منحتك الجمعية درعاً حصيناً لحماية أحد معالمك من التخريب والهجوم!",
        "action": "shield", "icon": "🛡️"
    },
    {
        "title": "تذكرة ذهبية لعجلة الحظ! 🎡",
        "desc": "حصلت على فرصة نادرة لدخول عجلة الحظ والمخاطرة! العجلة قد تنفع وقد تضر، أدرها واكتشف نصيبك!",
        "action": "wheel", "icon": "🎡"
    }
]

LANDMARKS = [
    {
        "id": "pyramids",
        "name": "أهرامات الجيزة الخالدة",
        "icon": "🐫",
        "stages": [
            {"name": "أساسات الحجر الجيري", "cost": 120, "netWorth": 40},
            {"name": "بناء الهرم الأكبر (خوفو)", "cost": 180, "netWorth": 60},
            {"name": "بناء هرم خفرع وتمثال أبو الهول", "cost": 260, "netWorth": 90},
            {"name": "الكساء الملكي الخارجي الأملس", "cost": 360, "netWorth": 120},
            {"name": "القمة الذهبية المشعة للأهرام", "cost": 500, "netWorth": 180}
        ]
    },
    {
        "id": "cairo_tower",
        "name": "برج القاهرة وزهرة اللوتس",
        "icon": "🗼",
        "stages": [
            {"name": "قاعدة اللوتس الجرانيتية الفاخرة", "cost": 140, "netWorth": 45},
            {"name": "الهيكل الخرساني الشبكي المشبك", "cost": 200, "netWorth": 70},
            {"name": "المصاعد البانورامية السريعة", "cost": 280, "netWorth": 100},
            {"name": "صالة المراقبة البانورامية العلوية", "cost": 380, "netWorth": 130},
            {"name": "المطعم الدوار ومروحة الإرسال الذهبية", "cost": 520, "netWorth": 190}
        ]
    },
    {
        "id": "citadel",
        "name": "قلعة صلاح الدين الأيوبي",
        "icon": "🏰",
        "stages": [
            {"name": "الأسوار الحجرية والخنادق الحصينة", "cost": 130, "netWorth": 40},
            {"name": "أبراج المراقبة وقاعة العرش", "cost": 190, "netWorth": 65},
            {"name": "مئذنتا جامع محمد علي الشاهقتان", "cost": 270, "netWorth": 95},
            {"name": "القباب الفضية المتلألئة المضاءة", "cost": 370, "netWorth": 125},
            {"name": "المتحف الحربي والثريات الملكية", "cost": 490, "netWorth": 175}
        ]
    },
    {
        "id": "alex_lighthouse",
        "name": "منارة الإسكندرية الأسطورية",
        "icon": "🏮",
        "stages": [
            {"name": "الرصيف الحجري البحري وحواجز الأمواج", "cost": 110, "netWorth": 35},
            {"name": "البرج الثماني والأبراج المساعدة", "cost": 170, "netWorth": 60},
            {"name": "الفانوس البصري الكريستالي العاكس", "cost": 250, "netWorth": 85},
            {"name": "الشعلة النارية الأزلية الهادية للسفن", "cost": 340, "netWorth": 115},
            {"name": "تمثال بوسيدون الذهبي والأسطول البحري", "cost": 470, "netWorth": 165}
        ]
    },
    {
        "id": "luxor_temple",
        "name": "معبد الكرنك وطريق الكباش",
        "icon": "🏛️",
        "stages": [
            {"name": "الصرح الأول والبوابة الضخمة", "cost": 125, "netWorth": 40},
            {"name": "بهو الأعمدة الكبرى العملاقة", "cost": 185, "netWorth": 65},
            {"name": "المسلات الجرانيتية المنقوشة بالهيروغليفية", "cost": 265, "netWorth": 90},
            {"name": "طريق الكباش الملكي المضاء ليلاً", "cost": 355, "netWorth": 120},
            {"name": "قدس الأقداس وقرص الشمس المجنح", "cost": 480, "netWorth": 170}
        ]
    }
]

CHARACTERS = [
    {
        "id": "mr_hazz",
        "name": "مستر حظ",
        "title": "الملياردير الطموح",
        "avatar": "🎩",
        "color": "#ef4444",
        "quote": "الفرصة لا تأتي مرتين، والحظ حليف الجريء!"
    },
    {
        "id": "cleo_kid",
        "name": "كليوباترا كيد",
        "title": "أميرة المال والذهب",
        "avatar": "👑",
        "color": "#eab308",
        "quote": "الأهرامات بُنيت بالذهب والعزيمة!"
    },
    {
        "id": "omda_farfoush",
        "name": "العمدة فرفوش",
        "title": "كبير أعيان البلد",
        "avatar": "🧔",
        "color": "#10b981",
        "quote": "يا صلاة الزين! عقاراتنا تسوى ملايين!"
    },
    {
        "id": "mini_explorer",
        "name": "المكتشف الصغير",
        "title": "صياد الكنوز والألغاز",
        "avatar": "🧭",
        "color": "#3b82f6",
        "quote": "وراء كل مربع سر، ووراء كل سكة قطار مغامرة!"
    }
]

WHEEL_ITEMS = [
    {
        "label": "💰 +500 $",
        "type": "cash_win",
        "amount": 500,
        "color": "#16a34a",
        "isWin": True,
        "desc": "مبروك! ربحت جائزة نقدية كبرى قدرها +500 $!",
        "desc_en": "Jackpot! Won +500 Cash prize!"
    },
    {
        "label": "💸 -300 $",
        "type": "cash_loss",
        "amount": 300,
        "color": "#dc2626",
        "isWin": False,
        "desc": "لسوء الحظ! غرامة بقيمة -300 $ تُودع في وعاء الاستراحة!",
        "desc_en": "Penalty! -300 fine sent to Free Parking pot!"
    },
    {
        "label": "🎲 +25 نرد",
        "type": "rolls_win",
        "amount": 25,
        "color": "#ea580c",
        "isWin": True,
        "desc": "طاقة متجددة! حصلت على +25 رمية نرد إضافية!",
        "desc_en": "Energy boost! +25 Extra dice rolls awarded!"
    },
    {
        "label": "⛓️ ادخل السجن!",
        "type": "jail",
        "amount": 0,
        "color": "#1e293b",
        "isWin": False,
        "desc": "أمر حبس فوري! تم نقلك مباشرة إلى سجن القلعة!",
        "desc_en": "Arrested! Sent directly to Citadel Prison!"
    },
    {
        "label": "🛡️ شحن دروع",
        "type": "shield_win",
        "amount": 3,
        "color": "#2563eb",
        "isWin": True,
        "desc": "حصانة ملكية! تم شحن دروعك الثلاثة بالكامل!",
        "desc_en": "Defense restored! All 3 shields fully recharged!"
    },
    {
        "label": "💔 -200 للخصم",
        "type": "pay_rival",
        "amount": 200,
        "color": "#9333ea",
        "isWin": False,
        "desc": "خسارة فادحة! سددت 200 $ كتعويض مباشر لمنافسك!",
        "desc_en": "Penalty! Paid 200 directly to your rival!"
    },
    {
        "label": "🌟 كنز +750",
        "type": "cash_win",
        "amount": 750,
        "color": "#ca8a04",
        "isWin": True,
        "desc": "ضربة حظ أسطورية! فزت بالكنز الذهبي +750 $!",
        "desc_en": "Legendary Luck! Won golden treasure of +750 Cash!"
    },
    {
        "label": "🔨 هدم دروعك",
        "type": "shield_loss",
        "amount": 0,
        "color": "#b91c1c",
        "isWin": False,
        "desc": "ضربة قاصمة! تحطمت دروعك بالكامل وأصبحت بلا حماية!",
        "desc_en": "Shields shattered! All your shields are destroyed!"
    }
]

print("board_data.py module ready!")
