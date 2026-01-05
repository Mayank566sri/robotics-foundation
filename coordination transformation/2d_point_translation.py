import matplotlib.pyplot as plt

# Original point
x, y = 6, 3       

# Translated point
tx, ty = -4, 5
x1 = x + tx
y1 = y + ty

plt.figure()
plt.scatter(x, y, color='b')
plt.scatter(x1, y1, color='r')
plt.text(x1, y1, "Translated ")
plt.text(x, y, "Original")
plt.axhline(0)
plt.axvline(0)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("2D Point Translation")
plt.grid()
plt.show()