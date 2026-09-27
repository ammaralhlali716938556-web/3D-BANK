import json

with open("svg_assets.json", "r", encoding="utf-8") as f:
    all_svgs = json.load(f)

with open("super_3d_assets.json", "r", encoding="utf-8") as f:
    super_svgs = json.load(f)

all_svgs.update(super_svgs)

with open("complete_3d_assets.json", "w", encoding="utf-8") as f:
    json.dump(all_svgs, f, ensure_ascii=False)

print(f"Total merged 3D assets: {len(all_svgs)}")
