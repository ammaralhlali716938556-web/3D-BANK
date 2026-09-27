# Let's test generating a matte 3D sculptural SVG with soft directional shading (no cheap gloss)
# Light source: Top-left at 45 degrees. Ambient occlusion underneath.
sample_svg = """<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Soft diffuse lighting gradients for matte stone/clay -->
    <linearGradient id="matteSandL" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#f5e6ca"/>
      <stop offset="100%" stop-color="#dfc59b"/>
    </linearGradient>
    <linearGradient id="matteSandR" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#cfb083"/>
      <stop offset="100%" stop-color="#9a7a4f"/>
    </linearGradient>
    <linearGradient id="goldCapMatte" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fcd34d"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <radialGradient id="aoShadow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="rgba(0,0,0,0.5)"/>
      <stop offset="60%" stop-color="rgba(0,0,0,0.2)"/>
      <stop offset="100%" stop-color="rgba(0,0,0,0)"/>
    </radialGradient>
  </defs>
  <!-- Ambient Contact Shadow -->
  <ellipse cx="50" cy="85" rx="38" ry="10" fill="url(#aoShadow)"/>
  <!-- Base Sand Dune Pedestal -->
  <polygon points="50,22 14,78 50,84" fill="url(#matteSandL)"/>
  <polygon points="50,22 50,84 86,74" fill="url(#matteSandR)"/>
  <!-- Gold Capstone -->
  <polygon points="50,22 40,38 50,40" fill="url(#goldCapMatte)"/>
  <polygon points="50,22 50,40 60,37" fill="#d97706"/>
  <!-- Sphinx Miniature in foreground -->
  <ellipse cx="32" cy="78" rx="10" ry="5" fill="#b45309"/>
  <circle cx="26" cy="73" r="4.5" fill="#dfc59b"/>
</svg>"""

with open("/bank_el_hazz/test_matte.svg", "w") as f:
    f.write(sample_svg)

print("Saved test_matte.svg successfully!")
