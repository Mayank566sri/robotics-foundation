import math
import matplotlib.pyplot as plt

class Robot:
    # Initialize robot state
    def __init__(self, x=0.0, y=0.0, theta=0.0):
        self.x = x
        self.y = y
        self.theta = theta
        self.traj_x = [x]
        self.traj_y = [y]
        
    # Update robot state based on velocities and time step
    def upate(self, v, w, dt):
        self.x += v*math.cos(self.theta)*dt
        self.y += v*math.sin(self.theta)*dt
        self.theta += w*dt
        self.traj_x.append(self.x)
        self.traj_y.append(self.y)

# Value given for testing        
robot = Robot(x=0.0, y=0.0, theta=0.0)
v = 1.0  # linear velocity
w = 0.5  # angular velocity
dt = 0.1  # time step
steps = 300

# Simulate robot movement
for _ in range(steps):
    robot.upate(v, w, dt)

# Plot the trajectory  
plt.plot(robot.traj_x, robot.traj_y)
plt.xlabel('X position')
plt.ylabel('Y position')
plt.scatter(robot.traj_x[0], robot.traj_y[0], color='b', label='Start')
plt.scatter(robot.traj_x[-1], robot.traj_y[-1], color='r', label='End')
plt.legend()
plt.title('Robot Trajectory')
plt.axis('equal')
plt.grid()
plt.show()
