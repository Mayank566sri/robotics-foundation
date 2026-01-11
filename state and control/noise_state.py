import math
import matplotlib.pyplot as plt
import random

class Noise:
    # Initialize noise state
    def __init__(self, x=0.0, y=0.0, theta=0.0):
        self.x = x
        self.y = y
        self.theta = theta
        self.traj_x = [x]
        self.traj_y = [y]

    # Update noise state based on velocities and time step with added noise
    def update(self, v, w, dt, v_noise =0.0 , w_noise =0.0):
        v_noise = v + random.gauss(0, v_noise)
        w_noise = w + random.gauss(0, w_noise)

        self.x += (v_noise) * math.cos(self.theta) * dt
        self.y += (v_noise) * math.sin(self.theta) * dt
        self.theta += (w_noise) * dt
        self.traj_x.append(self.x)
        self.traj_y.append(self.y)
        
# Value given for testing
noise = Noise(x=0.0, y=0.0, theta=0.0)
v = 1.0  # linear velocity
w = 0.5  # angular velocity
dt = 0.1  # time step
steps = 300
v_noise = 0.1  # linear velocity noise 
w_noise = 0.05  # angular velocity noise 

# Simulate noise movement
for _ in range(steps):
    noise.update(v, w, dt, v_noise, w_noise)
    
# Plot the trajectory
plt.plot(noise.traj_x, noise.traj_y)
plt.xlabel('X position')
plt.ylabel('Y position')
plt.scatter(noise.traj_x[0], noise.traj_y[0], color='b', label='Start')
plt.scatter(noise.traj_x[-1], noise.traj_y[-1], color='r', label='End')
plt.legend()
plt.title('Noise Trajectory')
plt.axis('equal')
plt.grid()
plt.show()