import json
import os
from board_data import TILES, CHANCE_CARDS, CHEST_CARDS, LANDMARKS, WHEEL_ITEMS
from sound_engine import SOUND_JS
from i18n_module import (
    I18N_CSS,
    I18N_LANGUAGES,
    I18N_LANGUAGES_JSON,
    I18N_TILES,
    I18N_TILES_JSON,
    I18N_UI,
    I18N_UI_JSON,
    SETTINGS_MODAL_HTML
)

print("Generating Matte Physical 3D Bank El Hazz (2-Player Duel)...")

# Load SVG assets
with open("svg_assets.json", "r", encoding="utf-8") as f:
    all_svgs = json.load(f)

with open("matte_3d_assets.json", "r", encoding="utf-8") as f:
    matte_svgs = json.load(f)

# Override with matte assets
all_svgs.update(matte_svgs)
all_svgs['golden_eiffel_3d'] = '''<svg viewBox="0 0 60 70" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="eiffel_ao" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="rgba(0,0,0,0.6)"/>
      <stop offset="60%" stop-color="rgba(0,0,0,0.2)"/>
      <stop offset="100%" stop-color="rgba(0,0,0,0)"/>
    </radialGradient>
    <linearGradient id="gold_grad1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="40%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
    <linearGradient id="gold_grad2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fef9c3"/>
      <stop offset="50%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#92400e"/>
    </linearGradient>
  </defs>
  <ellipse cx="30" cy="64" rx="24" ry="5" fill="url(#eiffel_ao)"/>
  <polygon points="12,62 18,62 25,44 20,44" fill="url(#gold_grad1)"/>
  <polygon points="18,62 23,62 27,44 25,44" fill="url(#gold_grad2)"/>
  <polygon points="48,62 42,62 35,44 40,44" fill="url(#gold_grad1)"/>
  <polygon points="42,62 37,62 33,44 35,44" fill="url(#gold_grad2)"/>
  <path d="M 18,62 Q 30,46 42,62 L 39,62 Q 30,49 21,62 Z" fill="#d97706"/>
  <rect x="18" y="41" width="24" height="3.5" rx="1" fill="url(#gold_grad2)" stroke="#78350f" stroke-width="0.5"/>
  <line x1="22" y1="44" x2="38" y2="41" stroke="#b45309" stroke-width="0.7"/>
  <line x1="38" y1="44" x2="22" y2="41" stroke="#b45309" stroke-width="0.7"/>
  <polygon points="21,41 24,25 36,25 39,41" fill="url(#gold_grad1)"/>
  <polygon points="25,41 27,25 33,25 35,41" fill="url(#gold_grad2)"/>
  <line x1="24" y1="39" x2="36" y2="27" stroke="#78350f" stroke-width="0.7"/>
  <line x1="36" y1="39" x2="24" y2="27" stroke="#78350f" stroke-width="0.7"/>
  <rect x="23" y="23" width="14" height="2.5" rx="0.8" fill="url(#gold_grad2)" stroke="#78350f" stroke-width="0.5"/>
  <polygon points="25,23 28,8 32,8 35,23" fill="url(#gold_grad1)"/>
  <polygon points="27,23 29,8 31,8 33,23" fill="url(#gold_grad2)"/>
  <line x1="30" y1="8" x2="30" y2="1" stroke="#fef08a" stroke-width="1.8" stroke-linecap="round"/>
  <circle cx="30" cy="1" r="1.8" fill="#fef08a"/>
  <circle cx="30" cy="1" r="3.5" fill="#fef08a" opacity="0.4"/>
</svg>'''

all_svgs['token_rocket'] = '''<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="rocketShine" cx="35%" cy="30%" r="70%"><stop offset="0%" stop-color="#38bdf8"/><stop offset="50%" stop-color="#0284c7"/><stop offset="100%" stop-color="#0c4a6e"/></radialGradient>
    <linearGradient id="rocketFin" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f87171"/><stop offset="100%" stop-color="#b91c1c"/></linearGradient>
    <linearGradient id="rocketFlame" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fef08a"/><stop offset="50%" stop-color="#f97316"/><stop offset="100%" stop-color="#dc2626"/></linearGradient>
  </defs>
  <ellipse cx="30" cy="54" rx="20" ry="5" fill="rgba(0,0,0,0.4)"/>
  <polygon points="26,45 34,45 30,55" fill="url(#rocketFlame)"/>
  <polygon points="28,45 32,45 30,52" fill="#fff"/>
  <polygon points="18,44 24,40 24,45" fill="url(#rocketFin)"/>
  <polygon points="42,44 36,40 36,45" fill="url(#rocketFin)"/>
  <path d="M30,8 C22,22 22,38 24,45 L36,45 C38,38 38,22 30,8 Z" fill="url(#rocketShine)"/>
  <circle cx="30" cy="25" r="5" fill="#f8fafc" stroke="#0284c7" stroke-width="1.5"/>
  <circle cx="30" cy="25" r="3.2" fill="#0284c7"/>
  <circle cx="28.5" cy="23.5" r="1.2" fill="#ffffff"/>
  <path d="M30,8 L28,14 L32,14 Z" fill="#ef4444"/>
</svg>'''

all_svgs['token_diamond'] = '''<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="diamShine" cx="30%" cy="25%" r="70%"><stop offset="0%" stop-color="#ffffff"/><stop offset="35%" stop-color="#67e8f9"/><stop offset="70%" stop-color="#06b6d4"/><stop offset="100%" stop-color="#0e7490"/></radialGradient>
    <linearGradient id="diamFacet" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#cffafe"/><stop offset="100%" stop-color="#0891b2"/></linearGradient>
  </defs>
  <ellipse cx="30" cy="54" rx="20" ry="5" fill="rgba(0,0,0,0.4)"/>
  <polygon points="15,22 45,22 30,50" fill="url(#diamShine)"/>
  <polygon points="15,22 30,50 30,22" fill="#0891b2" opacity="0.6"/>
  <polygon points="30,22 45,22 30,50" fill="#22d3ee" opacity="0.4"/>
  <polygon points="22,12 38,12 45,22 15,22" fill="url(#diamFacet)"/>
  <polygon points="22,12 38,12 34,22 26,22" fill="#ffffff" opacity="0.7"/>
  <polygon points="22,12 26,22 15,22" fill="#a5f3fc" opacity="0.5"/>
  <polygon points="38,12 45,22 34,22" fill="#0891b2" opacity="0.5"/>
  <circle cx="25" cy="18" r="1.5" fill="#ffffff"/>
  <circle cx="32" cy="30" r="1.8" fill="#ffffff" opacity="0.9"/>
</svg>'''

all_svgs['token_pawn_classic'] = '''<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="pawnHeadShine" cx="35%" cy="30%" r="65%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="40%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#78350f"/>
    </radialGradient>
    <linearGradient id="pawnBodyGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#92400e"/>
      <stop offset="30%" stop-color="#fbbf24"/>
      <stop offset="70%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
    <radialGradient id="pawnBaseAo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="rgba(0,0,0,0.6)"/>
      <stop offset="100%" stop-color="rgba(0,0,0,0)"/>
    </radialGradient>
  </defs>
  <ellipse cx="30" cy="54" rx="22" ry="5" fill="url(#pawnBaseAo)"/>
  <ellipse cx="30" cy="51" rx="19" ry="4.5" fill="#78350f"/>
  <path d="M11,51 C11,48 49,48 49,51 L49,46 C49,43 11,43 11,46 Z" fill="url(#pawnBodyGrad)"/>
  <ellipse cx="30" cy="46" rx="19" ry="4" fill="#fef08a"/>
  <ellipse cx="30" cy="43" rx="14" ry="3.2" fill="#78350f"/>
  <path d="M16,43 C16,40 44,40 44,43 L42,37 C42,35 18,35 18,37 Z" fill="url(#pawnBodyGrad)"/>
  <ellipse cx="30" cy="37" rx="12" ry="2.8" fill="#fbbf24"/>
  <path d="M19,37 C22,28 23,23 25,19 L35,19 C37,23 38,28 41,37 Z" fill="url(#pawnBodyGrad)"/>
  <ellipse cx="30" cy="19" rx="8" ry="2.2" fill="#78350f"/>
  <ellipse cx="30" cy="18" rx="8" ry="2.2" fill="#fef08a"/>
  <circle cx="30" cy="12" r="7.5" fill="url(#pawnHeadShine)"/>
  <ellipse cx="28" cy="9.5" rx="2.5" ry="1.4" fill="#ffffff" opacity="0.6"/>
</svg>'''

all_svgs['token_knight'] = '''<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="knightGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="35%" stop-color="#cbd5e1"/>
      <stop offset="70%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
    <radialGradient id="knightBaseAo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="rgba(0,0,0,0.5)"/>
      <stop offset="100%" stop-color="rgba(0,0,0,0)"/>
    </radialGradient>
  </defs>
  <ellipse cx="30" cy="54" rx="20" ry="5" fill="url(#knightBaseAo)"/>
  <path d="M14,50 C14,46 46,46 46,50 L45,44 C45,41 15,41 15,44 Z" fill="#475569"/>
  <ellipse cx="30" cy="44" rx="15" ry="3.5" fill="#e2e8f0"/>
  <path d="M18,44 C19,36 17,28 20,20 C22,15 25,12 28,10 C29,8 33,6 35,9 C36,11 35,14 38,14 C41,14 43,18 42,22 C41,25 36,26 34,26 C33,28 35,32 38,36 C40,39 41,41 42,44 Z" fill="url(#knightGrad)"/>
  <path d="M22,18 C20,22 19,26 19,30" stroke="#334155" stroke-width="1.8" stroke-linecap="round" fill="none"/>
  <path d="M24,14 C22,17 21,20 21,24" stroke="#334155" stroke-width="1.8" stroke-linecap="round" fill="none"/>
  <circle cx="40" cy="18" r="1.2" fill="#1e293b"/>
  <circle cx="33" cy="14" r="1.6" fill="#1e293b"/>
  <circle cx="32.5" cy="13.5" r="0.6" fill="#ffffff"/>
  <polygon points="28,10 32,5 33,10" fill="#cbd5e1" stroke="#475569" stroke-width="0.8"/>
</svg>'''

all_svgs['token_rook'] = '''<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rookStone" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="35%" stop-color="#94a3b8"/>
      <stop offset="70%" stop-color="#64748b"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <ellipse cx="30" cy="54" rx="20" ry="5" fill="rgba(0,0,0,0.5)"/>
  <path d="M13,50 C13,46 47,46 47,50 L46,45 C46,42 14,42 14,45 Z" fill="#1e293b"/>
  <ellipse cx="30" cy="45" rx="16" ry="3.5" fill="#cbd5e1"/>
  <path d="M17,45 L20,20 L40,20 L43,45 Z" fill="url(#rookStone)"/>
  <line x1="20" y1="36" x2="40" y2="36" stroke="#1e293b" stroke-width="1" opacity="0.4"/>
  <line x1="19" y1="28" x2="41" y2="28" stroke="#1e293b" stroke-width="1" opacity="0.4"/>
  <rect x="28.5" y="27" width="3" height="7" rx="1.5" fill="#0f172a"/>
  <path d="M18,20 L16,14 L44,14 L42,20 Z" fill="url(#rookStone)"/>
  <ellipse cx="30" cy="14" rx="14" ry="3" fill="#cbd5e1"/>
  <rect x="17" y="8" width="5" height="7" fill="#64748b"/>
  <rect x="25" y="8" width="4.5" height="7" fill="#94a3b8"/>
  <rect x="32" y="8" width="4.5" height="7" fill="#64748b"/>
  <rect x="39" y="8" width="5" height="7" fill="#475569"/>
</svg>'''

all_svgs['token_crown'] = '''<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="crownGold" cx="35%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="45%" stop-color="#eab308"/>
      <stop offset="85%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#78350f"/>
    </radialGradient>
    <radialGradient id="velvetRed" cx="40%" cy="30%" r="65%">
      <stop offset="0%" stop-color="#f87171"/>
      <stop offset="50%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#7f1d1d"/>
    </radialGradient>
  </defs>
  <ellipse cx="30" cy="54" rx="20" ry="5" fill="rgba(0,0,0,0.5)"/>
  <ellipse cx="30" cy="50" rx="18" ry="4" fill="#78350f"/>
  <path d="M12,50 C12,47 48,47 48,50 L48,46 C48,43 12,43 12,46 Z" fill="url(#crownGold)"/>
  <ellipse cx="30" cy="46" rx="18" ry="3.5" fill="#fef08a"/>
  <path d="M16,42 C16,24 44,24 44,42 Z" fill="url(#velvetRed)"/>
  <path d="M13,44 C13,40 47,40 47,44 L47,38 C47,35 13,35 13,38 Z" fill="url(#crownGold)"/>
  <circle cx="21" cy="41" r="2.2" fill="#38bdf8"/>
  <circle cx="30" cy="41" r="2.5" fill="#22c55e"/>
  <circle cx="39" cy="41" r="2.2" fill="#ec4899"/>
  <path d="M14,37 L17,20 L23,32 L30,16 L37,32 L43,20 L46,37 Z" fill="url(#crownGold)"/>
  <circle cx="30" cy="14" r="3" fill="#fef08a"/>
  <path d="M28.5,8 L31.5,8 M30,6.5 L30,11" stroke="#fef08a" stroke-width="1.8" stroke-linecap="round"/>
</svg>'''

all_svgs['token_falcon'] = '''<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="falconGold" cx="35%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="40%" stop-color="#fbbf24"/>
      <stop offset="80%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#78350f"/>
    </radialGradient>
  </defs>
  <ellipse cx="30" cy="54" rx="20" ry="5" fill="rgba(0,0,0,0.5)"/>
  <rect x="15" y="47" width="30" height="5" rx="1.5" fill="#78350f"/>
  <rect x="17" y="44" width="26" height="4" rx="1" fill="#fef08a"/>
  <path d="M24,44 C22,34 23,24 28,18 C29,14 31,10 35,8 C38,7 41,9 41,12 C40,15 36,18 36,22 C37,27 38,36 34,44 Z" fill="url(#falconGold)"/>
  <path d="M41,12 C43,12 45,14 44,16 C43,17 41,17 39,16 Z" fill="#78350f"/>
  <circle cx="37" cy="12" r="1.8" fill="#1e293b"/>
  <circle cx="36.5" cy="11.5" r="0.7" fill="#ffffff"/>
  <path d="M37,14 L36,18 M37,14 L40,16" stroke="#1e293b" stroke-width="1" stroke-linecap="round"/>
  <polygon points="26,44 28,52 31,44" fill="#b45309"/>
</svg>'''

all_svgs['jail_cage_3d'] = '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="jail-cage-svg">
  <defs>
    <linearGradient id="ironBarGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="35%" stop-color="#64748b"/>
      <stop offset="60%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="padlockGold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="40%" stop-color="#eab308"/>
      <stop offset="100%" stop-color="#854d0e"/>
    </linearGradient>
    <radialGradient id="shackleShine" cx="30%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#cbd5e1"/>
      <stop offset="60%" stop-color="#64748b"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </radialGradient>
  </defs>
  <rect x="2" y="2" width="96" height="96" rx="4" fill="none" stroke="url(#ironBarGrad)" stroke-width="5"/>
  <rect x="2" y="16" width="96" height="5" fill="url(#ironBarGrad)"/>
  <rect x="2" y="80" width="96" height="5" fill="url(#ironBarGrad)"/>
  <rect x="2" y="48" width="96" height="4" fill="url(#ironBarGrad)"/>
  <rect x="14" y="2" width="5.5" height="96" fill="url(#ironBarGrad)" rx="1"/>
  <rect x="28" y="2" width="5.5" height="96" fill="url(#ironBarGrad)" rx="1"/>
  <rect x="42" y="2" width="5.5" height="96" fill="url(#ironBarGrad)" rx="1"/>
  <rect x="56" y="2" width="5.5" height="96" fill="url(#ironBarGrad)" rx="1"/>
  <rect x="70" y="2" width="5.5" height="96" fill="url(#ironBarGrad)" rx="1"/>
  <rect x="84" y="2" width="5.5" height="96" fill="url(#ironBarGrad)" rx="1"/>
  <circle cx="16.5" cy="18.5" r="1.8" fill="#cbd5e1"/>
  <circle cx="30.5" cy="18.5" r="1.8" fill="#cbd5e1"/>
  <circle cx="44.5" cy="18.5" r="1.8" fill="#cbd5e1"/>
  <circle cx="58.5" cy="18.5" r="1.8" fill="#cbd5e1"/>
  <circle cx="72.5" cy="18.5" r="1.8" fill="#cbd5e1"/>
  <circle cx="86.5" cy="18.5" r="1.8" fill="#cbd5e1"/>
  <circle cx="16.5" cy="82.5" r="1.8" fill="#cbd5e1"/>
  <circle cx="30.5" cy="82.5" r="1.8" fill="#cbd5e1"/>
  <circle cx="44.5" cy="82.5" r="1.8" fill="#cbd5e1"/>
  <circle cx="58.5" cy="82.5" r="1.8" fill="#cbd5e1"/>
  <circle cx="72.5" cy="82.5" r="1.8" fill="#cbd5e1"/>
  <circle cx="86.5" cy="82.5" r="1.8" fill="#cbd5e1"/>
  <path d="M41,40 C41,29 59,29 59,40 L59,47 L41,47 Z" fill="none" stroke="url(#shackleShine)" stroke-width="5" stroke-linecap="round"/>
  <rect x="36" y="44" width="28" height="24" rx="4" fill="url(#padlockGold)" stroke="#78350f" stroke-width="1.5"/>
  <circle cx="50" cy="53" r="3" fill="#1c1917"/>
  <polygon points="48.5,53 51.5,53 52,61 48,61" fill="#1c1917"/>
