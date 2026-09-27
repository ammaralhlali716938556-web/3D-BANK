# Multilingual Module for Bank El Hazz 3D (14 Languages)
import json

I18N_LANGUAGES = [
  {
    "code": "ar",
    "name": "العربية",
    "flag": "🇾🇪",
    "region": "arab",
    "dir": "rtl"
  },
  {
    "code": "en",
    "name": "English",
    "flag": "🇬🇧",
    "region": "europe",
    "dir": "ltr"
  },
  {
    "code": "zh",
    "name": "中文",
    "flag": "🇨🇳",
    "region": "asia",
    "dir": "ltr"
  },
  {
    "code": "fr",
    "name": "Français",
    "flag": "🇫🇷",
    "region": "europe",
    "dir": "ltr"
  },
  {
    "code": "es",
    "name": "Español",
    "flag": "🇪🇸",
    "region": "europe",
    "dir": "ltr"
  },
  {
    "code": "ru",
    "name": "Русский",
    "flag": "🇷🇺",
    "region": "europe",
    "dir": "ltr"
  },
  {
    "code": "de",
    "name": "Deutsch",
    "flag": "🇩🇪",
    "region": "europe",
    "dir": "ltr"
  },
  {
    "code": "it",
    "name": "Italiano",
    "flag": "🇮🇹",
    "region": "europe",
    "dir": "ltr"
  },
  {
    "code": "pt",
    "name": "Português",
    "flag": "🇵🇹",
    "region": "europe",
    "dir": "ltr"
  },
  {
    "code": "tr",
    "name": "Türkçe",
    "flag": "🇹🇷",
    "region": "europe",
    "dir": "ltr"
  },
  {
    "code": "hi",
    "name": "हिन्दी",
    "flag": "🇮🇳",
    "region": "asia",
    "dir": "ltr"
  },
  {
    "code": "ja",
    "name": "日本語",
    "flag": "🇯🇵",
    "region": "asia",
    "dir": "ltr"
  },
  {
    "code": "ko",
    "name": "한국어",
    "flag": "🇰🇷",
    "region": "asia",
    "dir": "ltr"
  },
  {
    "code": "fa",
    "name": "فارسی",
    "flag": "🇮🇷",
    "region": "asia",
    "dir": "rtl"
  }
]

