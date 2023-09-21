import numpy as np
import matplotlib.pyplot as plt
import math

# mass, spring constant, initial position and velocity
m = 1000
G = 6.67e-11
M = 5.972e24
position = np.array([0,0,1e10])
r0_mag = 6.37e6
velocity = np.array([0,0,0])

# simulation time, timestep and time
t_max = 1000
dt = 0.1
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
alt_list = []
pos_list = []

################## Verlet integration ###############
for t in t_array:

    # append current state to trajectories
    pos_list.append(position)

    if t == 0:
        pos_prev = position-velocity*dt
    
    else:
        pos_prev = pos_list[-2]

    # calculate new position and velocity
    position_mag = math.sqrt(position[0]**2 + position[1]**2 + position[2]**2)
    

    if position_mag > r0_mag:
        altitude = position_mag - r0_mag
        a = -1*G*M*position/(position_mag**2)        
        position = 2*position -pos_prev + (dt)**2 * a
        velocity = (1/dt) *((position)-pos_prev[-1]) 
    
    else:
        altitude = 0


    
    alt_list.append(altitude)

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
alt_array = np.array(alt_list)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.title("Verlet Integration")
plt.grid()
plt.plot(t_array, alt_array, label='altitude (m)')
plt.legend()
plt.show()
