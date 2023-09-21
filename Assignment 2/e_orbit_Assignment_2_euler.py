import numpy as np
import matplotlib.pyplot as plt
import math

# Constants
G = 6.67e-11
M = 5.972e24
r0 = 6.37e6
a = 1.5e7  # Semi-major axis of the ellipse (half of the longest axis)
e = 0.7    # Eccentricity of the ellipse

# Calculate the initial position and velocity based on elliptical orbit parameters
r_periapsis = a * (1 - e)
v_periapsis = np.sqrt(G * M * ((2 / r_periapsis) - (1 / a)))
initial_position = np.array([r_periapsis, 0, 0])
initial_velocity = np.array([0, v_periapsis, 0])

# Simulation parameters
t_max = 1e5
dt = 1
t_array = np.arange(0, t_max, dt)

# Initialize empty lists to record trajectories
pos_list = []

# Verlet integration loop
prev_position = initial_position - initial_velocity * dt  # Initial position at t-dt
position = initial_position
velocity = initial_velocity

for t in t_array:
    # append current state to trajectories
    pos_list.append(position)

    # calculate new position and velocity
    position_mag = math.sqrt(position[0]**2 + position[1]**2 + position[2]**2)

    a = -1*G*M*position/(position_mag**3)
    velocity = velocity + dt * a
    position = position + dt * velocity

# Convert trajectory list into arrays for plotting
pos_array = np.array(pos_list)
pos_x_array = pos_array[:, 0]
pos_y_array = pos_array[:, 1]

# Plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title("Euler Elliptical Orbit")
plt.grid()
plt.plot(pos_x_array, pos_y_array, label='Orbit')
plt.scatter([0], [0], color='red', label='Earth')
plt.legend()
plt.axis('equal')  # Set equal scaling for x and y axes
plt.show()