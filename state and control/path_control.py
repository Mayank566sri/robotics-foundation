import numpy as np
import matplotlib.pyplot as plt

#parameters
dt = 0.1
steps = 100
k = 0.4      #(control gain) as k increases, path converges faster to target

#target and starting point
target = np.array([2000.0,1600.0])
start = np.array([0.0,0.0])

#without control
pos = start.copy()
velocity = np.array([30, 70]) 
path = [pos.copy()]

for i in range(steps):
    pos += velocity *dt
    path.append(pos.copy())
path = np.array(path)

#with control
pos = start.copy()
path_control = [pos.copy()]

for i in range(steps):
    error = target - pos
    velocity = k * error
    pos += velocity * dt
    path_control.append(pos.copy())
path_control = np.array(path_control)

#plotting
plt.figure()
plt.plot(path[:,0], path[:,1], label='Without Control')
plt.plot(path_control[:,0], path_control[:,1], label='With Control')
plt.scatter(*target, marker='x', color = 'red', label='Target')
plt.scatter(*start, marker='o', color = 'green', label='Start')
plt.legend()
plt.title('Path Control')
plt.xlabel('X position')
plt.ylabel('Y position')
plt.grid()
plt.show()