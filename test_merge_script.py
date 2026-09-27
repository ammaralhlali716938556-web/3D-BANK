import json

with open("matte_3d_assets.json", "r", encoding="utf-8") as f:
    matte_assets = json.load(f)

print(f"Loaded {len(matte_assets)} matte assets successfully.")
