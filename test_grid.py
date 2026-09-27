def get_grid_pos(tile_id):
    if 0 <= tile_id <= 10:
        row = 11
        col = 11 - tile_id
    elif 11 <= tile_id <= 20:
        col = 1
        row = 11 - (tile_id - 10)
    elif 21 <= tile_id <= 30:
        row = 1
        col = 1 + (tile_id - 20)
    elif 31 <= tile_id <= 39:
        col = 11
        row = 1 + (tile_id - 30)
    else:
        raise ValueError("Invalid tile")
    return row, col

for i in range(40):
    r, c = get_grid_pos(i)
    # verify boundary
    assert 1 <= r <= 11 and 1 <= c <= 11
    if i in [0, 10, 20, 30]:
        print(f"Corner tile {i}: row {r}, col {c}")

print("Grid pos mapping verified successfully for all 40 tiles!")