</svg>'''


# Characters (Strictly 2 Players)
CHARACTERS_2P = [
    {
        "id": "mr_hazz",
        "name": "مستر حظ",
        "title": "الملياردير الطموح",
        "avatar": "🎩",
        "color": "#b91c1c",
        "accent": "#f59e0b",
        "tokenSvg": all_svgs['fig_mr_hazz'],
        "quote": "الفرصة لا تأتي مرتين، والحظ حليف الجريء!"
    },
    {
        "id": "cleo_queen",
        "name": "الملكة كليوباترا",
        "title": "أميرة العرش والذهب",
        "avatar": "👑",
        "color": "#1e3a8a",
        "accent": "#d97706",
        "tokenSvg": all_svgs['fig_cleopatra'],
        "quote": "الأهرامات بُنيت بالذهب والعزيمة الملكية!"
    }
]

# Serialized data
tiles_json = json.dumps(TILES, ensure_ascii=False)
chance_json = json.dumps(CHANCE_CARDS, ensure_ascii=False)
chest_json = json.dumps(CHEST_CARDS, ensure_ascii=False)
landmarks_json = json.dumps(LANDMARKS, ensure_ascii=False)
characters_json = json.dumps(CHARACTERS_2P, ensure_ascii=False)
wheel_json = json.dumps(WHEEL_ITEMS, ensure_ascii=False)
svg_assets_json = json.dumps(all_svgs, ensure_ascii=False)

lang_options_list = [f'<option value="{l["code"]}">{l["flag"]} {l["name"]}</option>' for l in I18N_LANGUAGES]
lang_options_html = "\n            ".join(lang_options_list)

MATTE_PHYSICAL_CSS = """
:root {
  --bg-table: #150c08;
  --board-wood: #3d2314;
  --board-trim: #b45309;
  --felt-green: #0d4a38;
  --tile-ivory: #fdfbf7;
  --tile-ivory-dark: #f0ebd9;
  --text-dark: #1f1b16;
  --text-light: #f8fafc;
  --accent-gold: #f59e0b;
  --accent-gold-dark: #b45309;
  --font-family: 'Cairo', 'Segoe UI', system-ui, -apple-system, sans-serif;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
}

body {
  background: radial-gradient(ellipse at 50% 30%, #291811 0%, #150c08 65%, #080403 100%);
  color: var(--text-light);
  font-family: var(--font-family);
  direction: rtl;
  min-height: 100vh;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
}

/* App Header */
.app-header {
  background: rgba(26, 15, 10, 0.9);
  backdrop-filter: blur(10px);
  border-bottom: 2px solid rgba(245, 158, 11, 0.35);
  padding: 8px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 4px 15px rgba(0,0,0,0.6);
}

.brand-title {
  display: flex;
  align-items: center;
  gap: 10px;
}

.brand-logo-icon {
  width: 42px;
  height: 42px;
  background: linear-gradient(135deg, #d97706, #92400e);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.5), inset 0 2px 0 rgba(255,255,255,0.4);
  border: 2px solid #fef08a;
}

.brand-text h1 {
  font-size: 20px;
  font-weight: 900;
  background: linear-gradient(to left, #fef08a, #ffffff, #f59e0b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1.2;
}

.brand-badge {
  font-size: 10px;
  font-weight: 800;
  background: linear-gradient(90deg, #b91c1c, #d97706);
  color: white;
  padding: 2px 8px;
  border-radius: 20px;
  margin-right: 6px;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

/* Tactile Matte Buttons */
.btn-matte {
  background: linear-gradient(180deg, #475569, #1e293b);
  border: 1px solid #64748b;
  color: white;
  font-family: inherit;
  font-weight: 800;
  font-size: 13px;
  padding: 8px 14px;
  border-radius: 10px;
  cursor: pointer;
  position: relative;
  box-shadow: 0 3px 0 #0f172a, 0 4px 8px rgba(0,0,0,0.3);
  transition: all 0.1s ease;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.btn-matte:active {
  transform: translateY(2px);
  box-shadow: 0 1px 0 #0f172a;
}

.btn-matte.gold {
  background: linear-gradient(180deg, #d97706, #92400e);
  border-color: #fef08a;
  box-shadow: 0 3px 0 #451a03, 0 4px 8px rgba(0,0,0,0.4);
  color: #fffbeb;
}

.btn-matte.wood {
  background: linear-gradient(180deg, #9a3412, #451a03);
  border-color: #f59e0b;
  box-shadow: 0 3px 0 #270f03;
}

.btn-matte.crimson {
  background: linear-gradient(180deg, #b91c1c, #7f1d1d);
  border-color: #f87171;
  box-shadow: 0 3px 0 #450a0a;
}

/* Head-to-Head 2-Player Versus Bar */
.versus-clash-bar {
  background: linear-gradient(180deg, rgba(38, 22, 15, 0.95) 0%, rgba(20, 11, 7, 0.98) 100%);
  border-bottom: 2px solid rgba(245, 158, 11, 0.3);
  padding: 10px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7);
  position: relative;
  z-index: 50;
}

.player-duel-card {
  flex: 1;
  max-width: 480px;
  background: #25160f;
  border-radius: 16px;
  padding: 10px 18px;
  display: flex;
  align-items: center;
  gap: 16px;
  border: 2.5px solid #4a2d1d;
  box-shadow: 0 5px 0 #120905, 0 8px 16px rgba(0,0,0,0.5);
  position: relative;
  transition: all 0.3s ease;
}

.player-duel-card.active-turn {
  border-color: #f59e0b;
  background: linear-gradient(135deg, #2d1a12, #3b2419);
  box-shadow: 0 5px 0 #78350f, 0 0 22px rgba(245, 158, 11, 0.4);
  transform: translateY(-2px);
}

.player-duel-card.p1 {
  border-right: 6px solid #b91c1c;
}

.player-duel-card.p2 {
  border-left: 6px solid #1e3a8a;
  flex-direction: row-reverse;
  text-align: left;
}

.duel-avatar-3d {
  width: 62px;
  height: 62px;
  filter: drop-shadow(0 4px 6px rgba(0,0,0,0.6));
  cursor: pointer;
  transition: transform 0.2s ease;
}

.duel-avatar-3d:hover {
  transform: scale(1.06);
}

.duel-info-col {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.duel-name-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.player-duel-card.p2 .duel-name-row {
  justify-content: flex-end;
}

.duel-name {
  font-size: 16px;
  font-weight: 900;
  color: #fffbeb;
}

.duel-bot-pill {
  font-size: 10px;
  background: rgba(30, 58, 138, 0.3);
  color: #bfdbfe;
  border: 1px solid #3b82f6;
  padding: 1px 6px;
  border-radius: 6px;
  font-weight: 700;
}

.duel-money {
  font-size: 19px;
  font-weight: 900;
  color: #fef08a;
  text-shadow: 0 2px 4px rgba(0,0,0,0.6);
}

.duel-net-worth {
  font-size: 11px;
  color: #d1c4b2;
  font-weight: 700;
}

.duel-shields-row {
  display: flex;
  gap: 4px;
}

.player-duel-card.p2 .duel-shields-row {
  justify-content: flex-end;
}

.shield-3d-badge {
  font-size: 13px;
  opacity: 0.25;
  filter: grayscale(1);
  transition: all 0.3s;
}

.shield-3d-badge.active {
  opacity: 1;
  filter: drop-shadow(0 0 6px #38bdf8);
}

/* Center VS Badge */
.versus-center-emblem {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
}

.vs-icon-badge {
  width: 46px;
  height: 46px;
  background: radial-gradient(circle, #991b1b 0%, #450a0a 100%);
  border: 2.5px solid #fef08a;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 900;
  color: #ffffff;
  box-shadow: 0 4px 12px rgba(0,0,0,0.6), 0 0 15px rgba(245, 158, 11, 0.5);
}

.versus-sub-label {
  font-size: 10px;
  font-weight: 800;
  color: #fbbf24;
  letter-spacing: 1px;
}

/* Main Layout Viewport */
.game-viewport {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding: 16px;
  gap: 20px;
  max-width: 1540px;
  margin: 0 auto;
  width: 100%;
}

/* The Solid Wooden Physical Board Container */
.board-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
}

.board-perspective-wrapper {
  perspective: 1400px;
  transition: perspective 0.6s ease;
}

.board-grid {
  width: min(960px, 95vw);
  height: min(960px, 95vw);
  background: #1a0f0a; /* dark recessed groove between tiles */
  border: 14px solid #3d2314; /* solid beveled mahogany wood rim */
  outline: 3px solid #b45309; /* inlaid brass trim */
  border-radius: 28px;
  display: grid;
  grid-template-columns: 1.4fr repeat(9, 1fr) 1.4fr;
  grid-template-rows: 1.4fr repeat(9, 1fr) 1.4fr;
  gap: 3px;
  padding: 8px;
  position: relative;
  box-shadow: 0 25px 0 #1b0f0a, 0 30px 0 #0d0705, 0 45px 80px rgba(0, 0, 0, 0.9), inset 0 2px 4px rgba(255,255,255,0.15);
  transform-origin: center center;
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.6s ease;
}


/* Large Matte Ivory Board Tiles */
.tile {
  background: linear-gradient(180deg, #fdfbf7 0%, #f4eee2 100%) !important;
  border: 1px solid #dcd4c3 !important;
  border-radius: 7px !important;
  box-shadow: 0 4px 0 #b8ad98, 0 6px 10px rgba(0, 0, 0, 0.3) !important;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 3px 2px !important;
  position: relative;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
  overflow: visible !important;
  text-align: center;
}

.tile:hover {
  transform: translateY(-6px) scale(1.04) !important;
  box-shadow: 0 9px 0 #b8ad98, 0 14px 20px rgba(0, 0, 0, 0.45) !important;
  border-color: #d97706 !important;
  z-index: 35 !important;
}

.tile-corner {
  background: linear-gradient(180deg, #f5ebd7 0%, #e8dcbe 100%) !important;
  border: 1.5px solid #c2b291 !important;
  box-shadow: 0 5px 0 #a89878, 0 8px 14px rgba(0, 0, 0, 0.35) !important;
}

.tile-corner:hover {
  border-color: #b45309 !important;
}

.corner-title {
  font-size: 11px;
  font-weight: 900;
  color: #451a03;
}

.corner-sub {
  font-size: 8px;
  color: #78350f;
  font-weight: 700;
}

/* Matte Color Header Band */
.color-bar {
  width: 100%;
  height: 14px;
  border-radius: 5px 5px 0 0;
  border-bottom: 2px solid #b45309;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.4);
}

.tile-name {
  font-size: 10px;
  font-weight: 800;
  color: #1e1b18;
  line-height: 1.15;
  white-space: nowrap;
  max-width: 96%;
  overflow: hidden;
  text-overflow: ellipsis;
}

.tile-price {
  font-size: 9px;
  font-weight: 900;
  color: #78350f;
  background: #fef3c7;
  padding: 1px 5px;
  border-radius: 4px;
  border: 1px solid #f59e0b;
}

/* Large 3D Sculptural Art inside Tiles */
.tile-3d-art {
  width: 95%;
  height: 52px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 1px 0;
  filter: drop-shadow(0 3px 5px rgba(0, 0, 0, 0.35));
  transition: transform 0.2s ease;
}

.tile-3d-art svg {
  width: 100%;
  height: 100%;
  max-height: 52px;
  object-fit: contain;
}

.tile:hover .tile-3d-art {
  transform: scale(1.15) translateY(-2px);
}

.tile-corner .tile-3d-art {
  height: 58px;
}

.tile-corner .tile-3d-art svg {
  max-height: 58px;
}

/* 3D Painted Miniature Houses & Hotels on Tiles */
.tile-buildings-3d {
  position: absolute;
  top: 11px;
  right: 2px;
  display: flex;
  gap: 1px;
  z-index: 10;
  filter: drop-shadow(0 3px 4px rgba(0, 0, 0, 0.5));
}

.mini-house-3d {
  width: 17px;
  height: 17px;
  animation: pop-bounce 0.4s cubic-bezier(0.2, 0.8, 0.2, 1.2);
}

.mini-hotel-3d {
  width: 24px;
  height: 24px;
  animation: pop-bounce 0.5s cubic-bezier(0.2, 0.8, 0.2, 1.2);
}

@keyframes pop-bounce {
  0% { transform: scale(0); opacity: 0; }
  60% { transform: scale(1.2); }
  100% { transform: scale(1); opacity: 1; }
}

/* 3D Standing Figurine Tokens on Tiles */
.player-tokens-container {
  position: absolute;
  bottom: 2px;
  display: flex;
  gap: 4px;
  justify-content: center;
  align-items: center;
  z-index: 20;
  width: 100%;
}

.board-token-3d {
  width: 36px;
  height: 36px;
  filter: drop-shadow(0 5px 8px rgba(0, 0, 0, 0.7));
  cursor: pointer;
  transition: transform 0.15s ease-out;
  position: relative;
}

.board-token-3d svg {
  width: 100%;
  height: 100%;
}

.board-token-3d:hover {
  transform: scale(1.15) translateY(-3px);
}

.board-token-3d.stepping {
  animation: token-step-hop 0.14s ease-out;
}

@keyframes token-step-hop {
  0% { transform: translateY(0) scale(1); }
  50% { transform: translateY(-10px) scale(1.15); }
  100% { transform: translateY(0) scale(1); }
}

/* Owner Stripe on Board */
.tile.owned {
  box-shadow: inset 0 0 0 2px var(--owner-color), 0 4px 0 #b8ad98, 0 6px 10px rgba(0, 0, 0, 0.3) !important;
}

.owner-indicator {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: var(--owner-color, transparent);
  border-radius: 0 0 6px 6px;
}

.tile.mortgaged::after {
  content: 'مرهون';
  position: absolute;
  inset: 0;
  background: rgba(185, 28, 28, 0.8);
  backdrop-filter: blur(1px);
  color: white;
  font-size: 11px;
  font-weight: 900;
  display: flex;
  align-items: center;
  justify-content: center;
  transform: rotate(-15deg);
  z-index: 8;
  border-radius: 6px;
}

/* Inset Emerald Green Baize Felt Dice Tray (Center of Board) */
.board-center {
  grid-column: 2 / 11;
  grid-row: 2 / 11;
  background: radial-gradient(circle at center, #0f4c3a 0%, #072b21 100%) !important;
  border: 4px solid #2a160d !important;
  border-radius: 18px !important;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 14px;
  position: relative;
  overflow: hidden;
  box-shadow: inset 0 8px 24px rgba(0,0,0,0.8), 0 2px 4px rgba(255,255,255,0.1) !important;
}

.center-top-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  z-index: 3;
}

.free-parking-pot {
  background: rgba(18, 10, 6, 0.85);
  border: 2px solid #f59e0b;
  padding: 6px 14px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.5);
}

.pot-icon { font-size: 20px; }
.pot-amount { font-size: 15px; font-weight: 900; color: #fef08a; }

.board-title-emblem {
  text-align: center;
  z-index: 3;
}

.emblem-title {
  font-size: 28px;
  font-weight: 900;
  background: linear-gradient(180deg, #fef08a 0%, #f59e0b 50%, #b45309 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: -1px;
}

.emblem-sub {
  font-size: 11px;
  font-weight: 800;
  color: #93c5fd;
  letter-spacing: 1.5px;
}

/* 3D Animated Cairo Skyline Diorama & In-Board Event Cards */
.center-diorama-container {
  width: 100%;
  max-width: 460px;
  height: 145px;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.7);
  border: 2px solid rgba(245, 158, 11, 0.5);
  margin-bottom: 6px;
  position: relative;
  z-index: 5;
  perspective: 900px;
  background: #0f172a;
  transition: border-color 0.35s ease, box-shadow 0.35s ease;
}

/* Layer 1: Pyramids Skyline Diorama */
.diorama-pyramids-layer {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
  transition: opacity 0.4s ease, transform 0.4s ease;
  opacity: 1;
  transform: scale(1);
}
.diorama-pyramids-layer.hidden {
  opacity: 0;
  transform: scale(0.92);
  pointer-events: none;
}
.diorama-pyramids-layer svg {
  width: 100%;
  height: 100%;
  display: block;
}

/* Layer 2: 3D Physical Event Card (Replaces Pyramids) */
.diorama-card-layer {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 8px;
  transition: opacity 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
  transform: perspective(800px) rotateX(0deg) scale(1);
  opacity: 1;
}
.diorama-card-layer.hidden {
  opacity: 0;
  transform: perspective(800px) rotateX(-55deg) scale(0.85);
  pointer-events: none;
}

.diorama-card-inner {
  cursor: pointer;
  width: 100%;
  height: 100%;
  border-radius: 10px;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 12px;
  position: relative;
  overflow: hidden;
  box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.2), 0 6px 18px rgba(0, 0, 0, 0.6);
  border: 2px solid #f59e0b;
}

/* Art Column */
.diorama-card-art-col {
  width: 66px;
  height: 66px;
  flex-shrink: 0;
  border-radius: 12px;
  background: rgba(0, 0, 0, 0.35);
  border: 1px solid rgba(255, 255, 255, 0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 5px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
}
.diorama-card-art-3d {
  width: 100%;
  height: 100%;
}
.diorama-card-art-3d svg {
  width: 100%;
  height: 100%;
  display: block;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.5));
}

/* Content Column */
.diorama-card-content-col {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: right;
}
.diorama-card-badge-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 3px;
}
.diorama-card-badge {
  padding: 2px 8px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 800;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.diorama-card-player-tag {
  font-size: 10px;
  color: #94a3b8;
  background: rgba(0, 0, 0, 0.35);
  padding: 2px 6px;
  border-radius: 4px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}
.diorama-card-title {
  font-size: 13.5px;
  font-weight: 800;
  color: #fff;
  margin-bottom: 2px;
  line-height: 1.25;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.diorama-card-desc {
  font-size: 11px;
  line-height: 1.35;
  color: #cbd5e1;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Action Column */
.diorama-card-action-col {
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-right: 4px;
}
.diorama-card-btn {
  background: linear-gradient(180deg, #f59e0b 0%, #d97706 100%);
  color: #1a0f0a;
  font-weight: 900;
  font-size: 12px;
  border-radius: 8px;
  padding: 8px 12px;
  border: 1px solid #fef08a;
  cursor: pointer;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.4);
  transition: transform 0.15s ease, box-shadow 0.15s ease, filter 0.15s ease;
  white-space: nowrap;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.diorama-card-btn:hover {
  transform: translateY(-2px) scale(1.03);
  filter: brightness(1.1);
  box-shadow: 0 6px 14px rgba(0, 0, 0, 0.5);
}
.diorama-card-btn:active {
  transform: translateY(1px) scale(0.98);
}
.diorama-card-btn:disabled {
  opacity: 0.7;
  cursor: default;
  transform: none;
}

/* THEMES */
/* 1. Community Chest */
.card-theme-chest {
  border-color: #f59e0b !important;
  box-shadow: 0 8px 25px rgba(245, 158, 11, 0.35) !important;
}
.card-theme-chest .diorama-card-inner {
  background: radial-gradient(circle at top right, #1e293b 0%, #0f172a 100%);
  border-color: #f59e0b;
}
.card-theme-chest .diorama-card-badge {
  background: rgba(245, 158, 11, 0.25);
  color: #fbbf24;
  border: 1px solid rgba(245, 158, 11, 0.5);
}
.card-theme-chest .diorama-card-btn {
  background: linear-gradient(180deg, #f59e0b 0%, #d97706 100%);
  border-color: #fef08a;
}

/* 2. Chance */
.card-theme-chance {
  border-color: #f97316 !important;
  box-shadow: 0 8px 25px rgba(249, 115, 22, 0.35) !important;
}
.card-theme-chance .diorama-card-inner {
  background: radial-gradient(circle at top right, #431407 0%, #1e0d05 100%);
  border-color: #f97316;
}
.card-theme-chance .diorama-card-badge {
  background: rgba(249, 115, 22, 0.25);
  color: #fdba74;
  border: 1px solid rgba(249, 115, 22, 0.5);
}
.card-theme-chance .diorama-card-btn {
  background: linear-gradient(180deg, #fb923c 0%, #ea580c 100%);
  border-color: #fed7aa;
}

/* 3. Income Tax */
.card-theme-income_tax {
  border-color: #10b981 !important;
  box-shadow: 0 8px 25px rgba(16, 185, 129, 0.35) !important;
}
.card-theme-income_tax .diorama-card-inner {
  background: radial-gradient(circle at top right, #064e3b 0%, #022c22 100%);
  border-color: #10b981;
}
.card-theme-income_tax .diorama-card-badge {
  background: rgba(16, 185, 129, 0.25);
  color: #6ee7b7;
  border: 1px solid rgba(16, 185, 129, 0.5);
}
.card-theme-income_tax .diorama-card-btn {
  background: linear-gradient(180deg, #34d399 0%, #059669 100%);
  border-color: #a7f3d0;
  color: #022c22;
}

/* 4. Luxury Tax */
.card-theme-luxury_tax {
  border-color: #c084fc !important;
  box-shadow: 0 8px 25px rgba(192, 132, 252, 0.35) !important;
}
.card-theme-luxury_tax .diorama-card-inner {
  background: radial-gradient(circle at top right, #3b0764 0%, #1e1b4b 100%);
  border-color: #c084fc;
}
.card-theme-luxury_tax .diorama-card-badge {
  background: rgba(192, 132, 252, 0.25);
  color: #e9d5ff;
  border: 1px solid rgba(192, 132, 252, 0.5);
}
.card-theme-luxury_tax .diorama-card-btn {
  background: linear-gradient(180deg, #c084fc 0%, #9333ea 100%);
  border-color: #f3e8ff;
  color: #1e1b4b;
}

/* 5. Jail (Sent to Jail) */
.card-theme-jail {
  border-color: #ef4444 !important;
  box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4) !important;
}
.card-theme-jail .diorama-card-inner {
  background: radial-gradient(circle at top right, #27272a 0%, #18181b 100%);
  border-color: #ef4444;
}
.card-theme-jail .diorama-card-badge {
  background: rgba(239, 68, 68, 0.25);
  color: #fca5a5;
  border: 1px solid rgba(239, 68, 68, 0.5);
}
.card-theme-jail .diorama-card-btn {
  background: linear-gradient(180deg, #ef4444 0%, #b91c1c 100%);
  border-color: #fecaca;
  color: #fff;
}

/* 6. Visiting Jail */
.card-theme-visiting {
  border-color: #64748b !important;
  box-shadow: 0 8px 25px rgba(100, 116, 139, 0.35) !important;
}
.card-theme-visiting .diorama-card-inner {
  background: radial-gradient(circle at top right, #1e293b 0%, #0f172a 100%);
  border-color: #64748b;
}
.card-theme-visiting .diorama-card-badge {
  background: rgba(100, 116, 139, 0.25);
  color: #cbd5e1;
  border: 1px solid rgba(100, 116, 139, 0.5);
}
.card-theme-visiting .diorama-card-btn {
  background: linear-gradient(180deg, #64748b 0%, #475569 100%);
  border-color: #e2e8f0;
  color: #fff;
}

/* 3D Rolling Dice on Felt */
.dice-arena {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 32px;
  margin: 6px 0;
  z-index: 3;
  perspective: 700px;
  min-height: 80px;
}

.dice-cube {
  width: 58px;
  height: 58px;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 1s cubic-bezier(0.2, 0.9, 0.3, 1.2);
}

.dice-cube.rolling {
  animation: dice-tumble 1s linear infinite;
}

@keyframes dice-tumble {
  0% { transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg); }
  25% { transform: rotateX(180deg) rotateY(90deg) rotateZ(45deg); }
  50% { transform: rotateX(360deg) rotateY(180deg) rotateZ(180deg); }
  75% { transform: rotateX(540deg) rotateY(270deg) rotateZ(270deg); }
  100% { transform: rotateX(720deg) rotateY(360deg) rotateZ(360deg); }
}

.dice-face {
  position: absolute;
  width: 58px;
  height: 58px;
  background: linear-gradient(135deg, #fdfbf7 0%, #ece6d8 100%);
  border: 2px solid #b8ad98;
  border-radius: 12px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  padding: 6px;
  box-shadow: inset 0 1px 3px rgba(255,255,255,0.8), inset 0 -2px 4px rgba(0,0,0,0.15);
}

.dice-pip {
  width: 10px;
  height: 10px;
  background: #b91c1c;
  border-radius: 50%;
  box-shadow: inset 0 1px 2px rgba(0,0,0,0.5);
  place-self: center;
}

.dice-cube:last-child .dice-pip {
  background: #1e3a8a;
}

.face-1 { transform: rotateY(0deg) translateZ(29px); }
.face-2 { transform: rotateY(-90deg) translateZ(29px); }
.face-3 { transform: rotateX(90deg) translateZ(29px); }
.face-4 { transform: rotateX(-90deg) translateZ(29px); }
.face-5 { transform: rotateY(90deg) translateZ(29px); }
.face-6 { transform: rotateY(180deg) translateZ(29px); }

/* Controls & Big Roll Button */
.center-controls-row {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  width: 100%;
  z-index: 3;
}

.btn-big-roll {
  background: linear-gradient(180deg, #f59e0b 0%, #d97706 50%, #92400e 100%);
  border: 2px solid #fef08a;
  color: #ffffff;
  font-family: inherit;
  font-size: 20px;
  font-weight: 900;
  padding: 12px 42px;
  border-radius: 20px;
  cursor: pointer;
  box-shadow: 0 5px 0 #451a03, 0 10px 20px rgba(0, 0, 0, 0.6);
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 10px;
}

.btn-big-roll:hover {
  filter: brightness(1.1);
  transform: translateY(-2px);
  box-shadow: 0 7px 0 #451a03, 0 14px 24px rgba(0, 0, 0, 0.7);
}

.btn-big-roll:active {
  transform: translateY(3px);
  box-shadow: 0 2px 0 #451a03;
}

.btn-big-roll:disabled {
  filter: grayscale(0.8);
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.turn-status-banner {
  background: rgba(18, 10, 6, 0.9);
  border: 1px solid rgba(245, 158, 11, 0.4);
  border-radius: 12px;
  padding: 6px 16px;
  font-size: 13px;
  font-weight: 800;
  color: #f8fafc;
  display: flex;
  align-items: center;
  gap: 8px;
  max-width: 90%;
  text-align: center;
  z-index: 3;
}

/* Sidebar / Duel Activity Feed */
.game-sidebar {
  width: 320px;
  background: rgba(26, 15, 10, 0.9);
  backdrop-filter: blur(10px);
  border: 2px solid #4a2d1d;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  height: min(960px, 95vw);
  box-shadow: 0 15px 35px rgba(0,0,0,0.6);
}

.sidebar-header {
  padding: 12px 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.sidebar-title {
  font-size: 14px;
  font-weight: 800;
  color: #fef08a;
  display: flex;
  align-items: center;
  gap: 6px;
}

.sidebar-content {
  flex: 1;
  padding: 12px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.log-entry {
  background: rgba(18, 10, 6, 0.7);
  border-radius: 10px;
  padding: 8px 10px;
  font-size: 12px;
  line-height: 1.45;
  border-right: 3px solid #f59e0b;
}

.log-entry.gold { border-right-color: #fef08a; }
.log-entry.green { border-right-color: #10b981; }
.log-entry.red { border-right-color: #ef4444; }

.log-time {
  font-size: 9px;
  color: #94a3b8;
  margin-bottom: 2px;
}

/* Modals */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.82);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 500;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
  padding: 16px;
}

.modal-overlay.active {
  opacity: 1;
  pointer-events: auto;
}

.modal-box {
  background: #25160f;
  border: 2px solid #f59e0b;
  border-radius: 22px;
  width: min(560px, 94vw);
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 25px 60px rgba(0,0,0,0.85), 0 0 35px rgba(245, 158, 11, 0.3);
  display: flex;
  flex-direction: column;
  position: relative;
  transform: scale(0.92);
  transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1.2);
}

.modal-overlay.active .modal-box { transform: scale(1); }

.modal-header {
  padding: 16px 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-title {
  font-size: 18px;
  font-weight: 900;
  color: #fef08a;
  display: flex;
  align-items: center;
  gap: 8px;
}

.modal-close-btn {
  background: transparent;
  border: none;
  color: #94a3b8;
  font-size: 20px;
  cursor: pointer;
  padding: 4px;
}

.modal-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.modal-footer {
  padding: 14px 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

/* Large Physical Property Deed Card */
.deed-card {
  background: #fdfbf7;
  color: #1f1b16;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 10px 25px rgba(0,0,0,0.4);
  border: 3px solid #4a2d1d;
  font-size: 13px;
}

.deed-header {
  padding: 14px;
  text-align: center;
  color: white;
  font-weight: 900;
}

.deed-header h2 {
  font-size: 22px;
  text-shadow: 0 2px 4px rgba(0,0,0,0.4);
}

.deed-table {
  padding: 12px 18px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.deed-row {
  display: flex;
  justify-content: space-between;
  border-bottom: 1px dashed #dcd4c3;
  padding-bottom: 4px;
  font-weight: 700;
}

.deed-row.highlight {
  background: #fef3c7;
  padding: 4px 6px;
  border-radius: 6px;
  border-bottom: none;
}

/* Bank Heist Mini-Game */
.heist-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.heist-vault-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
  width: 100%;
}

.vault-door {
  aspect-ratio: 1;
  background: linear-gradient(135deg, #475569, #1e293b);
  border: 2px solid #94a3b8;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 8px rgba(0,0,0,0.4);
}

.vault-door:hover:not(.opened) {
  transform: scale(1.08);
  border-color: #f59e0b;
}

.vault-door.opened {
  background: linear-gradient(135deg, #2d1a12, #451a03);
  border-color: #f59e0b;
  cursor: default;
}

.heist-match-tracker {
  display: flex;
  justify-content: space-around;
  width: 100%;
  background: rgba(18, 10, 6, 0.8);
  padding: 10px;
  border-radius: 12px;
}

.match-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.match-icons { display: flex; gap: 4px; }

.match-slot {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #334155;
  border: 1px solid #64748b;
}

.match-slot.filled {
  background: #fbbf24;
  box-shadow: 0 0 8px #fbbf24;
}

/* Shutdown Mini-Game */
.shutdown-stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  position: relative;
}

.target-landmark-box {
  width: 100%;
  height: 190px;
  background: radial-gradient(circle at center, #2d1a12 0%, #150c08 100%);
  border-radius: 18px;
  border: 2px solid #ef4444;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.target-crosshair {
  position: absolute;
  width: 130px;
  height: 130px;
  border: 2px dashed #ef4444;
  border-radius: 50%;
  animation: rotate-crosshair 6s linear infinite;
  pointer-events: none;
}

@keyframes rotate-crosshair {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.shield-deflection-dome {
  position: absolute;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(56, 189, 248, 0.3) 0%, rgba(56, 189, 248, 0.7) 100%);
  border: 3px solid #38bdf8;
  box-shadow: 0 0 30px #38bdf8;
  animation: shield-pulse 0.4s ease-out;
}

@keyframes shield-pulse {
  0% { transform: scale(0.3); opacity: 0; }
  50% { transform: scale(1.1); opacity: 1; }
  100% { transform: scale(1); opacity: 1; }
}

/* City Landmarks */
.landmarks-list { display: flex; flex-direction: column; gap: 12px; }

.landmark-builder-card {
  background: #1e120b;
  border: 1px solid #4a2d1d;
  border-radius: 14px;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.landmark-icon-badge {
  width: 62px;
  height: 62px;
  background: #0d0705;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #78350f;
  padding: 4px;
}

.landmark-meta { flex: 1; }
.landmark-stars-row { display: flex; gap: 4px; margin-top: 4px; }
.star-slot { font-size: 14px; color: #475569; }
.star-slot.filled { color: #fbbf24; filter: drop-shadow(0 0 4px #fbbf24); }

/* Wheel of Fortune */
.wheel-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  position: relative;
}

.wheel-canvas {
  width: 280px;
  height: 280px;
  border-radius: 50%;
  border: 6px solid #f59e0b;
  box-shadow: 0 0 25px rgba(245, 158, 11, 0.5);
  transition: transform 4s cubic-bezier(0.15, 0.9, 0.2, 1);
}

.wheel-pointer {
  position: absolute;
  top: -10px;
  width: 0;
  height: 0;
  border-left: 12px solid transparent;
  border-right: 12px solid transparent;
  border-top: 24px solid #b91c1c;
  filter: drop-shadow(0 4px 6px rgba(0,0,0,0.5));
  z-index: 10;
}

/* Floating Cash FX */
.floating-fx {
  position: absolute;
  font-size: 20px;
  font-weight: 900;
  pointer-events: none;
  z-index: 1000;
  animation: float-up-fade 1.5s forwards cubic-bezier(0.1, 0.8, 0.2, 1);
  text-shadow: 0 2px 6px rgba(0,0,0,0.9);
}

.floating-fx.plus { color: #10b981; }
.floating-fx.minus { color: #ef4444; }

@keyframes float-up-fade {
  0% { opacity: 0; transform: translateY(0) scale(0.6); }
  20% { opacity: 1; transform: translateY(-16px) scale(1.2); }
  80% { opacity: 1; }
  100% { opacity: 0; transform: translateY(-55px) scale(0.9); }
}

#confettiCanvas {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 9999;
}

@media (max-width: 900px) {
  .game-viewport { flex-direction: column; align-items: center; }
  .game-sidebar { width: min(960px, 95vw); height: 220px; }
  .versus-clash-bar { flex-direction: column; gap: 10px; }
  .player-duel-card { width: 100%; max-width: 100%; }
}
"""

MATTE_PHYSICAL_CSS += """
/* Duel Avatar 3D SVG Fitting */
.duel-avatar-3d svg {
  width: 100%;
  height: 100%;
}

/* Token Picker Modal Grid & Cards */
.token-picker-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  gap: 12px;
  max-height: 55vh;
  overflow-y: auto;
  padding: 4px;
}

.token-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 12px 8px;
  background: rgba(30, 20, 15, 0.75);
  border: 2px solid #57351d;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  text-align: center;
}

.token-card:hover {
  transform: translateY(-3px) scale(1.03);
  border-color: #f59e0b;
  background: rgba(245, 158, 11, 0.15);
  box-shadow: 0 6px 16px rgba(245, 158, 11, 0.25);
}

.token-card.active {
  border-color: #10b981;
  background: rgba(16, 185, 129, 0.18);
  box-shadow: 0 0 16px rgba(16, 185, 129, 0.4);
}

.token-card-preview {
  width: 54px;
  height: 54px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 8px;
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.6));
}

.token-card-preview svg {
  width: 100%;
  height: 100%;
}

.token-card-name {
  font-size: 12px;
  font-weight: 700;
  color: #fdfbf7;
  margin-bottom: 6px;
  line-height: 1.3;
}

.token-card-badge {
  font-size: 10px;
  padding: 2px 8px;
  border-radius: 8px;
  font-weight: 800;
}

.token-card.active .token-card-badge {
  background: #10b981;
  color: #ffffff;
}

.token-card:not(.active) .token-card-badge {
  background: rgba(255, 255, 255, 0.08);
  color: #94a3b8;
}


/* Jail Iron Cage Overlay & Padlock Animation */
.jail-iron-bars-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 35;
  display: none;
  justify-content: center;
  align-items: center;
}

.jail-iron-bars-overlay.active {
  display: flex;
}

.jail-iron-bars-overlay.dropping {
  display: flex;
  animation: jailGateDrop 0.65s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
}

.jail-cage-svg {
  width: 90%;
  height: 90%;
  filter: drop-shadow(0 8px 12px rgba(0, 0, 0, 0.85));
}

@keyframes jailGateDrop {
  0% {
    transform: translateY(-130%) scale(1.15);
    opacity: 0;
  }
  65% {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
  80% {
    transform: translateY(-8px) scale(1.02);
  }
  92% {
    transform: translateY(2px) scale(0.99);
  }
  100% {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
}

.jail-tile-slam-shake {
  animation: jailTileShake 0.4s ease-out;
}

@keyframes jailTileShake {
  0% { transform: scale(1); }
  25% { transform: scale(1.04) rotate(1.2deg); }
  50% { transform: scale(0.98) rotate(-1.2deg); }
  75% { transform: scale(1.02) rotate(0.6deg); }
  100% { transform: scale(1); }
}

/* Rules Modal Tabs */
.rules-tabs-bar {
  display: flex;
  gap: 8px;
  background: rgba(15, 23, 42, 0.8);
  padding: 6px;
  border-radius: 10px;
  margin-bottom: 14px;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.rules-tab-btn {
  flex: 1;
  padding: 10px 12px;
  font-size: 13.5px;
  font-weight: 800;
  border-radius: 8px;
  border: 1.5px solid transparent;
  background: transparent;
  color: #94a3b8;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
}

.rules-tab-btn:hover {
  color: #f8fafc;
  background: rgba(255, 255, 255, 0.05);
}

.rules-tab-btn.active {
  background: rgba(245, 158, 11, 0.2);
  border-color: #f59e0b;
  color: #fbbf24;
  box-shadow: 0 4px 12px rgba(245, 158, 11, 0.2);
}

.rules-tab-content {
  display: none;
}

.rules-tab-content.active {
  display: block;
}

/* Token Player Tabs */
.token-player-tabs {
  display: flex;
  gap: 8px;
  background: rgba(15, 23, 42, 0.6);
  padding: 4px;
  border-radius: 10px;
  margin-bottom: 12px;
}

.token-player-tab {
  flex: 1;
  padding: 8px 12px;
  font-size: 13px;
  font-weight: 800;
  border-radius: 8px;
  border: 1px solid transparent;
  background: transparent;
  color: #94a3b8;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
}

.token-player-tab.active {
  background: rgba(16, 185, 129, 0.2);
  border-color: #10b981;
  color: #6ee7b7;
}

/* Read-Only Rules Cards */
.rule-card-readonly {
  background: rgba(15, 23, 42, 0.65);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 12px 14px;
  margin-bottom: 12px;
  transition: transform 0.15s ease;
}
.rule-card-readonly:hover {
  background: rgba(15, 23, 42, 0.9);
}
.rule-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 6px;
}
.rule-card-title {
  font-weight: 800;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.rule-card-badge {
  font-size: 11px;
  padding: 2px 8px;
  border-radius: 6px;
  font-weight: 700;
}
.rule-card-body {
  font-size: 12.5px;
  line-height: 1.7;
  color: #cbd5e1;
}
.rule-card-body b {
  color: #f8fafc;
}
"""

MATTE_PHYSICAL_CSS += "\n" + I18N_CSS

full_matte_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>بنك الحظ 3D - رقعة اللعب الحقيقية الفاخرة (نزال لاعبين 1 ضد 1)</title>
  <style>
{MATTE_PHYSICAL_CSS}
  /* Setup Modal & Form Controls */
.modal-setup-box {{
  width: min(580px, 94vw);
  background: linear-gradient(180deg, #2b170e 0%, #1a0d07 100%);
  border: 2px solid #b45309;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.9), 0 0 25px rgba(245, 158, 11, 0.25);
}}

.setup-modal-body {{
  display: flex;
  flex-direction: column;
  gap: 16px;
  text-align: right;
  direction: rtl;
  padding: 10px 4px;
}}

.setup-group {{
  display: flex;
  flex-direction: column;
  gap: 8px;
}}

.setup-label {{
  font-size: 13px;
  font-weight: 800;
  color: #fef08a;
  display: flex;
  align-items: center;
  gap: 6px;
}}

.setup-pill-group {{
  display: flex;
  gap: 8px;
  width: 100%;
}}

.setup-pill {{
  flex: 1;
  background: #190e09;
  border: 1.5px solid #4a2c1a;
  border-radius: 12px;
  padding: 10px 8px;
  color: #cbd5e1;
  font-family: inherit;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 3px;
  transition: all 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
}}

.setup-pill:hover {{
  border-color: #f59e0b;
  transform: translateY(-2px);
  background: #25140c;
}}

.setup-pill.active {{
  background: linear-gradient(135deg, #78350f 0%, #b45309 100%);
  border-color: #fef08a;
  color: #ffffff;
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.35);
  transform: translateY(-2px);
}}

.setup-pill-icon {{
  font-size: 20px;
}}

.setup-pill-title {{
  font-size: 13px;
  font-weight: 800;
  color: inherit;
}}

.setup-pill-sub {{
  font-size: 10px;
  color: #94a3b8;
  font-weight: 600;
}}

.setup-pill.active .setup-pill-sub {{
  color: #fef08a;
}}

.setup-inputs-row {{
  display: flex;
  gap: 10px;
  width: 100%;
}}

.setup-input-wrap {{
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 5px;
}}

.setup-input-prefix {{
  font-size: 11px;
  font-weight: 800;
  color: #cbd5e1;
}}

.setup-input {{
  background: #150c07;
  border: 1.5px solid #57331e;
  border-radius: 10px;
  padding: 10px 12px;
  color: #ffffff;
  font-family: inherit;
  font-size: 14px;
  font-weight: 700;
  outline: none;
  direction: rtl;
  transition: all 0.2s;
}}

.setup-input:focus {{
  border-color: #f59e0b;
  box-shadow: 0 0 10px rgba(245, 158, 11, 0.3);
  background: #1f110a;
}}

.setup-input:read-only {{
  background: #100805;
  color: #94a3b8;
  border-color: #3b2214;
  cursor: not-allowed;
}}

.duel-human-pill {{
  font-size: 10px;
  background: #065f46;
  color: #a7f3d0;
  padding: 2px 7px;
  border-radius: 10px;
  font-weight: 800;
  border: 1px solid #10b981;
}}

@media (max-width: 520px) {{
  .setup-inputs-row {{
    flex-direction: column;
  }}
  .setup-pill-group {{
    flex-wrap: wrap;
  }}
  .setup-pill {{
    min-width: calc(50% - 4px);
  }}
}}


/* Lime & Golden Eiffel Tower Buildings on Tiles */
.tile-buildings-3d {{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 26px;
  position: absolute;
  top: 13px;
  z-index: 10;
  pointer-events: none;
}}

.building-lime-3d {{
  width: 28px;
  height: 28px;
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.7));
  animation: pop-bounce 0.4s cubic-bezier(0.2, 0.8, 0.2, 1.2);
}}

.building-lime-3d svg {{
  width: 100%;
  height: 100%;
}}

.building-eiffel-3d {{
  width: 32px;
  height: 36px;
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.85));
  animation: pop-bounce 0.5s cubic-bezier(0.2, 0.8, 0.2, 1.2);
}}

.building-eiffel-3d svg {{
  width: 100%;
  height: 100%;
}}

/* Construction Panel in Deed Modal */
.deed-construction-panel {{
  margin-top: 12px;
  background: #180e08;
  border: 1.5px solid #57331e;
  border-radius: 12px;
  padding: 12px 14px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  text-align: right;
  direction: rtl;
}}

.deed-group-header {{
  font-size: 12px;
  font-weight: 800;
  color: #fef08a;
  display: flex;
  align-items: center;
  justify-content: space-between;
}}

.deed-group-chips {{
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}}

.group-tile-chip {{
  background: #25140c;
  border: 1px solid #78350f;
  border-radius: 8px;
  padding: 4px 8px;
  font-size: 11px;
  font-weight: 700;
  color: #e2e8f0;
  display: flex;
  align-items: center;
  gap: 4px;
}}

.group-tile-chip.active {{
  border-color: #84cc16;
  background: rgba(132, 204, 22, 0.18);
  color: #bef264;
}}

.deed-action-btn-row {{
  display: flex;
  gap: 8px;
  width: 100%;
  margin-top: 4px;
}}

.btn-lime-build {{
  flex: 1;
  background: linear-gradient(180deg, #84cc16 0%, #65a30d 50%, #365314 100%) !important;
  border: 2px solid #bef264 !important;
  color: #ffffff !important;
  font-weight: 800 !important;
  border-radius: 12px !important;
  padding: 10px 14px !important;
  box-shadow: 0 4px 12px rgba(132, 204, 22, 0.4) !important;
  cursor: pointer;
  transition: all 0.2s;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  font-family: inherit;
}}

.btn-lime-build:hover:not(:disabled) {{
  filter: brightness(1.15);
  transform: translateY(-2px);
}}

.btn-lime-build.gold-tower {{
  background: linear-gradient(180deg, #fef08a 0%, #f59e0b 50%, #92400e 100%) !important;
  border-color: #fef08a !important;
  color: #ffffff !important;
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.5) !important;
}}

.btn-lime-build:disabled {{
  opacity: 0.55;
  cursor: not-allowed;
  filter: grayscale(0.5);
}}

.btn-demolish {{
  flex: 1;
  background: linear-gradient(180deg, #ef4444 0%, #b91c1c 50%, #7f1d1d 100%) !important;
  border: 1.5px solid #fca5a5 !important;
  color: #ffffff !important;
  font-weight: 800 !important;
  border-radius: 12px !important;
  padding: 10px 14px !important;
  cursor: pointer;
  transition: all 0.2s;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  font-family: inherit;
}}

.btn-demolish:hover:not(:disabled) {{
  filter: brightness(1.15);
  transform: translateY(-2px);
}}

.btn-demolish:disabled {{
  opacity: 0.5;
  cursor: not-allowed;
}}

.construction-reason-hint {{
  font-size: 11px;
  color: #fef08a;
  line-height: 1.5;
  background: rgba(120, 53, 15, 0.35);
  padding: 6px 10px;
  border-radius: 8px;
  border-right: 3px solid #f59e0b;
}}


/* Trade & Negotiation Modal Styles */
.modal-trade-box {{
  width: min(840px, 96vw);
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  background: linear-gradient(180deg, #2b170e 0%, #150a05 100%);
  border: 2px solid #b45309;
  box-shadow: 0 12px 50px rgba(0, 0, 0, 0.95), 0 0 30px rgba(245, 158, 11, 0.25);
  overflow-y: auto;
}}

.trade-modal-body {{
  display: flex;
  flex-direction: column;
  gap: 14px;
  direction: rtl;
  text-align: right;
  padding: 8px 4px;
}}

.trade-columns-container {{
  display: flex;
  gap: 12px;
  align-items: stretch;
}}

.trade-column {{
  flex: 1;
  background: #1c0f08;
  border: 1.5px solid #4a2c1a;
  border-radius: 14px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}}

.trade-col-header {{
  display: flex;
  align-items: center;
  gap: 10px;
  padding-bottom: 8px;
  border-bottom: 1px solid #3d2315;
}}

.trade-col-avatar {{
  font-size: 24px;
  width: 42px;
  height: 42px;
  background: #2b170e;
  border: 1.5px solid #b45309;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}}

.trade-col-info {{
  display: flex;
  flex-direction: column;
}}

.trade-col-title {{
  font-size: 13px;
  font-weight: 800;
  color: #fef08a;
}}

.trade-col-balance {{
  font-size: 11px;
  color: #94a3b8;
  font-weight: 700;
}}

.trade-field-group {{
  display: flex;
  flex-direction: column;
  gap: 6px;
}}

.trade-field-label {{
  font-size: 11px;
  font-weight: 800;
  color: #cbd5e1;
}}

.trade-cash-input-row {{
  display: flex;
  align-items: center;
  gap: 8px;
}}

.trade-cash-input {{
  flex: 1;
  background: #140a05;
  border: 1.5px solid #57331e;
  border-radius: 8px;
  padding: 8px 12px;
  color: #fef08a;
  font-family: inherit;
  font-size: 14px;
  font-weight: 800;
  outline: none;
  direction: ltr;
  text-align: right;
}}

.trade-cash-input:focus {{
  border-color: #f59e0b;
}}

.trade-cash-unit {{
  font-size: 12px;
  color: #f59e0b;
  font-weight: 800;
}}

.trade-props-list {{
  display: flex;
  flex-direction: column;
  gap: 5px;
  max-height: 180px;
  overflow-y: auto;
  padding-left: 4px;
  scrollbar-width: thin;
}}

.trade-prop-item {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #25140c;
  border: 1px solid #4a2b18;
  border-radius: 8px;
  padding: 6px 10px;
  cursor: pointer;
  transition: all 0.15s;
  user-select: none;
}}

.trade-prop-item:hover {{
  background: #311b10;
  border-color: #f59e0b;
}}

.trade-prop-item.selected {{
  background: rgba(245, 158, 11, 0.22);
  border-color: #f59e0b;
  box-shadow: 0 0 8px rgba(245, 158, 11, 0.3);
}}

.trade-prop-right {{
  display: flex;
  align-items: center;
  gap: 8px;
}}

.trade-prop-color-bar {{
  width: 6px;
  height: 20px;
  border-radius: 3px;
}}

.trade-prop-name {{
  font-size: 12px;
  font-weight: 800;
  color: #fdfbf7;
}}

.trade-prop-price {{
  font-size: 11px;
  font-weight: 700;
  color: #fef08a;
}}

.trade-empty-props {{
  font-size: 11px;
  color: #94a3b8;
  text-align: center;
  padding: 16px 8px;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  font-style: italic;
}}

.trade-center-divider {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  width: 40px;
}}

.trade-arrows-badge {{
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #78350f;
  border: 2px solid #fef08a;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  font-weight: 900;
  box-shadow: 0 0 12px rgba(245, 158, 11, 0.4);
}}

.trade-exchange-label {{
  font-size: 10px;
  font-weight: 800;
  color: #fef08a;
}}

.trade-valuation-bar {{
  background: #160b06;
  border: 1px solid #78350f;
  border-radius: 12px;
  padding: 10px 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
}}

.trade-val-item {{
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
}}

.trade-val-lbl {{
  color: #cbd5e1;
  font-weight: 700;
}}

.trade-val-num {{
  font-weight: 800;
  color: #fef08a;
}}

.trade-val-status {{
  font-size: 11px;
  font-weight: 700;
  color: #fbbf24;
}}

.trade-footer-actions {{
  display: flex;
  gap: 12px;
  margin-top: 4px;
}}

.btn-submit-trade {{
  flex: 2;
  font-size: 16px;
  padding: 12px;
  border-radius: 12px;
}}

.trade-deal-card-box {{
  background: #190e09;
  border: 1px solid #78350f;
  border-radius: 10px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}}

.trade-deal-side-title {{
  font-size: 12px;
  font-weight: 800;
  color: #fef08a;
}}

.trade-deal-item {{
  font-size: 12px;
  color: #e2e8f0;
  padding: 3px 0;
}}

@media (max-width: 680px) {{
  .trade-columns-container {{
    flex-direction: column;
  }}
  .trade-center-divider {{
    width: 100%;
    flex-direction: row;
  }}
}}


/* Direct Property Buyout Negotiation Modal */
.modal-buyout-box {{
  width: min(580px, 94vw);
  background: linear-gradient(180deg, #2a160d 0%, #150904 100%);
  border: 2px solid #f59e0b;
  box-shadow: 0 12px 50px rgba(0, 0, 0, 0.95), 0 0 25px rgba(245, 158, 11, 0.3);
}}

.buyout-modal-body {{
  display: flex;
  flex-direction: column;
  gap: 14px;
  direction: rtl;
  text-align: right;
  padding: 10px 4px;
}}

.buyout-prop-card {{
  background: #1c0f08;
  border: 1.5px solid #57331e;
  border-radius: 12px;
  padding: 12px 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}}

.buyout-prop-info {{
  display: flex;
  align-items: center;
  gap: 10px;
}}

.buyout-prop-stripe {{
  width: 8px;
  height: 38px;
  border-radius: 4px;
}}

.buyout-prop-title {{
  font-size: 15px;
  font-weight: 800;
  color: #fdfbf7;
}}

.buyout-prop-sub {{
  font-size: 11px;
  color: #94a3b8;
  margin-top: 2px;
}}

.buyout-feedback-box {{
  background: rgba(185, 28, 28, 0.28);
  border: 1.5px solid #ef4444;
  border-radius: 10px;
  padding: 10px 14px;
  color: #fef08a;
  font-size: 12px;
  line-height: 1.5;
  animation: pop-bounce 0.35s cubic-bezier(0.2, 0.8, 0.2, 1.2);
}}

.buyout-feedback-box.success {{
  background: rgba(16, 185, 129, 0.25);
  border-color: #10b981;
  color: #a7f3d0;
}}

.buyout-price-control-box {{
  background: #180e08;
  border: 1.5px solid #4a2c1a;
  border-radius: 12px;
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}}

.buyout-quick-btns-row {{
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}}

.btn-quick-price {{
  flex: 1;
  background: #25140c;
  border: 1px solid #78350f;
  border-radius: 8px;
  padding: 7px 10px;
  font-size: 12px;
  font-weight: 800;
  color: #fef08a;
  cursor: pointer;
  transition: all 0.15s;
  font-family: inherit;
}}

.btn-quick-price:hover {{
  background: #78350f;
  color: #ffffff;
  border-color: #f59e0b;
}}

</style>
</head>
<body>

  <!-- Confetti Canvas -->
  <canvas id="confettiCanvas"></canvas>

  <!-- Top App Navigation Header -->
  <header class="app-header">
    <div class="brand-title">
      <div class="brand-logo-icon">🎲</div>
      <div class="brand-text">
        <h1>بنك الحظ <span class="brand-badge">رقعة اللعب الحقيقية 3D</span></h1>
      </div>
    </div>

    <div class="header-actions">



      <button class="btn-matte" id="btnOpenTrade">
        <span>🤝</span>
        <span id="btnTradeText">مفاوضة وتبادل</span>
      </button>

      <button class="btn-matte" id="btnOpenRules">
        <span>📜</span>
        <span id="btnRulesText">القواعد</span>
      </button>
      <button class="btn-matte" id="btnOpenSettings" title="الإعدادات">
        <span>⚙️</span>
        <span id="btnSettingsNavText">الإعدادات</span>
      </button>
      <button class="btn-matte" id="btnToggleSound" title="كتم / تشغيل الصوت">
        <span id="soundIcon">🔊</span>
      </button>
      <button class="btn-matte crimson" id="btnResetGame" title="لعبة جديدة">
        <span>🔄</span>
      </button>
    </div>
  </header>

  <!-- Head-to-Head 2-Player Clash Bar -->
  <section class="versus-clash-bar">
    
    <!-- Player 1 Card -->
    <div class="player-duel-card p1" id="cardP1">
      <div class="duel-avatar-3d" id="avatarP1Box" title="اللاعب 1"></div>
      <div class="duel-info-col">
        <div class="duel-name-row">
          <span class="duel-name" id="nameP1Display">مستر حظ</span>
          <span style="font-size: 10px; color: #ef4444; font-weight: 800;" id="subP1Display">(أنت)</span>
        </div>
        <div class="duel-money" id="moneyP1Display">6000 $</div>
        <div class="duel-net-worth" id="netWorthP1Display">الثروة: 6000 $</div>
        <div class="duel-shields-row" id="shieldsP1Row">
          <span class="shield-3d-badge active">🛡️</span>
          <span class="shield-3d-badge active">🛡️</span>
          <span class="shield-3d-badge active">🛡️</span>
        </div>
      </div>
    </div>

    <!-- Center VS Emblem -->
    <div class="versus-center-emblem">
      <div class="vs-icon-badge">VS</div>
      <div class="versus-sub-label">مواجهة ثنائية</div>
    </div>

    <!-- Player 2 Card -->
    <div class="player-duel-card p2" id="cardP2">
      <div class="duel-avatar-3d" id="avatarP2Box" title="المنافس"></div>
      <div class="duel-info-col">
        <div class="duel-name-row">
          <span class="duel-name" id="nameP2Display">روبوت</span>
          <span class="duel-bot-pill" id="badgeP2Display">روبوت 🤖 (متوسط)</span>
        </div>
        <div class="duel-money" id="moneyP2Display">6000 $</div>
        <div class="duel-net-worth" id="netWorthP2Display">الثروة: 6000 $</div>
        <div class="duel-shields-row" id="shieldsP2Row">
          <span class="shield-3d-badge active">🛡️</span>
          <span class="shield-3d-badge active">🛡️</span>
          <span class="shield-3d-badge active">🛡️</span>
        </div>
      </div>
    </div>

  </section>

  <!-- Main Game Viewport -->
  <main class="game-viewport">
    
    <!-- 3D Perspective Wrapper -->
    <div class="board-container">
      <div class="board-perspective-wrapper" id="boardWrapper">
        <div class="board-grid" id="boardGrid">
          
          <!-- Board Center Stage: Inset Emerald Green Baize Felt Tray -->
          <div class="board-center">
            
            <div class="center-top-row">
              <div class="free-parking-pot" title="حصيلة وعاء الاستراحة المجانية">
                <span class="pot-icon">🏺</span>
                <div>
                  <div style="font-size: 9px; color: #cbd5e1;" id="potLabelText">وعاء الاستراحة</div>
                  <div class="pot-amount" id="potAmountDisplay">200 $</div>
                </div>
              </div>

              <div class="board-title-emblem">
                <div class="emblem-title" id="boardTitleText">بنك الحظ</div>
                <div class="emblem-sub" id="boardCityLabel">عواصم عربية • رقعة كلاسيكية 🌟</div>
              </div>

              <div class="free-parking-pot" style="border-color: #38bdf8;">
                <span class="pot-icon">⚡</span>
                <div>
                  <div style="font-size: 9px; color: #cbd5e1;" id="energyLabelText">طاقة النرد</div>
                  <div class="pot-amount" style="color: #38bdf8;" id="rollsLeftDisplay">50</div>
                </div>
              </div>
            </div>

            <!-- 3D Cairo Skyline Animated Diorama & In-Board Event Cards -->
            <div class="center-diorama-container" id="centerDioramaBox">
              <!-- Layer 1: Pyramids Skyline Diorama -->
              <div class="diorama-pyramids-layer" id="dioramaPyramidsLayer"></div>
              <!-- Layer 2: 3D In-Board Event Card (Appears in place of Pyramids) -->
              <div class="diorama-card-layer hidden" id="dioramaCardLayer">
                <div class="diorama-card-inner" id="dioramaCardInner">
                  <div class="diorama-card-art-col">
                    <div class="diorama-card-art-3d" id="dioramaCard3DArt"></div>
                  </div>
                  <div class="diorama-card-content-col">
                    <div class="diorama-card-badge-row">
                      <span class="diorama-card-badge" id="dioramaCardBadge">🎁 صندوق الدنيا</span>
                      <span class="diorama-card-player-tag" id="dioramaCardPlayerTag">مستر حظ</span>
                    </div>
                    <div class="diorama-card-title" id="dioramaCardTitle">عنوان الكارت</div>
                    <div class="diorama-card-desc" id="dioramaCardDesc">شروط ونتائج الكارت تظهر هنا بوضوح</div>
                  </div>
                  <div class="diorama-card-action-col">
                    <button class="btn-matte diorama-card-btn" id="dioramaCardBtn">
                      <span id="dioramaCardBtnText">تنفيذ الكارت</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- 3D Rolling Dice Stage on Green Felt -->
            <div class="dice-arena" id="diceArena">
              <!-- 3D Die 1 (Mr. Hazz - Crimson Pips) -->
              <div class="dice-cube" id="die1">
                <div class="dice-face face-1"><div class="dice-pip" style="grid-area: 2/2;"></div></div>
                <div class="dice-face face-2"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-3"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 2/2;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-4"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-5"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 2/2;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-6"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 2/1;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 2/3;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
              </div>

              <!-- 3D Die 2 (Cleopatra - Navy Pips) -->
              <div class="dice-cube" id="die2">
                <div class="dice-face face-1"><div class="dice-pip" style="grid-area: 2/2;"></div></div>
                <div class="dice-face face-2"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-3"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 2/2;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-4"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-5"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 2/2;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
                <div class="dice-face face-6"><div class="dice-pip" style="grid-area: 1/1;"></div><div class="dice-pip" style="grid-area: 2/1;"></div><div class="dice-pip" style="grid-area: 3/1;"></div><div class="dice-pip" style="grid-area: 1/3;"></div><div class="dice-pip" style="grid-area: 2/3;"></div><div class="dice-pip" style="grid-area: 3/3;"></div></div>
              </div>
            </div>

            <!-- Controls and Roll Section -->
            <div class="center-controls-row">
              
              <!-- Multiplier Selector -->

              <!-- Main Roll Button -->
              <button class="btn-big-roll" id="btnRollDice">
                <span>🎲</span>
                <span id="btnRollDiceText">ارمي النرد!</span>
              </button>

              <!-- Turn Banner -->
              <div class="turn-status-banner" id="turnStatusBanner">
                <span id="turnAvatarSpan">🎩</span>
                <span id="turnStatusText">دور مستر حظ... اضغط لرمي النرد!</span>
              </div>

            </div>

          </div>
          <!-- End Board Center -->

        </div>
      </div>
    </div>

    <!-- Sidebar Activity Log -->
    <aside class="game-sidebar">
      <div class="sidebar-header">
        <div class="sidebar-title">
          <span>📜</span>
          <span id="activityLogTitle">سجل الأحداث المباشر</span>
        </div>
        <button class="btn-matte" style="padding: 4px 8px; font-size: 11px;" id="btnClearLog">مسح</button>
      </div>
      <div class="sidebar-content" id="activityLog"></div>
    </aside>

  </main>

  <!-- MODAL 1: Property Deed Card Modal with Large 3D Display -->
  <div class="modal-overlay" id="modalDeed">
    <div class="modal-box">
      <div class="modal-header">
        <div class="modal-title">
          <span>🏠</span>
          <span>سند ملكية العقار (بطاقة حقيقية)</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalDeed')">✕</button>
      </div>
      <div class="modal-body" id="deedModalBody"></div>
      <div class="modal-footer" id="deedModalFooter"></div>
    </div>
  </div>

  <!-- MODAL 2: Chance & Community Chest Card Modal -->
  <div class="modal-overlay" id="modalCard">
    <div class="modal-box" style="text-align: center;">
      <div class="modal-header">
        <div class="modal-title" id="cardModalCategory">
          <span>❓</span>
          <span>كارت الحظ</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalCard')">✕</button>
      </div>
      <div class="modal-body" style="align-items: center;">
        <div style="width: 120px; height: 120px; margin-bottom: 8px;" id="cardModal3DArt"></div>
        <h2 style="font-size: 20px; color: #fef08a; margin-bottom: 8px;" id="cardModalTitle">عنوان الكارت</h2>
        <p style="font-size: 14px; color: #f8fafc; line-height: 1.6;" id="cardModalDesc">وصف وتأثير الكارت...</p>
      </div>
      <div class="modal-footer" style="justify-content: center;">
        <button class="btn-matte gold" id="btnExecuteCardAction" style="padding: 10px 28px; font-size: 15px;">
          <span>تنفيذ الأمر</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 3: Bank Heist Mini-Game (Direct Rival Heist) -->
  <div class="modal-overlay" id="modalHeist">
    <div class="modal-box" style="width: min(560px, 95vw);">
      <div class="modal-header">
        <div class="modal-title">
          <span>🏦</span>
          <span>السطو على خزنة الخصم (Bank Heist)</span>
        </div>
      </div>
      <div class="modal-body heist-container">
        <p style="text-align: center; font-size: 13px; color: #cbd5e1;" id="heistTargetText">
          أنت الآن تقتحم خزينة منافسك! افتح الأبواب وطابق 3 عناصر لتحديد غنيمتك!
        </p>

        <div class="heist-match-tracker">
          <div class="match-item">
            <span style="font-size: 18px;">🪙 فضة</span>
            <div class="match-icons" id="trackerSilver">
              <div class="match-slot"></div><div class="match-slot"></div><div class="match-slot"></div>
            </div>
            <span style="font-size: 10px; color: #94a3b8;">سرقة صغيرة</span>
          </div>
          <div class="match-item">
            <span style="font-size: 18px;">💰 أكياس</span>
            <div class="match-icons" id="trackerCash">
              <div class="match-slot"></div><div class="match-slot"></div><div class="match-slot"></div>
            </div>
            <span style="font-size: 10px; color: #fbbf24;">سرقة كبيرة</span>
          </div>
          <div class="match-item">
            <span style="font-size: 18px;">💎 ماس</span>
            <div class="match-icons" id="trackerDiamond">
              <div class="match-slot"></div><div class="match-slot"></div><div class="match-slot"></div>
            </div>
            <span style="font-size: 10px; color: #38bdf8;">إفلاس البنك!</span>
          </div>
        </div>

        <div class="heist-vault-grid" id="heistVaultGrid"></div>
        <div id="heistResultBanner" style="font-size: 16px; font-weight: 900; color: #fbbf24; text-align: center; min-height: 24px;"></div>
      </div>
      <div class="modal-footer" style="justify-content: center;">
        <button class="btn-matte gold" id="btnCollectHeist" style="display: none; padding: 10px 24px;">
          <span>استلام الغنائم 💰</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 4: Landmark Shutdown Mini-Game (Direct Rival Mallet Smash) -->
  <div class="modal-overlay" id="modalShutdown">
    <div class="modal-box">
      <div class="modal-header">
        <div class="modal-title">
          <span>🔨</span>
          <span>الهجوم والتعطيل على معالم الخصم (Shutdown)</span>
        </div>
      </div>
      <div class="modal-body shutdown-stage">
        <p style="text-align: center; font-size: 13px; color: #cbd5e1;" id="shutdownSubtext">
          استهدف معالم منافسك بالمطرقة الكرتونية! هل يمتلك درعاً لصد الهجوم؟
        </p>

        <div class="target-landmark-box" id="targetLandmarkBox">
          <div class="target-crosshair"></div>
          <div class="target-landmark-icon" id="targetLandmarkIcon" style="width: 120px; height: 120px;"></div>
          <div style="font-size: 15px; font-weight: 800; margin-top: 8px; color: #fef08a;" id="targetLandmarkName">
            برج القاهرة للخصم
          </div>
        </div>

        <div id="shutdownResultText" style="font-size: 16px; font-weight: 900; text-align: center; min-height: 30px;"></div>
      </div>
      <div class="modal-footer" style="justify-content: center;">
        <button class="btn-matte crimson" id="btnLaunchShutdown" style="padding: 10px 30px; font-size: 16px;">
          <span>💥 أطلق الهجوم!</span>
        </button>
        <button class="btn-matte gold" id="btnFinishShutdown" style="display: none; padding: 10px 24px;">
          <span>تم الاستيلاء على الجائزة</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 5: City Landmarks Construction -->
  <div class="modal-overlay" id="modalLandmarks">
    <div class="modal-box" style="width: min(600px, 95vw);">
      <div class="modal-header">
        <div class="modal-title">
          <span>🏛️</span>
          <span>معالم المدينة (ترقية وبناء اللوحة ثلاثية الأبعاد)</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalLandmarks')">✕</button>
      </div>
      <div class="modal-body">
        <div style="background: rgba(18, 10, 6, 0.8); padding: 10px; border-radius: 12px; margin-bottom: 6px;">
          <div style="display: flex; justify-content: space-between; font-size: 13px; font-weight: 800; margin-bottom: 4px;">
            <span style="color: #fef08a;">إتمام لوحة القاهرة التاريخية</span>
            <span id="boardProgressText">0 / 25 نجمة</span>
          </div>
          <div style="width: 100%; height: 8px; background: #334155; border-radius: 4px; overflow: hidden;">
            <div id="boardProgressBar" style="width: 0%; height: 100%; background: linear-gradient(90deg, #d97706, #10b981); transition: width 0.4s;"></div>
          </div>
        </div>

        <div class="landmarks-list" id="landmarksListContainer"></div>
      </div>
      <div class="modal-footer">
        <button class="btn-matte" onclick="closeModal('modalLandmarks')">إغلاق</button>
      </div>
    </div>
  </div>

  <!-- MODAL 6: Wheel of Fortune & Risk Modal -->
  <div class="modal-overlay" id="modalWheel">
    <div class="modal-box" style="width: min(440px, 94vw); text-align: center;">
      <div class="modal-header">
        <div class="modal-title">
          <span>🎡</span>
          <span id="wheelModalTitleText">عجلة الحظ والمجازفة (ربح وخسارة)</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalWheel')">✕</button>
      </div>
      <div class="modal-body wheel-container">
        <div id="wheelSubText" style="font-size: 13px; color: #fde047; font-weight: 700; margin-bottom: 8px;">
          عجلة الحظ قد تنفع وقد تضر! أدر العجلة واكتشف مصيرك...
        </div>
        <div style="position: relative; display: flex; justify-content: center; align-items: center;">
          <div class="wheel-pointer"></div>
          <canvas id="wheelCanvas" width="280" height="280" class="wheel-canvas"></canvas>
        </div>
        <div id="wheelResultDisplay" style="font-size: 14.5px; font-weight: 900; color: #fef08a; min-height: 48px; margin-top: 10px; padding: 8px 12px; border-radius: 10px; background: rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: center; border: 1px solid rgba(245, 158, 11, 0.3);">
          أدر العجلة لتكتشف نصيبك بين الربح والخسارة!
        </div>
      </div>
      <div class="modal-footer" style="justify-content: center;">
        <button class="btn-matte gold" id="btnSpinWheel" style="padding: 12px 36px; font-size: 16px; border-radius: 14px;">
          <span id="btnSpinWheelText">🌀 تدوير العجلة الآن!</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 7: Complete Game Rules & Guide -->
  <div class="modal-overlay" id="modalRules">
    <div class="modal-box" style="width: min(680px, 95vw); max-height: 85vh; display: flex; flex-direction: column;">
      <div class="modal-header">
        <div class="modal-title">
          <span>📜</span>
          <span id="rulesModalHeaderTitle">دليل وقواعد بنك الحظ & شروط الكروت</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalRules')">&times;</button>
      </div>

      <!-- Navigation Tabs inside Rules Modal -->
      <div style="padding: 10px 16px 0 16px;">
        <div class="rules-tabs-bar">
          <button type="button" class="rules-tab-btn active" id="tabRulesBtnGeneral" onclick="switchRulesTab('general')">
            <span>📜</span>
            <span id="tabRulesTitleGeneral">قواعد اللعبة العامة</span>
          </button>
          <button type="button" class="rules-tab-btn" id="tabRulesBtnCards" onclick="switchRulesTab('cards')">
            <span>🃏</span>
            <span id="tabRulesTitleCards">قائمة شروط الكروت</span>
          </button>
        </div>
      </div>

      <div class="modal-body" style="font-size: 13px; line-height: 1.8; color: #fdfbf7; overflow-y: auto; flex: 1; padding: 12px 18px;">
        
        <!-- Tab 1: General Rules -->
        <div class="rules-tab-content active" id="rulesContentGeneral">
          <h3 style="color: #fef08a; margin-bottom: 6px;">⚔️ نظام المواجهة الثنائية (1 ضد 1):</h3>
          <ul style="padding-right: 20px; margin-bottom: 14px;">
            <li><b>المواجهة المباشرة:</b> مواجهة سريعة ومثيرة! كل رمية نرد وكل عقار تشتريه يقلص خيارات خصمك.</li>
            <li><b>شراء المدن وتأسيس الطوابق:</b> بعد امتلاك كامل مدن المجموعة اللونية يمكنك بناء طوابق ليمونية (من 1 إلى 4) بقيمة 33% من سعر العقار، وعند اكتمال 4 طوابق في المجموعة يُتاح بناء برج إيفل الذهبي (الطابق الخامس) لرفع الأرباح بنسبة 50% لكل طابق!</li>
            <li><b>المفاوضة والتبادل:</b> يمكنك في أي وقت بدء مفاوضة لشراء عقارات خصمك أو تبادل الأراضي والمساومة على الأسعار بالدولار ($).</li>
          </ul>

          <h3 style="color: #38bdf8; margin-bottom: 6px;">🎲 قواعد الرقعة الكلاسيكية (40 مربعاً):</h3>
          <ul style="padding-right: 20px; margin-bottom: 14px;">
            <li><b>نقطة البداية (انطلق):</b> مر أو اهبط عليها لتقبض 200 $.</li>
            <li><b>محطات القطار والمرافق:</b> 4 محطات قطار يتضاعف إيجارها مع كثرة الامتلاك، وشركتا الكهرباء والمياه تعتمدان على ضرب ناتج النرد.</li>
            <li><b>الاستراحة المجانية:</b> تجمع كل ضرائب اللاعبين وغرامات الرادار، ومن يقف عليها يفوز بالحصيلة كاملة!</li>
            <li><b>سجن القلعة:</b> يدخله اللاعب عند مربع ادخل السجن أو كروت الحظ أو رمي دبل 3 مرات متتالية.</li>
          </ul>
        </div>

        <!-- Tab 2: Read-Only Cards List -->
        <div class="rules-tab-content" id="rulesContentCards">
          <div style="background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.35); border-radius: 8px; padding: 10px 14px; margin-bottom: 14px; font-size: 12.5px; color: #fde68a; text-align: center;">
            ℹ️ <b>قائمة شروط الكروت والخانات الخاصة:</b><br>
            هذه الشروط غير تفاعلية هنا، وتُنفّذ تلقائياً أثناء اللعب عند هبوط البيدق على خانتها المخصصة:
          </div>

          <h4 style="color: #fbbf24; margin: 12px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>🎁</span> <span>كروت صندوق الدنيا (محفظة الشعب - الخانات: 2، 17، 33)</span>
          </h4>
          <div class="rule-card-readonly" style="border-right: 4px solid #f59e0b;">
            <div class="rule-card-body">
              • <b>استرداد ضريبي من وزارة المالية:</b> مراجعة الحسابات أسفرت عن استرداد لصالحك (+100 $ فوراً من البنك).<br>
              • <b>عيد ميلادك السعيد:</b> احتفل مع منافسيك! يدفع لك المنافس هدية نقدية قدرها 25 $.<br>
              • <b>عائد استثمار قناة السويس:</b> استثمارك في شهادات الاستثمار حقق أرباحاً (+200 $).<br>
              • <b>تذكرة خروج مجاني من السجن:</b> احتفظ بهذا الكارت لاستخدامه فوراً عند صدور أي أمر بالحبس.<br>
              • <b>تكاليف الفحص الطبي:</b> سداد تكاليف الفحوصات الطورية (-50 $ تودع بوعاء الاستراحة).<br>
              • <b>بيع أسهم استثمارية:</b> بيع جزء من المحفظة المالية (+50 $).<br>
              • <b>قسط التأمين الصحي:</b> سداد القسط السنوي للرعاية (-50 $ تودع بوعاء الاستراحة).<br>
              • <b>مكافأة تفوق استثماري:</b> جائزة التميز المالي (+100 $ من البنك).<br>
              • <b>أرباح استشارات تجارية:</b> أتعاب تقديم خدمات استشارية (+25 $).<br>
              • <b>تسوية فواتير مرافق عامة:</b> سداد فواتير الاستهلاك العام (-50 $ لوعاء الاستراحة).
            </div>
          </div>

          <h4 style="color: #fdba74; margin: 14px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>❓</span> <span>كروت الحظ (المجازفة والأقدار - الخانات: 7، 22، 36)</span>
          </h4>
          <div class="rule-card-readonly" style="border-right: 4px solid #f97316;">
            <div class="rule-card-body">
              • <b>عملية سطو على البنك (Bank Heist):</b> اقتحام خزينة المنافس ونهب أموال طائلة نقداً!<br>
              • <b>هجوم المطرقة والتعطيل (Shutdown):</b> ضرب معالم الخصم الكرتونية لهدمها، وتخطي دروعه الدفاعية!<br>
              • <b>تقدم إلى نقطة البداية (انطلق):</b> تحرك فوراً إلى مربع انطلق واستلم مكافأة 200 $.<br>
              • <b>رحلة إلى قلب العاصمة (القاهرة):</b> تقدم فوراً لعقار القاهرة (شراء إن كان متاحاً أو دفع الإيجار).<br>
              • <b>أرباح استثمارية في البورصة:</b> مكاسب مضاربة في الأسهم (+150 $ نقداً).<br>
              • <b>غرامة تجاوز السرعة:</b> القيادة بسرعة زائدة (-50 $ تودع بوعاء الاستراحة).<br>
              • <b>أعمال صيانة وترميم شاملة:</b> ادفع 25 $ عن كل طابق و 100 $ عن برج إيفل لوعاء الاستراحة.<br>
              • <b>تقدم لأقرب محطة قطار:</b> تحرك فوراً لأقرب محطة قطار (شراء أو سداد ضعف الإيجار).<br>
              • <b>رحلة سياحية إلى الإسكندرية:</b> السفر الفوري لعروس البحر الأبيض المتوسط.<br>
              • <b>عطل فني في شبكة المرافق:</b> إصلاحات طارئة في الخطوط (-50 $ لوعاء الاستراحة).<br>
              • <b>أمر قضائي فوري بالحبس:</b> اذهب فوراً إلى سجن القلعة دون أن تمر بنقطة انطلق ودون قبض 200 $.
            </div>
          </div>

          <h4 style="color: #6ee7b7; margin: 14px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>💸</span> <span>الضرائب والغرامات الحكومية السيادية</span>
          </h4>
          <div class="rule-card-readonly" style="border-right: 4px solid #10b981;">
            <div class="rule-card-body">
              • <b>ضريبة الدخل العامة (الخانة 4):</b> التزام مالي سيادي إلزامي بقيمة 200 $ يُخصم فور الوقوف على الخانة ويُحوّل بالكامل إلى <b>وعاء الاستراحة المجانية</b>.<br>
              • <b>ضريبة الرفاهية والكماليات (الخانة 38):</b> رسم فخامة بقيمة 100 $ يُخصم من رصيد اللاعب ويُودع في <b>وعاء الاستراحة المجانية</b>.
            </div>
          </div>

          <h4 style="color: #fca5a5; margin: 14px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>⛓️</span> <span>سجن القلعة (أمر الحبس الفوري vs الزيارة التفقدية)</span>
          </h4>
          <div class="rule-card-readonly" style="border-right: 4px solid #ef4444;">
            <div class="rule-card-body">
              • <b>أمر الحبس الفوري (الخانة 30):</b> ينتقل اللاعب بأسرع مسار (للأمام أو للخلف) بصافرة الشرطة، ويسقط السور الحديدي بقفل محكم. للخروج: رمي دبل نرد، استخدام تذكرة العفو، أو دفع كفالة 50 $ بعد 3 أدوار.<br>
              • <b>الزيارة التفقدية (الخانة 10):</b> الوقوف عبر حركة النرد العادية يعتبر زيارة آمنة دون حبس أو غرامات.
            </div>
          </div>

          <h4 style="color: #7dd3fc; margin: 14px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>🚗</span> <span>وعاء الاستراحة المجانية (الخانة 20)</span>
          </h4>
          <div class="rule-card-readonly" style="border-right: 4px solid #38bdf8;">
            <div class="rule-card-body">
              محطة حيادية استراتيجية لا إيجار فيها ولا ضرائب. تجمع وتراكم كافة حصائل ضرائب الدخل والرفاهية والغرامات، وأول لاعب يقف عليها يحصد كامل الأموال المتراكمة في الوعاء فوراً!
            </div>
          </div>
        </div>

      </div>
      <div class="modal-footer" style="padding: 10px 16px; border-top: 1px solid #3d2315; text-align: center;">
        <button class="btn-matte gold" onclick="closeModal('modalRules')" style="padding: 8px 28px;">فهمت القواعد! هيا لنلعب</button>
      </div>
    </div>
  </div>

  <!-- MODAL 8: Game Setup & New Game Configuration -->
  <div class="modal-overlay" id="modalNewGame">
    <div class="modal-box modal-setup-box">
      <div class="modal-header">
        <div class="modal-title">
          <span>🎲</span>
          <span id="setupModalTitleText">إعداد وبدء لعبة بنك الحظ</span>
        </div>
        <button class="modal-close-btn" id="btnCloseNewGameModal">&times;</button>
      </div>
      
      <div class="setup-modal-body">
        
        <!-- 0. Language Selection -->
        <div class="setup-group">
          <label class="setup-label" id="lblSetupLang">🌐 لغة اللعبة (Language):</label>
          <select class="setup-select" id="setupLanguageSelect">
            {lang_options_html}
          </select>
        </div>

        <!-- 1. Game Mode -->
        <div class="setup-group">
          <label class="setup-label" id="lblSetupMode">🎮 اختر نمط اللعب:</label>
          <div class="setup-pill-group" id="setupModeGroup">
            <button type="button" class="setup-pill active" data-mode="bot">
              <span class="setup-pill-icon">🤖</span>
              <span class="setup-pill-title" id="pillModeBotTitle">ضد الكمبيوتر</span>
              <span class="setup-pill-sub" id="pillModeBotSub">(لاعب 1 ضد الروبوت)</span>
            </button>
            <button type="button" class="setup-pill" data-mode="human">
              <span class="setup-pill-icon">👥</span>
              <span class="setup-pill-title" id="pillModeHumanTitle">لاعبين اثنين</span>
              <span class="setup-pill-sub" id="pillModeHumanSub">(على نفس الجهاز)</span>
            </button>
          </div>
        </div>

        <!-- 2. Player Names -->
        <div class="setup-group">
          <label class="setup-label" id="lblSetupNames">👤 أسماء اللاعبين:</label>
          <div class="setup-inputs-row">
            <div class="setup-input-wrap">
              <span class="setup-input-prefix" id="p1Prefix">🎩 اسم اللاعب 1:</span>
              <input type="text" id="setupPlayer1Name" class="setup-input" value="مستر حظ" maxlength="15" placeholder="اكتب اسم اللاعب 1">
            </div>
            <div class="setup-input-wrap">
              <span class="setup-input-prefix" id="p2Prefix">🤖 اسم المنافس:</span>
              <input type="text" id="setupPlayer2Name" class="setup-input" value="روبوت" maxlength="15" placeholder="روبوت" readonly>
            </div>
          </div>
        </div>

        <!-- 3. Starting Money -->
        <div class="setup-group">
          <label class="setup-label" id="lblSetupMoney">💰 رصيد البداية لكل لاعب:</label>
          <div class="setup-pill-group" id="setupMoneyGroup">
            <button type="button" class="setup-pill" data-money="3000">
              <span class="setup-pill-icon">💵</span>
              <span class="setup-pill-title" id="pillMoney3kTitle">3,000 $</span>
              <span class="setup-pill-sub" id="pillMoney3kSub">نزال سريع وحاسم</span>
            </button>
            <button type="button" class="setup-pill active" data-money="6000">
              <span class="setup-pill-icon">💰</span>
              <span class="setup-pill-title" id="pillMoney6kTitle">6,000 $</span>
              <span class="setup-pill-sub" id="pillMoney6kSub">متوازنة وكلاسيكية</span>
            </button>
            <button type="button" class="setup-pill" data-money="9000">
              <span class="setup-pill-icon">💎</span>
              <span class="setup-pill-title" id="pillMoney9kTitle">9,000 $</span>
              <span class="setup-pill-sub" id="pillMoney9kSub">استثمارية كبرى</span>
            </button>
          </div>
        </div>

        <!-- 4. AI Difficulty (Visible only when vs bot) -->
        <div class="setup-group" id="setupDifficultySection">
          <label class="setup-label" id="lblSetupDiff">⚡ صعوبة الذكاء الاصطناعي (الروبوت):</label>
          <div class="setup-pill-group" id="setupDifficultyGroup">
            <button type="button" class="setup-pill" data-diff="easy">
              <span class="setup-pill-icon">🟢</span>
              <span class="setup-pill-title" id="pillDiffEasyTitle">سهل</span>
              <span class="setup-pill-sub" id="pillDiffEasySub">مبتدئ ومسالم</span>
            </button>
            <button type="button" class="setup-pill active" data-diff="medium">
              <span class="setup-pill-icon">🟡</span>
              <span class="setup-pill-title" id="pillDiffMediumTitle">متوسط</span>
              <span class="setup-pill-sub" id="pillDiffMediumSub">متوازن وذكي</span>
            </button>
            <button type="button" class="setup-pill" data-diff="hard">
              <span class="setup-pill-icon">🔴</span>
              <span class="setup-pill-title" id="pillDiffHardTitle">صعب</span>
              <span class="setup-pill-sub" id="pillDiffHardSub">شرس ومفاوض محترف</span>
            </button>
          </div>
        </div>

        <!-- Start Button -->
        <div style="margin-top: 14px; text-align: center;">
          <button class="btn-big-roll" id="btnConfirmStartGame" style="width: 100%; border-radius: 16px; padding: 14px 20px; font-size: 18px;">
            <span>🚀</span>
            <span id="btnStartGameText">ابدأ اللعبة الآن</span>
          </button>
        </div>

      </div>
    </div>
  </div>

  <!-- MODAL 9: Trade & Negotiation Room -->
  <div class="modal-overlay" id="modalTrade">
    <div class="modal-box modal-trade-box">
      
      <div class="modal-header">
        <div class="modal-title">
          <span>🤝</span>
          <span>غرفة المفاوضة والتبادل التجاري</span>
        </div>
        <button class="modal-close-btn" id="btnCloseTradeModal">&times;</button>
      </div>

      <div class="trade-modal-body">
        
        <div class="trade-columns-container">
          
          <!-- Column 1: ما تقدمه (Offer) -->
          <div class="trade-column" id="tradeOfferCol">
            <div class="trade-col-header">
              <span class="trade-col-avatar" id="tradeOfferAvatar">🎩</span>
              <div class="trade-col-info">
                <span class="trade-col-title" id="tradeOfferName">عرضك أنت</span>
                <span class="trade-col-balance" id="tradeOfferBalance">رصيدك المتاح: 0 $</span>
              </div>
            </div>

            <!-- Cash Input -->
            <div class="trade-field-group">
              <label class="trade-field-label">💵 النقد المعروض في الصفقة:</label>
              <div class="trade-cash-input-row">
                <input type="number" id="tradeOfferCash" class="trade-cash-input" value="0" min="0" step="50">
                <span class="trade-cash-unit">$</span>
              </div>
            </div>

            <!-- Properties Selection -->
            <div class="trade-field-group">
              <label class="trade-field-label">🏛️ العقارات المعروضة للتبادل:</label>
              <div class="trade-props-list" id="tradeOfferPropsList"></div>
            </div>

            <!-- Jail Card -->
            <div class="trade-jail-card-row" id="tradeOfferJailCardRow" style="display: none;">
              <label style="font-size: 11px; color: #fef08a; display: flex; align-items: center; gap: 6px; cursor: pointer;">
                <input type="checkbox" id="tradeOfferJailCard">
                <span>🗝️ تضمين كارت الخروج من السجن</span>
              </label>
            </div>

          </div>

          <!-- Center Divider -->
          <div class="trade-center-divider">
            <div class="trade-arrows-badge">⇄</div>
            <div class="trade-exchange-label">تبادل</div>
          </div>

          <!-- Column 2: ما تطلبه من الخصم (Request) -->
          <div class="trade-column" id="tradeRequestCol">
            <div class="trade-col-header">
              <span class="trade-col-avatar" id="tradeRequestAvatar">🤖</span>
              <div class="trade-col-info">
                <span class="trade-col-title" id="tradeRequestName">طلبك من المنافس</span>
                <span class="trade-col-balance" id="tradeRequestBalance">رصيد المنافس: 0 $</span>
              </div>
            </div>

            <!-- Cash Input -->
            <div class="trade-field-group">
              <label class="trade-field-label">💵 النقد المطلوب من المنافس:</label>
              <div class="trade-cash-input-row">
                <input type="number" id="tradeRequestCash" class="trade-cash-input" value="0" min="0" step="50">
                <span class="trade-cash-unit">$</span>
              </div>
            </div>

            <!-- Properties Selection -->
            <div class="trade-field-group">
              <label class="trade-field-label">🏛️ العقارات المطلوبة في الصفقة:</label>
              <div class="trade-props-list" id="tradeRequestPropsList"></div>
            </div>

            <!-- Jail Card -->
            <div class="trade-jail-card-row" id="tradeRequestJailCardRow" style="display: none;">
              <label style="font-size: 11px; color: #fef08a; display: flex; align-items: center; gap: 6px; cursor: pointer;">
                <input type="checkbox" id="tradeRequestJailCard">
                <span>🗝️ طلب كارت الخروج من السجن</span>
              </label>
            </div>

          </div>

        </div>

        <!-- Trade Valuation Summary -->
        <div class="trade-valuation-bar" id="tradeValuationBar">
          <div class="trade-val-item">
            <span class="trade-val-lbl">قيمة ما تقدمه:</span>
            <span class="trade-val-num" id="tradeValOffer">0 $</span>
          </div>
          <div class="trade-val-item">
            <span class="trade-val-lbl">قيمة ما تطلبه:</span>
            <span class="trade-val-num" id="tradeValRequest">0 $</span>
          </div>
          <div class="trade-val-status" id="tradeValStatus">حدد العقارات أو الأموال لبدء المفاوضة</div>
        </div>

        <!-- Actions -->
        <div class="trade-footer-actions">
          <button class="btn-big-roll btn-submit-trade" id="btnSubmitTrade">
            <span>🤝</span>
            <span>إرسال عرض المفاوضة</span>
          </button>
          <button class="btn-matte" id="btnCancelTrade">
            <span>إلغاء</span>
          </button>
        </div>

      </div>

    </div>
  </div>

  <!-- MODAL 10: Trade Offer Review (for human 2-player mode) -->
  <div class="modal-overlay" id="modalTradeReview">
    <div class="modal-box modal-setup-box">
      <div class="modal-header">
        <div class="modal-title">
          <span>🤝</span>
          <span id="tradeReviewTitle">مراجعة عرض الصفقة التجارية</span>
        </div>
      </div>
      <div class="setup-modal-body" id="tradeReviewBody"></div>
      <div class="deed-action-btn-row" style="margin-top: 14px;">
        <button class="btn-matte btn-lime-build" id="btnAcceptTradeDeal" style="flex: 1.5; font-size: 16px; padding: 12px;">
          <span>✅</span>
          <span>أوافق على إتمام الصفقة</span>
        </button>
        <button class="btn-matte btn-demolish" id="btnRejectTradeDeal" style="flex: 1; font-size: 16px; padding: 12px;">
          <span>❌</span>
          <span>أرفض العرض</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 11: Direct Property Buyout Negotiation Window -->
  <div class="modal-overlay" id="modalBuyout">
    <div class="modal-box modal-buyout-box">
      
      <div class="modal-header">
        <div class="modal-title">
          <span>🤝</span>
          <span>مفاوضة شراء عقار من الخصم</span>
        </div>
        <button class="modal-close-btn" id="btnCloseBuyoutModal">&times;</button>
      </div>

      <div class="buyout-modal-body">
        
        <!-- Target Property Card Preview -->
        <div class="buyout-prop-card">
          <div class="buyout-prop-info">
            <div class="buyout-prop-stripe" id="buyoutPropColorStripe"></div>
            <div>
              <div class="buyout-prop-title" id="buyoutPropName">اسم العقار</div>
              <div class="buyout-prop-sub" id="buyoutPropOwner">المالك الحالي: روبوت 🤖</div>
            </div>
          </div>
          <div style="text-align: left;">
            <div style="font-size: 10px; color: #94a3b8;">السعر الأساسي بالرقعة:</div>
            <div style="font-size: 14px; font-weight: 800; color: #fef08a;" id="buyoutPropBasePrice">0 $</div>
          </div>
        </div>

        <!-- Feedback & Rejection Banner (Dynamic) -->
        <div class="buyout-feedback-box" id="buyoutFeedbackBox" style="display: none;"></div>

        <!-- Price Negotiation Controls -->
        <div class="buyout-price-control-box">
          <label class="trade-field-label">💰 السعر المعروض للشراء نقداً:</label>
          <div class="trade-cash-input-row">
            <input type="number" id="buyoutOfferInput" class="trade-cash-input" value="0" min="50" step="50" style="font-size: 18px; padding: 10px 14px;">
            <span class="trade-cash-unit" style="font-size: 15px;">$</span>
          </div>

          <!-- Quick Increment Buttons -->
          <div class="buyout-quick-btns-row">
            <button type="button" class="btn-quick-price" data-add="100">+100 $</button>
            <button type="button" class="btn-quick-price" data-add="250">+250 $</button>
            <button type="button" class="btn-quick-price" data-add="500">+500 $</button>
            <button type="button" class="btn-quick-price" data-add="1000">+1000 $</button>
          </div>

          <!-- Buyer Balance Info -->
          <div style="display: flex; justify-content: space-between; font-size: 11px; color: #cbd5e1; margin-top: 4px;">
            <span id="buyoutBuyerBalance">رصيدك المتاح: 0 $</span>
            <span id="buyoutMarkupPercent" style="color: #bef264; font-weight: 700;">(100% من السعر الأصلي)</span>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="trade-footer-actions">
          <button class="btn-big-roll" id="btnSendBuyoutOffer" style="flex: 2; padding: 12px 20px; font-size: 16px; border-radius: 12px;">
            <span>🤝</span>
            <span>إرسال عرض الشراء</span>
          </button>
          <button class="btn-matte" id="btnCancelBuyout" style="flex: 1; padding: 12px; font-size: 14px; border-radius: 12px;">
            <span>إلغاء الصفقة</span>
          </button>
        </div>

      </div>

    </div>
  </div>


  <!-- MODAL 13: Quick Cards Conditions Selector -->
  <!-- MODAL 12: Buyout Review for Human Rival (2-Player Mode) -->
  <div class="modal-overlay" id="modalBuyoutRivalReview">
    <div class="modal-box modal-setup-box">
      <div class="modal-header">
        <div class="modal-title">
          <span>🤝</span>
          <span>عرض شراء لعقارك!</span>
        </div>
      </div>
      <div class="setup-modal-body" id="buyoutRivalReviewBody"></div>
      <div class="deed-action-btn-row" style="margin-top: 14px;">
        <button class="btn-matte btn-lime-build" id="btnAcceptBuyoutDeal" style="flex: 1.5; font-size: 16px; padding: 12px;">
          <span>✅ موافقة وبيع العقار</span>
        </button>
        <button class="btn-matte btn-demolish" id="btnRejectBuyoutDeal" style="flex: 1; font-size: 16px; padding: 12px;">
          <span>❌ رفض هذا السعر</span>
        </button>
      </div>
    </div>
  </div>

{SETTINGS_MODAL_HTML}

  <!-- MODAL 15: About Us (من نحن) -->
  <div class="modal-overlay" id="modalAboutUs">
    <div class="modal-box modal-setup-box" style="max-width: 560px; border-color: #38bdf8; box-shadow: 0 10px 40px rgba(2, 132, 199, 0.4);">
      <div class="modal-header" style="background: linear-gradient(135deg, #0f172a, #0369a1); border-bottom: 1px solid rgba(56, 189, 248, 0.3);">
        <div class="modal-title" style="color: #38bdf8;">
          <span>ℹ️</span>
          <span id="aboutUsModalTitle">من نحن - بنك الحظ 3D الفاخرة</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalAboutUs')">&times;</button>
      </div>
      <div class="setup-modal-body" id="aboutUsModalContent" style="padding: 16px 14px; font-size: 13.5px; line-height: 1.8; color: #e2e8f0; max-height: 60vh; overflow-y: auto;">
      </div>
      <div class="modal-footer" style="padding: 12px 16px; border-top: 1px solid #334155; text-align: center;">
        <button type="button" class="btn-matte" onclick="closeModal('modalAboutUs')" style="padding: 8px 26px;">
          <span id="btnAboutUsClose">إغلاق النافذة</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 16: Token Picker (اختيار وتغيير أيقونات اللعب) -->
  <div class="modal-overlay" id="modalTokenPicker">
    <div class="modal-box modal-setup-box" style="max-width: 620px; border-color: #f59e0b; box-shadow: 0 10px 40px rgba(245, 158, 11, 0.4);">
      <div class="modal-header" style="background: linear-gradient(135deg, #1e130b, #451a03); border-bottom: 1px solid rgba(245, 158, 11, 0.3);">
        <div class="modal-title" style="color: #fbbf24;">
          <span>🎭</span>
          <span id="tokenPickerModalTitle">اختيار وتغيير أيقونة البيدق</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('modalTokenPicker')">&times;</button>
      </div>
      <div class="setup-modal-body" style="padding: 14px 16px;">
        <!-- Player Switch Tabs -->
        <div class="token-player-tabs" style="margin-bottom: 12px;">
          <button type="button" class="token-player-tab active" id="tabPawnP1" onclick="switchTokenPickerTarget(0)">
            <span>🎩</span> <span id="lblTokenTargetP1">اللاعب 1 (أنت)</span>
          </button>
          <button type="button" class="token-player-tab" id="tabPawnP2" onclick="switchTokenPickerTarget(1)">
            <span>🤖</span> <span id="lblTokenTargetP2">المنافس (اللاعب 2)</span>
          </button>
        </div>
        <div id="tokenPickerSubtitle" style="font-size: 13px; color: #cbd5e1; margin-bottom: 12px; text-align: center;">
          اختر البيدق أو الأيقونة ثلاثية الأبعاد المفضلة للتحرك بها على رقعة اللعب:
        </div>
        <div class="token-picker-grid" id="tokenPickerGrid">
        </div>
      </div>
      <div class="modal-footer" style="padding: 12px 16px; border-top: 1px solid #334155; text-align: center;">
        <button type="button" class="btn-matte" onclick="closeModal('modalTokenPicker')" style="padding: 8px 26px;">
          <span id="btnTokenPickerClose">إغلاق وتأكيد الاختيار</span>
        </button>
      </div>
    </div>
  </div>




  <!-- JAVASCRIPT GAME LOGIC & SOUND ENGINE -->
  <script>
  // Injected 2-Player Data & Matte 3D SVGs
  const TILES = {tiles_json};
  const CHANCE_CARDS = {chance_json};
  const CHEST_CARDS = {chest_json};
  const LANDMARKS_DEF = {landmarks_json};
  const CHARACTERS_DEF = {characters_json};
  const WHEEL_ITEMS_DEF = {wheel_json};
  const SVG_ASSETS = {svg_assets_json};

  // Multilingual Internationalization (14 Languages)
  const I18N_LANGUAGES = {I18N_LANGUAGES_JSON};
  const I18N_TILES = {I18N_TILES_JSON};
  const I18N_UI = {I18N_UI_JSON};

  let currentLanguage = 'ar';
  try {{
    const saved = localStorage.getItem('bank_el_hazz_lang');
    if (saved && I18N_UI[saved]) currentLanguage = saved;
  }} catch (e) {{}}

  function t(key, fallback = '') {{
    const cur = I18N_UI[currentLanguage] || I18N_UI['ar'];
    if (cur && cur[key] !== undefined) return cur[key];
    if (I18N_UI['ar'] && I18N_UI['ar'][key] !== undefined) return I18N_UI['ar'][key];
    return fallback || key;
  }}

  function getCurrency() {{
    return '$';
  }}

  // Game Animation Speed Settings
  const gameSettings = {{
    diceSpeed: 'normal', // 'slow', 'normal', 'fast', 'instant'
    moveSpeed: 'normal'  // 'slow', 'normal', 'fast', 'instant'
  }};

  try {{
    const savedDice = localStorage.getItem('bank_el_hazz_dice_speed');
    if (savedDice) gameSettings.diceSpeed = savedDice;
    const savedMove = localStorage.getItem('bank_el_hazz_move_speed');
    if (savedMove) gameSettings.moveSpeed = savedMove;
  }} catch (e) {{}}

  const DICE_SPEED_DELAYS = {{
    slow: 1500,
    normal: 800,
    fast: 350,
    instant: 100
  }};

  const MOVE_SPEED_DELAYS = {{
    slow: 240,
    normal: 120,
    fast: 50,
    instant: 15
  }};

    function updateRulesModalContent() {{
    const headerTitle = document.getElementById('rulesModalHeaderTitle');
    const tabTitleGen = document.getElementById('tabRulesTitleGeneral');
    const tabTitleCards = document.getElementById('tabRulesTitleCards');
    const contentGen = document.getElementById('rulesContentGeneral');
    const contentCards = document.getElementById('rulesContentCards');
    const modalBtn = document.querySelector('#modalRules .modal-footer button');
    
    if (currentLanguage === 'ar') {{
      if (headerTitle) headerTitle.innerText = 'دليل وقواعد بنك الحظ & شروط الكروت';
      if (tabTitleGen) tabTitleGen.innerText = 'قواعد اللعبة العامة';
      if (tabTitleCards) tabTitleCards.innerText = 'قائمة شروط الكروت';
      if (modalBtn) modalBtn.innerText = 'فهمت القواعد! هيا لنلعب';

      if (contentGen) {{
        contentGen.innerHTML = `
          <h3 style="color: #fef08a; margin-bottom: 6px;">⚔️ نظام المواجهة الثنائية (1 ضد 1):</h3>
          <ul style="padding-right: 20px; margin-bottom: 14px;">
            <li><b>المواجهة المباشرة:</b> مواجهة سريعة ومثيرة! كل رمية نرد وكل عقار تشتريه يقلص خيارات خصمك.</li>
            <li><b>شراء المدن وتأسيس الطوابق:</b> بعد امتلاك كامل مدن المجموعة اللونية يمكنك بناء طوابق ليمونية (من 1 إلى 4) بقيمة 33% من سعر العقار، وعند اكتمال 4 طوابق في المجموعة يُتاح بناء برج إيفل الذهبي (الطابق الخامس) لرفع الأرباح بنسبة 50% لكل طابق!</li>
            <li><b>المفاوضة والتبادل:</b> يمكنك في أي وقت بدء مفاوضة لشراء عقارات خصمك أو تبادل الأراضي والمساومة بالدولار ($).</li>
          </ul>

          <h3 style="color: #38bdf8; margin-bottom: 6px;">🎲 قواعد الرقعة الكلاسيكية (40 مربعاً):</h3>
          <ul style="padding-right: 20px; margin-bottom: 14px;">
            <li><b>نقطة البداية (انطلق):</b> مر أو اهبط عليها لتقبض 200 $.</li>
            <li><b>محطات القطار والمرافق:</b> 4 محطات قطار يتضاعف إيجارها مع كثرة الامتلاك، وشركتا الكهرباء والمياه تعتمدان على ضرب ناتج النرد.</li>
            <li><b>الاستراحة المجانية:</b> تجمع كل ضرائب اللاعبين وغرامات الرادار، ومن يقف عليها يفوز بالحصيلة كاملة!</li>
            <li><b>سجن القلعة:</b> يدخله اللاعب عند مربع ادخل السجن أو كروت الحظ أو رمي دبل 3 مرات متتالية، ويسقط سياج حديدي مع قفل وصوت زنزانة.</li>
          </ul>
        `;
      }}

      if (contentCards) {{
        contentCards.innerHTML = `
          <div style="background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.35); border-radius: 8px; padding: 10px 14px; margin-bottom: 14px; font-size: 12.5px; color: #fde68a; text-align: center;">
            ℹ️ <b>قائمة شروط الكروت والخانات الخاصة:</b><br>
            هذه الشروط غير تفاعلية هنا، وتُنفّذ تلقائياً أثناء اللعب عند هبوط البيدق على خانتها المخصصة:
          </div>

          <h4 style="color: #fbbf24; margin: 12px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>🎁</span> <span>كروت صندوق الدنيا (محفظة الشعب - الخانات: 2، 17، 33)</span>
          </h4>
          <div class="rule-card-readonly" style="border-right: 4px solid #f59e0b;">
            <div class="rule-card-body">
              • <b>استرداد ضريبي من وزارة المالية:</b> مراجعة الحسابات أسفرت عن استرداد لصالحك (+100 $ فوراً من البنك).<br>
              • <b>عيد ميلادك السعيد:</b> احتفل مع منافسيك! يدفع لك المنافس هدية نقدية قدرها 25 $.<br>
              • <b>عائد استثمار قناة السويس:</b> استثمارك في شهادات الاستثمار حقق أرباحاً (+200 $).<br>
              • <b>تذكرة خروج مجاني من السجن:</b> احتفظ بهذا الكارت لاستخدامه فوراً عند صدور أي أمر بالحبس.<br>
              • <b>تكاليف الفحص الطبي:</b> سداد تكاليف الفحوصات الطورية (-50 $ تودع بوعاء الاستراحة).<br>
              • <b>بيع أسهم استثمارية:</b> بيع جزء من المحفظة المالية (+50 $).<br>
              • <b>قسط التأمين الصحي:</b> سداد القسط السنوي للرعاية (-50 $ تودع بوعاء الاستراحة).<br>
              • <b>مكافأة تفوق استثماري:</b> جائزة التميز المالي (+100 $ من البنك).<br>
              • <b>أرباح استشارات تجارية:</b> أتعاب تقديم خدمات استشارية (+25 $).<br>
              • <b>تسوية فواتير مرافق عامة:</b> سداد فواتير الاستهلاك العام (-50 $ لوعاء الاستراحة).
            </div>
          </div>

          <h4 style="color: #fdba74; margin: 14px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>❓</span> <span>كروت الحظ (المجازفة والأقدار - الخانات: 7، 22، 36)</span>
          </h4>
          <div class="rule-card-readonly" style="border-right: 4px solid #f97316;">
            <div class="rule-card-body">
              • <b>عملية سطو على البنك (Bank Heist):</b> اقتحام خزينة المنافس ونهب أموال طائلة نقداً!<br>
              • <b>هجوم المطرقة والتعطيل (Shutdown):</b> ضرب معالم الخصم الكرتونية لهدمها، وتخطي دروعه الدفاعية!<br>
              • <b>تقدم إلى نقطة البداية (انطلق):</b> تحرك فوراً إلى مربع انطلق واستلم مكافأة 200 $.<br>
              • <b>رحلة إلى قلب العاصمة (القاهرة):</b> تقدم فوراً لعقار القاهرة (شراء إن كان متاحاً أو دفع الإيجار).<br>
              • <b>أرباح استثمارية في البورصة:</b> مكاسب مضاربة في الأسهم (+150 $ نقداً).<br>
              • <b>غرامة تجاوز السرعة:</b> القيادة بسرعة زائدة (-50 $ تودع بوعاء الاستراحة).<br>
              • <b>أعمال صيانة وترميم شاملة:</b> ادفع 25 $ عن كل طابق و 100 $ عن برج إيفل لوعاء الاستراحة.<br>
              • <b>تقدم لأقرب محطة قطار:</b> تحرك فوراً لأقرب محطة قطار (شراء أو سداد ضعف الإيجار).<br>
              • <b>رحلة سياحية إلى الإسكندرية:</b> السفر الفوري لعروس البحر الأبيض المتوسط.<br>
              • <b>عطل فني في شبكة المرافق:</b> إصلاحات طارئة في الخطوط (-50 $ لوعاء الاستراحة).<br>
              • <b>أمر قضائي فوري بالحبس:</b> اذهب فوراً إلى سجن القلعة دون أن تمر بنقطة انطلق ودون قبض 200 $.
            </div>
          </div>

          <h4 style="color: #6ee7b7; margin: 14px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>💸</span> <span>الضرائب والغرامات الحكومية السيادية</span>
          </h4>
          <div class="rule-card-readonly" style="border-right: 4px solid #10b981;">
            <div class="rule-card-body">
              • <b>ضريبة الدخل العامة (الخانة 4):</b> التزام مالي سيادي إلزامي بقيمة 200 $ يُخصم فور الوقوف على الخانة ويُحوّل بالكامل إلى <b>وعاء الاستراحة المجانية</b>.<br>
              • <b>ضريبة الرفاهية والكماليات (الخانة 38):</b> رسم فخامة بقيمة 100 $ يُخصم من رصيد اللاعب ويُودع في <b>وعاء الاستراحة المجانية</b>.
            </div>
          </div>

          <h4 style="color: #fca5a5; margin: 14px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>⛓️</span> <span>سجن القلعة (أمر الحبس الفوري vs الزيارة التفقدية)</span>
          </h4>
          <div class="rule-card-readonly" style="border-right: 4px solid #ef4444;">
            <div class="rule-card-body">
              • <b>أمر الحبس الفوري (الخانة 30):</b> ينتقل اللاعب بأسرع مسار (للأمام أو للخلف) بصافرة الشرطة، ويسقط السور الحديدي بقفل محكم. للخروج: رمي دبل نرد، استخدام تذكرة العفو، أو دفع كفالة 50 $ بعد 3 أدوار.<br>
              • <b>الزيارة التفقدية (الخانة 10):</b> الوقوف عبر حركة النرد العادية يعتبر زيارة آمنة دون حبس أو غرامات.
            </div>
          </div>

          <h4 style="color: #7dd3fc; margin: 14px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>🚗</span> <span>وعاء الاستراحة المجانية (الخانة 20)</span>
          </h4>
          <div class="rule-card-readonly" style="border-right: 4px solid #38bdf8;">
            <div class="rule-card-body">
              محطة حيادية استراتيجية لا إيجار فيها ولا ضرائب. تجمع وتراكم كافة حصائل ضرائب الدخل والرفاهية والغرامات، وأول لاعب يقف عليها يحصد كامل الأموال المتراكمة في الوعاء فوراً!
            </div>
          </div>
        `;
      }}
    }} else {{
      const isEuro = ['en', 'fr', 'ru', 'es', 'pt', 'de', 'it', 'tr'].includes(currentLanguage);
      const regionName = isEuro ? 'European Capitals' : 'Asian Capitals';
      if (headerTitle) headerTitle.innerText = `${{t('gameTitle')}} - Rules & Cards Guide`;
      if (tabTitleGen) tabTitleGen.innerText = 'General Rules';
      if (tabTitleCards) tabTitleCards.innerText = 'Cards & Tile Rules';
      if (modalBtn) modalBtn.innerText = t('btnStartGame', "Got it! Let's Play");

      if (contentGen) {{
        contentGen.innerHTML = `
          <h3 style="color: #fef08a; margin-bottom: 6px;">⚔️ Head-to-Head Duel Mode (1 vs 1):</h3>
          <ul style="padding-left: 20px; margin-bottom: 14px;">
            <li><b>Direct Clash:</b> Fast-paced, high-stakes duel on an authentic 40-tile board featuring ${{regionName}} in USD ($)!</li>
            <li><b>City Monopoly & Floors:</b> Own all properties of a color group to build lime floors (1 to 4) at 33% of base value. Reaching 4 floors unlocks the Golden Eiffel Tower (5th level), boosting rent by +50% of floor cost per level!</li>
            <li><b>Trade & Negotiation:</b> Negotiate buyouts and swap real estate with your rival in dollars ($) at any time.</li>
          </ul>

          <h3 style="color: #38bdf8; margin-bottom: 6px;">🎲 Classic Board Rules:</h3>
          <ul style="padding-left: 20px; margin-bottom: 14px;">
            <li><b>GO (Start):</b> Collect 200 $ as you pass or land.</li>
            <li><b>Railroads & Utilities:</b> 4 stations with scaling rent, plus Electric & Water works based on dice multipliers.</li>
            <li><b>Free Parking Pot:</b> Collects all tax penalties. Land here to claim the entire accumulated fortune!</li>
            <li><b>Citadel Jail:</b> Sent to jail by landing on 'Go to Jail', drawing a jail card, or rolling doubles 3 times. Iron bars drop down with padlock and cell door sound.</li>
          </ul>
        `;
      }}

      if (contentCards) {{
        contentCards.innerHTML = `
          <div style="background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.35); border-radius: 8px; padding: 10px 14px; margin-bottom: 14px; font-size: 12.5px; color: #fde68a; text-align: center;">
            ℹ️ <b>Cards & Special Tile Conditions:</b><br>
            These effects trigger automatically when a pawn lands on their respective tiles on the 3D board:
          </div>

          <h4 style="color: #fbbf24; margin: 12px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>🎁</span> <span>Community Chest Cards (Tiles: 2, 17, 33)</span>
          </h4>
          <div class="rule-card-readonly" style="border-left: 4px solid #f59e0b;">
            <div class="rule-card-body">
              • <b>Tax Refund:</b> Audit refund from Ministry of Finance (+100 $).<br>
              • <b>Happy Birthday:</b> Collect 25 $ birthday gift from your rival.<br>
              • <b>Suez Canal Dividend:</b> Massive returns on national investment (+200 $).<br>
              • <b>Get Out of Jail Free:</b> Keep to immediately exit the Citadel Jail without bail.<br>
              • <b>Hospital Examination:</b> Pay medical checkup bills (-50 $ to Free Parking pot).<br>
              • <b>Stock Sale:</b> Liquidate equities (+50 $).<br>
              • <b>Health Insurance:</b> Pay annual premium (-50 $ to Free Parking pot).<br>
              • <b>Investment Award:</b> Excellence reward (+100 $).<br>
              • <b>Consultancy Fees:</b> Business advisory income (+25 $).<br>
              • <b>Utility Bill Settlement:</b> Pay public utilities (-50 $ to Free Parking pot).
            </div>
          </div>

          <h4 style="color: #fdba74; margin: 14px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>❓</span> <span>Chance Mystery Cards (Tiles: 7, 22, 36)</span>
          </h4>
          <div class="rule-card-readonly" style="border-left: 4px solid #f97316;">
            <div class="rule-card-body">
              • <b>Bank Heist:</b> Break into your opponent's vault and plunder major cash!<br>
              • <b>Shutdown Hammer:</b> Strike and demolish rival landmarks, bypassing shields!<br>
              • <b>Advance to GO:</b> Move directly to start square and collect 200 $.<br>
              • <b>Trip to Cairo:</b> Advance to the capital property (buy or pay rent).<br>
              • <b>Stock Market Boom:</b> Capital gains dividend (+150 $).<br>
              • <b>Speeding Fine:</b> Pay traffic radar violation (-50 $ to Free Parking pot).<br>
              • <b>General Property Repairs:</b> Pay 25 $ per floor and 100 $ per Eiffel Tower.<br>
              • <b>Advance to Nearest Railroad:</b> Travel directly to the next train station.<br>
              • <b>Trip to Alexandria:</b> Direct voyage to the Mediterranean jewel.<br>
              • <b>Utility Breakdown:</b> Emergency maintenance fee (-50 $ to Free Parking pot).<br>
              • <b>Go to Jail:</b> Sent immediately to Citadel Jail without collecting 200 $.
            </div>
          </div>

          <h4 style="color: #6ee7b7; margin: 14px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>💸</span> <span>Government Taxes</span>
          </h4>
          <div class="rule-card-readonly" style="border-left: 4px solid #10b981;">
            <div class="rule-card-body">
              • <b>Income Tax (Tile 4):</b> Mandatory 200 $ fee, deposited in the Free Parking Pot.<br>
              • <b>Luxury Tax (Tile 38):</b> 100 $ luxury surcharge, deposited in the Free Parking Pot.
            </div>
          </div>

          <h4 style="color: #fca5a5; margin: 14px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>⛓️</span> <span>Citadel Jail (Arrest vs Just Visiting)</span>
          </h4>
          <div class="rule-card-readonly" style="border-left: 4px solid #ef4444;">
            <div class="rule-card-body">
              • <b>Go to Jail (Tile 30):</b> Nearest path transit with police siren; iron bars drop down with padlock. Escape by rolling doubles, using a card, or paying 50 $ bail after 3 turns.<br>
              • <b>Just Visiting (Tile 10):</b> Standard move landing is a routine safe visit.
            </div>
          </div>

          <h4 style="color: #7dd3fc; margin: 14px 0 8px 0; display: flex; align-items: center; gap: 8px;">
            <span>🚗</span> <span>Free Parking Pot (Tile 20)</span>
          </h4>
          <div class="rule-card-readonly" style="border-left: 4px solid #38bdf8;">
            <div class="rule-card-body">
              Neutral safe oasis collecting all taxes and penalties. First player to land here wins the entire accumulated pot immediately!
            </div>
          </div>
        `;
      }}
    }}
  }}

  function setGameLanguage(langCode, save = true) {{
    if (!I18N_LANGUAGES.some(l => l.code === langCode)) langCode = 'ar';
    currentLanguage = langCode;
    if (save) {{
      try {{ localStorage.setItem('bank_el_hazz_lang', langCode); }} catch (e) {{}}
    }}

    const langInfo = I18N_LANGUAGES.find(l => l.code === langCode) || I18N_LANGUAGES[0];
    document.documentElement.lang = langCode;
    document.documentElement.dir = langInfo.dir || (langCode === 'ar' || langCode === 'fa' ? 'rtl' : 'ltr');

    // Sync all 3 dropdowns
    ['settingsLanguageSelect', 'setupLanguageSelect', 'headerLanguageSelect'].forEach(id => {{
      const el = document.getElementById(id);
      if (el) el.value = langCode;
    }});

    // Update TILES property names & subtitles
    if (I18N_TILES[langCode]) {{
      TILES.forEach(tile => {{
        const trans = I18N_TILES[langCode][tile.id] || I18N_TILES[langCode][String(tile.id)];
        if (trans) {{
          tile.name = trans.name;
          tile.subtitle = trans.sub;
        }}
      }});
    }}

    // Update board city label
    const cityLbl = document.getElementById('boardCityLabel');
    if (cityLbl) cityLbl.innerText = t('boardCitySub');

    const titleElem = document.getElementById('boardTitleText');
    if (titleElem) titleElem.innerText = t('gameTitle');

    // Update bot name if applicable
    if (state.players && state.players[1] && state.players[1].isBot) {{
      state.players[1].name = t('botDefault', 'روبوت');
      const p2Input = document.getElementById('setupPlayer2Name');
      if (p2Input) p2Input.value = t('botDefault', 'روبوت');
    }}

    // Re-render board tiles with updated city names and currencies
    renderBoardTiles();

    // Update Header Buttons
    const btnLandmarksText = document.getElementById('btnLandmarksText');
    if (btnLandmarksText) btnLandmarksText.innerText = t('landmarksTitle', 'معالم المدينة');

    const btnWheelText = document.getElementById('btnWheelText');
    if (btnWheelText) btnWheelText.innerText = t('wheelTitle', 'عجلة الحظ');

    const btnTradeText = document.getElementById('btnTradeText');
    if (btnTradeText) btnTradeText.innerText = t('btnTrade');

    const btnCardRulesText = document.getElementById('btnCardRulesText');
    if (btnCardRulesText) btnCardRulesText.innerText = t('btnCardRules');

    const btnRulesText = document.getElementById('btnRulesText');
    if (btnRulesText) btnRulesText.innerText = t('btnRules');

        const btnAboutUsEl = document.getElementById('btnAboutUsText');
    if (btnAboutUsEl) btnAboutUsEl.innerText = t('btnAboutUs', 'ℹ️ من نحن (عن اللعبة)');

    const btnTokenPickerEl = document.getElementById('btnTokenPickerText');
    if (btnTokenPickerEl) btnTokenPickerEl.innerText = t('btnTokenPicker', '🎭 تغيير واختيار أيقونة البيدق');

    const aboutUsTitleEl = document.getElementById('aboutUsModalTitle');
    if (aboutUsTitleEl) aboutUsTitleEl.innerText = t('aboutUsModalTitle', 'من نحن - بنك الحظ 3D');

    const tokenPickerTitleEl = document.getElementById('tokenPickerModalTitle');
    if (tokenPickerTitleEl) tokenPickerTitleEl.innerText = t('tokenPickerModalTitle', 'اختيار وتغيير أيقونة البيدق');

    const btnAboutUsCloseEl = document.getElementById('btnAboutUsClose');
    if (btnAboutUsCloseEl) btnAboutUsCloseEl.innerText = currentLanguage === 'ar' ? 'إغلاق النافذة' : 'Close';

    const btnTokenPickerCloseEl = document.getElementById('btnTokenPickerClose');
    if (btnTokenPickerCloseEl) btnTokenPickerCloseEl.innerText = currentLanguage === 'ar' ? 'إغلاق وتأكيد الاختيار' : 'Close & Confirm';

    const tokenSubEl = document.getElementById('tokenPickerSubtitle');
    if (tokenSubEl) tokenSubEl.innerText = currentLanguage === 'ar' 
      ? 'اختر الأيقونة أو البيدق المفضل لديك ليتحرك به بطلك على رقعة اللعب ثلاثية الأبعاد:' 
      : 'Choose your favorite token or character to represent you on the 3D board:';

    renderTokenPickerGrid();

    const btnSettingsNavText = document.getElementById('btnSettingsNavText');
    if (btnSettingsNavText) btnSettingsNavText.innerText = t('btnSettings');

    const btnReset = document.getElementById('btnResetGame');
    if (btnReset) btnReset.title = t('btnNewGame');

    // Update Center & Bottom Indicators
    const potLbl = document.getElementById('potLabelText');
    if (potLbl) potLbl.innerText = t('freeParkingPot');

    const energyLbl = document.getElementById('energyLabelText');
    if (energyLbl) energyLbl.innerText = t('diceEnergy');

    const rollBtnText = document.getElementById('btnRollDiceText');
    if (rollBtnText) rollBtnText.innerText = t('btnRollDice');

    const logTitle = document.getElementById('activityLogTitle');
    if (logTitle) logTitle.innerText = t('activityLogTitle');

    const clearLogBtn = document.getElementById('btnClearLog');
    if (clearLogBtn) clearLogBtn.innerText = t('clearLog');

    // Update Setup Modal Strings
    const setupTitle = document.getElementById('setupModalTitleText');
    if (setupTitle) setupTitle.innerText = t('setupModalTitle');

    const lblSetupLang = document.getElementById('lblSetupLang');
    if (lblSetupLang) lblSetupLang.innerText = t('setupLanguageLabel');

    const lblSetupMode = document.getElementById('lblSetupMode');
    if (lblSetupMode) lblSetupMode.innerText = t('setupModeLabel');

    const pillModeBot = document.getElementById('pillModeBotTitle');
    if (pillModeBot) pillModeBot.innerText = t('modeBot');

    const pillModeBotSub = document.getElementById('pillModeBotSub');
    if (pillModeBotSub) pillModeBotSub.innerText = t('modeBotSub');

    const pillModeHuman = document.getElementById('pillModeHumanTitle');
    if (pillModeHuman) pillModeHuman.innerText = t('modeHuman');

    const pillModeHumanSub = document.getElementById('pillModeHumanSub');
    if (pillModeHumanSub) pillModeHumanSub.innerText = t('modeHumanSub');

    const lblSetupNames = document.getElementById('lblSetupNames');
    if (lblSetupNames) lblSetupNames.innerText = t('setupNamesLabel');

    const p1Pfx = document.getElementById('p1Prefix');
    if (p1Pfx) p1Pfx.innerText = t('p1Prefix');

    const p2Pfx = document.getElementById('p2Prefix');
    if (p2Pfx) p2Pfx.innerText = t('p2Prefix');

    const lblSetupMoney = document.getElementById('lblSetupMoney');
    if (lblSetupMoney) lblSetupMoney.innerText = t('setupMoneyLabel');

    const pillM3 = document.getElementById('pillMoney3kSub');
    if (pillM3) pillM3.innerText = t('money3kSub');

    const pillM6 = document.getElementById('pillMoney6kSub');
    if (pillM6) pillM6.innerText = t('money6kSub');

    const pillM9 = document.getElementById('pillMoney9kSub');
    if (pillM9) pillM9.innerText = t('money9kSub');

    const lblSetupDiff = document.getElementById('lblSetupDiff');
    if (lblSetupDiff) lblSetupDiff.innerText = t('setupDifficultyLabel');

    const pillDiffEasy = document.getElementById('pillDiffEasyTitle');
    if (pillDiffEasy) pillDiffEasy.innerText = t('diffEasy');

    const pillDiffEasySub = document.getElementById('pillDiffEasySub');
    if (pillDiffEasySub) pillDiffEasySub.innerText = t('diffEasySub');

    const pillDiffMed = document.getElementById('pillDiffMediumTitle');
    if (pillDiffMed) pillDiffMed.innerText = t('diffMedium');

    const pillDiffMedSub = document.getElementById('pillDiffMediumSub');
    if (pillDiffMedSub) pillDiffMedSub.innerText = t('diffMediumSub');

    const pillDiffHard = document.getElementById('pillDiffHardTitle');
    if (pillDiffHard) pillDiffHard.innerText = t('diffHard');

    const pillDiffHardSub = document.getElementById('pillDiffHardSub');
    if (pillDiffHardSub) pillDiffHardSub.innerText = t('diffHardSub');

    const btnStartGame = document.getElementById('btnStartGameText');
    if (btnStartGame) btnStartGame.innerText = t('btnStartGame');

    // Update Settings Modal Strings
    const settingsTitle = document.getElementById('settingsModalTitle');
    if (settingsTitle) settingsTitle.innerText = t('btnSettings');

    const lblSettingsLang = document.getElementById('lblSettingsLang');
    if (lblSettingsLang) lblSettingsLang.innerText = t('setupLanguageLabel');

    const lblSettingsDiff = document.getElementById('lblSettingsDiff');
    if (lblSettingsDiff) lblSettingsDiff.innerText = t('setupDifficultyLabel');

    const sDiffEasy = document.getElementById('pillDiffEasyTitle');
    if (sDiffEasy) sDiffEasy.innerText = t('diffEasy');

    const sDiffMed = document.getElementById('pillDiffMediumTitle');
    if (sDiffMed) sDiffMed.innerText = t('diffMedium');

    const sDiffHard = document.getElementById('pillDiffHardTitle');
    if (sDiffHard) sDiffHard.innerText = t('diffHard');

    // Speed labels translation in Settings
    const lblDiceSpeed = document.getElementById('lblSettingsDiceSpeed');
    if (lblDiceSpeed) lblDiceSpeed.innerText = t('lblSettingsDiceSpeed');

    const lblMoveSpeed = document.getElementById('lblSettingsMoveSpeed');
    if (lblMoveSpeed) lblMoveSpeed.innerText = t('lblSettingsMoveSpeed');

    ['pillDiceSlowTitle', 'pillMoveSlowTitle'].forEach(id => {{
      const el = document.getElementById(id);
      if (el) el.innerText = t('speedSlow');
    }});

    ['pillDiceNormalTitle', 'pillMoveNormalTitle'].forEach(id => {{
      const el = document.getElementById(id);
      if (el) el.innerText = t('speedNormal');
    }});

    ['pillDiceFastTitle', 'pillMoveFastTitle'].forEach(id => {{
      const el = document.getElementById(id);
      if (el) el.innerText = t('speedFast');
    }});

    ['pillDiceInstantTitle', 'pillMoveInstantTitle'].forEach(id => {{
      const el = document.getElementById(id);
      if (el) el.innerText = t('speedInstant');
    }});

    // Wheel Modal Strings
    const wheelTitleEl = document.getElementById('wheelModalTitleText');
    if (wheelTitleEl) wheelTitleEl.innerText = t('wheelModalTitle');

    const wheelSubEl = document.getElementById('wheelSubText');
    if (wheelSubEl) wheelSubEl.innerText = t('wheelInstruction');

    const btnSpinEl = document.getElementById('btnSpinWheelText');
    if (btnSpinEl) btnSpinEl.innerText = t('btnSpinWheelText');

    const btnSaveSettings = document.getElementById('btnSaveSettingsText');
    if (btnSaveSettings) btnSaveSettings.innerText = t('btnSaveSettings');

    updateRulesModalContent();
    updateUI();
  }}

  // Web Audio SFX
  {SOUND_JS}
  const sfx = new WebAudioSFX();

  // Core Game State (2 Players Only)
  const state = {{
    players: [],
    currentPlayerIdx: 0,
    freeParkingPot: 200,
    boardLevel: 1,
    cityName: 'القاهرة التاريخية',
    dice: [1, 1],
    doublesCount: 0,
    isRolling: false,
    tileOwnership: {{}}, // tileId -> {{ ownerId, houses: 0, mortgaged: false }}
    activeCard: null,
    heistState: null,
    shutdownState: null,
    wheelSpinning: false
  }};

  // Helper: Grid Position Formula for 11x11 Monopoly Board
  function getTileGridPos(tileId) {{
    if (tileId >= 0 && tileId <= 10) {{
      return {{ row: 11, col: 11 - tileId }};
    }} else if (tileId >= 11 && tileId <= 20) {{
      return {{ row: 11 - (tileId - 10), col: 1 }};
    }} else if (tileId >= 21 && tileId <= 30) {{
      return {{ row: 1, col: 1 + (tileId - 20) }};
    }} else {{
      return {{ row: 1 + (tileId - 30), col: 11 }};
    }}
  }}

  // 3D Architectural Model Mapper for All 40 Tiles
  
  // Generator for 3D Isometric Lime Buildings (Floors 1 to 4)
  function getLimeBuildingSvg(floors) {{
    const fl = Math.min(4, Math.max(1, floors));
    const base_y = 52;
    const top_y = base_y - (fl * 9);
    let s = '<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">';
    s += '<defs><radialGradient id="ao_lime" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="rgba(0,0,0,0.55)"/><stop offset="60%" stop-color="rgba(0,0,0,0.2)"/><stop offset="100%" stop-color="rgba(0,0,0,0)"/></radialGradient><linearGradient id="lime_roof" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#d9f99d"/><stop offset="100%" stop-color="#a3e635"/></linearGradient></defs>';
    s += '<ellipse cx="30" cy="54" rx="25" ry="5.5" fill="url(#ao_lime)"/>';
    s += '<polygon points="12,' + top_y + ' 30,' + (top_y + 10) + ' 30,' + base_y + ' 12,' + (base_y - 10) + '" fill="#84cc16" stroke="#4d7c0f" stroke-width="0.5"/>';
    s += '<polygon points="30,' + (top_y + 10) + ' 48,' + top_y + ' 48,' + (base_y - 10) + ' 30,' + base_y + '" fill="#65a30d" stroke="#365314" stroke-width="0.5"/>';
    s += '<polygon points="30,' + (top_y - 8) + ' 48,' + top_y + ' 30,' + (top_y + 10) + ' 12,' + top_y + '" fill="url(#lime_roof)" stroke="#a3e635" stroke-width="0.7"/>';
    for (let i = 0; i < fl; i++) {{
      const fl_top = base_y - 10 - (i * 9);
      const fl_mid = base_y - (i * 9);
      if (i > 0) {{
        s += '<line x1="12" y1="' + fl_top + '" x2="30" y2="' + fl_mid + '" stroke="#bef264" stroke-width="0.8" opacity="0.9"/>';
        s += '<line x1="30" y1="' + fl_mid + '" x2="48" y2="' + fl_top + '" stroke="#4d7c0f" stroke-width="0.8" opacity="0.9"/>';
      }}
      const win_y = fl_top + 2;
      s += '<polygon points="16,' + win_y + ' 22,' + (win_y + 3.5) + ' 22,' + (win_y + 6.5) + ' 16,' + (win_y + 3) + '" fill="#fef08a"/>';
      s += '<polygon points="38,' + (win_y + 3.5) + ' 44,' + win_y + ' 44,' + (win_y + 3) + ' 38,' + (win_y + 6.5) + '" fill="#fef9c3"/>';
    }}
    s += '<circle cx="30" cy="' + (top_y + 1) + '" r="1.8" fill="#fef08a"/>';
    s += '<rect x="22" y="' + (top_y - 13) + '" width="16" height="7.5" rx="3" fill="#365314" stroke="#a3e635" stroke-width="0.8"/>';
    s += '<text x="30" y="' + (top_y - 7.5) + '" font-size="5.5" font-family="sans-serif" font-weight="bold" fill="#bef264" text-anchor="middle">' + fl + ' طوابق</text>';
    s += '</svg>';
    return s;
  }}

  function getTile3DArt(tile) {{
    if (tile.id === 0) return SVG_ASSETS.tile_go;
    if (tile.id === 1) return SVG_ASSETS.tile_oasis_villa;
    if (tile.id === 2 || tile.id === 17 || tile.id === 33) return SVG_ASSETS.tile_chest;
    if (tile.id === 3) return SVG_ASSETS.tile_lighthouse;
    if (tile.id === 4 || tile.id === 38) return SVG_ASSETS.tile_tax;
    if (tile.type === 'station') return SVG_ASSETS.tile_train;
    if (tile.id === 6 || tile.id === 8 || tile.id === 9) return SVG_ASSETS.tile_delta_townhouse;
    if (tile.id === 7 || tile.id === 22 || tile.id === 36) return SVG_ASSETS.tile_chance;
    if (tile.id === 10) return SVG_ASSETS.tile_jail;
    if (tile.id === 11 || tile.id === 13 || tile.id === 14) return SVG_ASSETS.tile_neoclassic_palace;
    if (tile.id === 12) return SVG_ASSETS.tile_electric;
    if (tile.id === 16 || tile.id === 18 || tile.id === 19) return SVG_ASSETS.tile_fayoum_waterwheel;
    if (tile.id === 20) return SVG_ASSETS.tile_parking;
    if (tile.id === 21 || tile.id === 23 || tile.id === 24) return SVG_ASSETS.tile_citadel;
    if (tile.id === 26 || tile.id === 27 || tile.id === 29) return SVG_ASSETS.tile_redsea_resort;
    if (tile.id === 28) return SVG_ASSETS.tile_water;
    if (tile.id === 30) return SVG_ASSETS.tile_gotojail;
    if (tile.id === 31 || tile.id === 32 || tile.id === 34) return SVG_ASSETS.tile_alex_palace;
    if (tile.id === 37) return SVG_ASSETS.tile_pyramid;
    if (tile.id === 39) return SVG_ASSETS.tile_cairo_tower;

    if (tile.group === 'brown') return SVG_ASSETS.tile_oasis_villa;
    if (tile.group === 'lightblue') return SVG_ASSETS.tile_delta_townhouse;
    if (tile.group === 'pink') return SVG_ASSETS.tile_neoclassic_palace;
    if (tile.group === 'orange') return SVG_ASSETS.tile_fayoum_waterwheel;
    if (tile.group === 'red') return SVG_ASSETS.tile_citadel;
    if (tile.group === 'yellow') return SVG_ASSETS.tile_redsea_resort;
    if (tile.group === 'green') return SVG_ASSETS.tile_alex_palace;
    if (tile.group === 'darkblue') return SVG_ASSETS.tile_cairo_tower;

    return SVG_ASSETS.tile_pyramid;
  }}

  // Center Diorama Card Controller (Replaces Pyramids on Card/Tax/Jail Events)
  let dioramaCardTimeout = null;
  let dioramaCardCallback = null;

  // Interactive Preview Functions for Tile Clicks & Header Quick Menu
  function previewChestCard() {{
    const card = CHEST_CARDS[Math.floor(Math.random() * CHEST_CARDS.length)];
    sfx.playVaultOpen();
    showCenterDioramaCard({{
      theme: 'chest',
      badge: '🎁 صندوق الدنيا (محفظة الشعب)',
      player: state.players[state.currentPlayerIdx],
      title: card.title,
      desc: card.desc,
      svgArt: SVG_ASSETS.tile_chest,
      btnText: 'حسناً، إغلاق الكارت',
      onAction: () => {{
        dismissCenterDioramaCard();
      }}
    }});
  }}

  function previewChanceCard() {{
    const card = CHANCE_CARDS[Math.floor(Math.random() * CHANCE_CARDS.length)];
    sfx.playChanceMystery();
    showCenterDioramaCard({{
      theme: 'chance',
      badge: '❓ كارت الحظ (جرب حظك)',
      player: state.players[state.currentPlayerIdx],
      title: card.title,
      desc: card.desc,
      svgArt: SVG_ASSETS.tile_chance,
      btnText: 'حسناً، إغلاق الكارت',
      onAction: () => {{
        dismissCenterDioramaCard();
      }}
    }});
  }}

  function previewIncomeTaxCard() {{
    sfx.playTaxStamp();
    showCenterDioramaCard({{
      theme: 'income_tax',
      badge: t('incomeTaxBadge'),
      player: state.players[state.currentPlayerIdx],
      title: t('incomeTaxTitle'),
      desc: t('incomeTaxDesc'),
      svgArt: SVG_ASSETS.tile_tax,
      btnText: t('btnCloseCard'),
      onAction: () => {{
        dismissCenterDioramaCard();
      }}
    }});
  }}

  function previewLuxuryTaxCard() {{
    sfx.playTaxStamp();
    showCenterDioramaCard({{
      theme: 'luxury_tax',
      badge: t('luxuryTaxBadge'),
      player: state.players[state.currentPlayerIdx],
      title: t('luxuryTaxTitle'),
      desc: t('luxuryTaxDesc'),
      svgArt: SVG_ASSETS.tile_tax,
      btnText: t('btnCloseCard'),
      onAction: () => {{
        dismissCenterDioramaCard();
      }}
    }});
  }}

  function previewJailCommandCard() {{
    sfx.playJail();
    showCenterDioramaCard({{
      theme: 'jail',
      badge: t('jailBadge'),
      player: state.players[state.currentPlayerIdx],
      title: t('jailTitle'),
      desc: t('jailDesc'),
      svgArt: SVG_ASSETS.tile_jail,
      btnText: t('btnCloseCard'),
      onAction: () => {{
        dismissCenterDioramaCard();
      }}
    }});
  }}

  function previewVisitingJailCard() {{
    sfx.playVisitJail();
    showCenterDioramaCard({{
      theme: 'visiting',
      badge: t('visitingBadge'),
      player: state.players[state.currentPlayerIdx],
      title: t('visitingTitle'),
      desc: t('visitingDesc'),
      svgArt: SVG_ASSETS.tile_jail,
      btnText: t('btnCloseCard'),
      onAction: () => {{
        dismissCenterDioramaCard();
      }}
    }});
  }}

  function showCenterDioramaCard(config) {{
    if (dioramaCardTimeout) {{
      clearTimeout(dioramaCardTimeout);
      dioramaCardTimeout = null;
    }}

    const box = document.getElementById('centerDioramaBox');
    const pyramidsLayer = document.getElementById('dioramaPyramidsLayer');
    const cardLayer = document.getElementById('dioramaCardLayer');

    if (box) {{
      box.className = 'center-diorama-container ' + (config.theme ? 'card-theme-' + config.theme : '');
    }}

    document.getElementById('dioramaCard3DArt').innerHTML = config.svgArt || SVG_ASSETS.tile_chest;
    document.getElementById('dioramaCardBadge').innerHTML = config.badge || 'بطاقة حدث';
    document.getElementById('dioramaCardPlayerTag').innerText = config.player ? config.player.name : '';
    document.getElementById('dioramaCardTitle').innerText = config.title || '';
    document.getElementById('dioramaCardDesc').innerText = config.desc || '';

    const actionBtn = document.getElementById('dioramaCardBtn');
    const actionBtnText = document.getElementById('dioramaCardBtnText');
    const isBot = config.player && config.player.isBot;

    actionBtn.disabled = isBot;
    if (isBot) {{
      actionBtnText.innerText = '🤖 جاري التنفيذ...';
    }} else {{
      actionBtnText.innerText = config.btnText || 'موافق';
    }}

    dioramaCardCallback = config.onAction || null;

    if (pyramidsLayer) pyramidsLayer.classList.add('hidden');
    if (cardLayer) cardLayer.classList.remove('hidden');

    if (isBot) {{
      const delay = config.autoExecDelay || 1700;
      dioramaCardTimeout = setTimeout(() => {{
        executeDioramaCardAction();
      }}, delay);
    }}
  }}

  function executeDioramaCardAction() {{
    if (dioramaCardTimeout) {{
      clearTimeout(dioramaCardTimeout);
      dioramaCardTimeout = null;
    }}
    const cb = dioramaCardCallback;
    dioramaCardCallback = null;
    dismissCenterDioramaCard();
    if (typeof cb === 'function') {{
      cb();
    }}
  }}

  function dismissCenterDioramaCard() {{
    if (dioramaCardTimeout) {{
      clearTimeout(dioramaCardTimeout);
      dioramaCardTimeout = null;
    }}
    dioramaCardCallback = null;
    const box = document.getElementById('centerDioramaBox');
    const pyramidsLayer = document.getElementById('dioramaPyramidsLayer');
    const cardLayer = document.getElementById('dioramaCardLayer');
    if (cardLayer && !cardLayer.classList.contains('hidden')) {{
      cardLayer.classList.add('hidden');
    }}
    if (pyramidsLayer && pyramidsLayer.classList.contains('hidden')) {{
      pyramidsLayer.classList.remove('hidden');
    }}
    if (box) {{
      box.className = 'center-diorama-container';
    }}
  }}


  const AVAILABLE_TOKENS = [
    {{
      id: 'pawn_classic',
      nameAr: 'بيدق الشطرنج الكلاسيكي',
      nameEn: 'Classic Chess Pawn',
      icon: '♟️',
      svgKey: 'token_pawn_classic'
    }},
    {{
      id: 'knight',
      nameAr: 'بيدق الفارس الملكي (الحصان)',
      nameEn: 'Royal Knight Horse',
      icon: '♞',
      svgKey: 'token_knight'
    }},
    {{
      id: 'rook',
      nameAr: 'بيدق القلعة الحصينة (البرج)',
      nameEn: 'Fortress Castle Tower',
      icon: '♜',
      svgKey: 'token_rook'
    }},
    {{
      id: 'crown',
      nameAr: 'بيدق التاج الإمبراطوري',
      nameEn: 'Imperial Golden Crown',
      icon: '👑',
      svgKey: 'token_crown'
    }},
    {{
      id: 'falcon',
      nameAr: 'بيدق صقر حورس الذهبي',
      nameEn: 'Horus Golden Falcon',
      icon: '🦅',
      svgKey: 'token_falcon'
    }},
    {{
      id: 'tarboosh',
      nameAr: 'طربوش الباشا الذهبي',
      nameEn: 'Pasha Golden Fez',
      icon: '🏮',
      svgKey: 'token_tarboosh'
    }},
    {{
      id: 'pharaoh',
      nameAr: 'القناع الفرعوني الذهبي',
      nameEn: 'Pharaoh Golden Mask',
      icon: '🪙',
      svgKey: 'token_pharaoh'
    }},
    {{
      id: 'bastet',
      nameAr: 'قطة باستيت الأسطورية',
      nameEn: 'Bastet Sacred Cat',
      icon: '🐈',
      svgKey: 'token_bastet'
    }},
    {{
      id: 'roadster',
      nameAr: 'سيارة الرودستر الفارهة',
      nameEn: 'Classic Roadster Car',
      icon: '🏎️',
      svgKey: 'token_roadster'
    }},
    {{
      id: 'rocket',
      nameAr: 'المكوك الفضائي الذهبي',
      nameEn: 'Cosmic Rocket',
      icon: '🚀',
      svgKey: 'token_rocket'
    }},
    {{
      id: 'diamond',
      nameAr: 'الماسة الكريستالية الفاخرة',
      nameEn: 'Royal Diamond Gem',
      icon: '💎',
      svgKey: 'token_diamond'
    }},
    {{
      id: 'mr_hazz',
      nameAr: 'مستر حظ (الرجل الأنيق)',
      nameEn: 'Mr. Hazz (Gentleman)',
      icon: '🎩',
      svgKey: 'fig_mr_hazz'
    }},
    {{
      id: 'cleopatra',
      nameAr: 'الملكة كليوباترا',
      nameEn: 'Queen Cleopatra',
      icon: '👸',
      svgKey: 'fig_cleopatra'
    }}
  ];

  let tokenPickerTargetPlayer = 0; // 0 = Player 1, 1 = Player 2
  let selectedTokenP1 = 'pawn_classic';
  let selectedTokenP2 = 'knight';

  try {{
    selectedTokenP1 = localStorage.getItem('bank_el_hazz_p1_token') || 'pawn_classic';
    selectedTokenP2 = localStorage.getItem('bank_el_hazz_p2_token') || 'knight';
  }} catch (e) {{}}

  function switchTokenPickerTarget(playerIdx) {{
    tokenPickerTargetPlayer = playerIdx;
    const tab1 = document.getElementById('tabPawnP1');
    const tab2 = document.getElementById('tabPawnP2');
    if (tab1) tab1.classList.toggle('active', playerIdx === 0);
    if (tab2) tab2.classList.toggle('active', playerIdx === 1);
    renderTokenPickerGrid();
  }}

  function renderTokenPickerGrid() {{
    const grid = document.getElementById('tokenPickerGrid');
    if (!grid) return;
    grid.innerHTML = '';

    const currentTokenId = (tokenPickerTargetPlayer === 0) ? selectedTokenP1 : selectedTokenP2;

    AVAILABLE_TOKENS.forEach(token => {{
      const isSelected = (token.id === currentTokenId);
      const card = document.createElement('div');
      card.className = `token-card ${{isSelected ? 'active' : ''}}`;
      card.onclick = () => selectPlayerToken(token.id);

      const name = currentLanguage === 'ar' ? token.nameAr : token.nameEn;
      const badgeText = isSelected 
        ? (currentLanguage === 'ar' ? '✓ البيدق الحالي' : '✓ Active Pawn') 
        : (currentLanguage === 'ar' ? 'اختر هذا' : 'Select');

      card.innerHTML = `
        <div class="token-card-preview">
          ${{SVG_ASSETS[token.svgKey] || ''}}
        </div>
        <div class="token-card-name">${{token.icon}} ${{name}}</div>
        <div class="token-card-badge">${{badgeText}}</div>
      `;

      grid.appendChild(card);
    }});
  }}

  function selectPlayerToken(tokenId, save = true) {{
    const tokenObj = AVAILABLE_TOKENS.find(t => t.id === tokenId);
    if (!tokenObj || !SVG_ASSETS[tokenObj.svgKey]) return;

    const pIdx = tokenPickerTargetPlayer;
    if (pIdx === 0) selectedTokenP1 = tokenId;
    else selectedTokenP2 = tokenId;

    if (state && state.players && state.players[pIdx]) {{
      state.players[pIdx].tokenSvg = SVG_ASSETS[tokenObj.svgKey];
      state.players[pIdx].avatar = tokenObj.icon;
    }}

    // Update duel bar avatar
    const avatarBox = document.getElementById(pIdx === 0 ? 'avatarP1Box' : 'avatarP2Box');
    if (avatarBox) {{
      avatarBox.innerHTML = SVG_ASSETS[tokenObj.svgKey];
    }}

    // Update board 3D token
    const boardToken = document.getElementById(`player-token-${{pIdx}}`);
    if (boardToken) {{
      boardToken.innerHTML = SVG_ASSETS[tokenObj.svgKey];
    }}

    if (save) {{
      try {{
        localStorage.setItem(pIdx === 0 ? 'bank_el_hazz_p1_token' : 'bank_el_hazz_p2_token', tokenId);
      }} catch (e) {{}}
      if (typeof sfx !== 'undefined' && typeof sfx.playCoin === 'function') sfx.playCoin();
      const tokenName = currentLanguage === 'ar' ? tokenObj.nameAr : tokenObj.nameEn;
      const targetLabel = pIdx === 0 
        ? (currentLanguage === 'ar' ? 'اللاعب 1' : 'Player 1') 
        : (currentLanguage === 'ar' ? 'المنافس (اللاعب 2)' : 'Rival (Player 2)');
      addLog(`🎭 ${{currentLanguage === 'ar' ? `تم تغيير بيدق ${{targetLabel}} إلى: <b>${{tokenName}}</b>` : `${{targetLabel}} pawn changed to: <b>${{tokenName}}</b>`}}`);
    }}

    renderTokenPickerGrid();
  }}

  // Rules Modal Tab Navigation
  function switchRulesTab(tab) {{
    const btnGen = document.getElementById('tabRulesBtnGeneral');
    const btnCards = document.getElementById('tabRulesBtnCards');
    const contentGen = document.getElementById('rulesContentGeneral');
    const contentCards = document.getElementById('rulesContentCards');

    if (tab === 'cards') {{
      if (btnGen) btnGen.classList.remove('active');
      if (btnCards) btnCards.classList.add('active');
      if (contentGen) contentGen.classList.remove('active');
      if (contentCards) contentCards.classList.add('active');
    }} else {{
      if (btnGen) btnGen.classList.add('active');
      if (btnCards) btnCards.classList.remove('active');
      if (contentGen) contentGen.classList.add('active');
      if (contentCards) contentCards.classList.remove('active');
    }}
  }}

  // Police Siren & Smooth Shortest-Path Pawn Jail Movement Animation
  async function animatePawnToJail(player, onArrival) {{
    const targetPos = 10;
    const currentPos = player.position;

    if (currentPos === targetPos) {{
      triggerJailGateSlam();
      if (onArrival) onArrival();
      return;
    }}

    // Calculate shortest path: forward vs backward
    const fwdDist = (targetPos - currentPos + 40) % 40;
    const backDist = (currentPos - targetPos + 40) % 40;
    const goForward = (fwdDist <= backDist);
    const stepDelta = goForward ? 1 : -1;
    const totalSteps = goForward ? fwdDist : backDist;

    // Play police siren with duration matching transit
    const duration = Math.min(2.5, Math.max(1.2, totalSteps * 0.075));
    if (typeof sfx !== 'undefined' && typeof sfx.playPoliceSiren === 'function') {{
      sfx.playPoliceSiren(duration);
    }}

    // Step-by-step smooth movement
    const stepDelay = Math.max(30, Math.min(65, Math.floor((duration * 1000) / totalSteps)));

    for (let step = 1; step <= totalSteps; step++) {{
      player.position = (player.position + stepDelta + 40) % 40;
      renderTokens(player);
      if (typeof sfx !== 'undefined' && typeof sfx.playPawnHop === 'function') {{
        sfx.playPawnHop();
      }}
      await new Promise(r => setTimeout(r, stepDelay));
    }}

    player.position = targetPos;
    renderTokens();

    // Trigger Jail Gate Drop and Clank
    triggerJailGateSlam();

    if (onArrival) onArrival();
  }}

  function triggerJailGateSlam() {{
    const tile10 = document.getElementById('tile-10');
    let cage = document.getElementById('jailIronBarsOverlay');
    if (!cage && tile10) {{
      cage = document.createElement('div');
      cage.id = 'jailIronBarsOverlay';
      cage.className = 'jail-iron-bars-overlay';
      cage.innerHTML = SVG_ASSETS.jail_cage_3d || '';
      tile10.appendChild(cage);
    }}

    if (cage) {{
      cage.classList.remove('dropping', 'active');
      void cage.offsetWidth;
      cage.classList.add('dropping');
    }}

    if (tile10) {{
      tile10.classList.remove('jail-tile-slam-shake');
      void tile10.offsetWidth;
      tile10.classList.add('jail-tile-slam-shake');
    }}

    if (typeof sfx !== 'undefined' && typeof sfx.playJailGateSlam === 'function') {{
      setTimeout(() => sfx.playJailGateSlam(), 400);
    }}
  }}

  function updateJailGateVisibility() {{
    const cage = document.getElementById('jailIronBarsOverlay');
    if (!cage) return;
    const anyoneInJail = state.players && state.players.some(p => p.inJail && !p.isBankrupt);
    if (anyoneInJail) {{
      cage.classList.add('active');
    }} else {{
      cage.classList.remove('active', 'dropping');
    }}
  }}

  function renderAboutUsContent() {{
    const content = document.getElementById('aboutUsModalContent');
    if (!content) return;
    if (currentLanguage === 'ar') {{
      content.innerHTML = `
        <div style="text-align: center; margin-bottom: 16px;">
          <div style="font-size: 44px; margin-bottom: 6px;">🎩🏰🌟</div>
          <h2 style="font-size: 20px; color: #38bdf8; margin: 0 0 4px 0; font-weight: 900;">بنك الحظ 3D - النسخة الفاخرة ($)</h2>
          <div style="font-size: 13px; color: #f59e0b; font-weight: 700;">محاكاة رقمية مجسمة متطورة للعبة اللوحة الكلاسيكية بالدولار</div>
        </div>

        <!-- Developer Highlight Card -->
        <div style="background: linear-gradient(135deg, rgba(14, 165, 233, 0.22), rgba(30, 41, 59, 0.95)); border: 2px solid #38bdf8; border-radius: 14px; padding: 14px 16px; margin-bottom: 14px; text-align: center; box-shadow: 0 6px 20px rgba(56, 189, 248, 0.25);">
          <div style="font-size: 11px; color: #94a3b8; font-weight: 700; text-transform: uppercase; margin-bottom: 4px;">فكرة وإعداد وبرمجة وتطوير</div>
          <div style="font-size: 21px; color: #38bdf8; font-weight: 900; margin-bottom: 4px; display: flex; align-items: center; justify-content: center; gap: 8px;">
            <span style="font-size: 24px;">💻</span>
            <span>برمجة وتطوير: <span style="color: #fef08a;">عمار الهلالي</span></span>
          </div>
          <div style="font-size: 12px; color: #e2e8f0; font-weight: 600;">Programming & Development: Ammar Al-Hilali</div>
        </div>

        <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; border-radius: 12px; padding: 12px 14px; margin-bottom: 12px;">
          <h4 style="color: #fef08a; margin: 0 0 6px 0; font-size: 14.5px;">🌟 عن اللعبة:</h4>
          <p style="margin: 0; line-height: 1.8; color: #cbd5e1; font-size: 12.5px;">
            <b>بنك الحظ 3D</b> هي تجربة استراتيجية تفاعلية تعيد إحياء اللعبة الأكثر شهرة بنكهة عالمية بالدولار ($). صُممت بأحدث تقنيات الويب (HTML5 و CSS 3D و Web Audio API) مع محاكاة فيزيائية واقعية للبيادق ونرد اللعب وتأثيرات سجن القلعة بالسياج الحديدي وصافرات الشرطة.
          </p>
        </div>

        <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; border-radius: 12px; padding: 12px 14px; margin-bottom: 12px;">
          <h4 style="color: #38bdf8; margin: 0 0 6px 0; font-size: 14.5px;">🚀 أبرز المميزات:</h4>
          <ul style="margin: 0; padding-right: 18px; line-height: 1.85; color: #cbd5e1; font-size: 12.5px;">
            <li><b>عملة الدولار ($):</b> اعتماد عملة الدولار ($) في كامل الرقعة، العقارات، الكروت، والمفاوضات.</li>
            <li><b>مكتبة بيادق ثلاثية الأبعاد (13 تصميماً):</b> إمكانية تخصيص وتغيير بيدق كل من اللاعب الأول والمنافس بحرية.</li>
            <li><b>سجن القلعة الديناميكي:</b> انتقال سلس بأقصر مسار مع صافرة الشرطة وإسقاط السور الحديدي مع قفل ثقيل وصوت إغلاق الزنزانة.</li>
            <li><b>شروط الكروت:</b> تبويب خاص داخل القواعد يوضح شروط كافة كروت الصندوق والحظ والضرائب.</li>
            <li><b>ذكاء اصطناعي تفاوضي:</b> 3 مستويات احترافية مع نظام مساومة ومفاوضات شراء مباشر.</li>
            <li><b>دعم لغوي شامل:</b> ترجمة حية لـ 14 لغة عالمية مع تحويل الاتجاه RTL/LTR تلقائياً.</li>
          </ul>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(15, 23, 42, 0.8); border: 1px dashed #475569; border-radius: 10px; padding: 10px 14px; font-size: 11.5px; color: #94a3b8;">
          <div>الإصدار: <span style="color: #10b981; font-weight: 800;">v3.6 Pro Dollar Edition</span></div>
          <div>برمجة وتطوير: <span style="color: #38bdf8; font-weight: 900;">عمار الهلالي</span></div>
        </div>
      `;
    }} else {{
      content.innerHTML = `
        <div style="text-align: center; margin-bottom: 16px;">
          <div style="font-size: 44px; margin-bottom: 6px;">🎩🏰🌟</div>
          <h2 style="font-size: 20px; color: #38bdf8; margin: 0 0 4px 0; font-weight: 900;">Bank El Hazz 3D - Pro Edition ($)</h2>
          <div style="font-size: 13px; color: #f59e0b; font-weight: 700;">Matte Physical 3D Digital Tabletop Experience in USD ($)</div>
        </div>

        <!-- Developer Highlight Card -->
        <div style="background: linear-gradient(135deg, rgba(14, 165, 233, 0.22), rgba(30, 41, 59, 0.95)); border: 2px solid #38bdf8; border-radius: 14px; padding: 14px 16px; margin-bottom: 14px; text-align: center; box-shadow: 0 6px 20px rgba(56, 189, 248, 0.25);">
          <div style="font-size: 11px; color: #94a3b8; font-weight: 700; text-transform: uppercase; margin-bottom: 4px;">System Engineering & Game Development</div>
          <div style="font-size: 20px; color: #38bdf8; font-weight: 900; margin-bottom: 4px; display: flex; align-items: center; justify-content: center; gap: 8px;">
            <span style="font-size: 24px;">💻</span>
            <span>Programming & Development: <span style="color: #fef08a;">Ammar Al-Hilali</span></span>
          </div>
          <div style="font-size: 12px; color: #fef08a; font-weight: 700;">(برمجة وتطوير: عمار الهلالي)</div>
        </div>

        <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; border-radius: 12px; padding: 12px 14px; margin-bottom: 12px;">
          <h4 style="color: #fef08a; margin: 0 0 6px 0; font-size: 14.5px;">🌟 About The Game:</h4>
          <p style="margin: 0; line-height: 1.8; color: #cbd5e1; font-size: 12.5px;">
            <b>Bank El Hazz 3D</b> is a high-stakes strategic duel experience inspired by classic board game legacy. Built with modern web tech (HTML5, CSS 3D, Web Audio API), featuring authentic USD ($) economy, 13 pawn styles, and animated jail transfer with police sirens and dropping iron bars.
          </p>
        </div>

        <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; border-radius: 12px; padding: 12px 14px; margin-bottom: 12px;">
          <h4 style="color: #38bdf8; margin: 0 0 6px 0; font-size: 14.5px;">🚀 Key Features:</h4>
          <ul style="margin: 0; padding-left: 18px; line-height: 1.85; color: #cbd5e1; font-size: 12.5px;">
            <li><b>USD ($) Economy:</b> Standardized dollar currency across all tiles, cards, and trade.</li>
            <li><b>13 3D Pawn Styles:</b> Custom pawn selection for both Player 1 and Rival with immediate board update.</li>
            <li><b>Animated Jail Transfer:</b> Shortest-path smooth pawn transit with police siren and dropping iron gate slam.</li>
            <li><b>Card Guide:</b> Detailed rules tab outlining every card reward and condition.</li>
            <li><b>14-Language Engine:</b> Full UI and property translation with RTL/LTR support.</li>
          </ul>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(15, 23, 42, 0.8); border: 1px dashed #475569; border-radius: 10px; padding: 10px 14px; font-size: 11.5px; color: #94a3b8;">
          <div>Version: <span style="color: #10b981; font-weight: 800;">v3.6 Pro Dollar Edition</span></div>
          <div>Developer: <span style="color: #38bdf8; font-weight: 900;">Ammar Al-Hilali</span></div>
        </div>
      `;
    }}
  }}

  // Initialize strictly 2 Players
  function initGame(config = null) {{
    const cfg = config || currentSetup;
    const startingMoney = cfg.money || 6000;
    const mode = cfg.mode || 'bot'; // 'bot' or 'human'
    const isBot = mode === 'bot';
    const p1Name = (cfg.p1Name || 'مستر حظ').trim() || 'مستر حظ';
    const p2Name = isBot ? 'روبوت' : ((cfg.p2Name || 'اللاعب الثاني').trim() || 'اللاعب الثاني');
    const difficulty = cfg.difficulty || 'medium'; // 'easy', 'medium', 'hard'

    state.startingMoney = startingMoney;
    state.gameMode = mode;
    state.aiDifficulty = difficulty;
    state.currentPlayerIdx = 0;
    state.freeParkingPot = 200;
    state.boardLevel = 1;
    state.doublesCount = 0;
    state.isRolling = false;
    state.tileOwnership = {{}};

    const p1TokenObj = AVAILABLE_TOKENS.find(t => t.id === selectedTokenP1) || AVAILABLE_TOKENS[0];
    const p2TokenObj = AVAILABLE_TOKENS.find(t => t.id === selectedTokenP2) || AVAILABLE_TOKENS[1];

    state.players = [
      {{
        id: 0,
        name: p1Name,
        title: "الملياردير الطموح",
        avatar: p1TokenObj.icon,
        color: "#b91c1c",
        accent: "#f59e0b",
        tokenSvg: SVG_ASSETS[p1TokenObj.svgKey] || SVG_ASSETS.token_pawn_classic,
        isBot: false,
        money: startingMoney,
        position: 0,
        rolls: 50,
        shields: 3,
        inJail: false,
        jailTurns: 0,
        jailCards: 0,
        landmarks: {{ pyramids: 0, cairo_tower: 0, citadel: 0, alex_lighthouse: 0, luxor_temple: 0 }},
        netWorth: startingMoney,
        isBankrupt: false
      }},
      {{
        id: 1,
        name: p2Name,
        title: isBot ? "الذكاء الاصطناعي الخارق" : "المنافس الشجاع",
        avatar: isBot ? "🤖" : p2TokenObj.icon,
        color: "#1e3a8a",
        accent: "#d97706",
        tokenSvg: SVG_ASSETS[p2TokenObj.svgKey] || SVG_ASSETS.token_knight,
        isBot: isBot,
        money: startingMoney,
        position: 0,
        rolls: 50,
        shields: 3,
        inJail: false,
        jailTurns: 0,
        jailCards: 0,
        landmarks: {{ pyramids: 0, cairo_tower: 0, citadel: 0, alex_lighthouse: 0, luxor_temple: 0 }},
        netWorth: startingMoney,
        isBankrupt: false
      }}
    ];

    // Load Center Diorama (Pyramids Layer)
    dismissCenterDioramaCard();
    document.getElementById('dioramaPyramidsLayer').innerHTML = SVG_ASSETS.center_diorama;

    // Load Player Avatars in Duel Bar
    document.getElementById('avatarP1Box').innerHTML = state.players[0].tokenSvg;
    document.getElementById('avatarP2Box').innerHTML = state.players[1].tokenSvg;

    renderBoardTiles();
    updateUI();

    const diffNames = {{ easy: 'سهل', medium: 'متوسط', hard: 'صعب' }};
    const modeDesc = isBot ? `ضد الكمبيوتر [روبوت] (مستوى: ${{diffNames[difficulty]}})` : `لاعبين اثنين: [${{p1Name}}] ضد [${{p2Name}}]`;
    addLog(`⚔️ بدأت لعبة جديدة! ${{modeDesc}} - ميزانية الانطلاق: ${{startingMoney}} $!`, 'gold');
  }}

  // Render the 40 Tiles on CSS Grid
  function renderBoardTiles() {{
    const grid = document.getElementById('boardGrid');
    
    // Remove existing tile elements
    const oldTiles = grid.querySelectorAll('.tile');
    oldTiles.forEach(t => t.remove());

    TILES.forEach(tile => {{
      const pos = getTileGridPos(tile.id);
      const tileDiv = document.createElement('div');
      tileDiv.className = 'tile';
      tileDiv.id = `tile-${{tile.id}}`;
      tileDiv.style.gridRow = pos.row;
      tileDiv.style.gridColumn = pos.col;

      const art3D = getTile3DArt(tile);

      if ([0, 10, 20, 30].includes(tile.id)) {{
        tileDiv.classList.add('tile-corner');
        let cageOverlay = (tile.id === 10) ? `<div class="jail-iron-bars-overlay" id="jailIronBarsOverlay">${{SVG_ASSETS.jail_cage_3d || ''}}</div>` : '';
        tileDiv.innerHTML = `
          <div class="corner-title">${{tile.name}}</div>
          <div class="tile-3d-art">${{art3D}}</div>
          <div class="corner-sub">${{tile.subtitle}}</div>
          <div class="player-tokens-container" id="tokens-${{tile.id}}"></div>
          ${{cageOverlay}}
        `;
      }} else {{
        let bannerHtml = '';
        if (tile.type === 'property') {{
          bannerHtml = `<div class="color-bar" style="background: ${{tile.color}};"></div>`;
        }} else {{
          bannerHtml = `<div class="color-bar" style="background: #a8a29e;"></div>`;
        }}

        tileDiv.innerHTML = `
          ${{bannerHtml}}
          <div class="tile-buildings-3d" id="buildings-${{tile.id}}"></div>
          <div class="tile-3d-art">${{art3D}}</div>
          <div class="tile-name">${{tile.name}}</div>
          ${{tile.price > 0 ? `<div class="tile-price">${{tile.price}} ${{getCurrency()}}</div>` : `<div style="font-size:8px; color:#78350f; font-weight:700;">${{tile.subtitle}}</div>`}}
          <div class="owner-indicator" id="owner-bar-${{tile.id}}"></div>
          <div class="player-tokens-container" id="tokens-${{tile.id}}"></div>
        `;
      }}

      tileDiv.addEventListener('click', () => {{
        if (tile.type === 'chest') {{
          previewChestCard();
        }} else if (tile.type === 'chance') {{
          previewChanceCard();
        }} else if (tile.type === 'tax') {{
          if (tile.id === 4) {{
            previewIncomeTaxCard();
          }} else {{
            previewLuxuryTaxCard();
          }}
        }} else if (tile.type === 'gotojail') {{
          previewJailCommandCard();
        }} else if (tile.type === 'jail') {{
          previewVisitingJailCard();
        }} else {{
          openDeedModal(tile.id);
        }}
      }});

      grid.appendChild(tileDiv);
    }});

    renderTokens();
    updateTileOwnershipVisuals();
  }}

  // Persistent Player 3D Figurine Tokens: Guarantees rival pawn remains completely motionless
  function renderTokens(movingPlayer = null) {{
    state.players.forEach(p => {{
      let token = document.getElementById(`player-token-${{p.id}}`);

      if (p.isBankrupt) {{
        if (token && token.parentNode) token.parentNode.removeChild(token);
        return;
      }}

      if (!token) {{
        token = document.createElement('div');
        token.id = `player-token-${{p.id}}`;
        token.className = `board-token-3d token-p${{p.id}}`;
        token.innerHTML = p.tokenSvg;
      }}
      token.title = `${{p.name}} (${{p.money}} $)`;

      const targetCont = document.getElementById(`tokens-${{p.position}}`);
      if (targetCont && token.parentNode !== targetCont) {{
        targetCont.appendChild(token);
      }}

      // ONLY the actively moving player hops; the rival remains completely still with zero flashing
      if (movingPlayer && p.id === movingPlayer.id) {{
        token.classList.remove('stepping');
        void token.offsetWidth;
        token.classList.add('stepping');
      }} else {{
        token.classList.remove('stepping');
      }}
    }});
  }}

  // Update Visual Indicators for Properties
  function updateTileOwnershipVisuals() {{
    TILES.forEach(t => {{
      const tileDiv = document.getElementById(`tile-${{t.id}}`);
      const buildingsCont = document.getElementById(`buildings-${{t.id}}`);
      const ownerBar = document.getElementById(`owner-bar-${{t.id}}`);
      if (!tileDiv) return;

      const record = state.tileOwnership[t.id];
      if (record && record.ownerId !== null) {{
        const owner = state.players[record.ownerId];
        tileDiv.classList.add('owned');
        tileDiv.style.setProperty('--owner-color', owner.color);
        if (ownerBar) ownerBar.style.background = owner.color;

        if (record.mortgaged) {{
          tileDiv.classList.add('mortgaged');
        }} else {{
          tileDiv.classList.remove('mortgaged');
        }}

        if (buildingsCont) {{
          buildingsCont.innerHTML = '';
          if (record.houses === 5) {{
            buildingsCont.innerHTML = `<div class="building-eiffel-3d" title="برج إيفل الذهبي (5 طوابق - الحد النهائي)">${{SVG_ASSETS.golden_eiffel_3d}}</div>`;
          }} else if (record.houses > 0) {{
            buildingsCont.innerHTML = `<div class="building-lime-3d" title="مبنى ليموني (${{record.houses}} طوابق)">${{getLimeBuildingSvg(record.houses)}}</div>`;
          }}
        }}
      }} else {{
        tileDiv.classList.remove('owned');
        tileDiv.classList.remove('mortgaged');
        if (ownerBar) ownerBar.style.background = 'transparent';
        if (buildingsCont) buildingsCont.innerHTML = '';
      }}
    }});
  }}

  // Update UI for 2-Player Clash Arena
  function updateUI() {{
    const p1 = state.players[0];
    const p2 = state.players[1];
    const curr = state.players[state.currentPlayerIdx];

    const curUnit = getCurrency();
    const netLabel = t('netWorth', 'الثروة');

    // Player 1 Stats
    document.getElementById('nameP1Display').innerText = p1.name;
    document.getElementById('moneyP1Display').innerText = `${{p1.money}} ${{curUnit}}`;
    document.getElementById('netWorthP1Display').innerText = `${{netLabel}}: ${{p1.netWorth}} ${{curUnit}}`;
    updateShieldsRow('shieldsP1Row', p1.shields);
    document.getElementById('cardP1').className = `player-duel-card p1 ${{state.currentPlayerIdx === 0 ? 'active-turn' : ''}}`;
    document.getElementById('subP1Display').innerText = p2.isBot ? (currentLanguage === 'ar' ? '(أنت)' : '(You)') : (currentLanguage === 'ar' ? 'لاعب 1 🎩' : 'Player 1 🎩');

    // Player 2 Stats
    document.getElementById('nameP2Display').innerText = p2.name;
    document.getElementById('moneyP2Display').innerText = `${{p2.money}} ${{curUnit}}`;
    document.getElementById('netWorthP2Display').innerText = `${{netLabel}}: ${{p2.netWorth}} ${{curUnit}}`;
    updateShieldsRow('shieldsP2Row', p2.shields);
    document.getElementById('cardP2').className = `player-duel-card p2 ${{state.currentPlayerIdx === 1 ? 'active-turn' : ''}}`;

    const p2Badge = document.getElementById('badgeP2Display');
    if (p2Badge) {{
      if (p2.isBot) {{
        const diffMap = {{ easy: t('diffEasy', 'سهل'), medium: t('diffMedium', 'متوسط'), hard: t('diffHard', 'صعب') }};
        p2Badge.innerText = `${{t('botDefault', 'روبوت')}} 🤖 (${{diffMap[state.aiDifficulty] || diffMap.medium}})`;
        p2Badge.className = 'duel-bot-pill';
      }} else {{
        p2Badge.innerText = currentLanguage === 'ar' ? 'لاعب 2 👑' : 'Player 2 👑';
        p2Badge.className = 'duel-human-pill';
      }}
    }}

    // Center Indicators
    document.getElementById('potAmountDisplay').innerText = `${{state.freeParkingPot}} ${{curUnit}}`;
    document.getElementById('rollsLeftDisplay').innerText = curr.rolls;
    document.getElementById('turnAvatarSpan').innerText = curr.avatar;

    if (curr.isBot) {{
      document.getElementById('turnStatusText').innerText = currentLanguage === 'ar' ? `دور ${{curr.name}} (ذكاء آلي يفكر ويتصرف... 🤖)` : `${{curr.name}}'s turn (AI thinking... 🤖)`;
      document.getElementById('btnRollDice').disabled = true;
    }} else {{
      document.getElementById('turnStatusText').innerText = currentLanguage === 'ar' ? `دورك يا ${{curr.name}}! اضغط "${{t('btnRollDice')}}" للانطلاق 🎲` : `Your turn, ${{curr.name}}! Click "${{t('btnRollDice')}}" 🎲`;
      document.getElementById('btnRollDice').disabled = state.isRolling;
    }}

    renderTokens();
    updateJailGateVisibility();
    updateTileOwnershipVisuals();
  }}

  function updateShieldsRow(rowId, shieldCount) {{
    const badges = document.getElementById(rowId).querySelectorAll('.shield-3d-badge');
    badges.forEach((b, idx) => {{
      if (idx < shieldCount) b.classList.add('active');
      else b.classList.remove('active');
    }});
  }}

  // Activity Log
  function addLog(msg, colorClass = '') {{
    const logBox = document.getElementById('activityLog');
    const time = new Date().toLocaleTimeString('ar-EG', {{ hour: '2-digit', minute: '2-digit', second: '2-digit' }});
    const entry = document.createElement('div');
    entry.className = `log-entry ${{colorClass}}`;
    entry.innerHTML = `<div class="log-time">${{time}}</div><div>${{msg}}</div>`;
    logBox.insertBefore(entry, logBox.firstChild);
  }}

  // Floating Cash Visual FX
  function showFloatingFX(text, isPositive = true, targetTileId = null) {{
    const fx = document.createElement('div');
    fx.className = `floating-fx ${{isPositive ? 'plus' : 'minus'}}`;
    fx.innerText = text;

    let posX = window.innerWidth / 2;
    let posY = window.innerHeight / 2;

    if (targetTileId !== null) {{
      const tileElem = document.getElementById(`tile-${{targetTileId}}`);
      if (tileElem) {{
        const rect = tileElem.getBoundingClientRect();
        posX = rect.left + rect.width / 2;
        posY = rect.top + rect.height / 2;
      }}
    }}

    fx.style.left = `${{posX}}px`;
    fx.style.top = `${{posY}}px`;
    document.body.appendChild(fx);

    setTimeout(() => fx.remove(), 1500);
  }}

  // 3D Dice Roll
  function rollDiceAction() {{
    if (state.isRolling) return;
    const player = state.players[state.currentPlayerIdx];
    if (player.isBankrupt) return;

    if (player.rolls < 1) {{
      player.rolls += 10;
      addLog(`⚡ تم تزويد ${{player.name}} بـ 10 نرد إضافي تلقائياً!`, 'gold');
    }}
    player.rolls = Math.max(0, player.rolls - 1);

    state.isRolling = true;
    document.getElementById('btnRollDice').disabled = true;

    sfx.playDiceRoll();

    const die1 = document.getElementById('die1');
    const die2 = document.getElementById('die2');
    die1.classList.add('rolling');
    die2.classList.add('rolling');

    const d1 = Math.floor(Math.random() * 6) + 1;
    const d2 = Math.floor(Math.random() * 6) + 1;
    state.dice = [d1, d2];

    setTimeout(() => {{
      die1.classList.remove('rolling');
      die2.classList.remove('rolling');

      setDieTransform(die1, d1);
      setDieTransform(die2, d2);

      const isDoubles = d1 === d2;
      const totalSteps = d1 + d2;
      addLog(`🎲 رمى ${{player.name}} النرد: [${{d1}}] و [${{d2}}] = مجموع ${{totalSteps}}! ${{isDoubles ? '🔥 (دبل!)' : ''}}`, isDoubles ? 'gold' : '');

      if (player.inJail) {{
        if (isDoubles) {{
          player.inJail = false;
          player.jailTurns = 0;
          addLog(`🗝️ أطلق سراح ${{player.name}} من السجن بفضل رمية الدبل!`, 'green');
          sfx.playFanfare();
          movePlayerSteps(player, totalSteps);
        }} else {{
          player.jailTurns++;
          if (player.jailTurns >= 3) {{
            player.money = Math.max(0, player.money - 50);
            state.freeParkingPot += 50;
            player.inJail = false;
            player.jailTurns = 0;
            addLog(`💸 دفع ${{player.name}} كفالة 50 $ إجبارية وتم إخلاء سبيله!`, 'red');
            movePlayerSteps(player, totalSteps);
          }} else {{
            addLog(`⛓️ ${{player.name}} لا يزال في سجن القلعة (${{player.jailTurns}} من 3).`, 'red');
            state.isRolling = false;
            sfx.playJail();
            showCenterDioramaCard({{
              theme: 'jail',
              badge: '⛓️ سجن القلعة',
              player: player,
              title: `لا يزال محبوساً! (${{player.jailTurns}} من 3)`,
              desc: `فشلت محاولة رمي الدبل! متبقي ${{3 - player.jailTurns}} محاولة قبل فرض كفالة 50 $ إجبارية.`,
              svgArt: SVG_ASSETS.tile_jail,
              btnText: 'إنهاء الدور',
              autoExecDelay: 1700,
              onAction: () => {{
                endTurn();
              }}
            }});
          }}
        }}
        return;
      }}

      if (isDoubles) {{
        state.doublesCount++;
        if (state.doublesCount === 3) {{
          addLog(`🚨 رمى ${{player.name}} الدبل 3 مرات متتالية! إلى السجن فوراً!`, 'red');
          sendToJail(player);
          return;
        }}
      }} else {{
        state.doublesCount = 0;
      }}

      movePlayerSteps(player, totalSteps, isDoubles);

    }}, DICE_SPEED_DELAYS[gameSettings.diceSpeed] || 800);
  }}

  function setDieTransform(cubeElem, val) {{
    const transforms = {{
      1: 'rotateY(0deg) rotateX(0deg)',
      2: 'rotateY(90deg) rotateX(0deg)',
      3: 'rotateX(-90deg) rotateY(0deg)',
      4: 'rotateX(90deg) rotateY(0deg)',
      5: 'rotateY(-90deg) rotateX(0deg)',
      6: 'rotateY(180deg) rotateX(0deg)'
    }};
    cubeElem.style.transform = transforms[val];
  }}

  // Step-by-Step Hop Movement
  function movePlayerSteps(player, steps, isDoubles = false) {{
    let currentStep = 0;
    const interval = setInterval(() => {{
      currentStep++;
      player.position = (player.position + 1) % 40;
      
      if (player.position === 0) {{
        const goReward = 200;
        player.money += goReward;
        player.netWorth += goReward;
        sfx.playCoin();
        showFloatingFX(`+${{goReward}} $`, true, 0);
        addLog(`🚀 مر ${{player.name}} بنقطة انطلق ونال مكافأة ${{goReward}} $!`, 'green');
      }}

      renderTokens(player);

      if (currentStep >= steps) {{
        clearInterval(interval);
        state.isRolling = false;
        renderTokens(null);
        handleTileArrival(player, isDoubles);
      }}
    }}, MOVE_SPEED_DELAYS[gameSettings.moveSpeed] || 120);
  }}

  // Tile Actions
  function handleTileArrival(player, isDoubles) {{
    const tile = TILES[player.position];
    addLog(`📍 وصل ${{player.name}} إلى [${{tile.name}}] (${{tile.subtitle}})`);

    switch (tile.type) {{
      case 'go':
        const bonus = 200;
        player.money += bonus;
        player.netWorth += bonus;
        sfx.playCoin();
        showFloatingFX(`+${{bonus}} $`, true, tile.id);
        finishArrivalAction(player, isDoubles);
        break;

      case 'property':
      case 'station':
      case 'utility':
        handlePropertyArrival(player, tile, isDoubles);
        break;

      case 'tax':
        if (tile.id === 4) {{
          // 1. ضريبة الدخل
          const taxVal = 200;
          sfx.playTaxStamp();
          showCenterDioramaCard({{
            theme: 'income_tax',
            badge: '💸 مصلحة الضرائب المصرية',
            player: player,
            title: 'ضريبة الدخل العامة (200 $)',
            desc: 'يتعين عليك سداد ضريبة دخل حكومية بقيمة 200 $ تُحوّل فوراً لحصيلة وعاء الاستراحة المجانية!',
            svgArt: SVG_ASSETS.tile_tax,
            btnText: 'دفع 200 $',
            autoExecDelay: 1700,
            onAction: () => {{
              player.money = Math.max(0, player.money - taxVal);
              state.freeParkingPot += taxVal;
              sfx.playChaChing();
              showFloatingFX(`-${{taxVal}} $`, false, 4);
              addLog(`💸 سدد ${{player.name}} ضريبة الدخل (${{taxVal}} $) وتم إيداعها بوعاء الاستراحة!`, 'red');
              updateUI();
              finishArrivalAction(player, isDoubles);
            }}
          }});
        }} else {{
          // 2. ضريبة الرفاهية
          const taxVal = 100;
          sfx.playTaxStamp();
          showCenterDioramaCard({{
            theme: 'luxury_tax',
            badge: '💎 مصلحة الضرائب',
            player: player,
            title: 'ضريبة الرفاهية والكماليات (100 $)',
            desc: 'رسم إضافي على المقتنيات والكماليات الفاخرة بقيمة 100 $ تودع في وعاء الاستراحة المجانية!',
            svgArt: SVG_ASSETS.tile_tax,
            btnText: 'دفع 100 $',
            autoExecDelay: 1700,
            onAction: () => {{
              player.money = Math.max(0, player.money - taxVal);
              state.freeParkingPot += taxVal;
              sfx.playChaChing();
              showFloatingFX(`-${{taxVal}} $`, false, 38);
              addLog(`💎 سدد ${{player.name}} ضريبة الرفاهية (${{taxVal}} $) وتم إيداعها بوعاء الاستراحة!`, 'red');
              updateUI();
              finishArrivalAction(player, isDoubles);
            }}
          }});
        }}
        break;

      case 'parking':
        const winPot = state.freeParkingPot;
        player.money += winPot;
        player.netWorth += winPot;
        state.freeParkingPot = 50;
        sfx.playFanfare();
        showFloatingFX(`+${{winPot}} $`, true, tile.id);
        addLog(`🎉 هبط ${{player.name}} على الاستراحة المجانية واستولى على كامل الوعاء: ${{winPot}} $!`, 'gold');
        finishArrivalAction(player, isDoubles);
        break;

      case 'chance':
        drawChanceCard(player, isDoubles);
        break;

      case 'chest':
        drawChestCard(player, isDoubles);
        break;

      case 'gotojail':
        sendToJail(player, 'أمر قضائي بالحبس الفوري');
        break;

      case 'jail':
        sfx.playVisitJail();
        showCenterDioramaCard({{
          theme: 'visiting',
          badge: '👮 زيارة تفقدية',
          player: player,
          title: 'سجن القلعة (زيارة فقط)',
          desc: 'أنت في خانة السجن بصفة زائر بريء. لا توجد أي غرامات أو توقيف، يمكنك استكمال دورك بأمان.',
          svgArt: SVG_ASSETS.tile_jail,
          btnText: 'متابعة الجولة',
          autoExecDelay: 1600,
          onAction: () => {{
            addLog(`👮 ${{player.name}} في زيارة بريئة لسجن القلعة.`);
            finishArrivalAction(player, isDoubles);
          }}
        }});
        break;

      default:
        finishArrivalAction(player, isDoubles);
    }}

    updateUI();
  }}

  // Property Rent & Buy in 1v1
  function handlePropertyArrival(player, tile, isDoubles) {{
    const ownership = state.tileOwnership[tile.id];

    if (!ownership || ownership.ownerId === null) {{
      if (player.isBot) {{
        let shouldBuy = false;
        const diff = state.aiDifficulty || 'medium';
        if (diff === 'easy') {{
          // Easy: only buys if has plenty of cash and 55% chance
          if (player.money >= tile.price + 500 && Math.random() < 0.55) shouldBuy = true;
        }} else if (diff === 'hard') {{
          // Hard: aggressive purchase if has money
          if (player.money >= tile.price) shouldBuy = true;
        }} else {{
          // Medium: balanced
          if (player.money >= tile.price + 120) shouldBuy = true;
        }}

        if (shouldBuy) {{
          buyPropertyDirect(player, tile);
        }} else {{
          addLog(`🤖 قرر ${{player.name}} عدم شراء [${{tile.name}}] للحفاظ على السيولة.`);
        }}
        finishArrivalAction(player, isDoubles);
      }} else {{
        openDeedModal(tile.id, true, isDoubles);
      }}
      return;
    }}

    if (ownership.ownerId !== player.id) {{
      const rival = state.players[ownership.ownerId];
      if (ownership.mortgaged) {{
        addLog(`العقار [${{tile.name}}] مرهون، لم يتم دفع إيجار!`);
        finishArrivalAction(player, isDoubles);
        return;
      }}

      let rent = 0;
      if (tile.type === 'station') {{
        const stationsOwned = countGroupOwned(ownership.ownerId, 'station');
        const stationRents = [25, 50, 100, 200];
        rent = (stationRents[stationsOwned - 1] || 25);
      }} else if (tile.type === 'utility') {{
        const utilsOwned = countGroupOwned(ownership.ownerId, 'utility');
        const factor = utilsOwned >= 2 ? 10 : 4;
        const diceSum = state.dice[0] + state.dice[1];
        rent = factor * diceSum;
      }} else {{
        rent = calculatePropertyRent(tile, ownership);
      }}

      const actualPaid = Math.min(player.money, rent);
      player.money -= actualPaid;
      rival.money += actualPaid;
      rival.netWorth += actualPaid;
      player.netWorth = Math.max(0, player.netWorth - actualPaid);

      sfx.playChaChing();
      showFloatingFX(`-${{actualPaid}} $`, false, tile.id);
      showFloatingFX(`+${{actualPaid}} $`, true, rival.position);
      addLog(`🏠 دفع ${{player.name}} إيجاراً مباشراً قدره ${{actualPaid}} $ لمنافسه ${{rival.name}} في [${{tile.name}}]!`, 'red');

      if (player.money <= 0) {{
        handleBankruptcy(player, rival);
      }}

      finishArrivalAction(player, isDoubles);
    }} else {{
      addLog(`✨ ${{player.name}} في ضيافة عقاره الخاص [${{tile.name}}].`);
      if (player.isBot && tile.type === 'property') {{
        const check = canBuildFloor(player.id, tile.id);
        if (check.can) {{
          const diff = state.aiDifficulty || 'medium';
          let shouldBuild = false;
          if (diff === 'easy' && player.money > check.cost + 600 && check.nextFloor <= 2) shouldBuild = true;
          else if (diff === 'medium' && player.money > check.cost + 180 && check.nextFloor <= 4) shouldBuild = true;
          else if (diff === 'hard' && player.money > check.cost + 40) shouldBuild = true;

          if (shouldBuild) {{
            buildFloorDirect(player.id, tile.id);
          }}
        }}
      }}
      finishArrivalAction(player, isDoubles);
    }}
  }}

  function countGroupOwned(ownerId, groupName) {{
    return TILES.filter(t => t.group === groupName && state.tileOwnership[t.id]?.ownerId === ownerId).length;
  }}

  function checkFullGroupOwned(ownerId, groupName) {{
    const allInGroup = TILES.filter(t => t.group === groupName);
    return allInGroup.length > 0 && allInGroup.every(t => state.tileOwnership[t.id]?.ownerId === ownerId);
  }}

  function buyPropertyDirect(player, tile) {{
    if (player.money < tile.price) return false;
    player.money -= tile.price;
    state.tileOwnership[tile.id] = {{ ownerId: player.id, houses: 0, mortgaged: false }};
    player.netWorth += tile.price;
    sfx.playChaChing();
    showFloatingFX(`-${{tile.price}} $`, false, tile.id);
    addLog(`🎉 اشترى ${{player.name}} عقار [${{tile.name}}] مقابل ${{tile.price}} $!`, 'green');
    updateTileOwnershipVisuals();
    updateUI();
    return true;
  }}

  // Custom Property Rent Calculation (Base Rent + 50% of floor value for each built floor)
  function calculatePropertyRent(tile, ownership) {{
    if (!tile || !tile.rent) return 0;
    const baseRent = tile.rent[0];
    if (!ownership || ownership.ownerId === null) return baseRent;

    const floors = ownership.houses || 0;
    const floorCost = Math.round(tile.price * 0.33); // 33% of base price
    const rentPerFloor = Math.round(floorCost * 0.50); // 50% of floor cost added to rent

    if (floors > 0) {{
      return baseRent + (floors * rentPerFloor);
    }}

    // Full color group owned without floors: double base rent
    if (checkFullGroupOwned(ownership.ownerId, tile.group)) {{
      return baseRent * 2;
    }}

    return baseRent;
  }}

  // Check if player can build next floor on property
  function canBuildFloor(ownerId, tileId) {{
    const tile = TILES[tileId];
    if (!tile || tile.type !== 'property') return {{ can: false, reason: 'هذا العقار لا يقبل بناء الطوابق' }};

    const rec = state.tileOwnership[tileId];
    if (!rec || rec.ownerId !== ownerId) return {{ can: false, reason: 'أنت لست مالك هذا العقار' }};
    if (rec.mortgaged) return {{ can: false, reason: 'العقار مرهون، لا يمكن البناء عليه' }};

    // 1. Must own full color group
    const isFullSet = checkFullGroupOwned(ownerId, tile.group);
    if (!isFullSet) {{
      return {{ can: false, reason: `يجب امتلاك كافة عقارات مجموعة [${{tile.groupName || 'هذا اللون'}}] لتفعيل البناء!` }};
    }}

    const currentFloors = rec.houses || 0;
    if (currentFloors >= 5) {{
      return {{ can: false, reason: 'العقار اكتمل بالحد الأقصى (برج إيفل الذهبي - 5 طوابق)!' }};
    }}

    // 2. Even building rule:
    // To build floor N+1, all other properties in group must have at least N floors
    const groupTiles = TILES.filter(t => t.group === tile.group);
    const minFloorsInGroup = Math.min(...groupTiles.map(t => state.tileOwnership[t.id]?.houses || 0));

    if (currentFloors > minFloorsInGroup) {{
      const lagging = groupTiles.find(t => (state.tileOwnership[t.id]?.houses || 0) === minFloorsInGroup);
      return {{
        can: false,
        reason: `شرط التساوي في البناء: لا يمكنك بناء الطابق (${{currentFloors + 1}}) حتى تبني الطابق (${{minFloorsInGroup + 1}}) في عقار [${{lagging.name}}] أولاً!`
      }};
    }}

    // 3. Money check: 33% of base price
    const floorCost = Math.round(tile.price * 0.33);
    const player = state.players[ownerId];
    if (player.money < floorCost) {{
      return {{ can: false, reason: `رصيدك لا يكفي! تكلفة الطابق هي ${{floorCost}} $ (لديك ${{player.money}} $ فقط).` }};
    }}

    return {{ can: true, cost: floorCost, nextFloor: currentFloors + 1 }};
  }}

  // Check if player can demolish a floor on property
  function canDemolishFloor(ownerId, tileId) {{
    const tile = TILES[tileId];
    if (!tile || tile.type !== 'property') return {{ can: false, reason: 'هذا العقار لا يقبل الهدم' }};

    const rec = state.tileOwnership[tileId];
    if (!rec || rec.ownerId !== ownerId) return {{ can: false, reason: 'أنت لست مالك هذا العقار' }};

    const currentFloors = rec.houses || 0;
    if (currentFloors <= 0) {{
      return {{ can: false, reason: 'لا توجد طوابق مبنية على هذا العقار لهدمها!' }};
    }}

    // Even demolition rule:
    // Must demolish highest floor in group first
    const groupTiles = TILES.filter(t => t.group === tile.group);
    const maxFloorsInGroup = Math.max(...groupTiles.map(t => state.tileOwnership[t.id]?.houses || 0));

    if (currentFloors < maxFloorsInGroup) {{
      const leading = groupTiles.find(t => (state.tileOwnership[t.id]?.houses || 0) === maxFloorsInGroup);
      return {{
        can: false,
        reason: `شرط التساوي في الهدم: يجب هدم الطابق الأعلى من عقار [${{leading.name}}] أولاً!`
      }};
    }}

    const floorCost = Math.round(tile.price * 0.33);
    const refund = Math.round(floorCost * 0.50); // 50% refund

    return {{ can: true, refund: refund, remainingFloors: currentFloors - 1 }};
  }}

  // Build Floor Action
  function buildFloorDirect(ownerId, tileId) {{
    const check = canBuildFloor(ownerId, tileId);
    if (!check.can) {{
      alert(check.reason);
      return false;
    }}
    const tile = TILES[tileId];
    const player = state.players[ownerId];
    const rec = state.tileOwnership[tileId];

    player.money -= check.cost;
    rec.houses = check.nextFloor;
    player.netWorth += check.cost;

    sfx.playChaChing();
    const typeLabel = rec.houses === 5 ? '🗼 برج إيفل الذهبي الأسطوري (الطابق 5 - الحد النهائي)' : `🏢 طابقاً ليمونياً جديداً (الطابق ${{rec.houses}})`;
    addLog(`🏗️ بنى ${{player.name}} ${{typeLabel}} في عقار [${{tile.name}}] بقيمة ${{check.cost}} $!`, 'gold');
    showFloatingFX(`-${{check.cost}} $`, false, tileId);

    updateTileOwnershipVisuals();
    updateUI();
    return true;
  }}

  // Demolish Floor Action
  function demolishFloorDirect(ownerId, tileId) {{
    const check = canDemolishFloor(ownerId, tileId);
    if (!check.can) {{
      alert(check.reason);
      return false;
    }}
    const tile = TILES[tileId];
    const player = state.players[ownerId];
    const rec = state.tileOwnership[tileId];
    const floorCost = Math.round(tile.price * 0.33);

    player.money += check.refund;
    player.netWorth -= (floorCost - check.refund);
    rec.houses = check.remainingFloors;

    sfx.playSmash();
    addLog(`🏚️ هدم ${{player.name}} طابقاً من عقار [${{tile.name}}] واسترد ${{check.refund}} $ (50% من قيمة الطابق)!`, 'red');
    showFloatingFX(`+${{check.refund}} $`, true, tileId);

    updateTileOwnershipVisuals();
    updateUI();
    return true;
  }}


  function sendToJail(player, reason = 'أمر حبس فوري') {{
    showCenterDioramaCard({{
      theme: 'jail',
      badge: '⛓️ أمر قضائي وضبط',
      player: player,
      title: 'إلى سجن القلعة فوراً!',
      desc: `${{reason}}! لا تمر بخانة البداية ولا تستلم 200 $. للخروج ارمِ دبل، أو انتظر 3 أدوار مع دفع كفالة 50 $.`,
      svgArt: SVG_ASSETS.tile_jail,
      btnText: 'تنفيذ أمر الحبس',
      autoExecDelay: 1800,
      onAction: async () => {{
        dismissCenterDioramaCard();
        addLog(`🚓 انطلقت دورية الشرطة لتنفيذ أمر ضبط ${{player.name}} واقتياده للسجن!`, 'red');
        
        await animatePawnToJail(player, () => {{
          player.inJail = true;
          player.jailTurns = 0;
          state.doublesCount = 0;
          state.isRolling = false;
          addLog(`⛓️ أُسقط السور الحديدي وأُغلق القفل على ${{player.name}} في سجن القلعة!`, 'red');
          updateJailGateVisibility();
          updateUI();
          endTurn();
        }});
      }}
    }});
  }}

  function drawChanceCard(player, isDoubles) {{
    const card = CHANCE_CARDS[Math.floor(Math.random() * CHANCE_CARDS.length)];
    state.activeCard = {{ card, player, isDoubles }};
    sfx.playChanceMystery();

    showCenterDioramaCard({{
      theme: 'chance',
      badge: '❓ كارت الحظ',
      player: player,
      title: card.title,
      desc: card.desc,
      svgArt: SVG_ASSETS.tile_chance,
      btnText: 'تنفيذ الكارت',
      autoExecDelay: 1800,
      onAction: () => {{
        executeCardAction();
      }}
    }});
  }}

  function drawChestCard(player, isDoubles) {{
    const card = CHEST_CARDS[Math.floor(Math.random() * CHEST_CARDS.length)];
    state.activeCard = {{ card, player, isDoubles }};
    sfx.playVaultOpen();

    showCenterDioramaCard({{
      theme: 'chest',
      badge: '🎁 صندوق الدنيا',
      player: player,
      title: card.title,
      desc: card.desc,
      svgArt: SVG_ASSETS.tile_chest,
      btnText: 'تنفيذ الكارت',
      autoExecDelay: 1800,
      onAction: () => {{
        executeCardAction();
      }}
    }});
  }}

  function drawCard(deckType, player, isDoubles) {{
    if (deckType === 'chance') {{
      drawChanceCard(player, isDoubles);
    }} else {{
      drawChestCard(player, isDoubles);
    }}
  }}

  function executeCardAction() {{
    closeModal('modalCard');
    if (!state.activeCard) return;
    const {{ card, player, isDoubles }} = state.activeCard;
    state.activeCard = null;

    switch (card.action) {{
      case 'heist':
        startBankHeist(player);
        return;

      case 'shutdown':
        startShutdown(player);
        return;

      case 'wheel':
        sfx.playFanfare();
        openWheelModal(player, isDoubles);
        return;

      case 'cash':
        const cashWin = card.amount;
        player.money += cashWin;
        player.netWorth += cashWin;
        sfx.playCoin();
        showFloatingFX(`+${{cashWin}} $`, true, player.position);
        addLog(`💵 ${{player.name}} استلم ${{cashWin}} $ من الكارت!`, 'green');
        break;

      case 'pay_tax':
        const taxVal = card.amount;
        player.money = Math.max(0, player.money - taxVal);
        state.freeParkingPot += taxVal;
        sfx.playChaChing();
        showFloatingFX(`-${{taxVal}} $`, false, player.position);
        addLog(`💸 دفع ${{player.name}} ${{taxVal}} $ للوعاء العام!`, 'red');
        break;

      case 'shield':
        player.shields = Math.min(3, player.shields + 2);
        sfx.playShield();
        addLog(`🛡️ تم شحن دروع حماية ${{player.name}} بالكامل!`, 'gold');
        break;

      case 'jail_free':
        player.jailCards++;
        addLog(`🗝️ حصل ${{player.name}} على كارت خروج من السجن مجاني!`, 'gold');
        break;

      case 'jail':
        sendToJail(player);
        return;

      case 'move_to':
        player.position = card.target;
        addLog(`🚀 انتقل ${{player.name}} فوراً إلى [${{TILES[card.target].name}}]!`);
        renderTokens();
        handleTileArrival(player, false);
        return;

      case 'birthday':
        const rival = state.players[player.id === 0 ? 1 : 0];
        const gift = Math.min(rival.money, card.amount);
        rival.money -= gift;
        player.money += gift;
        sfx.playCoin();
        addLog(`🎂 قدم ${{rival.name}} هدية ${{gift}} $ لـ ${{player.name}} بمناسبة عيد ميلاده!`, 'gold');
        break;

      default:
        break;
    }}

    finishArrivalAction(player, isDoubles);
  }}

  // 1v1 Bank Heist Mini-Game
  function startBankHeist(attacker) {{
    const rival = state.players[attacker.id === 0 ? 1 : 0];
    state.heistState = {{
      attacker,
      rival,
      silverCount: 0,
      cashCount: 0,
      diamondCount: 0,
      completed: false,
      items: shuffleArray([
        'silver', 'silver', 'silver', 'silver', 'silver',
        'cash', 'cash', 'cash', 'cash',
        'diamond', 'diamond', 'diamond'
      ])
    }};

    document.getElementById('heistTargetText').innerText = `أنت الآن تقتحم خزينة منافسك [${{rival.name}}]! افتح الأبواب وطابق 3 عناصر لتحديد غنيمتك!`;

    const grid = document.getElementById('heistVaultGrid');
    grid.innerHTML = '';
    document.getElementById('heistResultBanner').innerText = '';
    document.getElementById('btnCollectHeist').style.display = 'none';

    resetTrackerSlots('trackerSilver');
    resetTrackerSlots('trackerCash');
    resetTrackerSlots('trackerDiamond');

    for (let i = 0; i < 12; i++) {{
      const door = document.createElement('div');
      door.className = 'vault-door';
      door.id = `vault-door-${{i}}`;
      door.innerHTML = '🔒';
      door.addEventListener('click', () => pickVaultDoor(i));
      grid.appendChild(door);
    }}

    openModal('modalHeist');

    if (attacker.isBot) {{
      botPlayHeist();
    }}
  }}

  function resetTrackerSlots(id) {{
    const cont = document.getElementById(id);
    const slots = cont.querySelectorAll('.match-slot');
    slots.forEach(s => s.classList.remove('filled'));
  }}

  function pickVaultDoor(idx) {{
    const h = state.heistState;
    if (!h || h.completed) return;
    const door = document.getElementById(`vault-door-${{idx}}`);
    if (door.classList.contains('opened')) return;

    door.classList.add('opened');
    sfx.playVaultOpen();

    const item = h.items[idx];
    if (item === 'silver') {{
      door.innerHTML = '🪙';
      h.silverCount++;
      fillTrackerSlot('trackerSilver', h.silverCount);
      if (h.silverCount === 3) finishHeist('silver');
    }} else if (item === 'cash') {{
      door.innerHTML = '💰';
      h.cashCount++;
      fillTrackerSlot('trackerCash', h.cashCount);
      if (h.cashCount === 3) finishHeist('cash');
    }} else if (item === 'diamond') {{
      door.innerHTML = '💎';
      h.diamondCount++;
      fillTrackerSlot('trackerDiamond', h.diamondCount);
      if (h.diamondCount === 3) finishHeist('diamond');
    }}
  }}

  function fillTrackerSlot(trackerId, count) {{
    const slots = document.getElementById(trackerId).querySelectorAll('.match-slot');
    if (slots[count - 1]) slots[count - 1].classList.add('filled');
  }}

  function finishHeist(type) {{
    const h = state.heistState;
    h.completed = true;

    let basePrize = 150;
    let label = 'سرقة فضية صغيرة 🪙';
    if (type === 'cash') {{
      basePrize = 350;
      label = 'سرقة أكياس نقدية كبرى! 💰';
    }} else if (type === 'diamond') {{
      basePrize = 750;
      label = '💎 إفلاس البنك الأسطوري (Mega Heist)!';
    }}

    const totalPrize = basePrize;
    const stolenFromRival = Math.min(h.rival.money, totalPrize);
    h.rival.money -= stolenFromRival;
    h.attacker.money += totalPrize;
    h.attacker.netWorth += totalPrize;

    sfx.playFanfare();
    launchConfetti();

    document.getElementById('heistResultBanner').innerText = `مبروك! حققت ${{label}} ونلت ${{totalPrize}} $ (سُرقت ${{stolenFromRival}} $ من ${{h.rival.name}} مباشرة)!`;
    const collectBtn = document.getElementById('btnCollectHeist');
    collectBtn.style.display = 'inline-flex';
    collectBtn.onclick = () => {{
      closeModal('modalHeist');
      addLog(`🏦 سطا ${{h.attacker.name}} على خزينة ${{h.rival.name}} ونهب ${{totalPrize}} $!`, 'gold');
      finishArrivalAction(h.attacker, false);
    }};

    if (h.attacker.isBot) {{
      setTimeout(() => collectBtn.click(), 1200);
    }}
  }}

  function botPlayHeist() {{
    const interval = setInterval(() => {{
      const h = state.heistState;
      if (!h || h.completed) {{
        clearInterval(interval);
        return;
      }}
      const unopened = [];
      for (let i = 0; i < 12; i++) {{
        const door = document.getElementById(`vault-door-${{i}}`);
        if (door && !door.classList.contains('opened')) unopened.push(i);
      }}
      if (unopened.length === 0) {{
        clearInterval(interval);
        return;
      }}
      const randomIdx = unopened[Math.floor(Math.random() * unopened.length)];
      pickVaultDoor(randomIdx);
    }}, 600);
  }}

  // 1v1 Landmark Shutdown Mini-Game
  function startShutdown(attacker) {{
    const rival = state.players[attacker.id === 0 ? 1 : 0];
    state.shutdownState = {{ attacker, rival }};

    document.getElementById('shutdownSubtext').innerText = `استهدف معالم منافسك [${{rival.name}}] بالمطرقة الكرتونية! هل يمتلك درعاً لصد الهجوم؟`;
    document.getElementById('targetLandmarkIcon').innerHTML = SVG_ASSETS.tile_cairo_tower;
    document.getElementById('targetLandmarkName').innerText = `برج القاهرة الخاص بـ ${{rival.name}}`;
    document.getElementById('shutdownResultText').innerText = '';
    document.getElementById('btnLaunchShutdown').style.display = 'inline-flex';
    document.getElementById('btnFinishShutdown').style.display = 'none';

    const oldDome = document.querySelector('.shield-deflection-dome');
    if (oldDome) oldDome.remove();

    openModal('modalShutdown');

    if (attacker.isBot) {{
      setTimeout(() => {{
        executeShutdownHit();
      }}, 1000);
    }}
  }}

  function executeShutdownHit() {{
    const s = state.shutdownState;
    if (!s) return;

    document.getElementById('btnLaunchShutdown').style.display = 'none';
    const box = document.getElementById('targetLandmarkBox');

    if (s.rival.shields > 0) {{
      s.rival.shields--;
      sfx.playShield();

      const dome = document.createElement('div');
      dome.className = 'shield-deflection-dome';
      box.appendChild(dome);

      const consolation = 100;
      s.attacker.money += consolation;
      s.attacker.netWorth += consolation;

      document.getElementById('shutdownResultText').innerHTML = `
        <span style="color: #38bdf8;">🛡️ تصدى درع ${{s.rival.name}} للهجوم! خسر درعاً ونلت ترضية: ${{consolation}} $</span>
      `;
      addLog(`🛡️ درع ${{s.rival.name}} يصد هجوم ${{s.attacker.name}} بالمطرقة!`);
    }} else {{
      sfx.playSmash();
      box.style.animation = 'token-hop 0.5s';

      const demolishPrize = 400;
      s.attacker.money += demolishPrize;
      s.attacker.netWorth += demolishPrize;

      document.getElementById('shutdownResultText').innerHTML = `
        <span style="color: #ef4444;">💥 ضربة قاضية! تم تعطيل معالم ${{s.rival.name}} وربحت ${{demolishPrize}} $!</span>
      `;
      addLog(`💥 ضرب ${{s.attacker.name}} معالم ${{s.rival.name}} ونال غنيمة ${{demolishPrize}} $!`, 'red');
    }}

    const finishBtn = document.getElementById('btnFinishShutdown');
    finishBtn.style.display = 'inline-flex';
    finishBtn.onclick = () => {{
      closeModal('modalShutdown');
      finishArrivalAction(s.attacker, false);
    }};

    if (s.attacker.isBot) {{
      setTimeout(() => finishBtn.click(), 1200);
    }}
  }}

  // City Landmarks Construction View
  function openLandmarksModal() {{
    const curr = state.players[state.currentPlayerIdx];
    const container = document.getElementById('landmarksListContainer');
    container.innerHTML = '';

    let totalStars = 0;
    const landmarkSVGs = [
      SVG_ASSETS.tile_pyramid,
      SVG_ASSETS.tile_cairo_tower,
      SVG_ASSETS.tile_citadel,
      SVG_ASSETS.tile_lighthouse,
      SVG_ASSETS.tile_alex_palace
    ];

    LANDMARKS_DEF.forEach((lm, idx) => {{
      const stageIdx = curr.landmarks[lm.id] || 0;
      totalStars += stageIdx;
      const isMaxed = stageIdx >= 5;
      const nextStage = !isMaxed ? lm.stages[stageIdx] : null;

      let starsHtml = '';
      for (let s = 1; s <= 5; s++) {{
        starsHtml += `<span class="star-slot ${{s <= stageIdx ? 'filled' : ''}}">★</span>`;
      }}

      const card = document.createElement('div');
      card.className = 'landmark-builder-card';
      card.innerHTML = `
        <div class="landmark-icon-badge" style="width: 62px; height: 62px; padding: 4px;">
          ${{landmarkSVGs[idx]}}
        </div>
        <div class="landmark-meta">
          <div style="font-size: 14px; font-weight: 800; color: #fdfbf7;">${{lm.name}}</div>
          <div style="font-size: 11px; color: #cbd5e1;">${{isMaxed ? 'مكتمل بالكامل! 👑' : nextStage.name}}</div>
          <div class="landmark-stars-row">${{starsHtml}}</div>
        </div>
        <div>
          ${{isMaxed ? `
            <span style="font-size: 11px; color: #10b981; font-weight: 800;">مكتمل 👑</span>
          ` : `
            <button class="btn-matte gold" onclick="upgradeLandmark('${{lm.id}}')" ${{curr.money < nextStage.cost ? 'disabled' : ''}}>
              ترقية (${{nextStage.cost}} $)
            </button>
          `}}
        </div>
      `;
      container.appendChild(card);
    }});

    const progressPct = Math.round((totalStars / 25) * 100);
    document.getElementById('boardProgressText').innerText = `${{totalStars}} / 25 نجمة (${{progressPct}}%)`;
    document.getElementById('boardProgressBar').style.width = `${{progressPct}}%`;

    openModal('modalLandmarks');
  }}

  function upgradeLandmark(landmarkId) {{
    const curr = state.players[state.currentPlayerIdx];
    const lm = LANDMARKS_DEF.find(l => l.id === landmarkId);
    const stageIdx = curr.landmarks[lm.id] || 0;
    if (stageIdx >= 5) return;

    const stage = lm.stages[stageIdx];
    if (curr.money < stage.cost) return;

    curr.money -= stage.cost;
    curr.landmarks[lm.id]++;
    curr.netWorth += stage.netWorth;

    sfx.playChaChing();
    addLog(`🏛️ طوّر ${{curr.name}} [${{lm.name}}] إلى المرحلة ${{curr.landmarks[lm.id]}} (+${{stage.netWorth}} ثروة)!`, 'gold');

    let totalStars = 0;
    LANDMARKS_DEF.forEach(l => {{ totalStars += curr.landmarks[l.id] || 0; }});

    if (totalStars === 25) {{
      state.boardLevel++;
      curr.rolls += 100;
      curr.money += 1500;
      curr.netWorth += 1500;
      sfx.playFanfare();
      launchConfetti();
      alert(`🎉 تهانينا الخالصة يا ${{curr.name}}! أتممت بناء لوحة القاهرة التاريخية بالكامل وفتحت اللوحة التالية بمكافأة 1500 $ و 100 نرد! 👑`);
      LANDMARKS_DEF.forEach(l => {{ curr.landmarks[l.id] = 0; }});
    }}

    openLandmarksModal();
    updateUI();
  }}

  // Wheel of Fortune & Risk (Profit & Loss)
  function openWheelModal(player = null, isDoubles = false) {{
    state.wheelPlayer = player || state.players[state.currentPlayerIdx];
    state.wheelIsDoubles = isDoubles;
    state.wheelSpinning = false;

    const resDisplay = document.getElementById('wheelResultDisplay');
    if (resDisplay) {{
      resDisplay.style.color = '#fef08a';
      resDisplay.innerText = t('wheelInstruction', 'عجلة الحظ قد تنفع وقد تضر! أدر العجلة واكتشف مصيرك...');
    }}

    const spinBtn = document.getElementById('btnSpinWheel');
    if (spinBtn) {{
      spinBtn.disabled = false;
      spinBtn.style.opacity = '1';
    }}

    const canvas = document.getElementById('wheelCanvas');
    if (canvas) {{
      canvas.style.transition = 'none';
      canvas.style.transform = 'rotate(0deg)';
      setTimeout(() => {{
        canvas.style.transition = 'transform 4s cubic-bezier(0.15, 0.9, 0.2, 1)';
      }}, 50);
    }}

    drawWheel();
    openModal('modalWheel');

    // If bot, automatically spin the wheel
    if (state.wheelPlayer && state.wheelPlayer.isBot) {{
      setTimeout(() => {{
        spinWheelAction();
      }}, 1200);
    }}
  }}

  function drawWheel() {{
    const canvas = document.getElementById('wheelCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const num = WHEEL_ITEMS_DEF.length;
    const arc = (2 * Math.PI) / num;
    const radius = canvas.width / 2;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    WHEEL_ITEMS_DEF.forEach((item, i) => {{
      const angle = i * arc;
      ctx.beginPath();
      ctx.fillStyle = item.color;
      ctx.moveTo(radius, radius);
      ctx.arc(radius, radius, radius - 4, angle, angle + arc);
      ctx.fill();
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = '#2a160d';
      ctx.stroke();

      ctx.save();
      ctx.translate(radius, radius);
      ctx.rotate(angle + arc / 2);
      ctx.textAlign = 'right';
      ctx.fillStyle = item.textColor || '#ffffff';
      ctx.font = 'bold 12.5px Cairo, sans-serif';
      ctx.shadowColor = 'rgba(0,0,0,0.9)';
      ctx.shadowBlur = 4;
      ctx.fillText(item.label, radius - 15, 4);
      ctx.restore();
    }});
  }}

  function spinWheelAction() {{
    if (state.wheelSpinning) return;
    state.wheelSpinning = true;
    const spinBtn = document.getElementById('btnSpinWheel');
    if (spinBtn) {{
      spinBtn.disabled = true;
      spinBtn.style.opacity = '0.5';
    }}

    const canvas = document.getElementById('wheelCanvas');
    const winningIdx = Math.floor(Math.random() * WHEEL_ITEMS_DEF.length);
    const num = WHEEL_ITEMS_DEF.length;
    const arcDeg = 360 / num;
    const targetDeg = (360 * 5) + (270 - (winningIdx * arcDeg + arcDeg / 2));

    canvas.style.transform = `rotate(${{targetDeg}}deg)`;

    let ticks = 0;
    const tickInterval = setInterval(() => {{
      sfx.playWheelTick();
      ticks++;
      if (ticks > 25) clearInterval(tickInterval);
    }}, 140);

    setTimeout(() => {{
      state.wheelSpinning = false;
      const prize = WHEEL_ITEMS_DEF[winningIdx];
      const player = state.wheelPlayer || state.players[state.currentPlayerIdx];
      const rival = state.players[player.id === 0 ? 1 : 0];
      const curUnit = getCurrency();

      const isWin = prize.isWin;

      // 1. Play Appropriate Sound Effect
      if (isWin) {{
        sfx.playFanfare();
        sfx.playChaChing();
      }} else {{
        sfx.playBuzzer();
      }}

      // 2. Execute Outcome IMMEDIATELY in game state
      if (prize.type === 'cash_win') {{
        player.money += prize.amount;
        player.netWorth += prize.amount;
        showFloatingFX(`+${{prize.amount}} ${{curUnit}}`, true, player.position);
        addLog(`🎉 عجلة الحظ: كسب ${{player.name}} مبلغ +${{prize.amount}} ${{curUnit}}!`, 'green');
      }} else if (prize.type === 'cash_loss') {{
        const actual = Math.min(player.money, prize.amount);
        player.money -= actual;
        player.netWorth = Math.max(0, player.netWorth - actual);
        state.freeParkingPot += actual;
        showFloatingFX(`-${{actual}} ${{curUnit}}`, false, player.position);
        addLog(`💸 عجلة الحظ: خسر ${{player.name}} مبلغ -${{actual}} ${{curUnit}} أودعت بوعاء الاستراحة!`, 'red');
        if (player.money <= 0) handleBankruptcy(player, rival);
      }} else if (prize.type === 'rolls_win') {{
        player.rolls += prize.amount;
        showFloatingFX(`+${{prize.amount}} 🎲`, true, player.position);
        addLog(`🎲 عجلة الحظ: نال ${{player.name}} +${{prize.amount}} رمية نرد إضافية!`, 'gold');
      }} else if (prize.type === 'jail') {{
        addLog(`⛓️ عجلة الحظ: أمر حبس فوري! تم ترحيل ${{player.name}} لسجن القلعة!`, 'red');
        sendToJail(player, 'عجلة الحظ السيئة');
      }} else if (prize.type === 'shield_win') {{
        player.shields = 3;
        sfx.playShield();
        showFloatingFX(`+3 🛡️`, true, player.position);
        addLog(`🛡️ عجلة الحظ: شحن كامل لدروع حماية ${{player.name}}!`, 'gold');
      }} else if (prize.type === 'pay_rival') {{
        const actual = Math.min(player.money, prize.amount);
        player.money -= actual;
        player.netWorth = Math.max(0, player.netWorth - actual);
        rival.money += actual;
        rival.netWorth += actual;
        showFloatingFX(`-${{actual}} ${{curUnit}}`, false, player.position);
        showFloatingFX(`+${{actual}} ${{curUnit}}`, true, rival.position);
        addLog(`💔 عجلة الحظ: دفع ${{player.name}} مبلغ ${{actual}} ${{curUnit}} لمنافسه ${{rival.name}}!`, 'red');
        if (player.money <= 0) handleBankruptcy(player, rival);
      }} else if (prize.type === 'shield_loss') {{
        player.shields = 0;
        showFloatingFX(`💥 0 🛡️`, false, player.position);
        addLog(`🔨 عجلة الحظ: تحطمت دروع ${{player.name}} بالكامل!`, 'red');
      }}

      // 3. Display Result on Modal
      const resDisplay = document.getElementById('wheelResultDisplay');
      if (resDisplay) {{
        resDisplay.style.color = isWin ? '#4ade80' : '#f87171';
        const msg = currentLanguage === 'ar' ? prize.desc : (prize.desc_en || prize.desc);
        resDisplay.innerText = (isWin ? '🎉 ' : '⚠️ ') + msg;
      }}

      // 4. Update UI
      updateUI();

      // 5. Automatically dismiss modal and continue turn after reaction delay
      setTimeout(() => {{
        closeModal('modalWheel');
        if (prize.type !== 'jail') {{
          finishArrivalAction(player, state.wheelIsDoubles);
        }}
      }}, 2400);

    }}, 4100);
  }}

  // Open Property Deed Modal with Custom Construction Controls
  function openDeedModal(tileId, showBuyOption = false, isDoubles = false) {{
    const tile = TILES[tileId];
    if (!tile) return;

    const body = document.getElementById('deedModalBody');
    const footer = document.getElementById('deedModalFooter');
    const rec = state.tileOwnership[tileId];
    const curr = state.players[state.currentPlayerIdx];

    let ownerName = t('deedBankOwner', 'شاغر للبيع (البنك)');
    let isOwner = false;
    if (rec && rec.ownerId !== null) {{
      ownerName = state.players[rec.ownerId].name;
      isOwner = rec.ownerId === curr.id;
    }}

    const art3D = getTile3DArt(tile);
    const floorCost = Math.round(tile.price * 0.33);
    const rentIncrease = Math.round(floorCost * 0.50);
    const currentFloors = rec?.houses || 0;
    const isFullSet = tile.type === 'property' && rec && rec.ownerId !== null && checkFullGroupOwned(rec.ownerId, tile.group);
    const currentRentVal = calculatePropertyRent(tile, rec);
    const curUnit = getCurrency();

    // Group properties overview chips
    let groupChipsHtml = '';
    if (tile.type === 'property') {{
      const groupTiles = TILES.filter(t => t.group === tile.group);
      groupChipsHtml = groupTiles.map(t => {{
        const tRec = state.tileOwnership[t.id];
        const fl = tRec?.houses || 0;
        const isCurrent = t.id === tile.id;
        const flIcon = fl === 5 ? '🗼' : (fl > 0 ? '🏢' : '⚪');
        return `<div class="group-tile-chip ${{isCurrent ? 'active' : ''}}"><span>${{flIcon}}</span><span>${{t.name}}: ${{fl}}</span></div>`;
      }}).join('');
    }}

    // Rent Table based on user specifications:
    let rentTableHtml = '';
    if (tile.type === 'property') {{
      rentTableHtml = `
        <div class="deed-row"><span>${{t('deedFloorCost')}}</span><span>${{floorCost}} ${{curUnit}}</span></div>
        <div class="deed-row"><span>${{t('deedRentIncrease')}}</span><span>+${{rentIncrease}} ${{curUnit}}</span></div>
        <div class="deed-row ${{currentFloors === 0 && !isFullSet ? 'highlight' : ''}}"><span>${{t('deedBaseRent')}}</span><span>${{tile.rent[0]}} ${{curUnit}}</span></div>
        <div class="deed-row ${{currentFloors === 0 && isFullSet ? 'highlight' : ''}}"><span>${{t('deedFullGroup')}}</span><span>${{tile.rent[0] * 2}} ${{curUnit}}</span></div>
        <div class="deed-row ${{currentFloors === 1 ? 'highlight' : ''}}"><span>1 ${{t('btnBuildFloor')}}:</span><span>${{tile.rent[0] + rentIncrease}} ${{curUnit}}</span></div>
        <div class="deed-row ${{currentFloors === 2 ? 'highlight' : ''}}"><span>2 ${{t('btnBuildFloor')}}:</span><span>${{tile.rent[0] + (2 * rentIncrease)}} ${{curUnit}}</span></div>
        <div class="deed-row ${{currentFloors === 3 ? 'highlight' : ''}}"><span>3 ${{t('btnBuildFloor')}}:</span><span>${{tile.rent[0] + (3 * rentIncrease)}} ${{curUnit}}</span></div>
        <div class="deed-row ${{currentFloors === 4 ? 'highlight' : ''}}"><span>4 ${{t('btnBuildFloor')}}:</span><span>${{tile.rent[0] + (4 * rentIncrease)}} ${{curUnit}}</span></div>
        <div class="deed-row ${{currentFloors === 5 ? 'highlight' : ''}}"><span>${{t('deedEiffel')}}</span><span>${{tile.rent[0] + (5 * rentIncrease)}} ${{curUnit}}</span></div>
      `;
    }} else if (tile.rent) {{
      rentTableHtml = `<div class="deed-row"><span>${{t('deedBaseRent')}}</span><span>${{tile.rent[0]}} ${{curUnit}}</span></div>`;
    }}

    body.innerHTML = `
      <div class="deed-card">
        <div class="deed-header" style="background: ${{tile.color}};">
          <h2>${{tile.name}}</h2>
          <div style="font-size: 11px;">${{tile.subtitle}}</div>
        </div>
        <div style="width: 100%; height: 105px; display: flex; align-items: center; justify-content: center; background: #1a0f0a; padding: 6px;">
          <div style="width: 95px; height: 95px;">${{art3D}}</div>
        </div>
        <div class="deed-table">
          <div class="deed-row"><span>${{t('btnBuyProperty')}}:</span><span>${{tile.price}} ${{curUnit}}</span></div>
          <div class="deed-row highlight"><span>${{t('deedOwner')}}</span><span>${{ownerName}}</span></div>
          <div class="deed-row" style="background: rgba(245, 158, 11, 0.15); font-weight:800; color:#fef08a;">
            <span>${{t('deedCurrentRent')}}</span><span>${{currentRentVal}} ${{curUnit}}</span>
          </div>
          ${{rentTableHtml}}
        </div>

        ${{tile.type === 'property' && isOwner ? `
          <div class="deed-construction-panel">
            <div class="deed-group-header">
              <span>🏗️ حالة بناء المجموعة اللونية:</span>
              <span style="color: ${{isFullSet ? '#bef264' : '#f87171'}};">${{isFullSet ? '✨ مكتملة الاحتكار' : '⚠️ غير مكتملة'}}</span>
            </div>
            <div class="deed-group-chips">
              ${{groupChipsHtml}}
            </div>
            <div id="constructionHintBox" class="construction-reason-hint"></div>
          </div>
        ` : ''}}

      </div>
    `;

    footer.innerHTML = '';

    if (showBuyOption && (!rec || rec.ownerId === null)) {{
      const buyBtn = document.createElement('button');
      buyBtn.className = 'btn-matte gold';
      buyBtn.innerHTML = `<span>${{t('btnBuyProperty')}} (${{tile.price}} ${{curUnit}})</span>`;
      buyBtn.onclick = () => {{
        buyPropertyDirect(curr, tile);
        closeModal('modalDeed');
        finishArrivalAction(curr, isDoubles);
      }};
      footer.appendChild(buyBtn);

      const declineBtn = document.createElement('button');
      declineBtn.className = 'btn-matte';
      declineBtn.innerHTML = `<span>${{t('deedSkip')}}</span>`;
      declineBtn.onclick = () => {{
        closeModal('modalDeed');
        finishArrivalAction(curr, isDoubles);
      }};
      footer.appendChild(declineBtn);
    }} else {{
      if (isOwner && tile.type === 'property') {{
        const canBuild = canBuildFloor(curr.id, tileId);
        const canDemolish = canDemolishFloor(curr.id, tileId);
        const hintBox = document.getElementById('constructionHintBox');

        // Build Button: "إنشاء طابق"
        const buildBtn = document.createElement('button');
        const isEiffelNext = (rec?.houses || 0) === 4;
        buildBtn.className = `btn-lime-build ${{isEiffelNext ? 'gold-tower' : ''}}`;
        const buildTitle = isEiffelNext ? ('🗼 ' + t('deedEiffel')) : ('🏗️ ' + t('btnBuildFloor'));
        buildBtn.innerHTML = `<span>${{buildTitle}} (${{floorCost}} ${{curUnit}})</span>`;

        if (!canBuild.can) {{
          buildBtn.disabled = true;
          if (hintBox) hintBox.innerText = `💡 ${{canBuild.reason}}`;
        }} else {{
          if (hintBox) hintBox.innerText = `✅ ${{canBuild.nextFloor === 5 ? t('deedEiffel') : canBuild.nextFloor + ' ' + t('btnBuildFloor')}} (+${{rentIncrease}} ${{curUnit}})`;
        }}

        buildBtn.onclick = () => {{
          if (buildFloorDirect(curr.id, tileId)) {{
            openDeedModal(tileId);
          }}
        }};
        footer.appendChild(buildBtn);

        // Demolish Button: "هدم طابق"
        const demolishBtn = document.createElement('button');
        demolishBtn.className = 'btn-demolish';
        const refundVal = Math.round(floorCost * 0.50);
        demolishBtn.innerHTML = `<span>🏚️ ${{t('btnDemolishFloor')}} (+${{refundVal}} ${{curUnit}})</span>`;

        if (!canDemolish.can) {{
          demolishBtn.disabled = true;
        }}

        demolishBtn.onclick = () => {{
          if (demolishFloorDirect(curr.id, tileId)) {{
            openDeedModal(tileId);
          }}
        }};
        footer.appendChild(demolishBtn);
      }}

      if (!isOwner && rec && rec.ownerId !== null) {{
        const negotiateBtn = document.createElement('button');
        negotiateBtn.className = 'btn-matte gold';
        negotiateBtn.innerHTML = `<span>${{t('btnNegotiateBuyout')}}</span>`;
        negotiateBtn.onclick = () => {{
          closeModal('modalDeed');
          openBuyoutNegotiationModal(tileId);
        }};
        footer.appendChild(negotiateBtn);
      }}

      const closeBtn = document.createElement('button');
      closeBtn.className = 'btn-matte';
      closeBtn.innerHTML = `<span>${{t('btnCloseCard', 'إغلاق')}}</span>`;
      closeBtn.onclick = () => closeModal('modalDeed');
      footer.appendChild(closeBtn);
    }}

    openModal('modalDeed');
  }}

  // Bankruptcy in 1v1
  function handleBankruptcy(bankruptPlayer, creditor) {{
    bankruptPlayer.isBankrupt = true;
    sfx.playBuzzer();
    addLog(`☠️ أعلن ${{bankruptPlayer.name}} إفلاسه! الفائز بالنزال هو ${{creditor.name}}!`, 'red');

    sfx.playFanfare();
    launchConfetti();
    alert(`👑 ألف مبروك! الفائز العظيم بنزال بنك الحظ 3D هو: ${{creditor.name}}! 🏆`);
  }}

  // Turn Cycle
  function finishArrivalAction(player, isDoubles) {{
    if (isDoubles && !player.inJail && !player.isBankrupt) {{
      addLog(`🎲 نرد دبل! يحصل ${{player.name}} على دور إضافي مجاني!`, 'gold');
      if (player.isBot) {{
        setTimeout(rollDiceAction, 1200);
      }} else {{
        state.isRolling = false;
        document.getElementById('btnRollDice').disabled = false;
      }}
    }} else {{
      setTimeout(endTurn, 1000);
    }}
  }}

  function endTurn() {{
    dismissCenterDioramaCard();
    state.isRolling = false;
    state.currentPlayerIdx = state.currentPlayerIdx === 0 ? 1 : 0;
    state.doublesCount = 0;
    updateUI();

    const curr = state.players[state.currentPlayerIdx];
    if (curr.isBot) {{
      setTimeout(() => {{
        rollDiceAction();
      }}, 1200);
    }}
  }}

  // Confetti FX
  function launchConfetti() {{
    const canvas = document.getElementById('confettiCanvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const particles = [];
    const colors = ['#f59e0b', '#ef4444', '#10b981', '#3b82f6', '#ec4899', '#8b5cf6'];

    for (let i = 0; i < 140; i++) {{
      particles.push({{
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height * 0.4,
        size: Math.random() * 8 + 4,
        color: colors[Math.floor(Math.random() * colors.length)],
        vx: (Math.random() - 0.5) * 6,
        vy: Math.random() * 4 + 3,
        rot: Math.random() * 360,
        vRot: (Math.random() - 0.5) * 10
      }});
    }}

    let frames = 0;
    function animate() {{
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach(p => {{
        p.x += p.vx;
        p.y += p.vy;
        p.rot += p.vRot;
        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rot * Math.PI) / 180);
        ctx.fillStyle = p.color;
        ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
        ctx.restore();
      }});

      frames++;
      if (frames < 140) {{
        requestAnimationFrame(animate);
      }} else {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }}
    }}
    animate();
  }}

  function openModal(id) {{ const el = document.getElementById(id); if (el) el.classList.add('active'); }}
  function closeModal(id) {{ const el = document.getElementById(id); if (el) el.classList.remove('active'); }}

  function shuffleArray(arr) {{
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {{
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }}
    return a;
  }}

    // Setup Modal State & Interaction
  const currentSetup = {{
    mode: 'bot',
    money: 6000,
    difficulty: 'medium',
    p1Name: 'مستر حظ',
    p2Name: 'روبوت'
  }};

  function openNewGameModal(isFirstLaunch = false) {{
    document.querySelectorAll('#setupModeGroup .setup-pill').forEach(b => {{
      b.classList.toggle('active', b.dataset.mode === currentSetup.mode);
    }});
    document.querySelectorAll('#setupMoneyGroup .setup-pill').forEach(b => {{
      b.classList.toggle('active', parseInt(b.dataset.money, 10) === currentSetup.money);
    }});
    document.querySelectorAll('#setupDifficultyGroup .setup-pill').forEach(b => {{
      b.classList.toggle('active', b.dataset.diff === currentSetup.difficulty);
    }});

    const p1Input = document.getElementById('setupPlayer1Name');
    const p2Input = document.getElementById('setupPlayer2Name');
    const p2Prefix = document.getElementById('p2Prefix');
    const diffSection = document.getElementById('setupDifficultySection');

    p1Input.value = currentSetup.p1Name;

    if (currentSetup.mode === 'bot') {{
      p2Input.value = 'روبوت';
      p2Input.readOnly = true;
      p2Prefix.innerText = '🤖 اسم المنافس:';
      diffSection.style.display = 'block';
    }} else {{
      p2Input.value = currentSetup.p2Name === 'روبوت' ? 'اللاعب الثاني' : currentSetup.p2Name;
      p2Input.readOnly = false;
      p2Prefix.innerText = '👑 اسم اللاعب 2:';
      diffSection.style.display = 'none';
    }}

    openModal('modalNewGame');
  }}

  function initSetupListeners() {{
    // Mode Pills
    document.querySelectorAll('#setupModeGroup .setup-pill').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('#setupModeGroup .setup-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const mode = btn.dataset.mode;
        currentSetup.mode = mode;

        const p2Input = document.getElementById('setupPlayer2Name');
        const p2Prefix = document.getElementById('p2Prefix');
        const diffSection = document.getElementById('setupDifficultySection');

        if (mode === 'bot') {{
          p2Input.value = 'روبوت';
          p2Input.readOnly = true;
          p2Prefix.innerText = '🤖 اسم المنافس:';
          diffSection.style.display = 'block';
        }} else {{
          if (p2Input.value === 'روبوت') p2Input.value = 'اللاعب الثاني';
          p2Input.readOnly = false;
          p2Prefix.innerText = '👑 اسم اللاعب 2:';
          diffSection.style.display = 'none';
        }}
      }});
    }});

    // Money Pills
    document.querySelectorAll('#setupMoneyGroup .setup-pill').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('#setupMoneyGroup .setup-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentSetup.money = parseInt(btn.dataset.money, 10);
      }});
    }});

    // Difficulty Pills
    document.querySelectorAll('#setupDifficultyGroup .setup-pill').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('#setupDifficultyGroup .setup-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentSetup.difficulty = btn.dataset.diff;
      }});
    }});

    // Start Button
    document.getElementById('btnConfirmStartGame').addEventListener('click', () => {{
      const chosenLang = document.getElementById('setupLanguageSelect')?.value || currentLanguage;
      setGameLanguage(chosenLang);

      const p1Name = document.getElementById('setupPlayer1Name').value.trim() || t('p1Default', 'مستر حظ');
      let p2Name = t('botDefault', 'روبوت');
      if (currentSetup.mode === 'human') {{
        p2Name = document.getElementById('setupPlayer2Name').value.trim() || t('p2Default', 'اللاعب الثاني');
      }}

      currentSetup.p1Name = p1Name;
      currentSetup.p2Name = p2Name;

      closeModal('modalNewGame');
      sfx.playFanfare();
      initGame(currentSetup);
    }});

    // Close button
    document.getElementById('btnCloseNewGameModal').addEventListener('click', () => {{
      closeModal('modalNewGame');
    }});
  }}

  
  
  // Direct Property Buyout Negotiation State
  let buyoutState = {{
    tileId: null,
    buyerId: null,
    sellerId: null,
    pendingOfferPrice: 0
  }};

  function openBuyoutNegotiationModal(tileId, initialPrice = null, feedbackMsg = null) {{
    const tile = TILES[tileId];
    if (!tile) return;
    const rec = state.tileOwnership[tileId];
    if (!rec || rec.ownerId === null) return;

    const buyer = state.players[state.currentPlayerIdx];
    const seller = state.players[rec.ownerId];

    if (buyer.id === seller.id) {{
      alert('هذا العقار ملك لك بالفعل!');
      return;
    }}

    buyoutState.tileId = tileId;
    buyoutState.buyerId = buyer.id;
    buyoutState.sellerId = seller.id;

    // Target property card preview
    document.getElementById('buyoutPropName').innerText = tile.name;
    document.getElementById('buyoutPropOwner').innerText = `المالك الحالي: ${{seller.name}} (${{seller.avatar}})`;
    document.getElementById('buyoutPropBasePrice').innerText = `${{tile.price}} $`;
    document.getElementById('buyoutPropColorStripe').style.background = tile.color || '#a8a29e';

    document.getElementById('buyoutBuyerBalance').innerText = `رصيدك المتاح (${{buyer.name}}): ${{buyer.money}} $`;

    const input = document.getElementById('buyoutOfferInput');
    const startVal = initialPrice !== null ? initialPrice : Math.round(tile.price * 1.2);
    input.value = startVal;
    input.max = buyer.money;
    buyoutState.pendingOfferPrice = startVal;

    updateBuyoutMarkupDisplay(tile.price, startVal);

    // Feedback banner (shown if rival rejected previous offer!)
    const feedbackBox = document.getElementById('buyoutFeedbackBox');
    if (feedbackMsg) {{
      feedbackBox.style.display = 'block';
      feedbackBox.className = 'buyout-feedback-box';
      feedbackBox.innerHTML = feedbackMsg;
    }} else {{
      feedbackBox.style.display = 'none';
      feedbackBox.innerHTML = '';
    }}

    openModal('modalBuyout');
  }}

  function updateBuyoutMarkupDisplay(basePrice, offerPrice) {{
    const pct = Math.round((offerPrice / basePrice) * 100);
    const markupEl = document.getElementById('buyoutMarkupPercent');
    if (markupEl) {{
      if (pct > 100) {{
        markupEl.innerText = `(+${{pct - 100}}% فوق السعر الأصلي)`;
        markupEl.style.color = '#bef264';
      }} else if (pct === 100) {{
        markupEl.innerText = '(السعر الأصلي تماماً)';
        markupEl.style.color = '#fef08a';
      }} else {{
        markupEl.innerText = `(خصم ${{100 - pct}}% تحت السعر الأصلي)`;
        markupEl.style.color = '#f87171';
      }}
    }}
  }}

  function sendBuyoutOfferAction() {{
    const tile = TILES[buyoutState.tileId];
    const buyer = state.players[buyoutState.buyerId];
    const seller = state.players[buyoutState.sellerId];
    const offerPrice = Math.max(0, parseInt(document.getElementById('buyoutOfferInput').value, 10) || 0);

    if (offerPrice <= 0) {{
      alert('يرجى تحديد مبلغ مالي صحيح لشراء العقار!');
      return;
    }}

    if (offerPrice > buyer.money) {{
      alert(`رصيدك المالي لا يكفي! رصيدك المتاح هو ${{buyer.money}} $ فقط بينما عرضت ${{offerPrice}} $.`);
      return;
    }}

    buyoutState.pendingOfferPrice = offerPrice;

    // Check if property has buildings
    const rec = state.tileOwnership[tile.id];
    if ((rec?.houses || 0) > 0) {{
      alert(`⚠️ العقار به طوابق مبنية (${{rec.houses}} طوابق). وفق قواعد اللعبة يجب هدم الطوابق أولاً قبل بيع العقار!`);
      return;
    }}

    if (seller.isBot) {{
      handleBotBuyoutEvaluation(tile, buyer, seller, offerPrice);
    }} else {{
      openHumanBuyoutReview(tile, buyer, seller, offerPrice);
    }}
  }}

  // AI Bot Buyout Evaluation
  function handleBotBuyoutEvaluation(tile, buyer, seller, offerPrice) {{
    const diff = state.aiDifficulty || 'medium';
    const basePrice = tile.price;

    // Check if selling this property gives the buyer a complete monopoly
    const groupTiles = TILES.filter(t => t.group === tile.group);
    const buyerCount = groupTiles.filter(t => state.tileOwnership[t.id]?.ownerId === buyer.id).length;
    const willGiveMonopoly = (buyerCount === groupTiles.length - 1);

    // Calculate required minimum price Bot demands to sell
    let multiplier = 1.25;
    if (diff === 'easy') {{
      multiplier = willGiveMonopoly ? 1.6 : 1.15;
    }} else if (diff === 'medium') {{
      multiplier = willGiveMonopoly ? 2.5 : 1.45;
    }} else {{
      // Hard: strictly protects monopolies
      multiplier = willGiveMonopoly ? 3.8 : 1.85;
    }}

    // If bot has low cash (< 1000), bot is hungrier for cash (-15% discount)
    if (seller.money < 1000) multiplier *= 0.85;

    const requiredPrice = Math.round(basePrice * multiplier);

    if (offerPrice >= requiredPrice) {{
      // Bot Accepts!
      executeBuyoutDeal(tile.id, buyer.id, seller.id, offerPrice);
      closeModal('modalBuyout');
      sfx.playFanfare();
      alert(`🎉 مبروك! وافق ${{seller.name}} على بيع عقار [${{tile.name}}] لك مقابل ${{offerPrice}} $! تمت الصفقة بنجاح 🤝`);
    }} else {{
      // Bot Rejects!
      sfx.playBuzzer();
      addLog(`❌ رفض ${{seller.name}} عرض شراء [${{tile.name}}] بقيمة ${{offerPrice}} $.`, 'red');

      let rejectionMsg = '';
      if (willGiveMonopoly) {{
        rejectionMsg = `❌ <b>رفض ${{seller.name}}</b> هذا العرض (<b>${{offerPrice}} $</b>)!<br>
        <i>"السعر منخفض جداً! هذا العقار يمنحك احتكار مجموعة [${{tile.groupName}}] الخطيرة. لن أتنازل عنه إلا بمبلغ أعلى بكثير (أطلب على الأقل ${{requiredPrice}} $)!"</i><br>
        <span style="color:#fef08a;">👈 يمكنك زيادة السعر أدناه وإعادة إرسال العرض، أو الضغط على "إلغاء الصفقة".</span>`;
      }} else {{
        rejectionMsg = `❌ <b>رفض ${{seller.name}}</b> هذا العرض (<b>${{offerPrice}} $</b>)!<br>
        <i>"عرضك غير كافٍ لإقناعي بالتخلي عن هذا العقار. ارفع سعرك إذا أردت إتمام الصفقة!"</i><br>
        <span style="color:#fef08a;">👈 يمكنك زيادة السعر أدناه وإعادة إرسال العرض، أو الضغط على "إلغاء الصفقة".</span>`;
      }}

      // Return the SAME modal with the rejection feedback, allowing price increase or cancel
      openBuyoutNegotiationModal(tile.id, offerPrice, rejectionMsg);
    }}
  }}

  // 2-Player Human Mode Review
  function openHumanBuyoutReview(tile, buyer, seller, offerPrice) {{
    closeModal('modalBuyout');
    const body = document.getElementById('buyoutRivalReviewBody');
    body.innerHTML = `
      <div class="trade-deal-card-box">
        <div style="font-size:14px; font-weight:800; color:#bef264;">💰 عرض شراء نقدي لعقارك!</div>
        <div style="font-size:13px; color:#ffffff; line-height:1.6; margin-top:6px;">
          يقدم لك اللاعب <b>[${{buyer.name}}]</b> مبلغاً نقدياً قدره: <b style="color:#fef08a; font-size:16px;">${{offerPrice}} $</b><br>
          مقابل شراء ونقل ملكية عقارك: <b style="color:#38bdf8;">[${{tile.name}}]</b> (سعره بالرقعة: ${{tile.price}} $).
        </div>
      </div>
      <div style="font-size: 12px; color: #fef08a; margin-top: 10px; font-weight: 700;">
        هل تقبل بيع العقار بهذا السعر يا ${{seller.name}}؟
      </div>
    `;

    openModal('modalBuyoutRivalReview');
  }}

  // Execute buyout transaction
  function executeBuyoutDeal(tileId, buyerId, sellerId, price) {{
    const buyer = state.players[buyerId];
    const seller = state.players[sellerId];
    const tile = TILES[tileId];

    buyer.money -= price;
    seller.money += price;

    state.tileOwnership[tileId].ownerId = buyer.id;
    buyer.netWorth += tile.price;
    seller.netWorth -= tile.price;

    sfx.playChaChing();
    addLog(`🤝 اشترى ${{buyer.name}} عقار [${{tile.name}}] من ${{seller.name}} مقابل ${{price}} $ بموجب المفاوضة!`, 'gold');
    showFloatingFX(`-${{price}} $`, false, tileId);
    showFloatingFX(`+${{price}} $`, true, seller.position);

    updateTileOwnershipVisuals();
    updateUI();
  }}

  // Trade & Negotiation System State
  let tradeState = {{
    activePlayerId: 0,
    rivalPlayerId: 1,
    selectedOfferProps: new Set(),
    selectedRequestProps: new Set(),
    pendingDeal: null
  }};

  function openTradeModal() {{
    const p1 = state.players[state.currentPlayerIdx];
    const p2 = state.players[state.currentPlayerIdx === 0 ? 1 : 0];

    tradeState.activePlayerId = p1.id;
    tradeState.rivalPlayerId = p2.id;
    tradeState.selectedOfferProps.clear();
    tradeState.selectedRequestProps.clear();
    tradeState.pendingDeal = null;

    // Header info
    document.getElementById('tradeOfferAvatar').innerText = p1.avatar;
    document.getElementById('tradeOfferName').innerText = `عرضك (${{p1.name}})`;
    document.getElementById('tradeOfferBalance').innerText = `رصيدك المتاح: ${{p1.money}} $`;

    document.getElementById('tradeRequestAvatar').innerText = p2.avatar;
    document.getElementById('tradeRequestName').innerText = `طلبك من (${{p2.name}})`;
    document.getElementById('tradeRequestBalance').innerText = `رصيده المتاح: ${{p2.money}} $`;

    // Cash inputs
    const offerCashInput = document.getElementById('tradeOfferCash');
    const requestCashInput = document.getElementById('tradeRequestCash');
    offerCashInput.value = 0;
    offerCashInput.max = p1.money;
    requestCashInput.value = 0;
    requestCashInput.max = p2.money;

    // Jail cards
    const offerJailRow = document.getElementById('tradeOfferJailCardRow');
    const requestJailRow = document.getElementById('tradeRequestJailCardRow');
    document.getElementById('tradeOfferJailCard').checked = false;
    document.getElementById('tradeRequestJailCard').checked = false;
    offerJailRow.style.display = p1.jailCards > 0 ? 'block' : 'none';
    requestJailRow.style.display = p2.jailCards > 0 ? 'block' : 'none';

    // Populate properties
    renderTradePropertiesLists(p1, p2);
    updateTradeValuation();

    openModal('modalTrade');
  }}

  function renderTradePropertiesLists(p1, p2) {{
    const offerList = document.getElementById('tradeOfferPropsList');
    const requestList = document.getElementById('tradeRequestPropsList');
    offerList.innerHTML = '';
    requestList.innerHTML = '';

    const p1Props = TILES.filter(t => state.tileOwnership[t.id]?.ownerId === p1.id);
    const p2Props = TILES.filter(t => state.tileOwnership[t.id]?.ownerId === p2.id);

    if (p1Props.length === 0) {{
      offerList.innerHTML = '<div class="trade-empty-props">لا تمتلك أي عقارات حالياً لعرضها.</div>';
    }} else {{
      p1Props.forEach(t => {{
        const item = createTradePropItem(t, false);
        offerList.appendChild(item);
      }});
    }}

    if (p2Props.length === 0) {{
      requestList.innerHTML = '<div class="trade-empty-props">المنافس لا يمتلك أي عقارات لطلبها.</div>';
    }} else {{
      p2Props.forEach(t => {{
        const item = createTradePropItem(t, true);
        requestList.appendChild(item);
      }});
    }}
  }}

  function createTradePropItem(tile, isRequest) {{
    const rec = state.tileOwnership[tile.id];
    const hasBuildings = (rec?.houses || 0) > 0;
    const div = document.createElement('div');
    div.className = 'trade-prop-item';
    div.dataset.tileId = tile.id;

    const buildingHint = hasBuildings ? ` (${{rec.houses === 5 ? 'برج ذهبي' : rec.houses + ' طوابق'}})` : '';

    div.innerHTML = `
      <div class="trade-prop-right">
        <div class="trade-prop-color-bar" style="background: ${{tile.color || '#a8a29e'}};"></div>
        <div>
          <div class="trade-prop-name">${{tile.name}}${{buildingHint}}</div>
          <div style="font-size: 10px; color: #94a3b8;">${{tile.groupName || tile.subtitle}}</div>
        </div>
      </div>
      <div class="trade-prop-price">${{tile.price}} $</div>
    `;

    div.addEventListener('click', () => {{
      if (hasBuildings) {{
        alert(`⚠️ العقار [${{tile.name}}] به طوابق مبنية! يجب هدم الطوابق أولاً قبل التبادل وفق القواعد.`);
        return;
      }}
      const targetSet = isRequest ? tradeState.selectedRequestProps : tradeState.selectedOfferProps;
      if (targetSet.has(tile.id)) {{
        targetSet.delete(tile.id);
        div.classList.remove('selected');
      }} else {{
        targetSet.add(tile.id);
        div.classList.add('selected');
      }}
      updateTradeValuation();
    }});

    return div;
  }}

  function updateTradeValuation() {{
    const offerCash = Math.max(0, parseInt(document.getElementById('tradeOfferCash').value, 10) || 0);
    const requestCash = Math.max(0, parseInt(document.getElementById('tradeRequestCash').value, 10) || 0);

    let totalOfferVal = offerCash;
    tradeState.selectedOfferProps.forEach(id => {{
      totalOfferVal += TILES[id].price;
    }});
    if (document.getElementById('tradeOfferJailCard').checked) totalOfferVal += 100;

    let totalRequestVal = requestCash;
    tradeState.selectedRequestProps.forEach(id => {{
      totalRequestVal += TILES[id].price;
    }});
    if (document.getElementById('tradeRequestJailCard').checked) totalRequestVal += 100;

    document.getElementById('tradeValOffer').innerText = `${{totalOfferVal}} $`;
    document.getElementById('tradeValRequest').innerText = `${{totalRequestVal}} $`;

    const statusEl = document.getElementById('tradeValStatus');
    const itemsCount = tradeState.selectedOfferProps.size + tradeState.selectedRequestProps.size + (offerCash > 0 ? 1 : 0) + (requestCash > 0 ? 1 : 0);

    if (itemsCount === 0) {{
      statusEl.innerText = 'حدد العقارات أو الأموال من الجانبين للتفاوض';
      statusEl.style.color = '#fbbf24';
    }} else if (totalOfferVal > totalRequestVal) {{
      const diff = totalOfferVal - totalRequestVal;
      statusEl.innerText = `عرضك مغرٍ (+${{diff}} $ لصالح المنافس)`;
      statusEl.style.color = '#bef264';
    }} else if (totalOfferVal < totalRequestVal) {{
      const diff = totalRequestVal - totalOfferVal;
      statusEl.innerText = `طلبك أعلى بقيمة (+${{diff}} $ لصالحك)`;
      statusEl.style.color = '#f87171';
    }} else {{
      statusEl.innerText = 'الصفقة متكافئة تماماً في القيمة المالية!';
      statusEl.style.color = '#fef08a';
    }}
  }}

  function submitTradeAction() {{
    const p1 = state.players[tradeState.activePlayerId];
    const p2 = state.players[tradeState.rivalPlayerId];

    const offerCash = Math.max(0, parseInt(document.getElementById('tradeOfferCash').value, 10) || 0);
    const requestCash = Math.max(0, parseInt(document.getElementById('tradeRequestCash').value, 10) || 0);
    const offerJail = document.getElementById('tradeOfferJailCard').checked;
    const requestJail = document.getElementById('tradeRequestJailCard').checked;

    if (offerCash > p1.money) {{
      alert(`لا يمكنك عرض ${{offerCash}} $، رصيدك المتاح هو ${{p1.money}} $ فقط!`);
      return;
    }}
    if (requestCash > p2.money) {{
      alert(`لا يمكنك طلب ${{requestCash}} $، رصيد المنافس هو ${{p2.money}} $ فقط!`);
      return;
    }}

    const offeredProps = Array.from(tradeState.selectedOfferProps).map(id => TILES[id]);
    const requestedProps = Array.from(tradeState.selectedRequestProps).map(id => TILES[id]);

    if (offeredProps.length === 0 && requestedProps.length === 0 && offerCash === 0 && requestCash === 0 && !offerJail && !requestJail) {{
      alert('الصفقة فارغة! يرجى تحديد عقارات أو أموال من أي من الطرفين.');
      return;
    }}

    const deal = {{
      p1, p2,
      offerCash, requestCash,
      offeredProps, requestedProps,
      offerJail, requestJail
    }};

    tradeState.pendingDeal = deal;
    closeModal('modalTrade');

    if (p2.isBot) {{
      handleBotTradeEvaluation(deal);
    }} else {{
      openHumanTradeReviewModal(deal);
    }}
  }}

  // AI Bot Negotiation Evaluation Logic
  function handleBotTradeEvaluation(deal) {{
    const bot = deal.p2;
    const human = deal.p1;
    const diff = state.aiDifficulty || 'medium';

    // 1. Calculate Bot Gain
    let botGain = deal.offerCash;
    deal.offeredProps.forEach(t => {{
      botGain += t.price;
      // Bonus if this tile completes a color monopoly for bot
      const groupTiles = TILES.filter(tile => tile.group === t.group);
      const botCount = groupTiles.filter(tile => state.tileOwnership[tile.id]?.ownerId === bot.id).length;
      if (botCount === groupTiles.length - 1) {{
        botGain += (t.price * 1.8); // Huge monopoly bonus!
      }}
    }});
    if (deal.offerJail) botGain += 100;

    // 2. Calculate Bot Loss
    let botLoss = deal.requestCash;
    deal.requestedProps.forEach(t => {{
      botLoss += t.price;
      // Penalty if giving this tile completes a monopoly for human
      const groupTiles = TILES.filter(tile => tile.group === t.group);
      const humanCount = groupTiles.filter(tile => state.tileOwnership[tile.id]?.ownerId === human.id).length;
      if (humanCount === groupTiles.length - 1) {{
        if (diff === 'easy') botLoss += (t.price * 0.4);
        else if (diff === 'medium') botLoss += (t.price * 1.5);
        else botLoss += (t.price * 3.5); // Hard bot hates giving monopolies
      }}
    }});
    if (deal.requestJail) botLoss += 100;

    // Check Bot cash
    if (deal.requestCash > bot.money) {{
      alert(`🤖 روبوت: أرفض العرض! لا أملك سيولة كافية لدفع ${{deal.requestCash}} $.`);
      return;
    }}

    // Evaluate ratio
    let accept = false;
    let reason = '';

    if (diff === 'easy') {{
      if (botGain >= botLoss * 0.85) {{
        accept = true;
      }} else {{
        reason = 'العرض غير متكافئ مالياً بالنسبة لي.';
      }}
    }} else if (diff === 'medium') {{
      if (botGain >= botLoss * 1.05) {{
        accept = true;
      }} else {{
        reason = 'العرض غير كافٍ. أطلب تعويضاً نقدياً أكبر أو عقاراً أفضل.';
      }}
    }} else {{
      // Hard
      if (botGain >= botLoss * 1.35) {{
        accept = true;
      }} else {{
        reason = 'أرفض بشدة! كخصم استراتيجي محترف، هذه الصفقة تفيدك أكثر مني ولن أسمح لك بالتقدم!';
      }}
    }}

    if (accept) {{
      sfx.playFanfare();
      executeTradeDeal(deal);
      alert(`🤖 روبوت: قبلت عرضك بكل سرور! تم إبرام الصفقة ونقل الملكيات بنجاح 🤝`);
    }} else {{
      sfx.playBuzzer();
      alert(`🤖 روبوت: [رفض الصفقة] ❌
"${{reason}}"`);
      addLog(`❌ رفض روبوت عرض المفاوضة المقدم من ${{human.name}}.`, 'red');
    }}
  }}

  // 2-Player Human Mode Review Modal
  function openHumanTradeReviewModal(deal) {{
    const body = document.getElementById('tradeReviewBody');
    document.getElementById('tradeReviewTitle').innerText = `🤝 عرض مفاوضة مقدم من [${{deal.p1.name}}] إلى [${{deal.p2.name}}]`;

    let offerItemsHtml = '';
    if (deal.offerCash > 0) offerItemsHtml += `<div class="trade-deal-item">💵 مبلغ نقد: <b>${{deal.offerCash}} $</b></div>`;
    deal.offeredProps.forEach(t => {{
      offerItemsHtml += `<div class="trade-deal-item">🏛️ عقار: <b>[${{t.name}}]</b> (${{t.price}} $)</div>`;
    }});
    if (deal.offerJail) offerItemsHtml += `<div class="trade-deal-item">🗝️ كارت الخروج من السجن مجاناً</div>`;
    if (!offerItemsHtml) offerItemsHtml = '<div style="font-size:11px; color:#94a3b8;">(لا يوجد نقد أو عقارات معروضة)</div>';

    let requestItemsHtml = '';
    if (deal.requestCash > 0) requestItemsHtml += `<div class="trade-deal-item">💵 مبلغ نقد: <b>${{deal.requestCash}} $</b></div>`;
    deal.requestedProps.forEach(t => {{
      requestItemsHtml += `<div class="trade-deal-item">🏛️ عقار: <b>[${{t.name}}]</b> (${{t.price}} $)</div>`;
    }});
    if (deal.requestJail) requestItemsHtml += `<div class="trade-deal-item">🗝️ كارت الخروج من السجن مجاناً</div>`;
    if (!requestItemsHtml) requestItemsHtml = '<div style="font-size:11px; color:#94a3b8;">(لا يوجد نقد أو عقارات مطلوبة)</div>';

    body.innerHTML = `
      <div class="trade-deal-card-box">
        <div class="trade-deal-side-title">🎁 ما ستحصل عليه يا ${{deal.p2.name}}:</div>
        ${{offerItemsHtml}}
      </div>
      <div class="trade-deal-card-box" style="margin-top: 10px;">
        <div class="trade-deal-side-title" style="color: #f87171;">📤 ما ستدفعه وتقدمه لـ ${{deal.p1.name}}:</div>
        ${{requestItemsHtml}}
      </div>
      <div style="font-size: 12px; color: #fef08a; margin-top: 8px; font-weight: 700;">
        هل توافق يا ${{deal.p2.name}} على اعتماد هذا التبادل ونقل الملكيات بينكما؟
      </div>
    `;

    openModal('modalTradeReview');
  }}

  // Execute the trade transfer
  function executeTradeDeal(deal) {{
    const {{ p1, p2, offerCash, requestCash, offeredProps, requestedProps, offerJail, requestJail }} = deal;

    // Cash transfer
    p1.money -= offerCash;
    p2.money += offerCash;

    p2.money -= requestCash;
    p1.money += requestCash;

    // Properties transfer
    offeredProps.forEach(t => {{
      if (state.tileOwnership[t.id]) {{
        state.tileOwnership[t.id].ownerId = p2.id;
        p1.netWorth -= t.price;
        p2.netWorth += t.price;
      }}
    }});

    requestedProps.forEach(t => {{
      if (state.tileOwnership[t.id]) {{
        state.tileOwnership[t.id].ownerId = p1.id;
        p2.netWorth -= t.price;
        p1.netWorth += t.price;
      }}
    }});

    // Jail cards transfer
    if (offerJail) {{ p1.jailCards--; p2.jailCards++; }}
    if (requestJail) {{ p2.jailCards--; p1.jailCards++; }}

    sfx.playChaChing();
    addLog(`🤝 تمت صفقة التبادل بنجاح بين [${{p1.name}}] و[${{p2.name}}]!`, 'gold');

    updateTileOwnershipVisuals();
    updateUI();
  }}

  // DOM Event Listeners
  function bootGame() {{
    initSetupListeners();
    initGame(currentSetup);
    openNewGameModal(true);

    document.getElementById('btnRollDice').addEventListener('click', rollDiceAction);

    document.getElementById('btnToggleSound').addEventListener('click', () => {{
      const muted = sfx.toggleMute();
      document.getElementById('soundIcon').innerText = muted ? '🔇' : '🔊';
    }});

    const btnLandmarks = document.getElementById('btnOpenLandmarks'); if (btnLandmarks) btnLandmarks.addEventListener('click', openLandmarksModal);
    const btnWheel = document.getElementById('btnOpenWheel'); if (btnWheel) btnWheel.addEventListener('click', openWheelModal);
    document.getElementById('btnOpenTrade').addEventListener('click', openTradeModal);
    document.getElementById('btnCloseTradeModal').addEventListener('click', () => closeModal('modalTrade'));
    document.getElementById('btnCancelTrade').addEventListener('click', () => closeModal('modalTrade'));
    document.getElementById('btnSubmitTrade').addEventListener('click', submitTradeAction);

    // Buyout Modal Listeners
    document.getElementById('btnCloseBuyoutModal').addEventListener('click', () => closeModal('modalBuyout'));
    document.getElementById('btnCancelBuyout').addEventListener('click', () => closeModal('modalBuyout'));
    document.getElementById('btnSendBuyoutOffer').addEventListener('click', sendBuyoutOfferAction);

    document.querySelectorAll('.btn-quick-price').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const addVal = parseInt(btn.dataset.add, 10);
        const input = document.getElementById('buyoutOfferInput');
        const cur = parseInt(input.value, 10) || 0;
        input.value = cur + addVal;
        const tile = TILES[buyoutState.tileId];
        if (tile) updateBuyoutMarkupDisplay(tile.price, input.value);
      }});
    }});

    document.getElementById('buyoutOfferInput').addEventListener('input', (e) => {{
      const tile = TILES[buyoutState.tileId];
      if (tile) updateBuyoutMarkupDisplay(tile.price, parseInt(e.target.value, 10) || 0);
    }});

    document.getElementById('btnAcceptBuyoutDeal').addEventListener('click', () => {{
      const {{ tileId, buyerId, sellerId, pendingOfferPrice }} = buyoutState;
      executeBuyoutDeal(tileId, buyerId, sellerId, pendingOfferPrice);
      closeModal('modalBuyoutRivalReview');
      sfx.playFanfare();
      alert(`✅ تمت الصفقة بنجاح! انتقل عقار [${{TILES[tileId].name}}] إلى ${{state.players[buyerId].name}}.`);
    }});

    document.getElementById('btnRejectBuyoutDeal').addEventListener('click', () => {{
      closeModal('modalBuyoutRivalReview');
      sfx.playBuzzer();
      const {{ tileId, buyerId, sellerId, pendingOfferPrice }} = buyoutState;
      const seller = state.players[sellerId];
      const buyer = state.players[buyerId];
      const msg = `❌ <b>رفض ${{seller.name}}</b> عرضك السابق (<b>${{pendingOfferPrice}} $</b>)!<br>
      <i>"السعر غير مناسب لي. يمكنك زيادة السعر وإعادة إرسال العرض، أو إلغاء الصفقة."</i><br>
      <span style="color:#fef08a;">👈 قم بزيادة السعر أدناه أو اضغط على "إلغاء الصفقة".</span>`;
      openBuyoutNegotiationModal(tileId, pendingOfferPrice, msg);
    }});

    document.getElementById('tradeOfferCash').addEventListener('input', updateTradeValuation);
    document.getElementById('tradeRequestCash').addEventListener('input', updateTradeValuation);
    document.getElementById('tradeOfferJailCard').addEventListener('change', updateTradeValuation);
    document.getElementById('tradeRequestJailCard').addEventListener('change', updateTradeValuation);

    document.getElementById('btnAcceptTradeDeal').addEventListener('click', () => {{
      if (tradeState.pendingDeal) {{
        executeTradeDeal(tradeState.pendingDeal);
        tradeState.pendingDeal = null;
      }}
      closeModal('modalTradeReview');
    }});

    document.getElementById('btnRejectTradeDeal').addEventListener('click', () => {{
      if (tradeState.pendingDeal) {{
        addLog(`❌ رفض ${{tradeState.pendingDeal.p2.name}} عرض الصفقة المقدم من ${{tradeState.pendingDeal.p1.name}}.`, 'red');
        tradeState.pendingDeal = null;
      }}
      closeModal('modalTradeReview');
    }});

        document.getElementById('btnOpenRules').addEventListener('click', () => {{
      updateRulesModalContent();
      openModal('modalRules');
    }});

    const btnOpenAboutUs = document.getElementById('btnOpenAboutUs');
    if (btnOpenAboutUs) {{
      btnOpenAboutUs.addEventListener('click', () => {{
        renderAboutUsContent();
        openModal('modalAboutUs');
      }});
    }}

    const btnOpenTokenPicker = document.getElementById('btnOpenTokenPicker');
    if (btnOpenTokenPicker) {{
      btnOpenTokenPicker.addEventListener('click', () => {{
        renderTokenPickerGrid();
        openModal('modalTokenPicker');
      }});
    }}
    document.getElementById('btnResetGame').addEventListener('click', () => {{
      openNewGameModal(false);
    }});

    document.getElementById('btnLaunchShutdown').addEventListener('click', executeShutdownHit);
    document.getElementById('btnSpinWheel').addEventListener('click', spinWheelAction);
    document.getElementById('btnExecuteCardAction').addEventListener('click', executeCardAction);

    document.getElementById('dioramaCardBtn').addEventListener('click', (e) => {{
      e.stopPropagation();
      sfx.playCoin();
      executeDioramaCardAction();
    }});

    document.getElementById('dioramaCardInner').addEventListener('click', () => {{
      sfx.playCoin();
      executeDioramaCardAction();
    }});

    document.getElementById('btnClearLog').addEventListener('click', () => {{
      document.getElementById('activityLog').innerHTML = '';
    }});

    // Multilingual Selectors & Settings Listeners
    const headerLangSelect = document.getElementById('headerLanguageSelect');
    if (headerLangSelect) {{
      headerLangSelect.addEventListener('change', (e) => {{
        setGameLanguage(e.target.value);
      }});
    }}

    const setupLangSelect = document.getElementById('setupLanguageSelect');
    if (setupLangSelect) {{
      setupLangSelect.addEventListener('change', (e) => {{
        setGameLanguage(e.target.value);
      }});
    }}

    const settingsLangSelect = document.getElementById('settingsLanguageSelect');
    if (settingsLangSelect) {{
      settingsLangSelect.addEventListener('change', (e) => {{
        setGameLanguage(e.target.value);
      }});
    }}

    // Dice Speed Pills in Settings
    document.querySelectorAll('#settingsDiceSpeedGroup .setup-pill').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('#settingsDiceSpeedGroup .setup-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        gameSettings.diceSpeed = btn.dataset.speed;
        try {{ localStorage.setItem('bank_el_hazz_dice_speed', btn.dataset.speed); }} catch (e) {{}}
      }});
    }});

    // Movement Speed Pills in Settings
    document.querySelectorAll('#settingsMoveSpeedGroup .setup-pill').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('#settingsMoveSpeedGroup .setup-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        gameSettings.moveSpeed = btn.dataset.speed;
        try {{ localStorage.setItem('bank_el_hazz_move_speed', btn.dataset.speed); }} catch (e) {{}}
      }});
    }});

    const btnOpenSettings = document.getElementById('btnOpenSettings');
    if (btnOpenSettings) {{
      btnOpenSettings.addEventListener('click', () => {{
        const sel = document.getElementById('settingsLanguageSelect');
        if (sel) sel.value = currentLanguage;

        // Sync Speed Pills
        document.querySelectorAll('#settingsDiceSpeedGroup .setup-pill').forEach(b => {{
          b.classList.toggle('active', b.dataset.speed === gameSettings.diceSpeed);
        }});
        document.querySelectorAll('#settingsMoveSpeedGroup .setup-pill').forEach(b => {{
          b.classList.toggle('active', b.dataset.speed === gameSettings.moveSpeed);
        }});

        openModal('modalSettings');
      }});
    }}

    const btnSaveSettingsApply = document.getElementById('btnSaveSettingsApply');
    if (btnSaveSettingsApply) {{
      btnSaveSettingsApply.addEventListener('click', () => {{
        const sel = document.getElementById('settingsLanguageSelect');
        if (sel) setGameLanguage(sel.value);

        try {{
          localStorage.setItem('bank_el_hazz_dice_speed', gameSettings.diceSpeed);
          localStorage.setItem('bank_el_hazz_move_speed', gameSettings.moveSpeed);
        }} catch (e) {{}}

        closeModal('modalSettings');
        sfx.playFanfare();
        showFloatingFX(`✅ ${{t('btnSaveSettings')}}`, true);
      }});
    }}

    const btnSettingsToggleAudio = document.getElementById('btnSettingsToggleAudio');
    if (btnSettingsToggleAudio) {{
      btnSettingsToggleAudio.addEventListener('click', () => {{
        const isMuted = sfx.toggleMute();
        const txt = document.getElementById('settingsAudioText');
        const icn = document.getElementById('settingsAudioIcon');
        if (txt) txt.innerText = isMuted ? 'المؤثرات الصوتية: مكتومة' : 'المؤثرات الصوتية: مفعلة';
        if (icn) icn.innerText = isMuted ? '🔇' : '🔊';
      }});
    }}

    // Apply active or saved language on initial boot
    setGameLanguage(currentLanguage, false);

    if (document.body) {{
      document.body.addEventListener('click', () => sfx.ensureContext(), {{ once: true }});
    }}
  }}

  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', bootGame);
  }} else {{
    bootGame();
  }}
  </script>

</body>
</html>
"""

# Save to target file
dest_path = "/bank_el_hazz/bank_el_hazz_monopoly_go.html"
with open(dest_path, "w", encoding="utf-8") as f:
    f.write(full_matte_html)

with open("/bank_el_hazz/index.html", "w", encoding="utf-8") as f:
    f.write(full_matte_html)

print("Saved Matte Physical 3D Bank El Hazz successfully to:", dest_path)
print("File size:", os.path.getsize(dest_path), "bytes")
