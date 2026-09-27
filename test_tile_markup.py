import json

with open("svg_assets.json", "r") as f:
    svg_dict = json.load(f)

print("SVG count:", len(svg_dict))
assert "house_3d" in svg_dict
assert "hotel_3d" in svg_dict
assert "token_tarboosh" in svg_dict
assert "tile_cairo_tower" in svg_dict
print("Asset checks passed!")
