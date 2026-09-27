import json

with open("svg_assets.json", "r") as f:
    svgs = json.load(f)

print(f"Loaded {len(svgs)} SVGs from svg_assets.json")
for k in svgs:
    print(" -", k, f"({len(svgs[k])} chars)")
