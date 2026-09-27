import math

# Let's verify isometric projection coordinates for SVG paths
# True isometric angles: 30 degrees (-30 and +30 from horizontal)
cos30 = math.cos(math.radians(30))
sin30 = math.sin(math.radians(30))
print(f"Isometric factors: cos30={cos30:.3f}, sin30={sin30:.3f}")

# Test building an isometric cube top, left, right in SVG coordinates
def iso_cube(cx, cy, w, h, depth):
    # top face
    top = f"{cx},{cy-depth} {cx+w},{cy-depth+w*sin30} {cx},{cy-depth+2*w*sin30} {cx-w},{cy-depth+w*sin30}"
    # left face
    left = f"{cx-w},{cy-depth+w*sin30} {cx},{cy-depth+2*w*sin30} {cx},{cy-depth+2*w*sin30+h} {cx-w},{cy-depth+w*sin30+h}"
    # right face
    right = f"{cx},{cy-depth+2*w*sin30} {cx+w},{cy-depth+w*sin30} {cx+w},{cy-depth+w*sin30+h} {cx},{cy-depth+2*w*sin30+h}"
    return top, left, right

top, left, right = iso_cube(50, 50, 20, 30, 10)
print("Isometric cube faces generated:")
print("Top:", top)
print("Left:", left)
print("Right:", right)
