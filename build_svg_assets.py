# Generator for rich 3D isometric SVG assets
import json

svg_dict = {}

# 1. 3D House
svg_dict['house_3d'] = """<svg viewBox="0 0 50 50" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hRoofL" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#34d399"/><stop offset="100%" stop-color="#059669"/></linearGradient>
    <linearGradient id="hRoofR" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#10b981"/><stop offset="100%" stop-color="#047857"/></linearGradient>
    <linearGradient id="hWallL" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ffffff"/><stop offset="100%" stop-color="#cbd5e1"/></linearGradient>
    <linearGradient id="hWallR" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f1f5f9"/><stop offset="100%" stop-color="#94a3b8"/></linearGradient>
    <filter id="hShadow" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="1" dy="3" stdDeviation="2" flood-color="#000" flood-opacity="0.45"/></filter>
  </defs>
  <ellipse cx="25" cy="42" rx="18" ry="5" fill="rgba(0,0,0,0.3)"/>
  <!-- Chimney -->
  <polygon points="30,12 35,14 35,22 30,20" fill="#b91c1c"/>
  <polygon points="35,14 37,13 37,21 35,22" fill="#991b1b"/>
  <polygon points="30,12 32,11 37,13 35,14" fill="#f87171"/>
  <!-- Walls -->
  <polygon points="10,28 25,36 25,43 10,35" fill="url(#hWallL)"/>
  <polygon points="25,36 40,28 40,35 25,43" fill="url(#hWallR)"/>
  <!-- Door -->
  <polygon points="15,32 20,35 20,40 15,37" fill="#78350f"/>
  <circle cx="16" cy="36" r="0.8" fill="#fbbf24"/>
  <!-- Window -->
  <polygon points="29,32 35,28 35,32 29,36" fill="#38bdf8"/>
  <line x1="32" y1="30" x2="32" y2="34" stroke="#ffffff" stroke-width="0.8"/>
  <!-- Roof -->
  <polygon points="25,12 10,24 10,28 25,16" fill="url(#hRoofL)" filter="url(#hShadow)"/>
  <polygon points="25,12 25,16 40,28 40,24" fill="url(#hRoofR)"/>
  <line x1="25" y1="12" x2="25" y2="16" stroke="#a7f3d0" stroke-width="1.2"/>
</svg>"""

# 2. 3D Luxury Hotel
svg_dict['hotel_3d'] = """<svg viewBox="0 0 50 50" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hotL" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f87171"/><stop offset="100%" stop-color="#b91c1c"/></linearGradient>
    <linearGradient id="hotR" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ef4444"/><stop offset="100%" stop-color="#7f1d1d"/></linearGradient>
    <linearGradient id="goldRoof" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fef08a"/><stop offset="100%" stop-color="#b45309"/></linearGradient>
  </defs>
  <ellipse cx="25" cy="45" rx="20" ry="4" fill="rgba(0,0,0,0.4)"/>
  <!-- Main Tower Walls -->
  <polygon points="12,18 25,25 25,43 12,36" fill="url(#hotL)"/>
  <polygon points="25,25 38,18 38,36 25,43" fill="url(#hotR)"/>
  <!-- Windows Rows -->
  <polygon points="15,22 18,24 18,26 15,24" fill="#fef08a"/>
  <polygon points="20,25 23,27 23,29 20,27" fill="#fef08a"/>
  <polygon points="15,27 18,29 18,31 15,29" fill="#fef08a"/>
  <polygon points="20,30 23,32 23,34 20,32" fill="#fef08a"/>
  <polygon points="27,25 30,23 30,25 27,27" fill="#fef08a"/>
  <polygon points="32,22 35,20 35,22 32,24" fill="#fef08a"/>
  <polygon points="27,30 30,28 30,30 27,32" fill="#fef08a"/>
  <polygon points="32,27 35,25 35,27 32,29" fill="#fef08a"/>
  <!-- Grand Canopy Door -->
  <polygon points="22,38 28,34 28,41 22,41" fill="#fbbf24"/>
  <!-- Gold Penthouse & Dome -->
  <polygon points="18,12 25,16 25,18 18,14" fill="#fbbf24"/>
  <polygon points="25,16 32,12 32,14 25,18" fill="#d97706"/>
  <!-- Dome Top -->
  <ellipse cx="25" cy="11" rx="6" ry="4" fill="url(#goldRoof)"/>
  <line x1="25" y1="11" x2="25" y2="4" stroke="#fbbf24" stroke-width="1.8"/>
  <circle cx="25" cy="4" r="1.5" fill="#fef08a"/>
</svg>"""