I18N_TILES = {
  "ar": {
    "0": {
      "name": "انطلق",
      "sub": "اقبض 200 $ عند المرور"
    },
    "1": {
      "name": "صنعاء",
      "sub": "عاصمة اليمن التاريخية"
    },
    "2": {
      "name": "صندوق الدنيا",
      "sub": "محفظة الشعب والجوائز"
    },
    "3": {
      "name": "غزة",
      "sub": "رمز العزة والكرامة"
    },
    "4": {
      "name": "ضريبة الدخل",
      "sub": "ادفع 200 $ للوعاء"
    },
    "5": {
      "name": "محطة الحجاز",
      "sub": "خط سكة حديد الحجاز"
    },
    "6": {
      "name": "مسقط",
      "sub": "عروس بحر العرب"
    },
    "7": {
      "name": "كارت الحظ",
      "sub": "جرب حظك ومفاجآتك"
    },
    "8": {
      "name": "المنامة",
      "sub": "لؤلؤة الخليج العربي"
    },
    "9": {
      "name": "الكويت",
      "sub": "درة الخليج العربي"
    },
    "10": {
      "name": "سجن القلعة",
      "sub": "زيارة بريئة / حبس"
    },
    "11": {
      "name": "عمان",
      "sub": "مدينة التلال الأردنية"
    },
    "12": {
      "name": "شركة الكهرباء",
      "sub": "مرفق الطاقة الوطني"
    },
    "13": {
      "name": "تونس",
      "sub": "الخضراء والزيتونة"
    },
    "14": {
      "name": "طرابلس",
      "sub": "عروس البحر المتوسط"
    },
    "15": {
      "name": "قطار الحرمين",
      "sub": "السريع الرابط بين المدن"
    },
    "16": {
      "name": "بيروت",
      "sub": "باريس الشرق وعاصمة الفن"
    },
    "17": {
      "name": "صندوق الدنيا",
      "sub": "محفظة الشعب والجوائز"
    },
    "18": {
      "name": "الخرطوم",
      "sub": "ملتقى النيلين الخالد"
    },
    "19": {
      "name": "الجزائر",
      "sub": "بلد المليون شهيد"
    },
    "20": {
      "name": "الاستراحة المجانية",
      "sub": "اربح كامل وعاء الاستراحة"
    },
    "21": {
      "name": "الدار البيضاء",
      "sub": "العاصمة الاقتصادية للمغرب"
    },
    "22": {
      "name": "كارت الحظ",
      "sub": "جرب حظك ومفاجآتك"
    },
    "23": {
      "name": "دمشق",
      "sub": "أقدم عاصمة مأهولة بالتاريخ"
    },
    "24": {
      "name": "بغداد",
      "sub": "دار السلام وعاصمة الرشيد"
    },
    "25": {
      "name": "محطة المشرق",
      "sub": "خطوط بلاد الشام والعراق"
    },
    "26": {
      "name": "دبي",
      "sub": "مدينة المستقبل والأبراج"
    },
    "27": {
      "name": "الدوحة",
      "sub": "واحة الإبداع والتطور"
    },
    "28": {
      "name": "شركة المياه",
      "sub": "مرفق المياه والري"
    },
    "29": {
      "name": "جدة",
      "sub": "عروس البحر الأحمر"
    },
    "30": {
      "name": "ادخل السجن!",
      "sub": "اذهب فوراً دون استلام 200"
    },
    "31": {
      "name": "الرياض",
      "sub": "عاصمة المملكة وقلب نجد"
    },
    "32": {
      "name": "أبوظبي",
      "sub": "عاصمة الأصالة والريادة"
    },
    "33": {
      "name": "صندوق الدنيا",
      "sub": "محفظة الشعب والجوائز"
    },
    "34": {
      "name": "الإسكندرية",
      "sub": "عروس المتوسط ومنارة العلم"
    },
    "35": {
      "name": "محطة المغرب",
      "sub": "قطار البراق فائق السرعة"
    },
    "36": {
      "name": "كارت الحظ",
      "sub": "جرب حظك ومفاجآتك"
    },
    "37": {
      "name": "القدس",
      "sub": "زهرة المدائن والمهد"
    },
    "38": {
      "name": "ضريبة الرفاهية",
      "sub": "ادفع 100 $ للوعاء"
    },
    "39": {
      "name": "القاهرة",
      "sub": "قاهرة المعز وأم الدنيا"
    }
  },
  "en": {
    "0": {
      "name": "GO",
      "sub": "Collect 200 as you pass"
    },
    "1": {
      "name": "Athens",
      "sub": "Ancient Greek Capital"
    },
    "2": {
      "name": "Community Chest",
      "sub": "Prizes & Rewards"
    },
    "3": {
      "name": "Dublin",
      "sub": "Emerald Isle Capital"
    },
    "4": {
      "name": "Income Tax",
      "sub": "Pay 200 to Pot"
    },
    "5": {
      "name": "Eurostar Central",
      "sub": "Cross-Channel Rail"
    },
    "6": {
      "name": "Lisbon",
      "sub": "Atlantic Coast Jewel"
    },
    "7": {
      "name": "Chance Card",
      "sub": "Try your luck"
    },
    "8": {
      "name": "Warsaw",
      "sub": "Historic Capital"
    },
    "9": {
      "name": "Budapest",
      "sub": "Pearl of the Danube"
    },
    "10": {
      "name": "Citadel Jail",
      "sub": "Just Visiting / In Jail"
    },
    "11": {
      "name": "Prague",
      "sub": "City of Hundred Spires"
    },
    "12": {
      "name": "Electric Grid",
      "sub": "Energy Utility"
    },
    "13": {
      "name": "Copenhagen",
      "sub": "Nordic Haven"
    },
    "14": {
      "name": "Stockholm",
      "sub": "Venice of the North"
    },
    "15": {
      "name": "Orient Express",
      "sub": "Continental Line"
    },
    "16": {
      "name": "Brussels",
      "sub": "Capital of Europe"
    },
    "17": {
      "name": "Community Chest",
      "sub": "Prizes & Rewards"
    },
    "18": {
      "name": "Amsterdam",
      "sub": "City of Canals"
    },
    "19": {
      "name": "Vienna",
      "sub": "Imperial Music Capital"
    },
    "20": {
      "name": "Free Parking",
      "sub": "Win Entire Pot"
    },
    "21": {
      "name": "Zurich",
      "sub": "Alpine Financial Center"
    },
    "22": {
      "name": "Chance Card",
      "sub": "Try your luck"
    },
    "23": {
      "name": "Munich",
      "sub": "Heart of Bavaria"
    },
    "24": {
      "name": "Milan",
      "sub": "Fashion & Design Hub"
    },
    "25": {
      "name": "TGV Grand",
      "sub": "High Speed Line"
    },
    "26": {
      "name": "Madrid",
      "sub": "Royal Spanish Capital"
    },
    "27": {
      "name": "Barcelona",
      "sub": "Catalan Wonder"
    },
    "28": {
      "name": "Water Works",
      "sub": "Water Utility"
    },
    "29": {
      "name": "Rome",
      "sub": "The Eternal City"
    },
    "30": {
      "name": "Go to Jail!",
      "sub": "Direct Incarceration"
    },
    "31": {
      "name": "Berlin",
      "sub": "Modern Cultural Core"
    },
    "32": {
      "name": "London",
      "sub": "Royal Thames Metropolis"
    },
    "33": {
      "name": "Community Chest",
      "sub": "Prizes & Rewards"
    },
    "34": {
      "name": "Paris",
      "sub": "City of Light"
    },
    "35": {
      "name": "Alpine Express",
      "sub": "Mountain Rail"
    },
    "36": {
      "name": "Chance Card",
      "sub": "Try your luck"
    },
    "37": {
      "name": "Geneva",
      "sub": "Global Peace Capital"
    },
    "38": {
      "name": "Luxury Tax",
      "sub": "Pay 100 to Pot"
    },
    "39": {
      "name": "Venice",
      "sub": "Serene Floating City"
    }
  },
  "fr": {
    "0": {
      "name": "DÉPART",
      "sub": "Recevez 200 au passage"
    },
    "1": {
      "name": "Athènes",
      "sub": "Berceau Historique"
    },
    "2": {
      "name": "Caisse de Communauté",
      "sub": "Prix et Récompenses"
    },
    "3": {
      "name": "Dublin",
      "sub": "Capitale Celte"
    },
    "4": {
      "name": "Impôt sur le Revenu",
      "sub": "Payez 200 au Parc"
    },
    "5": {
      "name": "Gare Eurostar",
      "sub": "Liaison Transmanche"
    },
    "6": {
      "name": "Lisbonne",
      "sub": "Joyau de l'Atlantique"
    },
    "7": {
      "name": "Carte Chance",
      "sub": "Tentez votre chance"
    },
    "8": {
      "name": "Varsovie",
      "sub": "Cité Phénix"
    },
    "9": {
      "name": "Budapest",
      "sub": "Perle du Danube"
    },
    "10": {
      "name": "Prison de la Citadelle",
      "sub": "Simple Visite / En Prison"
    },
    "11": {
      "name": "Prague",
      "sub": "Ville aux Cent Clochers"
    },
    "12": {
      "name": "Réseau Électrique",
      "sub": "Service Public"
    },
    "13": {
      "name": "Copenhague",
      "sub": "Capitale Nordique"
    },
    "14": {
      "name": "Stockholm",
      "sub": "Venise du Nord"
    },
    "15": {
      "name": "Orient-Express",
      "sub": "Ligne Légendaire"
    },
    "16": {
      "name": "Bruxelles",
      "sub": "Cœur de l'Europe"
    },
    "17": {
      "name": "Caisse de Communauté",
      "sub": "Prix et Récompenses"
    },
    "18": {
      "name": "Amsterdam",
      "sub": "Cité des Canaux"
    },
    "19": {
      "name": "Vienne",
      "sub": "Cité Impériale"
    },
    "20": {
      "name": "Parc Gratuit",
      "sub": "Remportez la Cagnotte"
    },
    "21": {
      "name": "Zurich",
      "sub": "Finance Alpine"
    },
    "22": {
      "name": "Carte Chance",
      "sub": "Tentez votre chance"
    },
    "23": {
      "name": "Munich",
      "sub": "Cité Bavaroise"
    },
    "24": {
      "name": "Milan",
      "sub": "Capitale de la Mode"
    },
    "25": {
      "name": "TGV Grand",
      "sub": "Grande Vitesse"
    },
    "26": {
      "name": "Madrid",
      "sub": "Cœur Ibérique"
    },
    "27": {
      "name": "Barcelone",
      "sub": "Merveille Catalane"
    },
    "28": {
      "name": "Compagnie des Eaux",
      "sub": "Service Public"
    },
    "29": {
      "name": "Rome",
      "sub": "La Ville Éternelle"
    },
    "30": {
      "name": "Allez en Prison !",
      "sub": "Incarcération Directe"
    },
    "31": {
      "name": "Berlin",
      "sub": "Cœur Culturel"
    },
    "32": {
      "name": "Londres",
      "sub": "Capitale Royale"
    },
    "33": {
      "name": "Caisse de Communauté",
      "sub": "Prix et Récompenses"
    },
    "34": {
      "name": "Paris",
      "sub": "La Ville Lumière"
    },
    "35": {
      "name": "Express Alpin",
      "sub": "Train des Cimes"
    },
    "36": {
      "name": "Carte Chance",
      "sub": "Tentez votre chance"
    },
    "37": {
      "name": "Genève",
      "sub": "Capitale Mondiale"
    },
    "38": {
      "name": "Taxe de Luxe",
      "sub": "Payez 100 au Parc"
    },
    "39": {
      "name": "Venise",
      "sub": "Sérénissime sur l'Eau"
    }
  },
  "es": {
    "0": {
      "name": "SALIDA",
      "sub": "Cobre 200 al pasar"
    },
    "1": {
      "name": "Atenas",
      "sub": "Cuna de la Historia"
    },
    "2": {
      "name": "Caja de Comunidad",
      "sub": "Premios y Recompensas"
    },
    "3": {
      "name": "Dublín",
      "sub": "Capital Esmeralda"
    },
    "4": {
      "name": "Impuesto sobre Renta",
      "sub": "Pague 200 al Bote"
    },
    "5": {
      "name": "Estación Eurostar",
      "sub": "Línea Europea"
    },
    "6": {
      "name": "Lisboa",
      "sub": "Perla del Atlántico"
    },
    "7": {
      "name": "Carta de Suerte",
      "sub": "Pruebe su fortuna"
    },
    "8": {
      "name": "Varsovia",
      "sub": "Ciudad Resurgida"
    },
    "9": {
      "name": "Budapest",
      "sub": "Perla del Danubio"
    },
    "10": {
      "name": "Cárcel de la Ciudadela",
      "sub": "Solo Visita / En Cárcel"
    },
    "11": {
      "name": "Praga",
      "sub": "Ciudad Dorada"
    },
    "12": {
      "name": "Compañía Eléctrica",
      "sub": "Servicio Eléctrico"
    },
    "13": {
      "name": "Copenhague",
      "sub": "Capital Nórdica"
    },
    "14": {
      "name": "Estocolmo",
      "sub": "Venecia del Norte"
    },
    "15": {
      "name": "Orient Express",
      "sub": "Línea Continental"
    },
    "16": {
      "name": "Bruselas",
      "sub": "Capital Europea"
    },
    "17": {
      "name": "Caja de Comunidad",
      "sub": "Premios y Recompensas"
    },
    "18": {
      "name": "Ámsterdam",
      "sub": "Canales Históricos"
    },
    "19": {
      "name": "Viena",
      "sub": "Ciudad Imperial"
    },
    "20": {
      "name": "Estacionamiento Libre",
      "sub": "Gane el Bote"
    },
    "21": {
      "name": "Zúrich",
      "sub": "Centro Financiero"
    },
    "22": {
      "name": "Carta de Suerte",
      "sub": "Pruebe su fortuna"
    },
    "23": {
      "name": "Múnich",
      "sub": "Corazón Bávaro"
    },
    "24": {
      "name": "Milán",
      "sub": "Capital de la Moda"
    },
    "25": {
      "name": "TGV Grand",
      "sub": "Alta Velocidad"
    },
    "26": {
      "name": "Madrid",
      "sub": "Corte y Capital"
    },
    "27": {
      "name": "Barcelona",
      "sub": "Ciudad Condal"
    },
    "28": {
      "name": "Aguas Corrientes",
      "sub": "Servicio Hídrico"
    },
    "29": {
      "name": "Roma",
      "sub": "La Ciudad Eterna"
    },
    "30": {
      "name": "¡Vaya a la Cárcel!",
      "sub": "Prisión Inmediata"
    },
    "31": {
      "name": "Berlín",
      "sub": "Metrópolis Moderna"
    },
    "32": {
      "name": "Londres",
      "sub": "Gran Metrópoli"
    },
    "33": {
      "name": "Caja de Comunidad",
      "sub": "Premios y Recompensas"
    },
    "34": {
      "name": "París",
      "sub": "Ciudad de la Luz"
    },
    "35": {
      "name": "Expreso Alpino",
      "sub": "Ferrocarril de Montaña"
    },
    "36": {
      "name": "Carta de Suerte",
      "sub": "Pruebe su fortuna"
    },
    "37": {
      "name": "Ginebra",
      "sub": "Centro Diplomático"
    },
    "38": {
      "name": "Impuesto de Lujo",
      "sub": "Pague 100 al Bote"
    },
    "39": {
      "name": "Venecia",
      "sub": "La Reina del Adriático"
    }
  },
  "ru": {
    "0": {
      "name": "СТАРТ",
      "sub": "Получите 200 при проходе"
    },
    "1": {
      "name": "Афины",
      "sub": "Колыбель цивилизации"
    },
    "2": {
      "name": "Общественная казна",
      "sub": "Призы и награды"
    },
    "3": {
      "name": "Дублин",
      "sub": "Изумрудная столица"
    },
    "4": {
      "name": "Подоходный налог",
      "sub": "Заплатите 200 в банк"
    },
    "5": {
      "name": "Вокзал Евростар",
      "sub": "Трансъевропейский"
    },
    "6": {
      "name": "Лиссабон",
      "sub": "Атлантическая жемчужина"
    },
    "7": {
      "name": "Карточка Шанс",
      "sub": "Испытайте удачу"
    },
    "8": {
      "name": "Варшава",
      "sub": "Сердце Польши"
    },
    "9": {
      "name": "Будапешт",
      "sub": "Жемчужина Дуная"
    },
    "10": {
      "name": "Тюрьма крепости",
      "sub": "Только визит / В тюрьме"
    },
    "11": {
      "name": "Прага",
      "sub": "Город ста шпилей"
    },
    "12": {
      "name": "Электросеть",
      "sub": "Энергетическая сеть"
    },
    "13": {
      "name": "Копенгаген",
      "sub": "Скандинавская столица"
    },
    "14": {
      "name": "Стокгольм",
      "sub": "Северная Венеция"
    },
    "15": {
      "name": "Восточный экспресс",
      "sub": "Легендарный маршрут"
    },
    "16": {
      "name": "Брюссель",
      "sub": "Столица Европы"
    },
    "17": {
      "name": "Общественная казна",
      "sub": "Призы и награды"
    },
    "18": {
      "name": "Амстердам",
      "sub": "Город каналов"
    },
    "19": {
      "name": "Вена",
      "sub": "Имперская столица"
    },
    "20": {
      "name": "Бесплатная стоянка",
      "sub": "Заберите весь куш"
    },
    "21": {
      "name": "Цюрих",
      "sub": "Альпийский финцентр"
    },
    "22": {
      "name": "Карточка Шанс",
      "sub": "Испытайте удачу"
    },
    "23": {
      "name": "Мюнхен",
      "sub": "Сердце Баварии"
    },
    "24": {
      "name": "Милан",
      "sub": "Столица моды"
    },
    "25": {
      "name": "Вокзал TGV",
      "sub": "Скоростная дорога"
    },
    "26": {
      "name": "Мадрид",
      "sub": "Королевский центр"
    },
    "27": {
      "name": "Барселона",
      "sub": "Каталонская жемчужина"
    },
    "28": {
      "name": "Водоканал",
      "sub": "Водная компания"
    },
    "29": {
      "name": "Рим",
      "sub": "Вечный город"
    },
    "30": {
      "name": "В тюрьму!",
      "sub": "Прямой арест"
    },
    "31": {
      "name": "Берлин",
      "sub": "Метрополия искусств"
    },
    "32": {
      "name": "Лондон",
      "sub": "Королевская столица"
    },
    "33": {
      "name": "Общественная казна",
      "sub": "Призы и награды"
    },
    "34": {
      "name": "Париж",
      "sub": "Город света"
    },
    "35": {
      "name": "Альпийский экспресс",
      "sub": "Горная железная дорога"
    },
    "36": {
      "name": "Карточка Шанс",
      "sub": "Испытайте удачу"
    },
    "37": {
      "name": "Женева",
      "sub": "Мировой центр дипломатии"
    },
    "38": {
      "name": "Налог на роскошь",
      "sub": "Заплатите 100 в банк"
    },
    "39": {
      "name": "Венеция",
      "sub": "Великолепный город на воде"
    }
  },
  "de": {
    "0": {
      "name": "LOS",
      "sub": "Ziehe 200 beim Passieren ein"
    },
    "1": {
      "name": "Athen",
      "sub": "Historische Wiege"
    },
    "2": {
      "name": "Gemeinschaftskasse",
      "sub": "Preise & Gewinne"
    },
    "3": {
      "name": "Dublin",
      "sub": "Hauptstadt Irlands"
    },
    "4": {
      "name": "Einkommensteuer",
      "sub": "Zahle 200 in den Pott"
    },
    "5": {
      "name": "Eurostar Hauptbahnhof",
      "sub": "Kontinentalbahn"
    },
    "6": {
      "name": "Lissabon",
      "sub": "Perle des Atlantiks"
    },
    "7": {
      "name": "Ereigniskarte",
      "sub": "Versuche dein Glück"
    },
    "8": {
      "name": "Warschau",
      "sub": "Metropole an der Weichsel"
    },
    "9": {
      "name": "Budapest",
      "sub": "Perle der Donau"
    },
    "10": {
      "name": "Festungsgefängnis",
      "sub": "Nur zu Besuch / Im Gefängnis"
    },
    "11": {
      "name": "Prag",
      "sub": "Goldene Stadt"
    },
    "12": {
      "name": "Elektrizitätswerk",
      "sub": "Energieversorger"
    },
    "13": {
      "name": "Kopenhagen",
      "sub": "Nordische Metropole"
    },
    "14": {
      "name": "Stockholm",
      "sub": "Venedig des Nordens"
    },
    "15": {
      "name": "Orient-Express",
      "sub": "Historische Bahnlinie"
    },
    "16": {
      "name": "Brüssel",
      "sub": "Hauptstadt Europas"
    },
    "17": {
      "name": "Gemeinschaftskasse",
      "sub": "Preise & Gewinne"
    },
    "18": {
      "name": "Amsterdam",
      "sub": "Grachtenmetropole"
    },
    "19": {
      "name": "Wien",
      "sub": "Kaiserstadt der Musik"
    },
    "20": {
      "name": "Freies Parken",
      "sub": "Gewinne den gesamten Pott"
    },
    "21": {
      "name": "Zürich",
      "sub": "Alpen-Finanzzentrum"
    },
    "22": {
      "name": "Ereigniskarte",
      "sub": "Versuche dein Glück"
    },
    "23": {
      "name": "München",
      "sub": "Bayerische Metropole"
    },
    "24": {
      "name": "Mailand",
      "sub": "Hauptstadt der Mode"
    },
    "25": {
      "name": "TGV Express",
      "sub": "Hochgeschwindigkeitsbahn"
    },
    "26": {
      "name": "Madrid",
      "sub": "Königliche Metropole"
    },
    "27": {
      "name": "Barcelona",
      "sub": "Katalanisches Juwel"
    },
    "28": {
      "name": "Wasserwerk",
      "sub": "Wasserversorger"
    },
    "29": {
      "name": "Rom",
      "sub": "Die Ewige Stadt"
    },
    "30": {
      "name": "Gehe ins Gefängnis!",
      "sub": "Sofortige Inhaftierung"
    },
    "31": {
      "name": "Berlin",
      "sub": "Kultur- und Bundeshauptstadt"
    },
    "32": {
      "name": "London",
      "sub": "Metropole an der Themse"
    },
    "33": {
      "name": "Gemeinschaftskasse",
      "sub": "Preise & Gewinne"
    },
    "34": {
      "name": "Paris",
      "sub": "Stadt des Lichts"
    },
    "35": {
      "name": "Alpexpress",
      "sub": "Panoramabahn"
    },
    "36": {
      "name": "Ereigniskarte",
      "sub": "Versuche dein Glück"
    },
    "37": {
      "name": "Genf",
      "sub": "Friedenshauptstadt"
    },
    "38": {
      "name": "Luxussteuer",
      "sub": "Zahle 100 in den Pott"
    },
    "39": {
      "name": "Venedig",
      "sub": "Königin der Adria"
    }
  },
  "it": {
    "0": {
      "name": "VIA",
      "sub": "Ritira 200 al passaggio"
    },
    "1": {
      "name": "Atene",
      "sub": "Culla della Civiltà"
    },
    "2": {
      "name": "Cassa Comune",
      "sub": "Premi e Ricompense"
    },
    "3": {
      "name": "Dublino",
      "sub": "Capitale d'Irlanda"
    },
    "4": {
      "name": "Tassa sul Reddito",
      "sub": "Paga 200 al Montepremi"
    },
    "5": {
      "name": "Eurostar Centrale",
      "sub": "Ferrovia Europea"
    },
    "6": {
      "name": "Lisbona",
      "sub": "Gemma dell'Atlantico"
    },
    "7": {
      "name": "Carta Imprevisti",
      "sub": "Tenta la fortuna"
    },
    "8": {
      "name": "Varsavia",
      "sub": "Città Storica"
    },
    "9": {
      "name": "Budapest",
      "sub": "Perla del Danubio"
    },
    "10": {
      "name": "Prigione Fortezza",
      "sub": "Solo in Visita / In Prigione"
    },
    "11": {
      "name": "Praga",
      "sub": "Città Magica"
    },
    "12": {
      "name": "Società Elettrica",
      "sub": "Servizio Pubblico"
    },
    "13": {
      "name": "Copenaghen",
      "sub": "Capitale del Nord"
    },
    "14": {
      "name": "Stoccolma",
      "sub": "Venezia del Nord"
    },
    "15": {
      "name": "Orient Express",
      "sub": "Linea Leggendaria"
    },
    "16": {
      "name": "Bruxelles",
      "sub": "Cuore d'Europa"
    },
    "17": {
      "name": "Cassa Comune",
      "sub": "Premi e Ricompense"
    },
    "18": {
      "name": "Amsterdam",
      "sub": "Città dei Canali"
    },
    "19": {
      "name": "Vienna",
      "sub": "Città Imperiale"
    },
    "20": {
      "name": "Parcheggio Gratuito",
      "sub": "Vinci l'Intero Montepremi"
    },
    "21": {
      "name": "Zurigo",
      "sub": "Centro Finanziario"
    },
    "22": {
      "name": "Carta Imprevisti",
      "sub": "Tenta la fortuna"
    },
    "23": {
      "name": "Monaco",
      "sub": "Cuore della Baviera"
    },
    "24": {
      "name": "Milano",
      "sub": "Capitale della Moda"
    },
    "25": {
      "name": "TGV Grand",
      "sub": "Alta Velocità"
    },
    "26": {
      "name": "Madrid",
      "sub": "Cuore di Spagna"
    },
    "27": {
      "name": "Barcellona",
      "sub": "Perla Catalana"
    },
    "28": {
      "name": "Società Acqua Potabile",
      "sub": "Servizio Idrico"
    },
    "29": {
      "name": "Roma",
      "sub": "La Città Eterna"
    },
    "30": {
      "name": "In Prigione!",
      "sub": "Arresto Immediato"
    },
    "31": {
      "name": "Berlino",
      "sub": "Metropoli Culturale"
    },
    "32": {
      "name": "Londra",
      "sub": "Capitale Reale"
    },
    "33": {
      "name": "Cassa Comune",
      "sub": "Premi e Ricompense"
    },
    "34": {
      "name": "Parigi",
      "sub": "La Ville Lumière"
    },
    "35": {
      "name": "Espresso Alpino",
      "sub": "Ferrovia Alpina"
    },
    "36": {
      "name": "Carta Imprevisti",
      "sub": "Tenta la fortuna"
    },
    "37": {
      "name": "Ginevra",
      "sub": "Centro Internazionale"
    },
    "38": {
      "name": "Tassa di Lusso",
      "sub": "Paga 100 al Montepremi"
    },
    "39": {
      "name": "Venezia",
      "sub": "La Serenissima"
    }
  },
  "pt": {
    "0": {
      "name": "INÍCIO",
      "sub": "Receba 200 ao passar"
    },
    "1": {
      "name": "Atenas",
      "sub": "Berço Histórico"
    },
    "2": {
      "name": "Caixa Comunitária",
      "sub": "Prêmios e Bônus"
    },
    "3": {
      "name": "Dublin",
      "sub": "Capital Esmeralda"
    },
    "4": {
      "name": "Imposto de Renda",
      "sub": "Pague 200 ao Pote"
    },
    "5": {
      "name": "Eurostar Central",
      "sub": "Ligação Europeia"
    },
    "6": {
      "name": "Lisboa",
      "sub": "Jóia do Atlântico"
    },
    "7": {
      "name": "Carta de Sorte",
      "sub": "Tente sua sorte"
    },
    "8": {
      "name": "Varsóvia",
      "sub": "Capital Histórica"
    },
    "9": {
      "name": "Budapeste",
      "sub": "Pérola do Danúbio"
    },
    "10": {
      "name": "Cadeia da Cidadela",
      "sub": "Apenas Visita / Preso"
    },
    "11": {
      "name": "Praga",
      "sub": "Cidade Dourada"
    },
    "12": {
      "name": "Companhia de Energia",
      "sub": "Serviço Elétrico"
    },
    "13": {
      "name": "Copenhaga",
      "sub": "Capital Nórdica"
    },
    "14": {
      "name": "Estocolmo",
      "sub": "Veneza do Norte"
    },
    "15": {
      "name": "Expresso Oriente",
      "sub": "Rota Lendária"
    },
    "16": {
      "name": "Bruxelas",
      "sub": "Capital da Europa"
    },
    "17": {
      "name": "Caixa Comunitária",
      "sub": "Prêmios e Bônus"
    },
    "18": {
      "name": "Amsterdã",
      "sub": "Metrópole dos Canais"
    },
    "19": {
      "name": "Viena",
      "sub": "Capital Imperial"
    },
    "20": {
      "name": "Estacionamento Grátis",
      "sub": "Ganhe o Pote"
    },
    "21": {
      "name": "Zurique",
      "sub": "Centro Financeiro"
    },
    "22": {
      "name": "Carta de Sorte",
      "sub": "Tente sua sorte"
    },
    "23": {
      "name": "Munique",
      "sub": "Centro da Baviera"
    },
    "24": {
      "name": "Milão",
      "sub": "Capital da Moda"
    },
    "25": {
      "name": "TGV Grand",
      "sub": "Alta Velocidade"
    },
    "26": {
      "name": "Madri",
      "sub": "Coração da Espanha"
    },
    "27": {
      "name": "Barcelona",
      "sub": "Maravilha Catalã"
    },
    "28": {
      "name": "Companhia de Água",
      "sub": "Serviço Hídrico"
    },
    "29": {
      "name": "Roma",
      "sub": "A Cidade Eterna"
    },
    "30": {
      "name": "Vá para a Cadeia!",
      "sub": "Prisão Direta"
    },
    "31": {
      "name": "Berlim",
      "sub": "Metrópole Criativa"
    },
    "32": {
      "name": "Londres",
      "sub": "Capital Histórica"
    },
    "33": {
      "name": "Caixa Comunitária",
      "sub": "Prêmios e Bônus"
    },
    "34": {
      "name": "Paris",
      "sub": "A Cidade Luz"
    },
    "35": {
      "name": "Expresso Alpino",
      "sub": "Trem da Montanha"
    },
    "36": {
      "name": "Carta de Sorte",
      "sub": "Tente sua sorte"
    },
    "37": {
      "name": "Genebra",
      "sub": "Centro Global"
    },
    "38": {
      "name": "Imposto de Luxo",
      "sub": "Pague 100 ao Pote"
    },
    "39": {
      "name": "Veneza",
      "sub": "A Rainha do Mar"
    }
  },
  "tr": {
    "0": {
      "name": "BAŞLANGIÇ",
      "sub": "Geçerken 200 al"
    },
    "1": {
      "name": "Atina",
      "sub": "Tarihi Başkent"
    },
    "2": {
      "name": "Kamu Kasası",
      "sub": "Ödüller ve İkramiyeler"
    },
    "3": {
      "name": "Dublin",
      "sub": "Zümrüt Başkent"
    },
    "4": {
      "name": "Gelir Vergisi",
      "sub": "Havuza 200 Öde"
    },
    "5": {
      "name": "Eurostar Merkez",
      "sub": "Avrupa Demiryolu"
    },
    "6": {
      "name": "Lizbon",
      "sub": "Atlantik İncisi"
    },
    "7": {
      "name": "Şans Kartı",
      "sub": "Şansını dene"
    },
    "8": {
      "name": "Varşova",
      "sub": "Tarihi Nehir Kenti"
    },
    "9": {
      "name": "Budapeşte",
      "sub": "Tuna'nın İncisi"
    },
    "10": {
      "name": "Kale Hapishanesi",
      "sub": "Ziyaretçi / Tutuklu"
    },
    "11": {
      "name": "Prag",
      "sub": "Yüz Kuleli Şehir"
    },
    "12": {
      "name": "Elektrik Şebekesi",
      "sub": "Kamu Hizmeti"
    },
    "13": {
      "name": "Kopenhag",
      "sub": "Kuzey Başkenti"
    },
    "14": {
      "name": "Stokholm",
      "sub": "Kuzeyin Venedik'i"
    },
    "15": {
      "name": "Şark Ekspresi",
      "sub": "Efsanevi Hat"
    },
    "16": {
      "name": "Brüksel",
      "sub": "Avrupa'nın Kalbi"
    },
    "17": {
      "name": "Kamu Kasası",
      "sub": "Ödüller ve İkramiyeler"
    },
    "18": {
      "name": "Amsterdam",
      "sub": "Kanallar Şehri"
    },
    "19": {
      "name": "Viyana",
      "sub": "İmparatorluk Kenti"
    },
    "20": {
      "name": "Ücretsiz Park",
      "sub": "Tüm Havuzu Kazan"
    },
    "21": {
      "name": "Zürih",
      "sub": "Alp Finans Merkezi"
    },
    "22": {
      "name": "Şans Kartı",
      "sub": "Şansını dene"
    },
    "23": {
      "name": "Münih",
      "sub": "Bavyera'nın Kalbi"
    },
    "24": {
      "name": "Milano",
      "sub": "Moda Başkenti"
    },
    "25": {
      "name": "TGV Grand",
      "sub": "Hızlı Tren"
    },
    "26": {
      "name": "Madrid",
      "sub": "İspanya'nın Kalbi"
    },
    "27": {
      "name": "Barselona",
      "sub": "Katalan Harikası"
    },
    "28": {
      "name": "Su İdaresi",
      "sub": "Kamu Hizmeti"
    },
    "29": {
      "name": "Roma",
      "sub": "Ölümsüz Şehir"
    },
    "30": {
      "name": "Hapse Gir!",
      "sub": "Doğrudan Tutuklama"
    },
    "31": {
      "name": "Berlin",
      "sub": "Kültür Merkezi"
    },
    "32": {
      "name": "Londra",
      "sub": "Krallık Başkenti"
    },
    "33": {
      "name": "Kamu Kasası",
      "sub": "Ödüller ve İkramiyeler"
    },
    "34": {
      "name": "Paris",
      "sub": "Işıklar Şehri"
    },
    "35": {
      "name": "Alp Ekspresi",
      "sub": "Dağ Demiryolu"
    },
    "36": {
      "name": "Şans Kartı",
      "sub": "Şansını dene"
    },
    "37": {
      "name": "Cenevre",
      "sub": "Barış Başkenti"
    },
    "38": {
      "name": "Lüks Vergisi",
      "sub": "Havuza 100 Öde"
    },
    "39": {
      "name": "Venedik",
      "sub": "Suların Kraliçesi"
    }
  },
  "zh": {
    "0": {
      "name": "始发站",
      "sub": "路过领取 200"
    },
    "1": {
      "name": "马尼拉",
      "sub": "千岛之国首都"
    },
    "2": {
      "name": "公共基金",
      "sub": "群众奖金与福利"
    },
    "3": {
      "name": "河内",
      "sub": "千年历史古都"
    },
    "4": {
      "name": "个人所得税",
      "sub": "缴纳 200 存入奖池"
    },
    "5": {
      "name": "新干线特快",
      "sub": "亚洲高铁干线"
    },
    "6": {
      "name": "雅加达",
      "sub": "千岛繁华之都"
    },
    "7": {
      "name": "机会卡",
      "sub": "试试你的手气"
    },
    "8": {
      "name": "吉隆坡",
      "sub": "双子塔之城"
    },
    "9": {
      "name": "曼谷",
      "sub": "微笑天使之城"
    },
    "10": {
      "name": "城堡监狱",
      "sub": "探监中 / 收押中"
    },
    "11": {
      "name": "台北",
      "sub": "东方明珠都会"
    },
    "12": {
      "name": "国家电网",
      "sub": "公共电力设施"
    },
    "13": {
      "name": "新加坡",
      "sub": "花园狮城之都"
    },
    "14": {
      "name": "首尔",
      "sub": "汉江科技之都"
    },
    "15": {
      "name": "泛亚铁路",
      "sub": "国际跨国干线"
    },
    "16": {
      "name": "孟买",
      "sub": "印度金融之都"
    },
    "17": {
      "name": "公共基金",
      "sub": "群众奖金与福利"
    },
    "18": {
      "name": "新德里",
      "sub": "文明历史古都"
    },
    "19": {
      "name": "班加罗尔",
      "sub": "科技创新硅谷"
    },
    "20": {
      "name": "免费停车场",
      "sub": "赢取全部奖池彩金"
    },
    "21": {
      "name": "伊斯法罕",
      "sub": "半个世界的古都"
    },
    "22": {
      "name": "机会卡",
      "sub": "试试你的手气"
    },
    "23": {
      "name": "设拉子",
      "sub": "诗歌与花园之都"
    },
    "24": {
      "name": "德黑兰",
      "sub": "高原历史名城"
    },
    "25": {
      "name": "丝绸之路特快",
      "sub": "古丝路商贸快线"
    },
    "26": {
      "name": "大阪",
      "sub": "天下厨房商业都"
    },
    "27": {
      "name": "京都",
      "sub": "千年古都风雅"
    },
    "28": {
      "name": "自来水公司",
      "sub": "公共供水设施"
    },
    "29": {
      "name": "东京",
      "sub": "全球繁华大都会"
    },
    "30": {
      "name": "进监狱！",
      "sub": "直接收押入狱"
    },
    "31": {
      "name": "广州",
      "sub": "海上丝路名城"
    },
    "32": {
      "name": "上海",
      "sub": "东方璀璨魔都"
    },
    "33": {
      "name": "公共基金",
      "sub": "群众奖金与福利"
    },
    "34": {
      "name": "北京",
      "sub": "古今交融之都"
    },
    "35": {
      "name": "磁悬浮中央站",
      "sub": "极速磁悬浮轨道"
    },
    "36": {
      "name": "机会卡",
      "sub": "试试你的手气"
    },
    "37": {
      "name": "迪拜",
      "sub": "中东奢华未来城"
    },
    "38": {
      "name": "奢侈税",
      "sub": "缴纳 100 存入奖池"
    },
    "39": {
      "name": "香港",
      "sub": "亚洲国际金融之都"
    }
  },
  "ja": {
    "0": {
      "name": "GO",
      "sub": "通過時に200受取"
    },
    "1": {
      "name": "マニラ",
      "sub": "フィリピンの首都"
    },
    "2": {
      "name": "共同基金",
      "sub": "コミュニティボーナス"
    },
    "3": {
      "name": "ハノイ",
      "sub": "千年の古都"
    },
    "4": {
      "name": "所得税",
      "sub": "ポットに200支払"
    },
    "5": {
      "name": "新幹線エクスプレス",
      "sub": "高速鉄道網"
    },
    "6": {
      "name": "ジャカルタ",
      "sub": "東南アジアの大都市"
    },
    "7": {
      "name": "チャンスカード",
      "sub": "運命のカードを引く"
    },
    "8": {
      "name": "クアラルンプール",
      "sub": "ツインタワーの街"
    },
    "9": {
      "name": "バンコク",
      "sub": "微笑みの天使の都"
    },
    "10": {
      "name": "城塞刑務所",
      "sub": "見学中 / 収監中"
    },
    "11": {
      "name": "台北",
      "sub": "活気ある名城"
    },
    "12": {
      "name": "電力会社",
      "sub": "インフラ施設"
    },
    "13": {
      "name": "シンガポール",
      "sub": "ガーデンシティ"
    },
    "14": {
      "name": "ソウル",
      "sub": "韓流とハイテクの都"
    },
    "15": {
      "name": "アジア横断鉄道",
      "sub": "国際幹線鉄道"
    },
    "16": {
      "name": "ムンバイ",
      "sub": "インド最大の経済都市"
    },
    "17": {
      "name": "共同基金",
      "sub": "コミュニティボーナス"
    },
    "18": {
      "name": "ニューデリー",
      "sub": "歴史ある首都"
    },
    "19": {
      "name": "バンガロール",
      "sub": "インドのシリコンバレー"
    },
    "20": {
      "name": "フリーパーキング",
      "sub": "ポットの全賞金を獲得"
    },
    "21": {
      "name": "イスファハン",
      "sub": "世界の半分の美"
    },
    "22": {
      "name": "チャンスカード",
      "sub": "運命のカードを引く"
    },
    "23": {
      "name": "シーラーズ",
      "sub": "詩と庭園の古都"
    },
    "24": {
      "name": "テヘラン",
      "sub": "ペルシャの首都"
    },
    "25": {
      "name": "シルクロード特急",
      "sub": "シルクロード横断"
    },
    "26": {
      "name": "大阪",
      "sub": "商都・天下の台所"
    },
    "27": {
      "name": "京都",
      "sub": "千年の古都"
    },
    "28": {
      "name": "水道会社",
      "sub": "インフラ施設"
    },
    "29": {
      "name": "東京",
      "sub": "世界のメガロポリス"
    },
    "30": {
      "name": "刑務所へ行け！",
      "sub": "直ちに収監される"
    },
    "31": {
      "name": "広州",
      "sub": "交易の古都"
    },
    "32": {
      "name": "上海",
      "sub": "東洋の国際経済都市"
    },
    "33": {
      "name": "共同基金",
      "sub": "コミュニティボーナス"
    },
    "34": {
      "name": "北京",
      "sub": "大いなる首都"
    },
    "35": {
      "name": "リニア中央駅",
      "sub": "次世代超電導リニア"
    },
    "36": {
      "name": "チャンスカード",
      "sub": "運命のカードを引く"
    },
    "37": {
      "name": "ドバイ",
      "sub": "未来のオアシス都市"
    },
    "38": {
      "name": "贅沢税",
      "sub": "ポットに100支払"
    },
    "39": {
      "name": "香港",
      "sub": "アジアの金融センター"
    }
  },
  "ko": {
    "0": {
      "name": "출발",
      "sub": "통과 시 200 수령"
    },
    "1": {
      "name": "마닐라",
      "sub": "열정의 섬 수도"
    },
    "2": {
      "name": "커뮤니티 체스트",
      "sub": "시민 보너스 & 보상"
    },
    "3": {
      "name": "하노이",
      "sub": "천년의 역사 수도"
    },
    "4": {
      "name": "소득세",
      "sub": "팟에 200 지불"
    },
    "5": {
      "name": "신칸센 고속선",
      "sub": "아시아 고속철도"
    },
    "6": {
      "name": "자카르타",
      "sub": "군도의 거대 수도"
    },
    "7": {
      "name": "찬스 카드",
      "sub": "행운의 기회 시험"
    },
    "8": {
      "name": "쿠알라룸푸르",
      "sub": "페트로나스 도시"
    },
    "9": {
      "name": "방콕",
      "sub": "미소의 천사 도시"
    },
    "10": {
      "name": "성채 감옥",
      "sub": "단순 면회 / 수감 중"
    },
    "11": {
      "name": "타이베이",
      "sub": "빛나는 아시아 허브"
    },
    "12": {
      "name": "전력 공사",
      "sub": "국가 에너지 공급"
    },
    "13": {
      "name": "싱가포르",
      "sub": "청정 정원 도시"
    },
    "14": {
      "name": "서울",
      "sub": "한강의 기적 중심지"
    },
    "15": {
      "name": "아시아 횡단열차",
      "sub": "대륙 횡단 간선"
    },
    "16": {
      "name": "뭄바이",
      "sub": "발리우드 금융 수도"
    },
    "17": {
      "name": "커뮤니티 체스트",
      "sub": "시민 보너스 & 보상"
    },
    "18": {
      "name": "뉴델리",
      "sub": "찬란한 유산 수도"
    },
    "19": {
      "name": "벵갈루루",
      "sub": "실리콘 밸리 허브"
    },
    "20": {
      "name": "무료 주차장",
      "sub": "팟의 전액 상금 획득"
    },
    "21": {
      "name": "이스파한",
      "sub": "세계의 절반 명성"
    },
    "22": {
      "name": "찬스 카드",
      "sub": "행운의 기회 시험"
    },
    "23": {
      "name": "시라즈",
      "sub": "시와 장미의 고도"
    },
    "24": {
      "name": "테헤란",
      "sub": "페르시아의 중심"
    },
    "25": {
      "name": "실크로드 특급",
      "sub": "고대 무역 특급"
    },
    "26": {
      "name": "오사카",
      "sub": "천하의 부엌 상업수도"
    },
    "27": {
      "name": "교토",
      "sub": "천년의 전통 고도"
    },
    "28": {
      "name": "수도 공사",
      "sub": "상수도 공급 시설"
    },
    "29": {
      "name": "도쿄",
      "sub": "세계 초거대 수도"
    },
    "30": {
      "name": "감옥으로 가라!",
      "sub": "즉시 수감 명령"
    },
    "31": {
      "name": "광저우",
      "sub": "해상 실크로드 거점"
    },
    "32": {
      "name": "상하이",
      "sub": "동방의 화려한 마도"
    },
    "33": {
      "name": "커뮤니티 체스트",
      "sub": "시민 보너스 & 보상"
    },
    "34": {
      "name": "베이징",
      "sub": "웅장한 역사 수도"
    },
    "35": {
      "name": "자기부상 중앙역",
      "sub": "초고속 자기부상열차"
    },
    "36": {
      "name": "찬스 카드",
      "sub": "행운의 기회 시험"
    },
    "37": {
      "name": "두바이",
      "sub": "미래형 럭셔리 도시"
    },
    "38": {
      "name": "사치세",
      "sub": "팟에 100 지불"
    },
    "39": {
      "name": "홍콩",
      "sub": "아시아 금융의 허브"
    }
  },
  "hi": {
    "0": {
      "name": "शुरू",
      "sub": "गुजरने पर 200 प्राप्त करें"
    },
    "1": {
      "name": "मनीला",
      "sub": "द्वीपों की राजधानी"
    },
    "2": {
      "name": "सामुदायिक कोष",
      "sub": "जनता का खजाना व इनाम"
    },
    "3": {
      "name": "हनोई",
      "sub": "हजार साल पुरानी राजधानी"
    },
    "4": {
      "name": "आयकर",
      "sub": "पॉट में 200 जमा करें"
    },
    "5": {
      "name": "शिंकानसेन एक्सप्रेस",
      "sub": "एशियाई हाई-स्पीड रेल"
    },
    "6": {
      "name": "जकार्ता",
      "sub": "महानगरीय द्वीप केंद्र"
    },
    "7": {
      "name": "भाग्य कार्ड",
      "sub": "अपनी किस्मत आजमाएं"
    },
    "8": {
      "name": "कुआलालंपुर",
      "sub": "ट्विन टावर्स का शहर"
    },
    "9": {
      "name": "बैंकॉक",
      "sub": "मुस्कानों का शहर"
    },
    "10": {
      "name": "किला जेल",
      "sub": "केवल मुलाकात / कैद में"
    },
    "11": {
      "name": "ताइपे",
      "sub": "चमकता एशियाई हब"
    },
    "12": {
      "name": "विद्युत निगम",
      "sub": "ऊर्जा ग्रिड सुविधा"
    },
    "13": {
      "name": "सिंगापुर",
      "sub": "गार्डन सिटी महानगर"
    },
    "14": {
      "name": "सियोल",
      "sub": "हाइ-टेक ऐतिहासिक राजधानी"
    },
    "15": {
      "name": "ट्रांस-एशियाई रेलवे",
      "sub": "अंतर्राष्ट्रीय रेल मार्ग"
    },
    "16": {
      "name": "मुंबई",
      "sub": "सपनों का वित्तीय शहर"
    },
    "17": {
      "name": "सामुदायिक कोष",
      "sub": "जनता का खजाना व इनाम"
    },
    "18": {
      "name": "नई दिल्ली",
      "sub": "भारत की ऐतिहासिक राजधानी"
    },
    "19": {
      "name": "बेंगलुरु",
      "sub": "भारत की सिलिकॉन वैली"
    },
    "20": {
      "name": "मुफ्त पार्किंग",
      "sub": "पूरा पॉट पुरस्कार जीतें"
    },
    "21": {
      "name": "इस्फ़हान",
      "sub": "विश्व की आधी सुंदरता"
    },
    "22": {
      "name": "भाग्य कार्ड",
      "sub": "अपनी किस्मत आजमाएं"
    },
    "23": {
      "name": "शिराज़",
      "sub": "शायरी व बागों का शहर"
    },
    "24": {
      "name": "तेहरान",
      "sub": "फारस का ऐतिहासिक केंद्र"
    },
    "25": {
      "name": "सिल्क रोड एक्सप्रेस",
      "sub": "ऐतिहासिक व्यापारिक रेल"
    },
    "26": {
      "name": "ओसाका",
      "sub": "व्यापारिक व सांस्कृतिक केंद्र"
    },
    "27": {
      "name": "क्योटो",
      "sub": "प्राचीन धरोहर नगरी"
    },
    "28": {
      "name": "जल बोर्ड",
      "sub": "जल आपूर्ति सुविधा"
    },
    "29": {
      "name": "टोक्यो",
      "sub": "विश्व का विशालतम महानगर"
    },
    "30": {
      "name": "जेल जाओ!",
      "sub": "तत्काल जेल की सजा"
    },
    "31": {
      "name": "ग्वांगझू",
      "sub": "व्यापारिक समुद्री बंदरगाह"
    },
    "32": {
      "name": "शंघाई",
      "sub": "पूर्व का चमकीला महानगर"
    },
    "33": {
      "name": "सामुदायिक कोष",
      "sub": "जनता का खजाना व इनाम"
    },
    "34": {
      "name": "बीजिंग",
      "sub": "प्राचीन व आधुनिक राजधानी"
    },
    "35": {
      "name": "मैग्लेव सेंट्रल",
      "sub": "सुपरफास्ट मैग्लेव रेल"
    },
    "36": {
      "name": "भाग्य कार्ड",
      "sub": "अपनी किस्मत आजमाएं"
    },
    "37": {
      "name": "दुबई",
      "sub": "भविष्य का लग्जरी शहर"
    },
    "38": {
      "name": "विलासिता कर",
      "sub": "पॉट में 100 जमा करें"
    },
    "39": {
      "name": "हांगकांग",
      "sub": "वैश्विक वित्तीय केंद्र"
    }
  },
  "fa": {
    "0": {
      "name": "شروع",
      "sub": "دریافت 200 هنگام عبور"
    },
    "1": {
      "name": "مانیل",
      "sub": "پایتخت تاریخی فیلیپین"
    },
    "2": {
      "name": "صندوقچه مردم",
      "sub": "جوایز و پاداش‌های مردمی"
    },
    "3": {
      "name": "هانوی",
      "sub": "پایتخت هزارساله ویتنام"
    },
    "4": {
      "name": "مالیات بر درآمد",
      "sub": "پرداخت 200 به صندوق"
    },
    "5": {
      "name": "قطار تندرو شینکانسن",
      "sub": "خط سریع‌السیر آسیا"
    },
    "6": {
      "name": "جاکارتا",
      "sub": "کلان‌شهر مجمع‌الجزایر"
    },
    "7": {
      "name": "کارت شانس",
      "sub": "شانس خود را امتحان کنید"
    },
    "8": {
      "name": "کوالالامپور",
      "sub": "شهر برج‌های دوقلو"
    },
    "9": {
      "name": "بانکوک",
      "sub": "شهر فرشتگان تایلند"
    },
    "10": {
      "name": "زندان قلعه",
      "sub": "ملاقات ساده / در بازداشت"
    },
    "11": {
      "name": "تایپه",
      "sub": "مروارید شرق آسیا"
    },
    "12": {
      "name": "شرکت برق سراسری",
      "sub": "تاسیسات انرژی ملی"
    },
    "13": {
      "name": "سنگاپور",
      "sub": "شهر گل‌ها و باغ‌ها"
    },
    "14": {
      "name": "سئول",
      "sub": "پایتخت فناوری و هنر"
    },
    "15": {
      "name": "راه‌آهن بین‌المللی آسیا",
      "sub": "خط ترانزیت قاره‌ای"
    },
    "16": {
      "name": "بمبئی",
      "sub": "پایتخت مالی و سینما"
    },
    "17": {
      "name": "صندوقچه مردم",
      "sub": "جوایز و پاداش‌های مردمی"
    },
    "18": {
      "name": "دهلی نو",
      "sub": "مهد تمدن و پایتخت"
    },
    "19": {
      "name": "بنگلور",
      "sub": "سیلیکون ولی آسیا"
    },
    "20": {
      "name": "استراحت رایگان",
      "sub": "برنده شدن کل موجودی صندوق"
    },
    "21": {
      "name": "اصفهان",
      "sub": "نصف جهان و مهد هنر"
    },
    "22": {
      "name": "کارت شانس",
      "sub": "شانس خود را امتحان کنید"
    },
    "23": {
      "name": "شیراز",
      "sub": "شهر راز، شعر و ادب"
    },
    "24": {
      "name": "تهران",
      "sub": "پایتخت همیشه بیدار"
    },
    "25": {
      "name": "قطار جاده ابریشم",
      "sub": "مسیر کهن بازرگانی"
    },
    "26": {
      "name": "اوساکا",
      "sub": "پایتخت تجاری ژاپن"
    },
    "27": {
      "name": "کیوتو",
      "sub": "پایتخت هزارساله سنت"
    },
    "28": {
      "name": "سازمان آب منطقه‌ای",
      "sub": "شبکه آبرسانی"
    },
    "29": {
      "name": "توکیو",
      "sub": "بزرگترین کلان‌شهر مدرن"
    },
    "30": {
      "name": "برو به زندان!",
      "sub": "بازداشت و حبس فوری"
    },
    "31": {
      "name": "گوانگژو",
      "sub": "بندر بزرگ جاده ابریشم"
    },
    "32": {
      "name": "شانگهای",
      "sub": "عروس شرق و تجارت جهانی"
    },
    "33": {
      "name": "صندوقچه مردم",
      "sub": "جوایز و پاداش‌های مردمی"
    },
    "34": {
      "name": "پکن",
      "sub": "پایتخت بزرگ امپراتوری"
    },
    "35": {
      "name": "ایستگاه مگلو مرکزی",
      "sub": "قطار مغناطیسی پرسرعت"
    },
    "36": {
      "name": "کارت شانس",
      "sub": "شانس خود را امتحان کنید"
    },
    "37": {
      "name": "دبی",
      "sub": "شهر شگفتی‌ها و آسمان‌خراش‌ها"
    },
    "38": {
      "name": "مالیات تجملات",
      "sub": "پرداخت 100 به صندوق"
    },
    "39": {
      "name": "هنگ کنگ",
      "sub": "مرکز مالی بین‌المللی"
    }
  }
}

