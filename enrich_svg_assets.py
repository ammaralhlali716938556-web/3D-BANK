import json

with open("svg_assets.json", "r") as f:
    svg_dict = json.load(f)

# 3D Oasis Desert Villa (Brown - العريش / بورسعيد)
svg_dict['tile_oasis_villa'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="mudWall" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fde68a"/><stop offset="100%" stop-color="#b45309"/></linearGradient>
    <linearGradient id="terracotta" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ea580c"/><stop offset="100%" stop-color="#9a3412"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="70" rx="30" ry="7" fill="rgba(0,0,0,0.4)"/>
  <!-- Palm tree -->
  <path d="M60,68 Q64,46 54,28" stroke="#78350f" stroke-width="3.5" fill="none"/>
  <path d="M54,28 Q70,22 74,32" stroke="#10b981" stroke-width="2.8" fill="none"/>
  <path d="M54,28 Q44,14 38,20" stroke="#10b981" stroke-width="2.8" fill="none"/>
  <path d="M54,28 Q56,12 60,24" stroke="#10b981" stroke-width="2.8" fill="none"/>
  <!-- Villa Base -->
  <polygon points="16,42 40,54 40,68 16,56" fill="url(#mudWall)"/>
  <polygon points="40,54 62,42 62,56 40,68" fill="#92400e"/>
  <!-- Terracotta Sloped Roof -->
  <polygon points="40,32 12,46 40,56 66,42" fill="url(#terracotta)"/>
  <!-- Wooden Arched Door -->
  <polygon points="24,54 32,58 32,65 24,61" fill="#451a03"/>
  <!-- Upper Terrace & Clay Urn -->
  <ellipse cx="40" cy="34" rx="3" ry="4" fill="#ea580c"/>
</svg>"""

# 3D Delta Mediterranean Townhouse (Light Blue - طنطا / شبين / المنصورة)
svg_dict['tile_delta_townhouse'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="blueWall" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#e0f2fe"/><stop offset="100%" stop-color="#7dd3fc"/></linearGradient>
    <linearGradient id="roofBlue" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#38bdf8"/><stop offset="100%" stop-color="#0369a1"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="70" rx="32" ry="7" fill="rgba(0,0,0,0.4)"/>
  <!-- Townhouse Left Wall -->
  <polygon points="18,36 38,48 38,68 18,56" fill="url(#blueWall)"/>
  <!-- Townhouse Right Wall -->
  <polygon points="38,48 62,34 62,54 38,68" fill="#0284c7"/>
  <!-- French Balconies -->
  <rect x="22" y="44" width="8" height="10" fill="#0369a1" rx="1"/>
  <rect x="44" y="42" width="10" height="10" fill="#0369a1" rx="1"/>
  <line x1="20" y1="52" x2="32" y2="52" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="42" y1="50" x2="56" y2="50" stroke="#ffffff" stroke-width="1.5"/>
  <!-- Mansard Roof -->
  <polygon points="38,20 14,38 38,48 64,34" fill="url(#roofBlue)"/>
  <!-- Chimney -->
  <polygon points="46,18 50,16 50,26 46,28" fill="#b91c1c"/>
</svg>"""

# 3D Belle Époque Neoclassical Palace (Pink - دمنهور / كفر الشيخ / الزقازيق)
svg_dict['tile_neoclassic_palace'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="pinkStucco" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#fdf4ff"/><stop offset="100%" stop-color="#f0abfc"/></linearGradient>
    <linearGradient id="pinkRoof" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#e879f9"/><stop offset="100%" stop-color="#a21caf"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="70" rx="32" ry="7" fill="rgba(0,0,0,0.4)"/>
  <!-- Palace Left Facade -->
  <polygon points="16,36 38,48 38,68 16,56" fill="url(#pinkStucco)"/>
  <!-- Palace Right Facade -->
  <polygon points="38,48 64,34 64,54 38,68" fill="#c026d3"/>
  <!-- Neoclassical Columns -->
  <line x1="22" y1="42" x2="22" y2="60" stroke="#ffffff" stroke-width="2.5"/>
  <line x1="30" y1="46" x2="30" y2="64" stroke="#ffffff" stroke-width="2.5"/>
  <line x1="46" y1="46" x2="46" y2="60" stroke="#ffffff" stroke-width="2.5"/>
  <line x1="56" y1="40" x2="56" y2="54" stroke="#ffffff" stroke-width="2.5"/>
  <!-- Ornate Gilded Dome Roof -->
  <ellipse cx="38" cy="28" rx="14" ry="12" fill="url(#pinkRoof)"/>
  <circle cx="38" cy="16" r="2" fill="#fbbf24"/>
</svg>"""

# 3D Fayoum Waterwheel & Oasis (Orange - بني سويف / الفيوم / المنيا)
svg_dict['tile_fayoum_waterwheel'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="waterwheelWood" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f59e0b"/><stop offset="100%" stop-color="#78350f"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="70" rx="32" ry="7" fill="rgba(0,0,0,0.4)"/>
  <!-- Canal Water -->
  <path d="M6,66 Q40,60 74,66 L74,72 L6,72 Z" fill="#0284c7"/>
  <!-- Stone Base -->
  <polygon points="14,48 34,48 30,68 12,68" fill="#d97706"/>
  <!-- Giant 3D Wooden Waterwheel (ساقية الهدير) -->
  <circle cx="48" cy="46" r="20" stroke="url(#waterwheelWood)" stroke-width="5" fill="none"/>
  <circle cx="48" cy="46" r="14" stroke="url(#waterwheelWood)" stroke-width="2" fill="none"/>
  <circle cx="48" cy="46" r="4" fill="#451a03"/>
  <!-- Spokes -->
  <line x1="28" y1="46" x2="68" y2="46" stroke="#b45309" stroke-width="2.5"/>
  <line x1="48" y1="26" x2="48" y2="66" stroke="#b45309" stroke-width="2.5"/>
  <line x1="34" y1="32" x2="62" y2="60" stroke="#b45309" stroke-width="2.5"/>
  <line x1="62" y1="32" x2="34" y2="60" stroke="#b45309" stroke-width="2.5"/>
  <!-- Water Drops Gushing from Paddles -->
  <circle cx="56" cy="56" r="2.5" fill="#38bdf8"/>
  <circle cx="62" cy="50" r="2" fill="#38bdf8"/>
</svg>"""

# 3D Red Sea Luxury Beach Resort (Yellow - الغردقة / شرم الشيخ / مرسى مطروح)
svg_dict['tile_redsea_resort'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="poolTurquoise" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#2dd4bf"/><stop offset="100%" stop-color="#0284c7"/></linearGradient>
    <linearGradient id="villaWhite" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ffffff"/><stop offset="100%" stop-color="#e2e8f0"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="72" rx="34" ry="7" fill="rgba(0,0,0,0.4)"/>
  <!-- Luxury Infinity Pool -->
  <ellipse cx="48" cy="62" rx="22" ry="9" fill="url(#poolTurquoise)"/>
  <ellipse cx="48" cy="62" rx="18" ry="6" fill="#67e8f9" opacity="0.6"/>
  <!-- Modern Cubist Resort Villa -->
  <polygon points="12,38 34,48 34,66 12,56" fill="url(#villaWhite)"/>
  <polygon points="34,48 52,38 52,56 34,66" fill="#94a3b8"/>
  <!-- Big Glass Patio Doors -->
  <polygon points="18,46 28,50 28,60 18,56" fill="#0284c7" opacity="0.8"/>
  <!-- Rooftop Terrace & Yellow Sun Umbrella -->
  <path d="M22,26 L38,26 L30,16 Z" fill="#eab308"/>
  <line x1="30" y1="26" x2="30" y2="38" stroke="#475569" stroke-width="1.8"/>
</svg>"""

# 3D Alexandria Royal Palace (Green - الأقصر / أسوان / الإسكندرية)
svg_dict['tile_alex_palace'] = """<svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="emeraldRoof" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#34d399"/><stop offset="100%" stop-color="#065f46"/></linearGradient>
    <linearGradient id="marbleWall" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#ffffff"/><stop offset="100%" stop-color="#cbd5e1"/></linearGradient>
  </defs>
  <ellipse cx="40" cy="70" rx="34" ry="7" fill="rgba(0,0,0,0.4)"/>
  <!-- Grand Palace Facade -->
  <polygon points="14,38 40,50 40,68 14,56" fill="url(#marbleWall)"/>
  <polygon points="40,50 66,38 66,56 40,68" fill="#64748b"/>
  <!-- Royal Emerald Domes -->
  <ellipse cx="26" cy="32" rx="9" ry="10" fill="url(#emeraldRoof)"/>
  <circle cx="26" cy="22" r="1.8" fill="#fbbf24"/>
  <ellipse cx="54" cy="32" rx="9" ry="10" fill="url(#emeraldRoof)"/>
  <circle cx="54" cy="22" r="1.8" fill="#fbbf24"/>
  <!-- Central Grand Tower -->
  <polygon points="34,22 46,22 44,48 36,48" fill="url(#marbleWall)"/>
  <polygon points="32,22 48,22 40,8" fill="url(#emeraldRoof)"/>
  <circle cx="40" cy="8" r="2.2" fill="#fbbf24"/>
  <!-- Palace Arches -->
  <path d="M22,54 C22,48 30,48 30,54 L30,62 L22,58 Z" fill="#047857"/>
  <path d="M48,54 C48,48 56,48 56,54 L56,62 L48,64 Z" fill="#047857"/>
</svg>"""

with open("svg_assets.json", "w", encoding="utf-8") as f:
    json.dump(svg_dict, f, ensure_ascii=False)

print("Enriched svg_assets.json successfully! Total SVGs now:", len(svg_dict))