# 3. 3D Figurine Tokens
svg_dict['token_tarboosh'] = """<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="fezShine" cx="30%" cy="30%" r="70%"><stop offset="0%" stop-color="#f87171"/><stop offset="40%" stop-color="#dc2626"/><stop offset="100%" stop-color="#7f1d1d"/></radialGradient>
    <linearGradient id="pedestalGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f1f5f9"/><stop offset="60%" stop-color="#cbd5e1"/><stop offset="100%" stop-color="#64748b"/></linearGradient>
  </defs>
  <!-- Pedestal -->
  <ellipse cx="30" cy="52" rx="22" ry="6" fill="rgba(0,0,0,0.4)"/>
  <path d="M12,46 C12,43 48,43 48,46 L48,50 C48,53 12,53 12,50 Z" fill="url(#pedestalGrad)"/>
  <ellipse cx="30" cy="46" rx="18" ry="4" fill="#f8fafc"/>
  <ellipse cx="30" cy="46" rx="15" ry="3" fill="#e2e8f0"/>
  <!-- Fez Body -->
  <path d="M18,44 L22,18 C22,17 38,17 38,18 L42,44 C42,47 18,47 18,44 Z" fill="url(#fezShine)"/>
  <!-- Fez Top Ellipse -->
  <ellipse cx="30" cy="18" rx="8" ry="2.5" fill="#ef4444"/>
  <!-- Gold Stud -->
  <ellipse cx="30" cy="18" rx="2.5" ry="1" fill="#fbbf24"/>
  <!-- Black Tassel -->
  <path d="M30,18 Q36,20 40,27 Q43,33 42,39" stroke="#1e293b" stroke-width="2.2" fill="none" stroke-linecap="round"/>
  <polygon points="40,36 44,38 41,45 37,42" fill="#0f172a"/>
</svg>"""

svg_dict['token_pharaoh'] = """<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="goldP" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fef08a"/><stop offset="50%" stop-color="#f59e0b"/><stop offset="100%" stop-color="#92400e"/></linearGradient>
    <linearGradient id="lapisP" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#1e3a8a"/></linearGradient>
  </defs>
  <!-- Pedestal -->
  <ellipse cx="30" cy="52" rx="22" ry="6" fill="rgba(0,0,0,0.4)"/>
  <path d="M14,46 C14,43 46,43 46,46 L46,50 C46,53 14,53 14,50 Z" fill="url(#lapisP)"/>
  <ellipse cx="30" cy="46" rx="16" ry="3.5" fill="#fbbf24"/>
  <!-- Pharaoh Bust / Nemes -->
  <path d="M16,42 L20,18 C20,12 40,12 40,18 L44,42 L36,44 L36,36 L24,36 L24,44 Z" fill="url(#goldP)"/>
  <!-- Nemes Blue Stripes -->
  <path d="M21,18 L39,18" stroke="#1d4ed8" stroke-width="2"/>
  <path d="M19,23 L41,23" stroke="#1d4ed8" stroke-width="2"/>
  <path d="M18,28 L42,28" stroke="#1d4ed8" stroke-width="2"/>
  <path d="M17,33 L43,33" stroke="#1d4ed8" stroke-width="2"/>
  <!-- Royal Face -->
  <ellipse cx="30" cy="27" rx="6" ry="7" fill="#fde68a"/>
  <!-- Eyes -->
  <path d="M26,26 Q28,24 30,26" stroke="#0f172a" stroke-width="1" fill="none"/>
  <path d="M30,26 Q32,24 34,26" stroke="#0f172a" stroke-width="1" fill="none"/>
  <!-- Uraeus Cobra on Forehead -->
  <circle cx="30" cy="15" r="2" fill="#ef4444"/>
  <!-- Royal False Beard -->
  <polygon points="28,34 32,34 31,43 29,43" fill="#1e3a8a"/>
</svg>"""

