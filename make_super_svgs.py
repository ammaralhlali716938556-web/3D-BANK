import json

svgs = {}

# 1. 3D Isometric Green Villa (House)
svgs['house_3d'] = """<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hRoofTop" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#34d399"/><stop offset="100%" stop-color="#059669"/></linearGradient>
    <linearGradient id="hRoofL" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#10b981"/><stop offset="100%" stop-color="#047857"/></linearGradient>
    <linearGradient id="hRoofR" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#059669"/><stop offset="100%" stop-color="#064e3b"/></linearGradient>
    <linearGradient id="hWallL" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f8fafc"/><stop offset="100%" stop-color="#cbd5e1"/></linearGradient>
    <linearGradient id="hWallR" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#e2e8f0"/><stop offset="100%" stop-color="#94a3b8"/></linearGradient>
    <filter id="hDrop" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="4" stdDeviation="3" flood-color="#000" flood-opacity="0.5"/></filter>
  </defs>
  <!-- Drop Shadow -->
  <ellipse cx="30" cy="52" rx="24" ry="6" fill="rgba(0,0,0,0.4)"/>
  <!-- Front Lawn Base -->
  <polygon points="30,42 52,30 52,33 30,45 8,33 8,30" fill="#15803d"/>
  <!-- Chimney with Smoke -->
  <polygon points="38,12 44,15 44,24 38,21" fill="#dc2626"/>
  <polygon points="44,15 47,13 47,22 44,24" fill="#991b1b"/>
  <polygon points="38,12 41,10 47,13 44,15" fill="#f87171"/>
  <circle cx="43" cy="8" r="3" fill="#f1f5f9" opacity="0.6"/>
  <circle cx="46" cy="4" r="4" fill="#f1f5f9" opacity="0.4"/>
  <!-- House Body Walls -->
  <polygon points="14,32 30,41 30,50 14,41" fill="url(#hWallL)"/>
  <polygon points="30,41 46,32 46,41 30,50" fill="url(#hWallR)"/>
  <!-- Wooden Arched Door -->
  <polygon points="20,38 26,41 26,48 20,44" fill="#78350f"/>
  <circle cx="21" cy="43" r="1" fill="#fbbf24"/>
  <!-- Lit Window -->
  <polygon points="35,36 41,33 41,39 35,42" fill="#38bdf8"/>
  <line x1="38" y1="34" x2="38" y2="40" stroke="#ffffff" stroke-width="1"/>
  <!-- 3D Hip Roof -->
  <polygon points="30,14 10,26 14,32 30,22" fill="url(#hRoofL)" filter="url(#hDrop)"/>
  <polygon points="30,14 30,22 46,32 50,26" fill="url(#hRoofR)"/>
  <polygon points="30,14 30,22 14,32 30,41 46,32 30,22" fill="url(#hRoofTop)"/>
  <!-- Roof Ridge Specular Highlight -->
  <line x1="30" y1="14" x2="30" y2="22" stroke="#a7f3d0" stroke-width="2" stroke-linecap="round"/>
</svg>"""

# 2. 3D Isometric Luxury Skyscraper Hotel
svgs['hotel_3d'] = """<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hotWallL" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f87171"/><stop offset="100%" stop-color="#b91c1c"/></linearGradient>
    <linearGradient id="hotWallR" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ef4444"/><stop offset="100%" stop-color="#7f1d1d"/></linearGradient>
    <linearGradient id="goldRoofG" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fef08a"/><stop offset="50%" stop-color="#f59e0b"/><stop offset="100%" stop-color="#92400e"/></linearGradient>
  </defs>
  <!-- Shadow -->
  <ellipse cx="30" cy="54" rx="26" ry="5" fill="rgba(0,0,0,0.45)"/>
  <!-- Base Tier -->
  <polygon points="12,32 30,42 30,52 12,42" fill="url(#hotWallL)"/>
  <polygon points="30,42 48,32 48,42 30,52" fill="url(#hotWallR)"/>
  <!-- Windows on Base -->
  <polygon points="16,36 21,39 21,42 16,39" fill="#fef08a"/>
  <polygon points="23,40 28,43 28,46 23,43" fill="#fef08a"/>
  <polygon points="32,41 37,38 37,41 32,44" fill="#fef08a"/>
  <polygon points="39,37 44,34 44,37 39,40" fill="#fef08a"/>
  <!-- Middle Tier -->
  <polygon points="16,20 30,28 30,38 16,30" fill="url(#hotWallL)"/>
  <polygon points="30,28 44,20 44,30 30,38" fill="url(#hotWallR)"/>
  <!-- Windows on Middle -->
  <polygon points="20,24 25,27 25,29 20,27" fill="#fef08a"/>
  <polygon points="35,27 40,24 40,27 35,29" fill="#fef08a"/>
  <!-- Penthouse Tier -->
  <polygon points="20,12 30,18 30,24 20,18" fill="url(#hotWallL)"/>
  <polygon points="30,18 40,12 40,18 30,24" fill="url(#hotWallR)"/>
  <!-- Golden Crown Roof & Dome -->
  <polygon points="30,8 20,12 30,18 40,12" fill="url(#goldRoofG)"/>
  <ellipse cx="30" cy="8" rx="6" ry="4" fill="url(#goldRoofG)"/>
  <!-- Antenna Spire -->
  <line x1="30" y1="8" x2="30" y2="2" stroke="#fbbf24" stroke-width="2"/>
  <circle cx="30" cy="2" r="1.5" fill="#fef08a"/>
  <!-- Grand Red Carpet Entrance -->
  <polygon points="27,47 33,43 33,52 27,52" fill="#fbbf24"/>
</svg>"""

