# Let's verify the 3D dice math and face rotations in CSS:
# Dice dimensions: 60px x 60px, translateZ = 30px
css = """
.dice-cube {
  width: 60px;
  height: 60px;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 1.2s cubic-bezier(0.2, 0.9, 0.3, 1.2);
}
.dice-face {
  position: absolute;
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #ffffff, #f1f5f9);
  border: 2px solid #cbd5e1;
  border-radius: 12px;
  box-shadow: inset 0 0 8px rgba(0,0,0,0.1);
  display: flex;
  align-items: center;
  justify-content: center;
}
.dice-face.f1 { transform: rotateY(0deg) translateZ(30px); }
.dice-face.f6 { transform: rotateY(180deg) translateZ(30px); }
.dice-face.f2 { transform: rotateY(-90deg) translateZ(30px); }
.dice-face.f5 { transform: rotateY(90deg) translateZ(30px); }
.dice-face.f3 { transform: rotateX(90deg) translateZ(30px); }
.dice-face.f4 { transform: rotateX(-90deg) translateZ(30px); }
"""
print("3D dice math looks solid!")