I18N_UI = {
  "ar": {
    "gameTitle": "بنك الحظ 3D",
    "boardCitySub": "عواصم عربية • رقعة كلاسيكية 🌟",
    "btnRollDice": "🎲 ارمِ النرد",
    "btnNewGame": "لعبة جديدة",
    "btnTrade": "مفاوضة وتبادل",
    "btnRules": "القواعد",
    "btnCardRules": "شروط الكروت",
    "btnSettings": "الإعدادات",
    "freeParkingPot": "وعاء الاستراحة",
    "diceEnergy": "طاقة النرد",
    "rollsLeft": "رمية متبقية",
    "clearLog": "مسح",
    "activityLogTitle": "سجل الأحداث المباشر",
    "setupModalTitle": "إعداد وبدء لعبة بنك الحظ",
    "setupLanguageLabel": "🌐 لغة اللعبة (Language):",
    "setupModeLabel": "🎮 اختر نمط اللعب:",
    "modeBot": "ضد الكمبيوتر",
    "modeBotSub": "(لاعب 1 ضد الروبوت)",
    "modeHuman": "لاعبين اثنين",
    "modeHumanSub": "(على نفس الجهاز)",
    "setupNamesLabel": "👤 أسماء اللاعبين:",
    "p1Prefix": "🎩 اسم اللاعب 1:",
    "p2Prefix": "🤖 اسم المنافس:",
    "p1Default": "مستر حظ",
    "p2Default": "اللاعب الثاني",
    "botDefault": "روبوت",
    "setupMoneyLabel": "💰 رصيد البداية لكل لاعب:",
    "money3kSub": "نزال سريع وحاسم",
    "money6kSub": "مباراة متوازنة كلاسيكية",
    "money9kSub": "ماراثون استراتيجي طويل",
    "setupDifficultyLabel": "⚡ صعوبة الذكاء الاصطناعي (الروبوت):",
    "diffEasy": "سهل",
    "diffEasySub": "مبتدئ ومسالم",
    "diffMedium": "متوسط",
    "diffMediumSub": "متوازن وذكي",
    "diffHard": "صعب",
    "diffHardSub": "شرس ومفاوض محترف",
    "btnStartGame": "🚀 ابدأ اللعبة الآن",
    "btnSaveSettings": "💾 حفظ الإعدادات واللغة",
    "chestBadge": "🎁 صندوق الدنيا",
    "chanceBadge": "❓ كارت الحظ",
    "incomeTaxBadge": "💸 مصلحة الضرائب المصرية",
    "luxuryTaxBadge": "💎 مصلحة الضرائب",
    "jailBadge": "⛓️ أمر قضائي وضبط",
    "visitingBadge": "👮 زيارة تفقدية",
    "incomeTaxTitle": "ضريبة الدخل العامة (200 $)",
    "incomeTaxDesc": "يتعين عليك سداد ضريبة دخل حكومية بقيمة 200 $ تُحوّل فوراً لحصيلة وعاء الاستراحة المجانية!",
    "luxuryTaxTitle": "ضريبة الرفاهية والكماليات (100 $)",
    "luxuryTaxDesc": "رسم إضافي على المقتنيات والكماليات الفاخرة بقيمة 100 $ تودع في وعاء الاستراحة المجانية!",
    "jailTitle": "إلى سجن القلعة فوراً!",
    "jailDesc": "صدر أمر حبس فوري! لا تمر بخانة البداية ولا تستلم 200 $. للخروج ارمِ دبل، أو انتظر 3 أدوار مع دفع كفالة 50 $.",
    "visitingTitle": "سجن القلعة (زيارة فقط)",
    "visitingDesc": "أنت في خانة السجن بصفة زائر بريء. لا توجد أي غرامات أو توقيف، يمكنك استكمال دورك بأمان.",
    "btnPayTax200": "دفع 200 $",
    "btnPayTax100": "دفع 100 $",
    "btnExecute": "تنفيذ الكارت",
    "btnEnterJail": "تنفيذ أمر الحبس",
    "btnContinue": "متابعة الجولة",
    "btnCloseCard": "حسناً، إغلاق الكارت",
    "btnBuyProperty": "شراء العقار",
    "btnBuildFloor": "إنشاء طابق",
    "btnDemolishFloor": "هدم طابق",
    "btnNegotiateBuyout": "🤝 مفاوضة شراء العقار",
    "currency": "$",
    "landmarksTitle": "معالم المدينة",
    "wheelTitle": "عجلة الحظ",
    "netWorth": "الثروة",
    "deedFloorCost": "قيمة الطابق (33% من العقار):",
    "deedRentIncrease": "زيادة الإيجار لكل طابق (+50%):",
    "deedBaseRent": "الإيجار الأساسي (0 طوابق):",
    "deedFullGroup": "إيجار كامل المجموعة (0 طوابق):",
    "deedEiffel": "مع برج إيفل الذهبي (5 طوابق):",
    "deedCurrentRent": "الإيجار الفعلي الحالي:",
    "deedOwner": "المالك الحالي:",
    "deedBankOwner": "شاغر للبيع (البنك)",
    "deedSkip": "تخطي",
    "lblSettingsDiceSpeed": "🎲 سرعة دحرجة النرد:",
    "lblSettingsMoveSpeed": "🏃 سرعة حركة اللاعبين:",
    "speedSlow": "بطيء",
    "speedNormal": "عادي",
    "speedFast": "سريع",
    "speedInstant": "فائق",
    "wheelModalTitle": "عجلة الحظ والمجازفة (ربح وخسارة)",
    "wheelInstruction": "عجلة الحظ قد تنفع وقد تضر! أدر العجلة واكتشف مصيرك...",
    "btnSpinWheelText": "🌀 تدوير العجلة الآن!",
    "btnAboutUs": "ℹ️ من نحن (عن اللعبة)",
    "btnTokenPicker": "🎭 تغيير واختيار أيقونة البيدق",
    "aboutUsModalTitle": "من نحن - بنك الحظ 3D",
    "tokenPickerModalTitle": "اختيار وتغيير أيقونة البيدق"
  },
  "en": {
    "gameTitle": "Bank El Hazz 3D",
    "boardCitySub": "European Capitals • Classic Board 🌟",
    "btnRollDice": "🎲 Roll Dice",
    "btnNewGame": "New Game",
    "btnTrade": "Trade & Negotiate",
    "btnRules": "Rules",
    "btnCardRules": "Card Rules",
    "btnSettings": "Settings",
    "freeParkingPot": "Free Parking Pot",
    "diceEnergy": "Dice Energy",
    "rollsLeft": "rolls left",
    "clearLog": "Clear",
    "activityLogTitle": "Live Activity Log",
    "setupModalTitle": "Game Setup & Settings",
    "setupLanguageLabel": "🌐 Game Language:",
    "setupModeLabel": "🎮 Choose Game Mode:",
    "modeBot": "Vs Computer",
    "modeBotSub": "(1 Player vs AI Bot)",
    "modeHuman": "2 Players",
    "modeHumanSub": "(Pass & Play)",
    "setupNamesLabel": "👤 Player Names:",
    "p1Prefix": "🎩 Player 1 Name:",
    "p2Prefix": "🤖 Rival Name:",
    "p1Default": "Player 1",
    "p2Default": "Player 2",
    "botDefault": "Robot",
    "setupMoneyLabel": "💰 Starting Cash per Player:",
    "money3kSub": "Fast & decisive clash",
    "money6kSub": "Classic balanced match",
    "money9kSub": "Long strategic duel",
    "setupDifficultyLabel": "⚡ AI Bot Difficulty:",
    "diffEasy": "Easy",
    "diffEasySub": "Casual and friendly",
    "diffMedium": "Medium",
    "diffMediumSub": "Smart and balanced",
    "diffHard": "Hard",
    "diffHardSub": "Aggressive & ruthless",
    "btnStartGame": "🚀 Start Game Now",
    "btnSaveSettings": "💾 Save & Apply Language",
    "chestBadge": "🎁 Community Chest",
    "chanceBadge": "❓ Chance Card",
    "incomeTaxBadge": "💸 Revenue & Tax Office",
    "luxuryTaxBadge": "💎 Luxury Department",
    "jailBadge": "⛓️ Judicial Arrest Order",
    "visitingBadge": "👮 Routine Prison Visit",
    "incomeTaxTitle": "General Income Tax (200 M)",
    "incomeTaxDesc": "You must pay an income tax of 200 M, deposited directly into the Free Parking Pot!",
    "luxuryTaxTitle": "Luxury & Asset Tax (100 M)",
    "luxuryTaxDesc": "An additional luxury asset fee of 100 M deposited into the Free Parking Pot!",
    "jailTitle": "Directly to Citadel Prison!",
    "jailDesc": "Immediate incarceration order! Do not pass GO, do not collect 200. To leave: roll doubles or pay 50 bail.",
    "visitingTitle": "Citadel Prison (Just Visiting)",
    "visitingDesc": "You are visiting the prison as a guest. No fines or penalties apply, continue your tour safely.",
    "btnPayTax200": "Pay 200 M",
    "btnPayTax100": "Pay 100 M",
    "btnExecute": "Execute Card",
    "btnEnterJail": "Go to Cell",
    "btnContinue": "Continue Turn",
    "btnCloseCard": "OK, Close Card",
    "btnBuyProperty": "Buy Property",
    "btnBuildFloor": "Build Floor",
    "btnDemolishFloor": "Demolish Floor",
    "btnNegotiateBuyout": "🤝 Negotiate Buyout",
    "currency": "M",
    "landmarksTitle": "City Landmarks",
    "wheelTitle": "Fortune Wheel",
    "netWorth": "Net Worth",
    "deedFloorCost": "Floor Cost (33% of base):",
    "deedRentIncrease": "Rent Increase per Floor (+50%):",
    "deedBaseRent": "Base Rent (0 floors):",
    "deedFullGroup": "Full Group Rent (0 floors):",
    "deedEiffel": "With Golden Eiffel Tower (5 floors):",
    "deedCurrentRent": "Current Active Rent:",
    "deedOwner": "Current Owner:",
    "deedBankOwner": "For Sale (The Bank)",
    "deedSkip": "Skip",
    "lblSettingsDiceSpeed": "🎲 Dice Roll Speed:",
    "lblSettingsMoveSpeed": "🏃 Movement Speed:",
    "speedSlow": "Slow",
    "speedNormal": "Normal",
    "speedFast": "Fast",
    "speedInstant": "Instant",
    "wheelModalTitle": "Fortune & Risk Wheel (Win or Lose)",
    "wheelInstruction": "The Wheel may reward or penalize! Spin to reveal your fate...",
    "btnSpinWheelText": "🌀 Spin Wheel Now!",
    "btnAboutUs": "ℹ️ About Us",
    "btnTokenPicker": "🎭 Change Player Token",
    "aboutUsModalTitle": "About Us - Bank El Hazz 3D",
    "tokenPickerModalTitle": "Choose Player Token"
  },
  "zh": {
    "gameTitle": "大富翁 3D (Bank El Hazz)",
    "boardCitySub": "亚洲名城 • 经典豪华棋盘 🌟",
    "btnRollDice": "🎲 掷骰子",
    "btnNewGame": "新游戏",
    "btnTrade": "交易与谈判",
    "btnRules": "游戏规则",
    "btnCardRules": "卡片规则",
    "btnSettings": "系统设置",
    "freeParkingPot": "免费停车奖池",
    "diceEnergy": "骰子体力",
    "rollsLeft": "次剩余",
    "clearLog": "清空",
    "activityLogTitle": "实时游戏动态记录",
    "setupModalTitle": "游戏开局与系统设置",
    "setupLanguageLabel": "🌐 游戏语言:",
    "setupModeLabel": "🎮 选择对战模式:",
    "modeBot": "人机对战",
    "modeBotSub": "(单人对抗智能AI)",
    "modeHuman": "双人对战",
    "modeHumanSub": "(同设备轮流操作)",
    "setupNamesLabel": "👤 玩家名称设置:",
    "p1Prefix": "🎩 玩家 1 名称:",
    "p2Prefix": "🤖 对手名称:",
    "p1Default": "玩家 1",
    "p2Default": "玩家 2",
    "botDefault": "机器人",
    "setupMoneyLabel": "💰 每位玩家初始资金:",
    "money3kSub": "快节奏快速对决",
    "money6kSub": "经典平衡标准战",
    "money9kSub": "深度策略持久战",
    "setupDifficultyLabel": "⚡ AI机器人难度级别:",
    "diffEasy": "简单",
    "diffEasySub": "新手温和模式",
    "diffMedium": "普通",
    "diffMediumSub": "智能平衡模式",
    "diffHard": "困难",
    "diffHardSub": "激进高手模式",
    "btnStartGame": "🚀 立即开始游戏",
    "btnSaveSettings": "💾 保存设置与语言",
    "chestBadge": "🎁 公共基金",
    "chanceBadge": "❓ 机会卡",
    "incomeTaxBadge": "💸 国家税务总局",
    "luxuryTaxBadge": "💎 奢侈品特别税",
    "jailBadge": "⛓️ 法院收押令",
    "visitingBadge": "👮 探监见学",
    "incomeTaxTitle": "个人所得税 (200 M)",
    "incomeTaxDesc": "您必须缴纳 200 M 个人所得税，全额存入中央免费停车奖池！",
    "luxuryTaxTitle": "奢侈品与豪车税 (100 M)",
    "luxuryTaxDesc": "按规定缴纳 100 M 奢侈资产税，直接存入免费停车奖池！",
    "jailTitle": "立即关进监狱！",
    "jailDesc": "立即收押入狱！不得经过起点，不领200。出狱方式：掷出双数，或在3回合后交50保释金。",
    "visitingTitle": "城堡监狱 (探监中)",
    "visitingDesc": "您作为无辜访客在此探望。无任何罚款与拘留，请安全继续您的回合。",
    "btnPayTax200": "支付 200 M",
    "btnPayTax100": "支付 100 M",
    "btnExecute": "执行卡片",
    "btnEnterJail": "执行收押",
    "btnContinue": "继续回合",
    "btnCloseCard": "好的，关闭卡片",
    "btnBuyProperty": "购买地产",
    "btnBuildFloor": "加盖楼层",
    "btnDemolishFloor": "拆除楼层",
    "btnNegotiateBuyout": "🤝 谈判收购地产",
    "currency": "M",
    "landmarksTitle": "城市地标",
    "wheelTitle": "幸运转盘",
    "netWorth": "总资产",
    "deedFloorCost": "楼层造价 (地产价格33%):",
    "deedRentIncrease": "每层增加租金 (+50%):",
    "deedBaseRent": "基础租金 (0层):",
    "deedFullGroup": "整组垄断租金 (0层):",
    "deedEiffel": "配金色埃菲尔铁塔 (5层):",
    "deedCurrentRent": "当前实际租金:",
    "deedOwner": "当前领主:",
    "deedBankOwner": "待售地产 (银行)",
    "deedSkip": "跳过",
    "lblSettingsDiceSpeed": "🎲 掷骰子速度:",
    "lblSettingsMoveSpeed": "🏃 玩家移动速度:",
    "speedSlow": "慢速",
    "speedNormal": "正常",
    "speedFast": "快速",
    "speedInstant": "极速",
    "wheelModalTitle": "命运之轮 (盈亏兼备)",
    "wheelInstruction": "命运之轮既可获利也可受损！快来旋转揭晓命运...",
    "btnSpinWheelText": "🌀 立即旋转转盘！",
    "btnAboutUs": "ℹ️ 关于我们",
    "btnTokenPicker": "🎭 选择更换玩家棋子",
    "aboutUsModalTitle": "关于我们 - 3D幸运银行",
    "tokenPickerModalTitle": "选择玩家棋子"
  },
  "fr": {
    "gameTitle": "Banque de la Chance 3D",
    "boardCitySub": "Capitales Européennes • Plateau Classique 🌟",
    "btnRollDice": "🎲 Lancer les Dés",
    "btnNewGame": "Nouvelle Partie",
    "btnTrade": "Échange & Négociation",
    "btnRules": "Règles",
    "btnCardRules": "Règles des Cartes",
    "btnSettings": "Paramètres",
    "freeParkingPot": "Cagnotte Parc",
    "diceEnergy": "Énergie Dés",
    "rollsLeft": "lancers restants",
    "clearLog": "Effacer",
    "activityLogTitle": "Journal des Activités",
    "setupModalTitle": "Configuration & Paramètres",
    "setupLanguageLabel": "🌐 Langue du Jeu :",
    "setupModeLabel": "🎮 Choisissez le Mode :",
    "modeBot": "Contre l'Ordinateur",
    "modeBotSub": "(1 Joueur contre l'IA)",
    "modeHuman": "2 Joueurs",
    "modeHumanSub": "(Sur le même appareil)",
    "setupNamesLabel": "👤 Noms des Joueurs :",
    "p1Prefix": "🎩 Nom Joueur 1 :",
    "p2Prefix": "🤖 Nom Adversaire :",
    "p1Default": "Joueur 1",
    "p2Default": "Joueur 2",
    "botDefault": "Robot",
    "setupMoneyLabel": "💰 Argent de Départ par Joueur :",
    "money3kSub": "Partie rapide et intense",
    "money6kSub": "Partie classique et équilibrée",
    "money9kSub": "Partie stratégique longue",
    "setupDifficultyLabel": "⚡ Niveau de l'IA (Robot) :",
    "diffEasy": "Facile",
    "diffEasySub": "Débutant et pacifique",
    "diffMedium": "Moyen",
    "diffMediumSub": "Intelligent et équilibré",
    "diffHard": "Difficile",
    "diffHardSub": "Agressif et expert",
    "btnStartGame": "🚀 Démarrer la Partie",
    "btnSaveSettings": "💾 Enregistrer la Langue",
    "chestBadge": "🎁 Caisse de Communauté",
    "chanceBadge": "❓ Carte Chance",
    "incomeTaxBadge": "💸 Administration Fiscale",
    "luxuryTaxBadge": "💎 Taxe sur les Biens de Luxe",
    "jailBadge": "⛓️ Mandat d'Arrêt Immédiat",
    "visitingBadge": "👮 Simple Visite en Prison",
    "incomeTaxTitle": "Impôt sur le Revenu (200 M)",
    "incomeTaxDesc": "Vous devez payer un impôt sur le revenu de 200 M, versé directement au Parc Gratuit !",
    "luxuryTaxTitle": "Taxe de Luxe (100 M)",
    "luxuryTaxDesc": "Une taxe spéciale sur vos actifs de 100 M est déposée dans la cagnotte du Parc Gratuit !",
    "jailTitle": "Directement en Prison !",
    "jailDesc": "Incarcération immédiate ! Ne passez pas par la case Départ. Pour sortir : faites un double ou payez 50 de caution.",
    "visitingTitle": "Prison de la Citadelle (Simple Visite)",
    "visitingDesc": "Vous êtes en simple visiteur. Aucune amende ni pénalité, poursuivez votre tour sereinement.",
    "btnPayTax200": "Payer 200 M",
    "btnPayTax100": "Payer 100 M",
    "btnExecute": "Exécuter la Carte",
    "btnEnterJail": "Aller en Cellule",
    "btnContinue": "Continuer le Tour",
    "btnCloseCard": "D'accord, Fermer",
    "btnBuyProperty": "Acheter la Propriété",
    "btnBuildFloor": "Construire Étage",
    "btnDemolishFloor": "Démolir Étage",
    "btnNegotiateBuyout": "🤝 Négocier le Rachat",
    "currency": "M",
    "landmarksTitle": "Monuments",
    "wheelTitle": "Roue de la Fortune",
    "netWorth": "Fortune",
    "deedFloorCost": "Coût par étage (33%):",
    "deedRentIncrease": "Augmentation loyer / étage (+50%):",
    "deedBaseRent": "Loyer de base (0 étage):",
    "deedFullGroup": "Loyer groupe complet (0 étage):",
    "deedEiffel": "Avec Tour Eiffel Dorée (5 étages):",
    "deedCurrentRent": "Loyer actuel:",
    "deedOwner": "Propriétaire actuel:",
    "deedBankOwner": "À vendre (Banque)",
    "deedSkip": "Passer",
    "lblSettingsDiceSpeed": "🎲 Vitesse des dés :",
    "lblSettingsMoveSpeed": "🏃 Vitesse de déplacement :",
    "speedSlow": "Lent",
    "speedNormal": "Normal",
    "speedFast": "Rapide",
    "speedInstant": "Instantané",
    "wheelModalTitle": "Roue de la Fortune (Gains & Risques)",
    "wheelInstruction": "La roue peut récompenser ou pénaliser ! Tournez-la...",
    "btnSpinWheelText": "🌀 Tourner la roue !",
    "btnAboutUs": "ℹ️ À propos",
    "btnTokenPicker": "🎭 Choisir son pion",
    "aboutUsModalTitle": "À propos - Bank El Hazz 3D",
    "tokenPickerModalTitle": "Choisir votre pion"
  },
  "es": {
    "gameTitle": "Banco de la Fortuna 3D",
    "boardCitySub": "Capitales Europeas • Tablero Clásico 🌟",
    "btnRollDice": "🎲 Tirar Dados",
    "btnNewGame": "Nueva Partida",
    "btnTrade": "Comerciar y Negociar",
    "btnRules": "Reglas",
    "btnCardRules": "Reglas de Cartas",
    "btnSettings": "Ajustes",
    "freeParkingPot": "Bote de Parada",
    "diceEnergy": "Energía Dados",
    "rollsLeft": "tiradas restantes",
    "clearLog": "Limpiar",
    "activityLogTitle": "Registro en Vivo",
    "setupModalTitle": "Configuración y Ajustes",
    "setupLanguageLabel": "🌐 Idioma del Juego:",
    "setupModeLabel": "🎮 Elegir Modo de Juego:",
    "modeBot": "Contra la Computadora",
    "modeBotSub": "(1 Jugador vs Bot IA)",
    "modeHuman": "2 Jugadores",
    "modeHumanSub": "(Mismo dispositivo)",
    "setupNamesLabel": "👤 Nombres de Jugadores:",
    "p1Prefix": "🎩 Nombre Jugador 1:",
    "p2Prefix": "🤖 Nombre Rival:",
    "p1Default": "Jugador 1",
    "p2Default": "Jugador 2",
    "botDefault": "Robot",
    "setupMoneyLabel": "💰 Dinero Inicial por Jugador:",
    "money3kSub": "Duelo rápido y decisivo",
    "money6kSub": "Partida clásica equilibrada",
    "money9kSub": "Maratón estratégico largo",
    "setupDifficultyLabel": "⚡ Dificultad del Bot IA:",
    "diffEasy": "Fácil",
    "diffEasySub": "Tranquilo y relajado",
    "diffMedium": "Medio",
    "diffMediumSub": "Inteligente y equilibrado",
    "diffHard": "Difícil",
    "diffHardSub": "Agresivo y calculador",
    "btnStartGame": "🚀 Iniciar Partida Ahora",
    "btnSaveSettings": "💾 Guardar Ajustes e Idioma",
    "chestBadge": "🎁 Caja de Comunidad",
    "chanceBadge": "❓ Carta de Suerte",
    "incomeTaxBadge": "💸 Agencia Tributaria",
    "luxuryTaxBadge": "💎 Impuesto de Lujo",
    "jailBadge": "⛓️ Orden Judicial de Arresto",
    "visitingBadge": "👮 Visita a la Cárcel",
    "incomeTaxTitle": "Impuesto sobre la Renta (200 M)",
    "incomeTaxDesc": "¡Debe pagar un impuesto de 200 M, ingresado directamente en el Bote de Parada Libre!",
    "luxuryTaxTitle": "Impuesto de Lujo (100 M)",
    "luxuryTaxDesc": "¡Tasa especial sobre bienes de lujo de 100 M depositada en el Bote de Parada Libre!",
    "jailTitle": "¡A la Cárcel Directamente!",
    "jailDesc": "¡Encarcelamiento inmediato! No pase por la Salida. Para salir: saque dobles o pague 50 tras 3 turnos.",
    "visitingTitle": "Cárcel de la Ciudadela (Solo Visita)",
    "visitingDesc": "Está aquí solo como visitante. Sin multas ni arrestos, continúe su turno con total tranquilidad.",
    "btnPayTax200": "Pagar 200 M",
    "btnPayTax100": "Pagar 100 M",
    "btnExecute": "Ejecutar Carta",
    "btnEnterJail": "Ir a Prisión",
    "btnContinue": "Continuar Turno",
    "btnCloseCard": "Entendido, Cerrar",
    "btnBuyProperty": "Comprar Propiedad",
    "btnBuildFloor": "Construir Piso",
    "btnDemolishFloor": "Demoler Piso",
    "btnNegotiateBuyout": "🤝 Negociar Compra",
    "currency": "M",
    "landmarksTitle": "Monumentos",
    "wheelTitle": "Ruleta de la Suerte",
    "netWorth": "Patrimonio",
    "deedFloorCost": "Costo por piso (33%):",
    "deedRentIncrease": "Aumento alquiler / piso (+50%):",
    "deedBaseRent": "Alquiler base (0 pisos):",
    "deedFullGroup": "Alquiler grupo completo:",
    "deedEiffel": "Con Torre Eiffel Dorada (5 pisos):",
    "deedCurrentRent": "Alquiler actual:",
    "deedOwner": "Propietario actual:",
    "deedBankOwner": "En venta (Banco)",
    "deedSkip": "Omitir",
    "lblSettingsDiceSpeed": "🎲 Velocidad de los dados:",
    "lblSettingsMoveSpeed": "🏃 Velocidad de movimiento:",
    "speedSlow": "Lento",
    "speedNormal": "Normal",
    "speedFast": "Rápido",
    "speedInstant": "Instantáneo",
    "wheelModalTitle": "Ruleta de la Fortuna (Ganancias y Riesgos)",
    "wheelInstruction": "¡La ruleta puede premiarte o penalizarte! Gira ahora...",
    "btnSpinWheelText": "🌀 ¡Girar la ruleta ahora!",
    "btnAboutUs": "ℹ️ Sobre nosotros",
    "btnTokenPicker": "🎭 Cambiar ficha de jugador",
    "aboutUsModalTitle": "Sobre nosotros - Bank El Hazz 3D",
    "tokenPickerModalTitle": "Elige tu ficha"
  },
  "ru": {
    "gameTitle": "Банк Удачи 3D",
    "boardCitySub": "Европейские столицы • Классическая доска 🌟",
    "btnRollDice": "🎲 Бросить кубики",
    "btnNewGame": "Новая игра",
    "btnTrade": "Торговля и обмен",
    "btnRules": "Правила",
    "btnCardRules": "Правила карт",
    "btnSettings": "Настройки",
    "freeParkingPot": "Банк стоянки",
    "diceEnergy": "Энергия кубиков",
    "rollsLeft": "бросков осталось",
    "clearLog": "Очистить",
    "activityLogTitle": "Журнал событий",
    "setupModalTitle": "Настройки и начало игры",
    "setupLanguageLabel": "🌐 Язык игры:",
    "setupModeLabel": "🎮 Режим игры:",
    "modeBot": "Против компьютера",
    "modeBotSub": "(Игрок 1 против ИИ)",
    "modeHuman": "2 Игрока",
    "modeHumanSub": "(На одном устройстве)",
    "setupNamesLabel": "👤 Имена игроков:",
    "p1Prefix": "🎩 Имя Игрока 1:",
    "p2Prefix": "🤖 Имя соперника:",
    "p1Default": "Игрок 1",
    "p2Default": "Игрок 2",
    "botDefault": "Робот",
    "setupMoneyLabel": "💰 Стартовый баланс игрока:",
    "money3kSub": "Быстрая дуэль",
    "money6kSub": "Сбалансированная игра",
    "money9kSub": "Долгая стратегия",
    "setupDifficultyLabel": "⚡ Сложность робота ИИ:",
    "diffEasy": "Легкий",
    "diffEasySub": "Спокойный новичок",
    "diffMedium": "Средний",
    "diffMediumSub": "Умный баланс",
    "diffHard": "Сложный",
    "diffHardSub": "Агрессивный мастер",
    "btnStartGame": "🚀 Начать игру сейчас",
    "btnSaveSettings": "💾 Сохранить язык",
    "chestBadge": "🎁 Общественная казна",
    "chanceBadge": "❓ Карточка Шанс",
    "incomeTaxBadge": "💸 Налоговая служба",
    "luxuryTaxBadge": "💎 Налог на роскошь",
    "jailBadge": "⛓️ Постановление об аресте",
    "visitingBadge": "👮 Визит в тюрьму",
    "incomeTaxTitle": "Подоходный налог (200 M)",
    "incomeTaxDesc": "Вы обязаны оплатить налог 200 M, который сразу поступает в банк бесплатной стоянки!",
    "luxuryTaxTitle": "Налог на роскошь (100 M)",
    "luxuryTaxDesc": "Сбор за премиальное имущество 100 M направляется в банк стоянки!",
    "jailTitle": "Немедленно в тюрьму!",
    "jailDesc": "Немедленный арест! Не проходите Старт. Выход: выбросите дубль или внесите залог 50 через 3 хода.",
    "visitingTitle": "Тюрьма крепости (Простой визит)",
    "visitingDesc": "Вы здесь как обычный посетитель. Никаких штрафов нет, спокойно продолжайте свой ход.",
    "btnPayTax200": "Оплатить 200 M",
    "btnPayTax100": "Оплатить 100 M",
    "btnExecute": "Применить карту",
    "btnEnterJail": "В камеру",
    "btnContinue": "Продолжить ход",
    "btnCloseCard": "Понятно, закрыть",
    "btnBuyProperty": "Купить недвижимость",
    "btnBuildFloor": "Построить этаж",
    "btnDemolishFloor": "Снести этаж",
    "btnNegotiateBuyout": "🤝 Переговоры о выкупе",
    "currency": "M",
    "landmarksTitle": "Достопримечательности",
    "wheelTitle": "Колесо фортуны",
    "netWorth": "Капитал",
    "deedFloorCost": "Стоимость этажа (33%):",
    "deedRentIncrease": "Прибавка аренды за этаж (+50%):",
    "deedBaseRent": "Базовая аренда (0 этажей):",
    "deedFullGroup": "Аренда полного набора:",
    "deedEiffel": "С золотой башней Эйфеля (5 этажей):",
    "deedCurrentRent": "Текущая аренда:",
    "deedOwner": "Владелец:",
    "deedBankOwner": "В продаже (Банк)",
    "deedSkip": "Пропустить",
    "lblSettingsDiceSpeed": "🎲 Скорость броска кубиков:",
    "lblSettingsMoveSpeed": "🏃 Скорость перемещения:",
    "speedSlow": "Медленно",
    "speedNormal": "Обычная",
    "speedFast": "Быстро",
    "speedInstant": "Мгновенно",
    "wheelModalTitle": "Колесо Фортуны (Прибыль и Риск)",
    "wheelInstruction": "Колесо может принести куш или штраф! Вращайте...",
    "btnSpinWheelText": "🌀 Крутить колесо сейчас!",
    "btnAboutUs": "ℹ️ О нас",
    "btnTokenPicker": "🎭 Выбрать фишку игрока",
    "aboutUsModalTitle": "О нас - Банк Удачи 3D",
    "tokenPickerModalTitle": "Выберите фишку"
  },
  "de": {
    "gameTitle": "Bank des Glücks 3D",
    "boardCitySub": "Europäische Hauptstädte • Klassisches Brett 🌟",
    "btnRollDice": "🎲 Würfeln",
    "btnNewGame": "Neues Spiel",
    "btnTrade": "Handeln & Tauschen",
    "btnRules": "Regeln",
    "btnCardRules": "Kartenregeln",
    "btnSettings": "Einstellungen",
    "freeParkingPot": "Freies Parken Pott",
    "diceEnergy": "Würfelenergie",
    "rollsLeft": "Würfe übrig",
    "clearLog": "Leeren",
    "activityLogTitle": "Live-Spielprotokoll",
    "setupModalTitle": "Spiel-Setup & Einstellungen",
    "setupLanguageLabel": "🌐 Spielsprache:",
    "setupModeLabel": "🎮 Spielmodus wählen:",
    "modeBot": "Gegen Computer",
    "modeBotSub": "(Spieler 1 gegen KI-Bot)",
    "modeHuman": "2 Spieler",
    "modeHumanSub": "(Auf demselben Gerät)",
    "setupNamesLabel": "👤 Spielernamen:",
    "p1Prefix": "🎩 Spieler 1 Name:",
    "p2Prefix": "🤖 Gegner Name:",
    "p1Default": "Spieler 1",
    "p2Default": "Spieler 2",
    "botDefault": "Roboter",
    "setupMoneyLabel": "💰 Startkapital pro Spieler:",
    "money3kSub": "Schnelle Entscheidung",
    "money6kSub": "Klassisch ausgeglichen",
    "money9kSub": "Langes Strategiespiel",
    "setupDifficultyLabel": "⚡ KI-Schwierigkeit (Bot):",
    "diffEasy": "Einfach",
    "diffEasySub": "Entspannt und friedlich",
    "diffMedium": "Mittel",
    "diffMediumSub": "Schlau und ausgewogen",
    "diffHard": "Schwer",
    "diffHardSub": "Aggressiv und fordernd",
    "btnStartGame": "🚀 Spiel jetzt starten",
    "btnSaveSettings": "💾 Sprache speichern",
    "chestBadge": "🎁 Gemeinschaftskasse",
    "chanceBadge": "❓ Ereigniskarte",
    "incomeTaxBadge": "💸 Finanzamt",
    "luxuryTaxBadge": "💎 Luxussteueramt",
    "jailBadge": "⛓️ Gerichtlicher Haftbefehl",
    "visitingBadge": "👮 Nur zu Besuch",
    "incomeTaxTitle": "Einkommensteuer (200 M)",
    "incomeTaxDesc": "Zahlen Sie 200 M Einkommensteuer direkt in den Freies-Parken-Pott ein!",
    "luxuryTaxTitle": "Luxussteuer (100 M)",
    "luxuryTaxDesc": "Eine Sonderabgabe auf Luxusgüter von 100 M wird in den Freies-Parken-Pott überwiesen!",
    "jailTitle": "Sofort ins Gefängnis!",
    "jailDesc": "Haftbefehl! Gehen Sie nicht über Los. Freilassung: Pasch würfeln oder nach 3 Runden 50 Kaution zahlen.",
    "visitingTitle": "Festungsgefängnis (Nur zu Besuch)",
    "visitingDesc": "Sie sind nur als Gast hier. Keine Strafen, setzen Sie Ihren Zug sicher fort.",
    "btnPayTax200": "200 M zahlen",
    "btnPayTax100": "100 M zahlen",
    "btnExecute": "Karte ausführen",
    "btnEnterJail": "Haft antreten",
    "btnContinue": "Zug fortsetzen",
    "btnCloseCard": "Verstanden, Schließen",
    "btnBuyProperty": "Immobilie kaufen",
    "btnBuildFloor": "Etage bauen",
    "btnDemolishFloor": "Etage abreißen",
    "btnNegotiateBuyout": "🤝 Kauf verhandeln",
    "currency": "M",
    "landmarksTitle": "Wahrzeichen",
    "wheelTitle": "Glücksrad",
    "netWorth": "Vermögen",
    "deedFloorCost": "Kosten pro Etage (33%):",
    "deedRentIncrease": "Mietsteigerung pro Etage (+50%):",
    "deedBaseRent": "Basismiete (0 Etagen):",
    "deedFullGroup": "Vollständige Farbengruppe:",
    "deedEiffel": "Mit goldenem Eiffelturm (5 Etagen):",
    "deedCurrentRent": "Aktuelle Miete:",
    "deedOwner": "Aktueller Besitzer:",
    "deedBankOwner": "Zu verkaufen (Bank)",
    "deedSkip": "Überspringen",
    "lblSettingsDiceSpeed": "🎲 Würfelgeschwindigkeit:",
    "lblSettingsMoveSpeed": "🏃 Bewegungsgeschwindigkeit:",
    "speedSlow": "Langsam",
    "speedNormal": "Normal",
    "speedFast": "Schnell",
    "speedInstant": "Sehr schnell",
    "wheelModalTitle": "Glücksrad (Gewinn & Risiko)",
    "wheelInstruction": "Das Rad kann belohnen oder bestrafen! Jetzt drehen...",
    "btnSpinWheelText": "🌀 Jetzt Rad drehen!",
    "btnAboutUs": "ℹ️ Über uns",
    "btnTokenPicker": "🎭 Spielfigur auswählen",
    "aboutUsModalTitle": "Über uns - Bank El Hazz 3D",
    "tokenPickerModalTitle": "Spielfigur wählen"
  },
  "it": {
    "gameTitle": "Banca della Fortuna 3D",
    "boardCitySub": "Capitali Europee • Tabellone Classico 🌟",
    "btnRollDice": "🎲 Lancia Dadi",
    "btnNewGame": "Nuova Partita",
    "btnTrade": "Scambio & Trattativa",
    "btnRules": "Regole",
    "btnCardRules": "Regole Carte",
    "btnSettings": "Impostazioni",
    "freeParkingPot": "Montepremi Parcheggio",
    "diceEnergy": "Energia Dadi",
    "rollsLeft": "tiri rimasti",
    "clearLog": "Cancella",
    "activityLogTitle": "Registro di Gioco",
    "setupModalTitle": "Impostazioni e Avvio Partita",
    "setupLanguageLabel": "🌐 Lingua del Gioco:",
    "setupModeLabel": "🎮 Scegli Modalità:",
    "modeBot": "Contro il Computer",
    "modeBotSub": "(1 Giocatore contro il Bot)",
    "modeHuman": "2 Giocatori",
    "modeHumanSub": "(Sullo stesso dispositivo)",
    "setupNamesLabel": "👤 Nomi dei Giocatori:",
    "p1Prefix": "🎩 Nome Giocatore 1:",
    "p2Prefix": "🤖 Nome Rival:",
    "p1Default": "Giocatore 1",
    "p2Default": "Giocatore 2",
    "botDefault": "Robot",
    "setupMoneyLabel": "💰 Denaro Iniziale:",
    "money3kSub": "Duello rapido",
    "money6kSub": "Partita equilibrata",
    "money9kSub": "Lunga strategia",
    "setupDifficultyLabel": "⚡ Difficoltà dell'IA (Bot):",
    "diffEasy": "Facile",
    "diffEasySub": "Tranquillo e semplice",
    "diffMedium": "Medio",
    "diffMediumSub": "Intelligente ed equilibrato",
    "diffHard": "Difficile",
    "diffHardSub": "Aggressivo ed esperto",
    "btnStartGame": "🚀 Inizia Partita Ora",
    "btnSaveSettings": "💾 Salva Impostazioni",
    "chestBadge": "🎁 Cassa Comune",
    "chanceBadge": "❓ Carta Imprevisti",
    "incomeTaxBadge": "💸 Agenzia delle Entrate",
    "luxuryTaxBadge": "💎 Tassa sui Beni di Lusso",
    "jailBadge": "⛓️ Mandato di Arresto",
    "visitingBadge": "👮 Solo in Visita",
    "incomeTaxTitle": "Tassa sul Reddito (200 M)",
    "incomeTaxDesc": "Devi pagare una tassa sul reddito di 200 M, versata direttamente nel Montepremi Parcheggio!",
    "luxuryTaxTitle": "Tassa di Lusso (100 M)",
    "luxuryTaxDesc": "Un'imposta sui beni di lusso di 100 M viene depositata nel Montepremi Parcheggio!",
    "jailTitle": "Subito in Prigione!",
    "jailDesc": "Arresto immediato! Non passare dal Via. Per uscire: tira un doppio o paga 50 di cauzione.",
    "visitingTitle": "Prigione della Fortezza (Visita)",
    "visitingDesc": "Sei qui solo come visitatore. Nessuna sanzione, prosegui il tuo turno in sicurezza.",
    "btnPayTax200": "Paga 200 M",
    "btnPayTax100": "Paga 100 M",
    "btnExecute": "Esegui Carta",
    "btnEnterJail": "Vai in Cella",
    "btnContinue": "Continua Turno",
    "btnCloseCard": "Ho capito, Chiudi",
    "btnBuyProperty": "Compra Proprietà",
    "btnBuildFloor": "Costruisci Piano",
    "btnDemolishFloor": "Demolisci Piano",
    "btnNegotiateBuyout": "🤝 Tratta Acquisizione",
    "currency": "M",
    "landmarksTitle": "Monumenti",
    "wheelTitle": "Ruota della Fortuna",
    "netWorth": "Patrimonio",
    "deedFloorCost": "Costo per piano (33%):",
    "deedRentIncrease": "Aumento affitto per piano (+50%):",
    "deedBaseRent": "Affitto base (0 piani):",
    "deedFullGroup": "Affitto gruppo completo:",
    "deedEiffel": "Con Torre Eiffel Dorata (5 piani):",
    "deedCurrentRent": "Affitto attuale:",
    "deedOwner": "Proprietario:",
    "deedBankOwner": "In vendita (Banca)",
    "deedSkip": "Salta",
    "lblSettingsDiceSpeed": "🎲 Velocità dei dadi:",
    "lblSettingsMoveSpeed": "🏃 Velocità di movimento:",
    "speedSlow": "Lento",
    "speedNormal": "Normale",
    "speedFast": "Veloce",
    "speedInstant": "Istantaneo",
    "wheelModalTitle": "Ruota della Fortuna (Guadagno & Rischio)",
    "wheelInstruction": "La ruota può premiare o penalizzare! Gira ora...",
    "btnSpinWheelText": "🌀 Gira la ruota ora!",
    "btnAboutUs": "ℹ️ Chi siamo",
    "btnTokenPicker": "🎭 Scegli la tua pedina",
    "aboutUsModalTitle": "Chi siamo - Bank El Hazz 3D",
    "tokenPickerModalTitle": "Scegli la tua pedina"
  },
  "pt": {
    "gameTitle": "Banco da Fortuna 3D",
    "boardCitySub": "Capitais Europeias • Tabuleiro Clássico 🌟",
    "btnRollDice": "🎲 Rolar Dados",
    "btnNewGame": "Novo Jogo",
    "btnTrade": "Negociação e Troca",
    "btnRules": "Regras",
    "btnCardRules": "Regras das Cartas",
    "btnSettings": "Configurações",
    "freeParkingPot": "Pote de Estacionamento",
    "diceEnergy": "Energia dos Dados",
    "rollsLeft": "jogadas restantes",
    "clearLog": "Limpar",
    "activityLogTitle": "Histórico de Ações",
    "setupModalTitle": "Configurações e Início",
    "setupLanguageLabel": "🌐 Idioma do Jogo:",
    "setupModeLabel": "🎮 Escolha o Modo:",
    "modeBot": "Contra o Computador",
    "modeBotSub": "(1 Jogador vs Bot IA)",
    "modeHuman": "2 Jogadores",
    "modeHumanSub": "(No mesmo aparelho)",
    "setupNamesLabel": "👤 Nomes dos Jogadores:",
    "p1Prefix": "🎩 Jogador 1:",
    "p2Prefix": "🤖 Nome do Rival:",
    "p1Default": "Jogador 1",
    "p2Default": "Jogador 2",
    "botDefault": "Robô",
    "setupMoneyLabel": "💰 Saldo Inicial por Jogador:",
    "money3kSub": "Duelo rápido e decisivo",
    "money6kSub": "Partida clássica equilibrada",
    "money9kSub": "Maratona estratégica longa",
    "setupDifficultyLabel": "⚡ Dificuldade do Bot IA:",
    "diffEasy": "Fácil",
    "diffEasySub": "Iniciante e amigável",
    "diffMedium": "Médio",
    "diffMediumSub": "Equilibrado e esperto",
    "diffHard": "Difícil",
    "diffHardSub": "Agressivo e implacável",
    "btnStartGame": "🚀 Iniciar o Jogo Agora",
    "btnSaveSettings": "💾 Salvar Configurações",
    "chestBadge": "🎁 Caixa Comunitária",
    "chanceBadge": "❓ Carta de Sorte",
    "incomeTaxBadge": "💸 Receita Tributária",
    "luxuryTaxBadge": "💎 Imposto de Luxo",
    "jailBadge": "⛓️ Mandado de Prisão",
    "visitingBadge": "👮 Visita à Cadeia",
    "incomeTaxTitle": "Imposto de Renda (200 M)",
    "incomeTaxDesc": "Você deve pagar 200 M de imposto de renda, transferidos diretamente para o Pote de Estacionamento!",
    "luxuryTaxTitle": "Imposto sobre Luxo (100 M)",
    "luxuryTaxDesc": "Taxa adicional sobre bens e patrimônio de luxo de 100 M depositada no Pote de Estacionamento!",
    "jailTitle": "Direto para a Cadeia!",
    "jailDesc": "Ordem de prisão imediata! Não passe pelo Início. Para sair: tire duplos ou pague 50 de fiança.",
    "visitingTitle": "Cadeia da Cidadela (Apenas Visita)",
    "visitingDesc": "Você está apenas visitando a cadeia. Sem multas nem penalidades, continue seu turno com calma.",
    "btnPayTax200": "Pagar 200 M",
    "btnPayTax100": "Pagar 100 M",
    "btnExecute": "Executar Carta",
    "btnEnterJail": "Ir para Cela",
    "btnContinue": "Continuar Turno",
    "btnCloseCard": "Entendido, Fechar",
    "btnBuyProperty": "Comprar Propriedade",
    "btnBuildFloor": "Construir Andar",
    "btnDemolishFloor": "Demolir Andar",
    "btnNegotiateBuyout": "🤝 Negociar Compra",
    "currency": "M",
    "landmarksTitle": "Monumentos",
    "wheelTitle": "Roda da Sorte",
    "netWorth": "Patrimônio",
    "deedFloorCost": "Custo por andar (33%):",
    "deedRentIncrease": "Aumento aluguel / andar (+50%):",
    "deedBaseRent": "Aluguel base (0 andares):",
    "deedFullGroup": "Aluguel conjunto completo:",
    "deedEiffel": "Com Torre Eiffel Dourada (5 andares):",
    "deedCurrentRent": "Aluguel atual:",
    "deedOwner": "Proprietário:",
    "deedBankOwner": "À venda (Banco)",
    "deedSkip": "Pular",
    "lblSettingsDiceSpeed": "🎲 Velocidade dos dados:",
    "lblSettingsMoveSpeed": "🏃 Velocidade de movimento:",
    "speedSlow": "Lento",
    "speedNormal": "Normal",
    "speedFast": "Rápido",
    "speedInstant": "Instantâneo",
    "wheelModalTitle": "Roda da Fortuna (Ganhos & Riscos)",
    "wheelInstruction": "A roda pode recompensar ou penalizar! Gire agora...",
    "btnSpinWheelText": "🌀 Girar a roda agora!",
    "btnAboutUs": "ℹ️ Sobre nós",
    "btnTokenPicker": "🎭 Escolher peão do jogador",
    "aboutUsModalTitle": "Sobre nós - Bank El Hazz 3D",
    "tokenPickerModalTitle": "Escolha o seu peão"
  },
  "tr": {
    "gameTitle": "Şans Bankası 3D",
    "boardCitySub": "Avrupa Başkentleri • Klasik Masa 🌟",
    "btnRollDice": "🎲 Zar At",
    "btnNewGame": "Yeni Oyun",
    "btnTrade": "Takas & Pazarlık",
    "btnRules": "Kurallar",
    "btnCardRules": "Kart Kuralları",
    "btnSettings": "Ayarlar",
    "freeParkingPot": "Park Havuzu",
    "diceEnergy": "Zar Enerjisi",
    "rollsLeft": "kalan zar",
    "clearLog": "Temizle",
    "activityLogTitle": "Canlı Oyun Günlüğü",
    "setupModalTitle": "Oyun Kurulumu ve Ayarlar",
    "setupLanguageLabel": "🌐 Oyun Dili:",
    "setupModeLabel": "🎮 Oyun Modunu Seçin:",
    "modeBot": "Bilgisayara Karşı",
    "modeBotSub": "(Yapay Zeka Botuna Karşı)",
    "modeHuman": "2 Oyuncu",
    "modeHumanSub": "(Aynı cihazda karşılıklı)",
    "setupNamesLabel": "👤 Oyuncu İsimleri:",
    "p1Prefix": "🎩 1. Oyuncu İsmi:",
    "p2Prefix": "🤖 Rakip İsmi:",
    "p1Default": "1. Oyuncu",
    "p2Default": "2. Oyuncu",
    "botDefault": "Robot",
    "setupMoneyLabel": "💰 Başlangıç Parası:",
    "money3kSub": "Hızlı ve belirleyici maç",
    "money6kSub": "Dengeli klasik karşılaşma",
    "money9kSub": "Uzun stratejik mücadele",
    "setupDifficultyLabel": "⚡ Yapay Zeka Bot Zorluğu:",
    "diffEasy": "Kolay",
    "diffEasySub": "Sakin ve yeni başlayan",
    "diffMedium": "Orta",
    "diffMediumSub": "Akıllı ve dengeli",
    "diffHard": "Zor",
    "diffHardSub": "Sert ve usta müzakereci",
    "btnStartGame": "🚀 Oyunu Şimdi Başlat",
    "btnSaveSettings": "💾 Ayarları ve Dili Kaydet",
    "chestBadge": "🎁 Kamu Kasası",
    "chanceBadge": "❓ Şans Kartı",
    "incomeTaxBadge": "💸 Gelir İdaresi Başkanlığı",
    "luxuryTaxBadge": "💎 Lüks Tüketim Vergisi",
    "jailBadge": "⛓️ Yargısal Tutuklama Emri",
    "visitingBadge": "👮 Karakol Ziyareti",
    "incomeTaxTitle": "Genel Gelir Vergisi (200 M)",
    "incomeTaxDesc": "Ücretsiz Park Havuzuna aktarılmak üzere 200 M gelir vergisi ödemelisiniz!",
    "luxuryTaxTitle": "Lüks ve Servet Vergisi (100 M)",
    "luxuryTaxDesc": "Lüks varlıklarınız için 100 M harç doğrudan Ücretsiz Park Havuzuna yatırılır!",
    "jailTitle": "Doğru Hapse!",
    "jailDesc": "Derhal tutuklama emri! Başlangıçtan geçmeyin. Çıkmak için: çift zar atın veya 50 kefalet ödeyin.",
    "visitingTitle": "Kale Hapishanesi (Ziyaretçi)",
    "visitingDesc": "Hapishanede sadece masum bir ziyaretçisiniz. Ceza yok, turunuza güvenle devam edin.",
    "btnPayTax200": "200 M Öde",
    "btnPayTax100": "100 M Öde",
    "btnExecute": "Kartı Uygula",
    "btnEnterJail": "Hücreye Gir",
    "btnContinue": "Tura Devam Et",
    "btnCloseCard": "Anlaşıldı, Kapat",
    "btnBuyProperty": "Mülkü Satın Al",
    "btnBuildFloor": "Kat İnşa Et",
    "btnDemolishFloor": "Kat Yık",
    "btnNegotiateBuyout": "🤝 Satın Alma Pazarlığı",
    "currency": "M",
    "landmarksTitle": "Şehir Simgeleri",
    "wheelTitle": "Şans Çarkı",
    "netWorth": "Varlık",
    "deedFloorCost": "Kat Maliyeti (%33):",
    "deedRentIncrease": "Kat Başına Kira Artışı (+%50):",
    "deedBaseRent": "Taban Kira (0 kat):",
    "deedFullGroup": "Tam Grup Kirası:",
    "deedEiffel": "Altın Eyfel Kulesi İle (5 kat):",
    "deedCurrentRent": "Geçerli Kira:",
    "deedOwner": "Mevcut Sahip:",
    "deedBankOwner": "Satılık (Banka)",
    "deedSkip": "Geç",
    "lblSettingsDiceSpeed": "🎲 Zar Atma Hızı:",
    "lblSettingsMoveSpeed": "🏃 Oyuncu Hareket Hızı:",
    "speedSlow": "Yavaş",
    "speedNormal": "Normal",
    "speedFast": "Hızlı",
    "speedInstant": "Anında",
    "wheelModalTitle": "Şans Çarkı (Kazanç ve Risk)",
    "wheelInstruction": "Çark ödül de verebilir ceza da! Şimdi çevir...",
    "btnSpinWheelText": "🌀 Çarkı Şimdi Çevir!",
    "btnAboutUs": "ℹ️ Hakkımızda",
    "btnTokenPicker": "🎭 Oyuncu Piyonunu Seç",
    "aboutUsModalTitle": "Hakkımızda - Bank El Hazz 3D",
    "tokenPickerModalTitle": "Piyonunu Seç"
  },
  "hi": {
    "gameTitle": "बैंक अल हज़ 3D",
    "boardCitySub": "एशियाई राजधानियां • क्लासिक बोर्ड 🌟",
    "btnRollDice": "🎲 पासा फेंकें",
    "btnNewGame": "नया खेल",
    "btnTrade": "व्यापार और बातचीत",
    "btnRules": "नियम",
    "btnCardRules": "कार्ड नियम",
    "btnSettings": "सेटिंग्स",
    "freeParkingPot": "मुफ्त पार्किंग पॉट",
    "diceEnergy": "पासा ऊर्जा",
    "rollsLeft": "शेष फेंक",
    "clearLog": "साफ करें",
    "activityLogTitle": "लाइव गेम लॉग",
    "setupModalTitle": "खेल सेटअप और सेटिंग्स",
    "setupLanguageLabel": "🌐 खेल की भाषा:",
    "setupModeLabel": "🎮 खेल मोड चुनें:",
    "modeBot": "कंप्यूटर के खिलाफ",
    "modeBotSub": "(1 खिलाड़ी बनाम एआई बॉट)",
    "modeHuman": "2 खिलाड़ी",
    "modeHumanSub": "(एक ही डिवाइस पर)",
    "setupNamesLabel": "👤 खिलाड़ियों के नाम:",
    "p1Prefix": "🎩 खिलाड़ी 1 का नाम:",
    "p2Prefix": "🤖 प्रतिद्वंद्वी का नाम:",
    "p1Default": "खिलाड़ी 1",
    "p2Default": "खिलाड़ी 2",
    "botDefault": "रोबोट",
    "setupMoneyLabel": "💰 प्रारंभिक राशि प्रति खिलाड़ी:",
    "money3kSub": "तेज और निर्णायक मुकाबला",
    "money6kSub": "संतुलित क्लासिक मैच",
    "money9kSub": "लंबा रणनीतिक मुकाबला",
    "setupDifficultyLabel": "⚡ एआई बॉट कठिनाई स्तर:",
    "diffEasy": "आसान",
    "diffEasySub": "शुरुआती व शांत",
    "diffMedium": "मध्यम",
    "diffMediumSub": "बुद्धिमान व संतुलित",
    "diffHard": "कठिन",
    "diffHardSub": "आक्रामक व अनुभवी",
    "btnStartGame": "🚀 खेल अभी शुरू करें",
    "btnSaveSettings": "💾 भाषा सहेजें",
    "chestBadge": "🎁 सामुदायिक कोष",
    "chanceBadge": "❓ भाग्य कार्ड",
    "incomeTaxBadge": "💸 आयकर विभाग",
    "luxuryTaxBadge": "💎 विलासिता कर विभाग",
    "jailBadge": "⛓️ अदालती गिरफ्तारी आदेश",
    "visitingBadge": "👮 जेल मुलाकात",
    "incomeTaxTitle": "सामान्य आयकर (200 M)",
    "incomeTaxDesc": "आपको 200 M का आयकर चुकाना होगा, जो सीधे मुफ्त पार्किंग पॉट में जमा होगा!",
    "luxuryTaxTitle": "विलासिता कर (100 M)",
    "luxuryTaxDesc": "लग्जरी संपत्ति पर 100 M का अतिरिक्त शुल्क मुफ्त पार्किंग पॉट में जमा किया जाता है!",
    "jailTitle": "सीधे जेल में!",
    "jailDesc": "तत्काल गिरफ्तारी आदेश! शुरुआत से न गुजरें। बाहर निकलने के लिए: डबल्स फेंकें या 50 ज़मानत दें।",
    "visitingTitle": "किला जेल (केवल मुलाकात)",
    "visitingDesc": "आप यहाँ केवल आगंतुक के रूप में हैं। कोई जुर्माना नहीं, सुरक्षित रूप से जारी रखें।",
    "btnPayTax200": "200 M भुगतान करें",
    "btnPayTax100": "100 M भुगतान करें",
    "btnExecute": "कार्ड लागू करें",
    "btnEnterJail": "जेल जाएं",
    "btnContinue": "बारी जारी रखें",
    "btnCloseCard": "ठीक है, बंद करें",
    "btnBuyProperty": "संपत्ति खरीदें",
    "btnBuildFloor": "मंजिल बनाएं",
    "btnDemolishFloor": "मंजिल गिराएं",
    "btnNegotiateBuyout": "🤝 खरीद पर बातचीत",
    "currency": "M",
    "landmarksTitle": "शहर के स्मारक",
    "wheelTitle": "भाग्य का पहिया",
    "netWorth": "कुल संपत्ति",
    "deedFloorCost": "प्रति मंजिल लागत (33%):",
    "deedRentIncrease": "प्रति मंजिल किराया वृद्धि (+50%):",
    "deedBaseRent": "मूल किराया (0 मंजिल):",
    "deedFullGroup": "पूर्ण समूह किराया:",
    "deedEiffel": "गोल्डन एफिल टॉवर के साथ (5 मंजिलें):",
    "deedCurrentRent": "वर्तमान किराया:",
    "deedOwner": "वर्तमान स्वामी:",
    "deedBankOwner": "बिक्री के लिए (बैंक)",
    "deedSkip": "छोड़ें",
    "lblSettingsDiceSpeed": "🎲 पासा फेंकने की गति:",
    "lblSettingsMoveSpeed": "🏃 चाल की गति:",
    "speedSlow": "धीमा",
    "speedNormal": "सामान्य",
    "speedFast": "तेज़",
    "speedInstant": "अति तीव्र",
    "wheelModalTitle": "भाग्य और जोखिम का पहिया (लाभ या हानि)",
    "wheelInstruction": "पहिया इनाम भी दे सकता है और दंड भी! घुमाएं...",
    "btnSpinWheelText": "🌀 पहिया अभी घुमाएं!",
    "btnAboutUs": "ℹ️ हमारे बारे में",
    "btnTokenPicker": "🎭 खिलाड़ी का मोहरा चुनें",
    "aboutUsModalTitle": "हमारे बारे में - बैंक एल हज़ 3D",
    "tokenPickerModalTitle": "अपना मोहरा चुनें"
  },
  "ja": {
    "gameTitle": "バンク・エル・ハズ 3D",
    "boardCitySub": "アジアの主要都市 • クラシック豪華ボード 🌟",
    "btnRollDice": "🎲 サイコロを振る",
    "btnNewGame": "新しいゲーム",
    "btnTrade": "取引と交渉",
    "btnRules": "ルール",
    "btnCardRules": "カードルール",
    "btnSettings": "設定",
    "freeParkingPot": "フリーパーキング",
    "diceEnergy": "サイコロエネルギー",
    "rollsLeft": "回残り",
    "clearLog": "消去",
    "activityLogTitle": "リアルタイムログ",
    "setupModalTitle": "ゲーム設定とスタート",
    "setupLanguageLabel": "🌐 ゲーム言語:",
    "setupModeLabel": "🎮 プレイモード選択:",
    "modeBot": "コンピューター対戦",
    "modeBotSub": "(1人 vs AIボット)",
    "modeHuman": "2人対戦",
    "modeHumanSub": "(同じ端末で対戦)",
    "setupNamesLabel": "👤 プレイヤー名設定:",
    "p1Prefix": "🎩 プレイヤー1名:",
    "p2Prefix": "🤖 対戦相手名:",
    "p1Default": "プレイヤー 1",
    "p2Default": "プレイヤー 2",
    "botDefault": "ロボット",
    "setupMoneyLabel": "💰 各プレイヤー初期所持金:",
    "money3kSub": "スピーディーな短期決戦",
    "money6kSub": "バランスの取れた標準戦",
    "money9kSub": "長期戦略バトル",
    "setupDifficultyLabel": "⚡ AIボットの難易度:",
    "diffEasy": "イージー",
    "diffEasySub": "初心者向けで穏やか",
    "diffMedium": "ノーマル",
    "diffMediumSub": "賢くバランス重視",
    "diffHard": "ハード",
    "diffHardSub": "攻撃的で手強い",
    "btnStartGame": "🚀 今すぐゲームを開始",
    "btnSaveSettings": "💾 言語と設定を保存",
    "chestBadge": "🎁 共同基金",
    "chanceBadge": "❓ チャンスカード",
    "incomeTaxBadge": "💸 国税庁",
    "luxuryTaxBadge": "💎 贅沢品税",
    "jailBadge": "⛓️ 収監命令書",
    "visitingBadge": "👮 刑務所見学",
    "incomeTaxTitle": "所得税 (200 M)",
    "incomeTaxDesc": "200 M の所得税を納付する必要があります。フリーパーキングポットに加算されます！",
    "luxuryTaxTitle": "贅沢品税 (100 M)",
    "luxuryTaxDesc": "高級資産への追加税 100 M がフリーパーキングポットに送金されます！",
    "jailTitle": "刑務所へ直行！",
    "jailDesc": "即時収監令！スタートを通過できず200も貰えません。脱出：ゾロ目を出すか50の保釈金を支払う。",
    "visitingTitle": "城塞刑務所 (見学中)",
    "visitingDesc": "見学として立ち寄っただけです。罰則はありません。安全に移動してください。",
    "btnPayTax200": "200 Mを支払う",
    "btnPayTax100": "100 Mを支払う",
    "btnExecute": "カードを実行",
    "btnEnterJail": "収監される",
    "btnContinue": "ターンを続ける",
    "btnCloseCard": "了解、閉じる",
    "btnBuyProperty": "土地を購入",
    "btnBuildFloor": "フロアを建設",
    "btnDemolishFloor": "フロアを解体",
    "btnNegotiateBuyout": "🤝 買収交渉を行う",
    "currency": "M",
    "landmarksTitle": "ランドマーク",
    "wheelTitle": "ラッキールーレット",
    "netWorth": "総資産",
    "deedFloorCost": "1階の建設費 (33%):",
    "deedRentIncrease": "1階あたりの家賃増加 (+50%):",
    "deedBaseRent": "基本家賃 (0階):",
    "deedFullGroup": "独占グループ家賃:",
    "deedEiffel": "黄金のエッフェル塔 (5階):",
    "deedCurrentRent": "現在の家賃:",
    "deedOwner": "現在の所有者:",
    "deedBankOwner": "販売中 (銀行)",
    "deedSkip": "スキップ",
    "lblSettingsDiceSpeed": "🎲 サイコロの速度:",
    "lblSettingsMoveSpeed": "🏃 移動速度:",
    "speedSlow": "遅い",
    "speedNormal": "標準",
    "speedFast": "速い",
    "speedInstant": "超高速",
    "wheelModalTitle": "運命のルーレット (損得チャンス)",
    "wheelInstruction": "運命のルーレットは吉凶混合！回して確かめよう...",
    "btnSpinWheelText": "🌀 ルーレットを回す！",
    "btnAboutUs": "ℹ️ このゲームについて",
    "btnTokenPicker": "🎭 プレイヤーのコマ変更",
    "aboutUsModalTitle": "概要 - バンク・エル・ハズ 3D",
    "tokenPickerModalTitle": "コマを選択"
  },
  "ko": {
    "gameTitle": "뱅크 엘 하즈 3D",
    "boardCitySub": "아시아 주요 도시 • 클래식 보드 🌟",
    "btnRollDice": "🎲 주사위 굴리기",
    "btnNewGame": "새 게임",
    "btnTrade": "거래 및 협상",
    "btnRules": "규칙 안내",
    "btnCardRules": "카드 규칙",
    "btnSettings": "환경 설정",
    "freeParkingPot": "무료 주차 팟",
    "diceEnergy": "주사위 에너지",
    "rollsLeft": "회 남음",
    "clearLog": "지우기",
    "activityLogTitle": "실시간 진행 기록",
    "setupModalTitle": "게임 설정 및 시작",
    "setupLanguageLabel": "🌐 게임 언어:",
    "setupModeLabel": "🎮 게임 모드 선택:",
    "modeBot": "컴퓨터 대전",
    "modeBotSub": "(AI 봇과 1:1 대결)",
    "modeHuman": "2인 대전",
    "modeHumanSub": "(한 기기에서 번갈아 플레이)",
    "setupNamesLabel": "👤 플레이어 이름:",
    "p1Prefix": "🎩 플레이어 1 이름:",
    "p2Prefix": "🤖 상대 플레이어 이름:",
    "p1Default": "플레이어 1",
    "p2Default": "플레이어 2",
    "botDefault": "로봇",
    "setupMoneyLabel": "💰 1인당 시작 자금:",
    "money3kSub": "빠르고 결단력 있는 승부",
    "money6kSub": "클래식 표준 경기",
    "money9kSub": "장기 전략 승부",
    "setupDifficultyLabel": "⚡ AI 봇 난이도:",
    "diffEasy": "쉬움",
    "diffEasySub": "초보자를 위한 온화한 모드",
    "diffMedium": "보통",
    "diffMediumSub": "스마트하고 균형 잡힌 모드",
    "diffHard": "어려움",
    "diffHardSub": "공격적이고 노련한 전문가",
    "btnStartGame": "🚀 지금 게임 시작",
    "btnSaveSettings": "💾 설정 및 언어 저장",
    "chestBadge": "🎁 커뮤니티 체스트",
    "chanceBadge": "❓ 찬스 카드",
    "incomeTaxBadge": "💸 국세청",
    "luxuryTaxBadge": "💎 사치품 특별세",
    "jailBadge": "⛓️ 사법 체포 영장",
    "visitingBadge": "👮 단순 감옥 면회",
    "incomeTaxTitle": "종합 소득세 (200 M)",
    "incomeTaxDesc": "소득세 200 M을 납부해야 하며, 무료 주차장 팟으로 직접 입금됩니다!",
    "luxuryTaxTitle": "사치세 및 자산세 (100 M)",
    "luxuryTaxDesc": "사치성 자산에 대한 추가 수수료 100 M이 무료 주차장 팟에 적립됩니다!",
    "jailTitle": "즉시 감옥으로!",
    "jailDesc": "즉시 수감 명령! 출발지를 통과하지 못합니다. 탈출: 더블을 던지거나 50 보석금을 지불하세요.",
    "visitingTitle": "성채 감옥 (단순 면회)",
    "visitingDesc": "단순 면회객으로 방문 중입니다. 벌금이나 구금 없이 차례를 안전하게 진행하세요.",
    "btnPayTax200": "200 M 납부",
    "btnPayTax100": "100 M 납부",
    "btnExecute": "카드 실행",
    "btnEnterJail": "수감되기",
    "btnContinue": "차례 계속하기",
    "btnCloseCard": "확인, 닫기",
    "btnBuyProperty": "부동산 구매",
    "btnBuildFloor": "층수 건설",
    "btnDemolishFloor": "층수 철거",
    "btnNegotiateBuyout": "🤝 부동산 인수 협상",
    "currency": "M",
    "landmarksTitle": "도시 랜드마크",
    "wheelTitle": "행운의 룰렛",
    "netWorth": "총 자산",
    "deedFloorCost": "층별 건설 비용 (33%):",
    "deedRentIncrease": "층당 임대료 증가 (+50%):",
    "deedBaseRent": "기본 임대료 (0층):",
    "deedFullGroup": "독점 세트 임대료:",
    "deedEiffel": "황금 에펠탑 (5층):",
    "deedCurrentRent": "현재 임대료:",
    "deedOwner": "현재 소유자:",
    "deedBankOwner": "판매 중 (은행)",
    "deedSkip": "건너뛰기",
    "lblSettingsDiceSpeed": "🎲 주사위 속도:",
    "lblSettingsMoveSpeed": "🏃 이동 속도:",
    "speedSlow": "느림",
    "speedNormal": "보통",
    "speedFast": "빠름",
    "speedInstant": "초고속",
    "wheelModalTitle": "행운과 위험의 룰렛 (득실 기회)",
    "wheelInstruction": "룰렛은 보상을 줄 수도 벌칙을 줄 수도 있습니다! 회전하세요...",
    "btnSpinWheelText": "🌀 지금 룰렛 회전하기!",
    "btnAboutUs": "ℹ️ 게임 정보",
    "btnTokenPicker": "🎭 플레이어 말 선택",
    "aboutUsModalTitle": "정보 - 뱅크 엘 하즈 3D",
    "tokenPickerModalTitle": "말 선택"
  },
  "fa": {
    "gameTitle": "بانک شانس 3D",
    "boardCitySub": "پایتخت‌های آسیایی • صفحه کلاسیک 🌟",
    "btnRollDice": "🎲 پرتاب تاس",
    "btnNewGame": "بازی جدید",
    "btnTrade": "مذاکره و مبادله",
    "btnRules": "قوانین بازی",
    "btnCardRules": "شرایط کارت‌ها",
    "btnSettings": "تنظیمات",
    "freeParkingPot": "صندوق استراحت",
    "diceEnergy": "انرژی تاس",
    "rollsLeft": "پرتاب باقی‌مانده",
    "clearLog": "پاک‌کردن",
    "activityLogTitle": "گزارش زنده رویدادها",
    "setupModalTitle": "تنظیمات و آغاز بازی",
    "setupLanguageLabel": "🌐 زبان بازی:",
    "setupModeLabel": "🎮 انتخاب حالت بازی:",
    "modeBot": "در برابر کامپیوتر",
    "modeBotSub": "(تک‌نفره در برابر ربات)",
    "modeHuman": "دو نفره",
    "modeHumanSub": "(روی همین دستگاه)",
    "setupNamesLabel": "👤 نام بازیکنان:",
    "p1Prefix": "🎩 نام بازیکن ۱:",
    "p2Prefix": "🤖 نام حریف:",
    "p1Default": "بازیکن ۱",
    "p2Default": "بازیکن ۲",
    "botDefault": "ربات",
    "setupMoneyLabel": "💰 موجودی اولیه هر بازیکن:",
    "money3kSub": "نبرد سریع و قاطع",
    "money6kSub": "رقابت کلاسیک و متعادل",
    "money9kSub": "ماراتن استراتژیک طولانی",
    "setupDifficultyLabel": "⚡ درجه سختی ربات:",
    "diffEasy": "آسان",
    "diffEasySub": "آرام و مبتدی",
    "diffMedium": "متوسط",
    "diffMediumSub": "هوشمند و متعادل",
    "diffHard": "سخت",
    "diffHardSub": "تهاجمی و مذاکره‌کننده حرفه‌ای",
    "btnStartGame": "🚀 شروع بازی اکنون",
    "btnSaveSettings": "💾 ذخیره زبان و تنظیمات",
    "chestBadge": "🎁 صندوقچه مردم",
    "chanceBadge": "❓ کارت شانس",
    "incomeTaxBadge": "💸 اداره مالیات بر درآمد",
    "luxuryTaxBadge": "💎 عوارض کالاهای تجملاتی",
    "jailBadge": "⛓️ حکم بازداشت قضایی",
    "visitingBadge": "👮 ملاقات عادی زندان",
    "incomeTaxTitle": "مالیات بر درآمد عمومی (200 M)",
    "incomeTaxDesc": "باید مبلغ 200 M مالیات دولتی پرداخت نمایید که مستقیماً به صندوق استراحت واریز می‌شود!",
    "luxuryTaxTitle": "عوارض کالاهای لوکس (100 M)",
    "luxuryTaxDesc": "عوارض اضافی دارایی‌های لوکس به مبلغ 100 M به صندوق استراحت واریز می‌گردد!",
    "jailTitle": "فوراً به زندان بروید!",
    "jailDesc": "حکم بازداشت فوری! از خانه آغاز رد نشوید و پاداش دریافت نکنید. خروج: تاس جفت یا ۵۰ وثیقه.",
    "visitingTitle": "زندان قلعه (فقط ملاقات)",
    "visitingDesc": "شما صرفاً به عنوان بازدیدکننده اینجایید. هیچ جریمه‌ای در کار نیست، با خیال راحت ادامه دهید.",
    "btnPayTax200": "پرداخت 200 M",
    "btnPayTax100": "پرداخت 100 M",
    "btnExecute": "اجرای کارت",
    "btnEnterJail": "ورود به بازداشتگاه",
    "btnContinue": "ادامه دور",
    "btnCloseCard": "متوجه شدم، بستن",
    "btnBuyProperty": "خرید ملک",
    "btnBuildFloor": "ساخت طبقه",
    "btnDemolishFloor": "تخریب طبقه",
    "btnNegotiateBuyout": "🤝 مذاکره خرید ملک",
    "currency": "M",
    "landmarksTitle": "جاذبه‌های شهر",
    "wheelTitle": "گردونه شانس",
    "netWorth": "دارایی کل",
    "deedFloorCost": "هزینه هر طبقه (۳۳٪):",
    "deedRentIncrease": "افزایش اجاره هر طبقه (+۵۰٪):",
    "deedBaseRent": "اجاره پایه (۰ طبقه):",
    "deedFullGroup": "اجاره انحصار کامل مجموعه:",
    "deedEiffel": "با برج ایفل طلایی (۵ طبقه):",
    "deedCurrentRent": "اجاره جاری فعلی:",
    "deedOwner": "مالک فعلی:",
    "deedBankOwner": "آماده فروش (بانک)",
    "deedSkip": "رد شدن",
    "lblSettingsDiceSpeed": "🎲 سرعت چرخش تاس:",
    "lblSettingsMoveSpeed": "🏃 سرعت حرکت بازیکن:",
    "speedSlow": "آهسته",
    "speedNormal": "معمولی",
    "speedFast": "سریع",
    "speedInstant": "فوری",
    "wheelModalTitle": "گردونه شانس و ریسک (سود و زیان)",
    "wheelInstruction": "گردونه ممکن است سود یا زیان بیاورد! بچرخانید...",
    "btnSpinWheelText": "🌀 اکنون گردونه را بچرخانید!",
    "btnAboutUs": "ℹ️ درباره ما",
    "btnTokenPicker": "🎭 تغییر مهره بازیکن",
    "aboutUsModalTitle": "درباره ما - بانک شانس 3D",
    "tokenPickerModalTitle": "انتخاب مهره بازی"
  }
}