# 3. 3D Figurine: Mr. Hazz (Red Fez Tarboosh on Gold Pedestal)
svgs['fig_mr_hazz'] = """<svg viewBox="0 0 70 70" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="fezBody" cx="35%" cy="30%" r="70%"><stop offset="0%" stop-color="#f87171"/><stop offset="35%" stop-color="#dc2626"/><stop offset="100%" stop-color="#7f1d1d"/></radialGradient>
    <linearGradient id="goldPed" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fef08a"/><stop offset="50%" stop-color="#f59e0b"/><stop offset="100%" stop-color="#78350f"/></linearGradient>
    <radialGradient id="goldRim" cx="30%" cy="30%" r="70%"><stop offset="0%" stop-color="#ffffff"/><stop offset="50%" stop-color="#fbbf24"/><stop offset="100%" stop-color="#b45309"/></radialGradient>
  </defs>
  <!-- Ambient Shadow -->
  <ellipse cx="35" cy="62" rx="26" ry="7" fill="rgba(0,0,0,0.55)"/>
  <!-- Heavy Gold Pedestal -->
  <path d="M12,54 C12,50 58,50 58,54 L58,60 C58,64 12,64 12,60 Z" fill="url(#goldPed)"/>
  <ellipse cx="35" cy="54" rx="23" ry="5" fill="url(#goldRim)"/>
  <ellipse cx="35" cy="54" rx="20" ry="4" fill="#78350f"/>
  <!-- Velvet Tarboosh Body -->
  <path d="M20,52 L25,20 C25,18 45,18 45,20 L50,52 C50,55 20,55 20,52 Z" fill="url(#fezBody)"/>
  <!-- Tarboosh Top -->
  <ellipse cx="35" cy="20" rx="10" ry="3" fill="#ef4444"/>
  <!-- Gold Button & Monocle -->
  <circle cx="35" cy="20" r="3" fill="url(#goldRim)"/>
  <circle cx="42" cy="38" r="6" stroke="#fbbf24" stroke-width="2" fill="rgba(56,189,248,0.3)"/>
  <line x1="48" y1="38" x2="52" y2="48" stroke="#fbbf24" stroke-width="1.5"/>
  <!-- Black Silk Tassel -->
  <path d="M35,20 Q44,22 49,30 Q54,38 52,46" stroke="#0f172a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <polygon points="50,44 55,46 51,54 47,50" fill="#0f172a"/>
</svg>"""

# 4. 3D Figurine: Queen Cleopatra (Pharaoh Nemes Mask on Lapis Lazuli Pedestal)
svgs['fig_cleopatra'] = """<svg viewBox="0 0 70 70" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="lapisPed" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#38bdf8"/><stop offset="50%" stop-color="#1e40af"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <linearGradient id="goldCleo" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fef08a"/><stop offset="40%" stop-color="#f59e0b"/><stop offset="100%" stop-color="#92400e"/></linearGradient>
  </defs>
  <!-- Ambient Shadow -->
  <ellipse cx="35" cy="62" rx="26" ry="7" fill="rgba(0,0,0,0.55)"/>
  <!-- Polished Lapis Lazuli Pedestal -->
  <path d="M12,54 C12,50 58,50 58,54 L58,60 C58,64 12,64 12,60 Z" fill="url(#lapisPed)"/>
  <ellipse cx="35" cy="54" rx="23" ry="5" fill="#38bdf8"/>
  <ellipse cx="35" cy="54" rx="20" ry="4" fill="#1e3a8a"/>
  <!-- Royal Headdress / Nemes Wings -->
  <path d="M16,50 L22,20 C22,12 48,12 48,20 L54,50 L44,52 L42,42 L28,42 L26,52 Z" fill="url(#goldCleo)"/>
  <!-- Royal Blue Lapis Stripes -->
  <line x1="23" y1="22" x2="47" y2="22" stroke="#1d4ed8" stroke-width="2.5"/>
  <line x1="20" y1="28" x2="50" y2="28" stroke="#1d4ed8" stroke-width="2.5"/>
  <line x1="18" y1="34" x2="52" y2="34" stroke="#1d4ed8" stroke-width="2.5"/>
  <line x1="17" y1="40" x2="53" y2="40" stroke="#1d4ed8" stroke-width="2.5"/>
  <!-- Serene Royal Face -->
  <ellipse cx="35" cy="30" rx="7" ry="8.5" fill="#fde68a"/>
  <!-- Kohl Eyeliner & Emerald Eyes -->
  <ellipse cx="31" cy="29" rx="1.8" ry="1.2" fill="#10b981"/>
  <ellipse cx="39" cy="29" rx="1.8" ry="1.2" fill="#10b981"/>
  <path d="M28,29 L34,29" stroke="#0f172a" stroke-width="1.2"/>
  <path d="M36,29 L42,29" stroke="#0f172a" stroke-width="1.2"/>
  <!-- Golden Uraeus Cobra Crown -->
  <path d="M35,18 C33,14 37,12 35,10" stroke="#ef4444" stroke-width="2" fill="none"/>
  <circle cx="35" cy="10" r="1.5" fill="#fbbf24"/>
  <!-- False Beard -->
  <polygon points="33,38 37,38 36,48 34,48" fill="#1d4ed8"/>
</svg>"""

with open("super_3d_assets.json", "w", encoding="utf-8") as f:
    json.dump(svgs, f, ensure_ascii=False)

print("make_super_svgs.py complete! Generated key 3D tokens and models.")