svg_dict['token_bastet'] = """<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="blackLacquer" cx="35%" cy="25%" r="65%"><stop offset="0%" stop-color="#475569"/><stop offset="35%" stop-color="#1e293b"/><stop offset="100%" stop-color="#020617"/></radialGradient>
  </defs>
  <!-- Pedestal -->
  <ellipse cx="30" cy="52" rx="20" ry="6" fill="rgba(0,0,0,0.4)"/>
  <ellipse cx="30" cy="48" rx="16" ry="4" fill="#334155"/>
  <ellipse cx="30" cy="47" rx="14" ry="3" fill="#d97706"/>
  <!-- Cat Body -->
  <path d="M22,46 C20,38 23,28 27,24 C27,20 33,20 33,24 C37,28 40,38 38,46 Z" fill="url(#blackLacquer)"/>
  <!-- Cat Head -->
  <ellipse cx="30" cy="22" rx="7" ry="6" fill="url(#blackLacquer)"/>
  <!-- Ears -->
  <polygon points="24,20 26,10 29,18" fill="url(#blackLacquer)"/>
  <polygon points="36,20 34,10 31,18" fill="url(#blackLacquer)"/>
  <!-- Gold Earrings -->
  <ellipse cx="24" cy="20" rx="1" ry="2" fill="#fbbf24"/>
  <ellipse cx="36" cy="20" rx="1" ry="2" fill="#fbbf24"/>
  <!-- Gold Collar -->
  <path d="M26,28 C28,30 32,30 34,28" stroke="#fbbf24" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <!-- Eyes -->
  <ellipse cx="27" cy="21" rx="1.2" ry="1.8" fill="#38bdf8"/>
  <ellipse cx="33" cy="21" rx="1.2" ry="1.8" fill="#38bdf8"/>
</svg>"""

svg_dict['token_roadster'] = """<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="carRed" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f87171"/><stop offset="50%" stop-color="#ef4444"/><stop offset="100%" stop-color="#991b1b"/></linearGradient>
  </defs>
  <!-- Pedestal -->
  <ellipse cx="30" cy="52" rx="22" ry="6" fill="rgba(0,0,0,0.4)"/>
  <ellipse cx="30" cy="48" rx="18" ry="4" fill="#cbd5e1"/>
  <!-- Wheels -->
  <circle cx="18" cy="42" r="5" fill="#0f172a"/>
  <circle cx="18" cy="42" r="2.5" fill="#f8fafc"/>
  <circle cx="42" cy="42" r="5" fill="#0f172a"/>
  <circle cx="42" cy="42" r="2.5" fill="#f8fafc"/>
  <!-- Car Body -->
  <path d="M12,40 C14,35 18,34 23,34 L37,34 C43,34 46,35 48,40 L45,43 L15,43 Z" fill="url(#carRed)"/>
  <!-- Windshield -->
  <polygon points="26,34 29,26 35,26 37,34" fill="#38bdf8" opacity="0.8"/>
  <!-- Chrome Grille & Headlight -->
  <polygon points="46,36 49,38 48,42 45,41" fill="#f8fafc"/>
  <circle cx="47" cy="37" r="1.5" fill="#fef08a"/>
</svg>"""

