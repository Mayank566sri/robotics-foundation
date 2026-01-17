import matplotlib.pyplot as plt

v1 = [2,6]      # defining vector 1
plt.quiver(0, 0, v1[0], v1[1], angles = 'xy', scale_units = 'xy', scale = 1, color = 'r', label='VECTOR 1')

v2 = [8,10]     # defining vector 2
plt.quiver(0, 0, v2[0], v2[1], angles = 'xy', scale_units = 'xy', scale = 1, color = 'y', label='VECTOR 2')  

plt.xlim(0, 12)    # set x-axis limit
plt.ylim(0, 12)    # set y-axis limit

plt.legend(loc = 2)     # legend at upper left corner
plt.grid()              # display grid

plt.title("Vector Representation")         
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
