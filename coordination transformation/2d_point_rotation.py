import math
import matplotlib.pyplot as plt

x,y = 6,3

A_deg = 45
A = math.radians(A_deg)

x1 = x*math.cos(A) - y*math.sin(A)
y1 = x*math.sin(A) + y*math.cos(A)

plt.figure()
plt.scatter(x,y)
plt.scatter(x1,y1,color='r')

plt.text(x,y,"Original")
plt.text(x1,y1,f"Rotated ({A_deg}°)")
plt.axhline(0)
plt.axvline(0)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("2D Point Rotation")
plt.grid()
plt.show()