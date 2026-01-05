import matplotlib.pyplot as plt
import math

# Original point
x, y = 4,3

# Rotation
A_deg = 45
A = math.radians(A_deg)
rx = x*math.cos(A) - y*math.sin(A)
ry = x*math.sin(A) + y*math.cos(A)

# Translation
tx, ty = 5,4
x1 = rx + tx
y1 = ry + ty

plt.figure()
plt.scatter(x, y, color='b')
plt.scatter(x1, y1, color='r')
plt.text(x, y, "Original")
plt.text(x1, y1, f"Rotated {A_deg}° + Translated")
plt.axhline(0)
plt.axvline(0)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("X-axis")
plt.xlim(0,10)
plt.ylabel("Y-axis")
plt.ylim(0,10)
plt.title("2D Point Rotation and Translation")
plt.grid()
plt.show()