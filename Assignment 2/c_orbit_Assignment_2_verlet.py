import numpy as np
import matplotlib.pyplot as plt
import math

# mass, spring constant, initial position and velocity
m = 1000
G = 6.67e-11
M = 5.972e24
h= 7e6
position = np.array([h,0,0])
r0_mag = 6.37e6
velocity = np.array([0,np.sqrt(G*M/h),0])

# simulation time, timestep and time
t_max = 2*np.pi/(np.sqrt(G*M/h)/h) +200
dt = 1
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
pos_list = []

################## Euler integration###############
for t in t_array:

    # append current state to trajectories
    pos_list.append(position)

    if t == 0:
        pos_prev = position-velocity*dt
    
    else:
        pos_prev = pos_list[-2]

    # calculate new position and velocity
    position_mag = math.sqrt(position[0]**2 + position[1]**2 + position[2]**2)
    
    a = -1*G*M*position/(position_mag**3)        
    position = 2*position -pos_prev + (dt)**2 * a
    velocity = (1/dt) *((position)-pos_prev[-1]) 


    
# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
pos_array = np.array(pos_list)
pos_x_array = pos_array[:, 0]
pos_y_array = pos_array[:, 1]

# Plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title("Verlet Circular Orbit")
plt.grid()
plt.plot(pos_x_array, pos_y_array, label='Orbit')
plt.scatter([0], [0], color='red', label='Earth')
plt.legend()
plt.show()