I18N_CSS = "\n/* Language Selectors & Internationalization Styles */\n.setup-select {\n  width: 100%;\n  background: #1e110b;\n  color: #fef08a;\n  border: 2px solid #b45309;\n  border-radius: 10px;\n  padding: 10px 14px;\n  font-size: 14.5px;\n  font-weight: 700;\n  font-family: var(--font-family);\n  cursor: pointer;\n  outline: none;\n  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.5);\n  transition: all 0.2s ease;\n}\n.setup-select:focus {\n  border-color: #f59e0b;\n  box-shadow: 0 0 12px rgba(245, 158, 11, 0.4), inset 0 2px 4px rgba(0, 0, 0, 0.5);\n}\n.setup-select option {\n  background: #2a160d;\n  color: #fef08a;\n  padding: 8px;\n}\n\n.header-lang-select {\n  background: linear-gradient(180deg, #3d2314 0%, #2a160d 100%) !important;\n  color: #fef08a !important;\n  border: 1px solid #b45309 !important;\n  border-radius: 8px;\n  padding: 6px 10px;\n  font-size: 12px;\n  font-weight: 800;\n  cursor: pointer;\n  outline: none;\n}\n.header-lang-select option {\n  background: #2a160d;\n  color: #fef08a;\n}\n\n/* LTR layout support when European / Asian LTR languages are active */\nhtml[dir=\"ltr\"] .versus-clash-bar {\n  direction: ltr;\n}\nhtml[dir=\"ltr\"] .modal-title,\nhtml[dir=\"ltr\"] .modal-box,\nhtml[dir=\"ltr\"] .setup-modal-body,\nhtml[dir=\"ltr\"] .diorama-card-content-col {\n  text-align: left;\n}\nhtml[dir=\"ltr\"] .diorama-card-action-col {\n  margin-right: 0;\n  margin-left: 4px;\n}\nhtml[dir=\"ltr\"] .diorama-card-badge-row {\n  flex-direction: row;\n}\nhtml[dir=\"ltr\"] .activity-log-pane {\n  direction: ltr;\n  text-align: left;\n}\n"