# 4. 3D Illustrated Icons for Board Tiles
svg_dict['tile_go'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rocketBody" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f8fafc"/><stop offset="50%" stop-color="#e2e8f0"/><stop offset="100%" stop-color="#94a3b8"/></linearGradient>
    <linearGradient id="goldCoin" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fef08a"/><stop offset="100%" stop-color="#b45309"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="68" rx="30" ry="8" fill="rgba(0,0,0,0.3)"/>
  <!-- Speed Flames -->
  <polygon points="34,50 40,74 46,50" fill="#f97316"/>
  <polygon points="36,50 40,68 44,50" fill="#fef08a"/>
  <!-- 3D Rocket / Arrow -->
  <path d="M40,8 L58,38 L48,38 L48,54 L32,54 L32,38 L22,38 Z" fill="#10b981" filter="drop-shadow(0 4px 6px rgba(0,0,0,0.4))"/>
  <path d="M40,12 L52,38 L44,38 L44,52 L36,52 L36,38 L28,38 Z" fill="#34d399"/>
  <!-- 3D Coins orbiting -->
  <circle cx="20" cy="30" r="7" fill="url(#goldCoin)"/>
  <circle cx="20" cy="30" r="5" fill="#f59e0b"/>
  <circle cx="60" cy="35" r="9" fill="url(#goldCoin)"/>
  <circle cx="60" cy="35" r="6.5" fill="#f59e0b"/>
</svg>"""

svg_dict['tile_pyramid'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="pyrLeft" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fde047"/><stop offset="100%" stop-color="#d97706"/></linearGradient>
    <linearGradient id="pyrRight" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#d97706"/><stop offset="100%" stop-color="#78350f"/></linearGradient>
    <linearGradient id="goldCap" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fef08a"/><stop offset="100%" stop-color="#b45309"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="68" rx="34" ry="9" fill="rgba(0,0,0,0.35)"/>
  <!-- Dunes -->
  <path d="M4,68 Q24,56 46,68 Q64,54 78,68 Z" fill="#ca8a04" opacity="0.6"/>
  <!-- Great Pyramid -->
  <polygon points="38,18 12,62 38,66" fill="url(#pyrLeft)"/>
  <polygon points="38,18 38,66 68,58" fill="url(#pyrRight)"/>
  <!-- Gold Capstone -->
  <polygon points="38,18 32,27 38,28" fill="url(#goldCap)"/>
  <polygon points="38,18 38,28 45,26" fill="#f59e0b"/>
  <!-- Second Pyramid (Khufu/Khafre) -->
  <polygon points="56,28 42,56 56,58" fill="url(#pyrLeft)" opacity="0.9"/>
  <polygon points="56,28 56,58 74,53" fill="url(#pyrRight)" opacity="0.9"/>
  <!-- Sphinx Silhouette -->
  <ellipse cx="24" cy="62" rx="7" ry="3.5" fill="#b45309"/>
  <circle cx="20" cy="58" r="3" fill="#f59e0b"/>
</svg>"""

svg_dict['tile_cairo_tower'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="towerShaft" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#e2e8f0"/><stop offset="40%" stop-color="#ffffff"/><stop offset="100%" stop-color="#64748b"/></linearGradient>
    <linearGradient id="nileBlue" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#0284c7"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="72" rx="30" ry="7" fill="rgba(0,0,0,0.4)"/>
  <!-- Nile River Strip -->
  <path d="M10,72 Q40,66 70,72 L68,76 Q40,70 12,76 Z" fill="url(#nileBlue)"/>
  <!-- Tower Base (Lotus) -->
  <polygon points="32,70 48,70 45,62 35,62" fill="#475569"/>
  <!-- Shaft with Wicker Lattice -->
  <polygon points="36,62 44,62 42,24 38,24" fill="url(#towerShaft)"/>
  <line x1="36" y1="62" x2="42" y2="24" stroke="#94a3b8" stroke-width="0.8"/>
  <line x1="44" y1="62" x2="38" y2="24" stroke="#94a3b8" stroke-width="0.8"/>
  <!-- Observation Pod & Revolving Restaurant -->
  <ellipse cx="40" cy="22" rx="8" ry="4" fill="#fbbf24"/>
  <rect x="34" y="19" width="12" height="4" fill="#d97706" rx="1"/>
  <!-- Spire & Beacons -->
  <line x1="40" y1="18" x2="40" y2="7" stroke="#f8fafc" stroke-width="1.8"/>
  <circle cx="40" cy="7" r="2" fill="#ef4444" filter="drop-shadow(0 0 4px #ef4444)"/>
</svg>"""

svg_dict['tile_citadel'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="domeSilver" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ffffff"/><stop offset="50%" stop-color="#94a3b8"/><stop offset="100%" stop-color="#475569"/></linearGradient>
    <linearGradient id="stoneWall" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fde68a"/><stop offset="100%" stop-color="#b45309"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="70" rx="34" ry="7" fill="rgba(0,0,0,0.35)"/>
  <!-- Citadel Fortress Walls -->
  <polygon points="12,48 68,48 66,66 14,66" fill="url(#stoneWall)"/>
  <!-- Bastion battlements -->
  <rect x="14" y="44" width="6" height="5" fill="#92400e"/>
  <rect x="24" y="44" width="6" height="5" fill="#92400e"/>
  <rect x="50" y="44" width="6" height="5" fill="#92400e"/>
  <rect x="60" y="44" width="6" height="5" fill="#92400e"/>
  <!-- Muhammad Ali Mosque Main Dome -->
  <ellipse cx="40" cy="38" rx="14" ry="12" fill="url(#domeSilver)"/>
  <ellipse cx="40" cy="26" rx="2" ry="1" fill="#fbbf24"/>
  <!-- Half Domes -->
  <ellipse cx="28" cy="42" rx="7" ry="6" fill="url(#domeSilver)"/>
  <ellipse cx="52" cy="42" rx="7" ry="6" fill="url(#domeSilver)"/>
  <!-- Two Tall Pencil Minarets -->
  <line x1="22" y1="50" x2="22" y2="12" stroke="#e2e8f0" stroke-width="2.5"/>
  <polygon points="20,12 24,12 22,6" fill="#fbbf24"/>
  <line x1="58" y1="50" x2="58" y2="12" stroke="#e2e8f0" stroke-width="2.5"/>
  <polygon points="56,12 60,12 58,6" fill="#fbbf24"/>
</svg>"""

svg_dict['tile_lighthouse'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="seaBlue" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#0369a1"/></linearGradient>
    <linearGradient id="lightBeam" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fef08a" stop-opacity="0.8"/><stop offset="100%" stop-color="#fef08a" stop-opacity="0"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="72" rx="34" ry="7" fill="rgba(0,0,0,0.4)"/>
  <!-- Mediterranean Waves -->
  <path d="M4,66 Q20,60 40,66 Q60,60 76,66 L76,74 L4,74 Z" fill="url(#seaBlue)"/>
  <!-- Stone Jetty -->
  <polygon points="26,68 54,68 50,60 30,60" fill="#64748b"/>
  <!-- Lighthouse Base -->
  <polygon points="32,60 48,60 46,40 34,40" fill="#f8fafc"/>
  <!-- Middle Octagonal Tier -->
  <polygon points="35,40 45,40 44,24 36,24" fill="#e2e8f0"/>
  <!-- Lantern Chamber & Flame -->
  <rect x="36" y="16" width="8" height="8" fill="#fbbf24"/>
  <!-- Giant Glowing Light Beams -->
  <polygon points="40,20 78,6 74,36" fill="url(#lightBeam)"/>
  <polygon points="40,20 2,6 6,36" fill="url(#lightBeam)"/>
  <circle cx="40" cy="20" r="4" fill="#ffffff" filter="drop-shadow(0 0 8px #fef08a)"/>
</svg>"""

svg_dict['tile_train'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="locoRed" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ef4444"/><stop offset="100%" stop-color="#991b1b"/></linearGradient>
    <linearGradient id="boilerBrass" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fef08a"/><stop offset="50%" stop-color="#d97706"/><stop offset="100%" stop-color="#78350f"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="70" rx="32" ry="7" fill="rgba(0,0,0,0.4)"/>
  <!-- Railway Track -->
  <line x1="6" y1="68" x2="74" y2="68" stroke="#475569" stroke-width="4"/>
  <line x1="6" y1="72" x2="74" y2="72" stroke="#334155" stroke-width="2"/>
  <!-- Steam Puffs -->
  <circle cx="28" cy="18" r="6" fill="#f8fafc" opacity="0.8"/>
  <circle cx="22" cy="12" r="8" fill="#f8fafc" opacity="0.6"/>
  <circle cx="14" cy="8" r="10" fill="#f8fafc" opacity="0.4"/>
  <!-- Locomotive Cab -->
  <polygon points="46,30 68,30 68,60 46,60" fill="url(#locoRed)"/>
  <rect x="52" y="34" width="10" height="10" fill="#38bdf8" rx="2"/>
  <!-- Boiler Body -->
  <path d="M22,38 L46,38 L46,60 L22,60 C16,60 16,38 22,38 Z" fill="url(#boilerBrass)"/>
  <!-- Smokestack Chimney -->
  <polygon points="26,24 32,24 30,38 28,38" fill="#0f172a"/>
  <!-- Cowcatcher front wedge -->
  <polygon points="12,62 20,54 20,62" fill="#ef4444"/>
  <!-- Big Wheels -->
  <circle cx="28" cy="62" r="7" fill="#0f172a" stroke="#d97706" stroke-width="2"/>
  <circle cx="44" cy="62" r="7" fill="#0f172a" stroke="#d97706" stroke-width="2"/>
  <circle cx="60" cy="62" r="7" fill="#0f172a" stroke="#d97706" stroke-width="2"/>
</svg>"""

svg_dict['tile_chest'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="chestWood" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#b45309"/><stop offset="100%" stop-color="#451a03"/></linearGradient>
    <linearGradient id="goldCoinsG" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fef08a"/><stop offset="100%" stop-color="#b45309"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="68" rx="30" ry="7" fill="rgba(0,0,0,0.45)"/>
  <!-- Chest Body -->
  <polygon points="16,38 64,38 60,64 20,64" fill="url(#chestWood)"/>
  <rect x="18" y="42" width="44" height="4" fill="#fbbf24"/>
  <rect x="20" y="56" width="40" height="4" fill="#fbbf24"/>
  <!-- Chest Open Lid -->
  <polygon points="12,24 68,24 64,38 16,38" fill="url(#chestWood)"/>
  <ellipse cx="40" cy="24" rx="28" ry="6" fill="#d97706"/>
  <!-- Gold Coins & Rubies Spilling Out -->
  <circle cx="34" cy="34" r="6" fill="url(#goldCoinsG)"/>
  <circle cx="44" cy="32" r="7" fill="url(#goldCoinsG)"/>
  <circle cx="28" cy="38" r="5" fill="url(#goldCoinsG)"/>
  <circle cx="52" cy="36" r="6" fill="url(#goldCoinsG)"/>
  <!-- Red Ruby -->
  <polygon points="40,28 44,32 40,36 36,32" fill="#ef4444"/>
  <!-- Golden Lock Clasp -->
  <rect x="37" y="38" width="6" height="8" fill="#fef08a" rx="1.5"/>
</svg>"""

svg_dict['tile_chance'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="qCubeTop" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f472b6"/><stop offset="100%" stop-color="#db2777"/></linearGradient>
    <linearGradient id="qCubeLeft" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ec4899"/><stop offset="100%" stop-color="#be185d"/></linearGradient>
    <linearGradient id="qCubeRight" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#db2777"/><stop offset="100%" stop-color="#831843"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="70" rx="26" ry="6" fill="rgba(0,0,0,0.4)"/>
  <!-- 3D Question Cube -->
  <polygon points="40,16 66,30 40,44 14,30" fill="url(#qCubeTop)"/>
  <polygon points="14,30 40,44 40,66 14,52" fill="url(#qCubeLeft)"/>
  <polygon points="40,44 66,30 66,52 40,66" fill="url(#qCubeRight)"/>
  <!-- Question Mark on Front/Right -->
  <text x="40" y="40" font-size="24" font-weight="900" fill="#ffffff" text-anchor="middle" font-family="sans-serif">?</text>
  <!-- Floating Star Gems -->
  <polygon points="18,18 20,22 24,22 21,25 22,29 18,26 14,29 15,25 12,22 16,22" fill="#fef08a"/>
  <polygon points="64,22 66,25 69,25 67,27 68,30 65,28 62,30 63,27 61,25 64,25" fill="#fef08a"/>
</svg>"""

svg_dict['tile_jail'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="jailStone" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#64748b"/><stop offset="100%" stop-color="#1e293b"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="70" rx="32" ry="7" fill="rgba(0,0,0,0.45)"/>
  <!-- Stone Wall Frame -->
  <rect x="12" y="16" width="56" height="50" fill="url(#jailStone)" rx="4"/>
  <rect x="18" y="22" width="44" height="38" fill="#0f172a" rx="2"/>
  <!-- Heavy Iron Bars -->
  <line x1="26" y1="22" x2="26" y2="60" stroke="#94a3b8" stroke-width="3"/>
  <line x1="35" y1="22" x2="35" y2="60" stroke="#94a3b8" stroke-width="3"/>
  <line x1="45" y1="22" x2="45" y2="60" stroke="#94a3b8" stroke-width="3"/>
  <line x1="54" y1="22" x2="54" y2="60" stroke="#94a3b8" stroke-width="3"/>
  <line x1="18" y1="40" x2="62" y2="40" stroke="#64748b" stroke-width="2"/>
  <!-- Giant Gold Padlock -->
  <path d="M36,46 C36,42 44,42 44,46 L44,50 L36,50 Z" stroke="#fbbf24" stroke-width="2.5" fill="none"/>
  <rect x="33" y="49" width="14" height="11" fill="#f59e0b" rx="2"/>
  <circle cx="40" cy="54" r="1.5" fill="#0f172a"/>
</svg>"""

svg_dict['tile_parking'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="convertibleRed" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f87171"/><stop offset="50%" stop-color="#ef4444"/><stop offset="100%" stop-color="#991b1b"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="70" rx="34" ry="7" fill="rgba(0,0,0,0.4)"/>
  <!-- Palm Shade -->
  <path d="M62,68 Q66,40 56,22" stroke="#92400e" stroke-width="4" fill="none"/>
  <path d="M56,22 Q72,18 78,28" stroke="#10b981" stroke-width="3" fill="none"/>
  <path d="M56,22 Q48,10 40,16" stroke="#10b981" stroke-width="3" fill="none"/>
  <!-- Luxury Red Convertible Car -->
  <ellipse cx="20" cy="62" rx="6" ry="6" fill="#0f172a"/>
  <circle cx="20" cy="62" r="3" fill="#cbd5e1"/>
  <ellipse cx="50" cy="62" rx="6" ry="6" fill="#0f172a"/>
  <circle cx="50" cy="62" r="3" fill="#cbd5e1"/>
  <path d="M10,58 C14,50 22,48 30,48 L48,48 C56,48 60,52 64,58 Z" fill="url(#convertibleRed)"/>
  <!-- Windshield -->
  <polygon points="34,48 38,38 46,38 48,48" fill="#38bdf8" opacity="0.8"/>
  <!-- Big Shiny Parking 'P' Symbol -->
  <circle cx="26" cy="24" r="12" fill="#3b82f6" stroke="#ffffff" stroke-width="2"/>
  <text x="26" y="30" font-size="16" font-weight="900" fill="#ffffff" text-anchor="middle" font-family="sans-serif">P</text>
</svg>"""

svg_dict['tile_gotojail'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="sirenGlow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#ef4444"/><stop offset="100%" stop-color="#991b1b"/></radialGradient>
  </defs>
  <ellipse cx="40" cy="68" rx="30" ry="7" fill="rgba(0,0,0,0.4)"/>
  <!-- Flashing Siren Light Base -->
  <polygon points="26,64 54,64 48,44 32,44" fill="#334155"/>
  <!-- Siren Glass Dome -->
  <path d="M30,44 C30,28 50,28 50,44 Z" fill="url(#sirenGlow)" filter="drop-shadow(0 0 10px #ef4444)"/>
  <!-- Light Rays -->
  <line x1="40" y1="26" x2="40" y2="12" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <line x1="28" y1="30" x2="16" y2="20" stroke="#3b82f6" stroke-width="3" stroke-linecap="round"/>
  <line x1="52" y1="30" x2="64" y2="20" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <!-- Chrome Handcuffs -->
  <circle cx="26" cy="56" r="6" stroke="#e2e8f0" stroke-width="2.5" fill="none"/>
  <circle cx="44" cy="56" r="6" stroke="#e2e8f0" stroke-width="2.5" fill="none"/>
  <line x1="32" y1="56" x2="38" y2="56" stroke="#cbd5e1" stroke-width="3"/>
</svg>"""

svg_dict['tile_tax'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sackGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fbbf24"/><stop offset="100%" stop-color="#d97706"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="70" rx="30" ry="7" fill="rgba(0,0,0,0.4)"/>
  <!-- Money Bag Body -->
  <path d="M22,66 C14,54 18,36 30,34 C30,30 36,22 40,22 C44,22 50,30 50,34 C62,36 66,54 58,66 Z" fill="url(#sackGrad)"/>
  <!-- Rope Tie -->
  <ellipse cx="40" cy="34" rx="10" ry="3" fill="#b45309"/>
  <!-- Egyptian Pound Sign £ / ج.م -->
  <circle cx="40" cy="50" r="10" fill="#92400e" opacity="0.3"/>
  <text x="40" y="55" font-size="14" font-weight="900" fill="#451a03" text-anchor="middle" font-family="sans-serif">ج.م</text>
  <!-- Flying Banknotes -->
  <rect x="14" y="24" width="16" height="8" rx="1" fill="#10b981" transform="rotate(-20 22 28)"/>
  <rect x="52" y="22" width="16" height="8" rx="1" fill="#10b981" transform="rotate(25 60 26)"/>
</svg>"""

svg_dict['tile_electric'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="boltGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fef08a"/><stop offset="50%" stop-color="#eab308"/><stop offset="100%" stop-color="#ca8a04"/></linearGradient>
    <radialGradient id="plasmaGlow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#38bdf8"/><stop offset="100%" stop-color="transparent"/></radialGradient>
  </defs>
  <ellipse cx="40" cy="70" rx="28" ry="6" fill="rgba(0,0,0,0.4)"/>
  <!-- Generator Turbine Base -->
  <polygon points="20,68 60,68 54,48 26,48" fill="#475569"/>
  <!-- Plasma Glow Sphere -->
  <circle cx="40" cy="36" r="24" fill="url(#plasmaGlow)"/>
  <!-- Giant 3D Lightning Bolt -->
  <polygon points="46,8 24,38 38,38 32,64 56,32 42,32" fill="url(#boltGrad)" filter="drop-shadow(0 0 8px #fef08a)"/>
</svg>"""

svg_dict['tile_water'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hydrantBlue" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#0284c7"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="70" rx="28" ry="6" fill="rgba(0,0,0,0.4)"/>
  <!-- Water Drops Splash -->
  <path d="M40,10 C40,10 24,32 24,42 C24,51 31,58 40,58 C49,58 56,51 56,42 C56,32 40,10 40,10 Z" fill="url(#hydrantBlue)" filter="drop-shadow(0 0 8px #38bdf8)"/>
  <ellipse cx="36" cy="36" rx="4" ry="8" fill="#bae6fd" opacity="0.7" transform="rotate(-20 36 36)"/>
  <!-- Splash ripples -->
  <ellipse cx="40" cy="64" rx="24" ry="4" stroke="#38bdf8" stroke-width="2" fill="none"/>
  <circle cx="18" cy="32" r="3.5" fill="#38bdf8"/>
  <circle cx="62" cy="28" r="4.5" fill="#38bdf8"/>
</svg>"""

# 5. Center Diorama 3D Animated Landscape
svg_dict['center_diorama'] = """<svg viewBox="0 0 400 240" class="center-diorama-svg" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1e1b4b"/><stop offset="50%" stop-color="#312e81"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <linearGradient id="nileWater" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#0284c7"/><stop offset="50%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#0369a1"/></linearGradient>
    <linearGradient id="pyrGoldDiorama" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fde047"/><stop offset="100%" stop-color="#b45309"/></linearGradient>
  </defs>
  <!-- Background Glowing Night/Sunset Sky -->
  <rect x="0" y="0" width="400" height="240" fill="url(#skyGrad)" rx="16"/>
  
  <!-- Glowing Sun / Moon -->
  <circle cx="200" cy="50" r="32" fill="#fbbf24" opacity="0.3" filter="blur(6px)"/>
  <circle cx="200" cy="50" r="22" fill="#fef08a"/>
  
  <!-- Distant Dunes -->
  <path d="M0,160 Q80,120 180,150 Q280,110 400,160 L400,240 L0,240 Z" fill="#92400e" opacity="0.5"/>
  
  <!-- 3D Great Pyramids in Center Horizon -->
  <polygon points="120,70 60,160 120,165" fill="#ca8a04"/>
  <polygon points="120,70 120,165 170,155" fill="#78350f"/>
  <polygon points="120,70 110,84 120,86" fill="#fef08a"/>
  
  <polygon points="190,85 145,160 190,165" fill="#eab308"/>
  <polygon points="190,85 190,165 230,158" fill="#92400e"/>
  
  <!-- Cairo Tower on the Right -->
  <polygon points="310,40 316,40 314,160 312,160" fill="#f8fafc"/>
  <line x1="313" y1="40" x2="313" y2="24" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="313" cy="24" r="2" fill="#ef4444"/>
  <ellipse cx="313" cy="46" rx="8" ry="3.5" fill="#fbbf24"/>
  
  <!-- Saladin Citadel on the Left -->
  <ellipse cx="40" cy="115" rx="14" ry="10" fill="#cbd5e1"/>
  <line x1="28" y1="125" x2="28" y2="88" stroke="#f8fafc" stroke-width="2"/>
  <line x1="52" y1="125" x2="52" y2="88" stroke="#f8fafc" stroke-width="2"/>
  
  <!-- Animated Nile River Stream -->
  <path d="M0,170 Q100,150 200,175 Q300,150 400,170 L400,240 L0,240 Z" fill="url(#nileWater)"/>
  
  <!-- Traditional Egyptian Felucca Sailboat sailing on the Nile -->
  <g transform="translate(180, 160)">
    <polygon points="0,20 36,20 30,28 6,28" fill="#78350f"/>
    <!-- Triangular Tall White Sail -->
    <polygon points="12,18 22,-14 26,18" fill="#ffffff" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.3))"/>
  </g>
  
  <!-- Palm Trees on Riverbank -->
  <g transform="translate(350, 140)">
    <path d="M10,40 Q16,20 12,0" stroke="#78350f" stroke-width="4" fill="none"/>
    <path d="M12,0 Q26,-6 32,8" stroke="#10b981" stroke-width="3" fill="none"/>
    <path d="M12,0 Q-4,-6 -10,8" stroke="#10b981" stroke-width="3" fill="none"/>
    <path d="M12,0 Q12,-16 16,-4" stroke="#10b981" stroke-width="3" fill="none"/>
  </g>
</svg>"""

with open("svg_assets.json", "w", encoding="utf-8") as f:
    json.dump(svg_dict, f, ensure_ascii=False)

print("build_svg_assets.py completed. Generated", len(svg_dict), "rich 3D SVG assets!")
