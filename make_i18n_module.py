import json

# Languages
LANGUAGES = [
    {"code": "ar", "name": "العربية", "flag": "🇪🇬", "region": "arab", "dir": "rtl"},
    {"code": "en", "name": "English", "flag": "🇬🇧", "region": "europe", "dir": "ltr"},
    {"code": "zh", "name": "中文 (Chinese)", "flag": "🇨🇳", "region": "asia", "dir": "ltr"},
    {"code": "fr", "name": "Français", "flag": "🇫🇷", "region": "europe", "dir": "ltr"},
    {"code": "es", "name": "Español", "flag": "🇪🇸", "region": "europe", "dir": "ltr"},
    {"code": "ru", "name": "Русский", "flag": "🇷🇺", "region": "europe", "dir": "ltr"},
    {"code": "de", "name": "Deutsch", "flag": "🇩🇪", "region": "europe", "dir": "ltr"},
    {"code": "it", "name": "Italiano", "flag": "🇮🇹", "region": "europe", "dir": "ltr"},
    {"code": "pt", "name": "Português", "flag": "🇵🇹", "region": "europe", "dir": "ltr"},
    {"code": "tr", "name": "Türkçe", "flag": "🇹🇷", "region": "europe", "dir": "ltr"},
    {"code": "hi", "name": "हिन्दी (Hindi)", "flag": "🇮🇳", "region": "asia", "dir": "ltr"},
    {"code": "ja", "name": "日本語 (Japanese)", "flag": "🇯🇵", "region": "asia", "dir": "ltr"},
    {"code": "ko", "name": "한국어 (Korean)", "flag": "🇰🇷", "region": "asia", "dir": "ltr"},
    {"code": "fa", "name": "فارسی (Persian)", "flag": "🇮🇷", "region": "asia", "dir": "rtl"}
]

# We need the tiles dictionary for all 14 languages
from generate_i18n_helper import get_all_tiles_i18n, get_all_ui_strings

tiles_i18n = get_all_tiles_i18n()
ui_strings = get_all_ui_strings()

tiles_json = json.dumps(tiles_i18n, ensure_ascii=False)
ui_json = json.dumps(ui_strings, ensure_ascii=False)
langs_json = json.dumps(LANGUAGES, ensure_ascii=False)

print("Tiles i18n count:", len(tiles_i18n))
print("UI strings count:", len(ui_strings))
print("Languages count:", len(LANGUAGES))