SETTINGS_MODAL_HTML = """
  <!-- MODAL 14: Game Settings & Speed Modal -->
  <div class="modal-overlay" id="modalSettings">
    <div class="modal-box modal-setup-box" style="max-width: 500px;">
      <div class="modal-header">
        <div class="modal-title">
          <span>⚙️</span>
          <span id="settingsModalTitle">الإعدادات والخيارات</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalSettings')">&times;</button>
      </div>
      <div class="setup-modal-body">
        
        <!-- Language Selection Dropdown (Only in Settings) -->
        <div class="setup-group">
          <label class="setup-label" id="lblSettingsLang">🌐 اختر لغة اللعبة (Language):</label>
          <select class="setup-select" id="settingsLanguageSelect">
            <option value="ar">🇾🇪 العربية</option>
            <option value="en">🇬🇧 English</option>
            <option value="zh">🇨🇳 中文</option>
            <option value="fr">🇫🇷 Français</option>
            <option value="es">🇪🇸 Español</option>
            <option value="ru">🇷🇺 Русский</option>
            <option value="de">🇩🇪 Deutsch</option>
            <option value="it">🇮🇹 Italiano</option>
            <option value="pt">🇵🇹 Português</option>
            <option value="tr">🇹🇷 Türkçe</option>
            <option value="hi">🇮🇳 हिन्दी</option>
            <option value="ja">🇯🇵 日本語</option>
            <option value="ko">🇰🇷 한국어</option>
            <option value="fa">🇮🇷 فارسی</option>
          </select>
        </div>

        <!-- Prominent Quick Action Buttons: Token Picker & About Us (Top of Settings) -->
        <div class="setup-group" style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 4px; margin-bottom: 10px;">
          <button type="button" class="btn-matte gold" id="btnOpenTokenPicker" style="padding: 12px 6px; font-size: 13.5px; font-weight: 800; border-radius: 10px; display: flex; align-items: center; justify-content: center; gap: 6px; box-shadow: 0 4px 12px rgba(245, 158, 11, 0.25);">
            <span style="font-size: 18px;">🎭</span>
            <span id="btnTokenPickerText">تغيير واختيار البيادق</span>
          </button>
          <button type="button" class="btn-matte" id="btnOpenAboutUs" style="padding: 12px 6px; font-size: 13.5px; font-weight: 800; border-radius: 10px; background: rgba(56, 189, 248, 0.2); border: 2px solid #38bdf8; color: #f0f9ff; display: flex; align-items: center; justify-content: center; gap: 6px; box-shadow: 0 4px 12px rgba(2, 132, 199, 0.25);">
            <span style="font-size: 18px;">ℹ️</span>
            <span id="btnAboutUsText">من نحن (عمار الهلالي)</span>
          </button>
        </div>

        <!-- Developer Credit Card in Settings -->
        <div class="developer-credit-card" style="background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.85)); border: 1.5px solid rgba(56, 189, 248, 0.45); border-radius: 12px; padding: 10px 14px; margin-bottom: 12px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35);">
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, #0284c7, #38bdf8); display: flex; align-items: center; justify-content: center; font-size: 18px; box-shadow: 0 2px 8px rgba(56, 189, 248, 0.35);">💻</div>
            <div>
              <div style="font-size: 11px; color: #94a3b8; font-weight: 700;" id="settingsDevLabel">برمجة وتطوير</div>
              <div style="font-size: 15px; color: #38bdf8; font-weight: 900; letter-spacing: 0.3px;" id="settingsDevName">عمار الهلالي</div>
            </div>
          </div>
          <span style="background: rgba(56, 189, 248, 0.15); border: 1px solid #38bdf8; color: #7dd3fc; font-size: 11px; padding: 4px 12px; border-radius: 20px; font-weight: 800;">Ammar Al-Hilali</span>
        </div>

        <!-- Dice Roll Speed -->
        <div class="setup-group">
          <label class="setup-label" id="lblSettingsDiceSpeed">🎲 سرعة دحرجة النرد:</label>
          <div class="setup-pill-group" id="settingsDiceSpeedGroup">
            <button type="button" class="setup-pill" data-speed="slow">
              <span class="setup-pill-icon">🐢</span>
              <span class="setup-pill-title" id="pillDiceSlowTitle">بطيء</span>
            </button>
            <button type="button" class="setup-pill active" data-speed="normal">
              <span class="setup-pill-icon">🚶</span>
              <span class="setup-pill-title" id="pillDiceNormalTitle">عادي</span>
            </button>
            <button type="button" class="setup-pill" data-speed="fast">
              <span class="setup-pill-icon">⚡</span>
              <span class="setup-pill-title" id="pillDiceFastTitle">سريع</span>
            </button>
            <button type="button" class="setup-pill" data-speed="instant">
              <span class="setup-pill-icon">🚀</span>
              <span class="setup-pill-title" id="pillDiceInstantTitle">فائق</span>
            </button>
          </div>
        </div>

        <!-- Movement / Pawn Speed -->
        <div class="setup-group">
          <label class="setup-label" id="lblSettingsMoveSpeed">🏃 سرعة حركة اللاعبين:</label>
          <div class="setup-pill-group" id="settingsMoveSpeedGroup">
            <button type="button" class="setup-pill" data-speed="slow">
              <span class="setup-pill-icon">🐢</span>
              <span class="setup-pill-title" id="pillMoveSlowTitle">بطيء</span>
            </button>
            <button type="button" class="setup-pill active" data-speed="normal">
              <span class="setup-pill-icon">🚶</span>
              <span class="setup-pill-title" id="pillMoveNormalTitle">عادي</span>
            </button>
            <button type="button" class="setup-pill" data-speed="fast">
              <span class="setup-pill-icon">⚡</span>
              <span class="setup-pill-title" id="pillMoveFastTitle">سريع</span>
            </button>
            <button type="button" class="setup-pill" data-speed="instant">
              <span class="setup-pill-icon">🚀</span>
              <span class="setup-pill-title" id="pillMoveInstantTitle">فائق</span>
            </button>
          </div>
        </div>

        <!-- AI Difficulty In Settings -->
        <div class="setup-group">
          <label class="setup-label" id="lblSettingsDiff">⚡ صعوبة الذكاء الاصطناعي (الروبوت):</label>
          <div class="setup-pill-group" id="settingsDiffGroup">
            <button type="button" class="setup-pill" data-diff="easy">
              <span class="setup-pill-icon">🟢</span>
              <span class="setup-pill-title" id="settingsDiffEasyTitle">سهل</span>
            </button>
            <button type="button" class="setup-pill active" data-diff="medium">
              <span class="setup-pill-icon">🟡</span>
              <span class="setup-pill-title" id="settingsDiffMediumTitle">متوسط</span>
            </button>
            <button type="button" class="setup-pill" data-diff="hard">
              <span class="setup-pill-icon">🔴</span>
              <span class="setup-pill-title" id="settingsDiffHardTitle">صعب</span>
            </button>
          </div>
        </div>

        <!-- Audio Quick Toggle -->
        <div class="setup-group">
          <label class="setup-label" id="lblSettingsAudio">🔊 المؤثرات الصوتية:</label>
          <button type="button" class="btn-matte" id="btnSettingsToggleAudio" style="width: 100%; padding: 12px; font-size: 15px; border-radius: 10px;">
            <span id="settingsAudioIcon">🔊</span>
            <span id="settingsAudioText">المؤثرات الصوتية: مفعلة</span>
          </button>
        </div>

        <button class="btn-matte btn-start-game" id="btnSaveSettingsApply" style="margin-top: 14px;">
          <span id="btnSaveSettingsText">💾 حفظ وتطبيق الإعدادات</span>
        </button>

      </div>
    </div>
  </div>
"""

I18N_LANGUAGES_JSON = json.dumps(I18N_LANGUAGES, ensure_ascii=False)
I18N_TILES_JSON = json.dumps(I18N_TILES, ensure_ascii=False)
I18N_UI_JSON = json.dumps(I18N_UI, ensure_ascii=False)
