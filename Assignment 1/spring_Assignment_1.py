# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# simulation time, timestep and time
t_max = 1000
dt = 2
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []

################## Euler integration###############
for t in t_array:

    # append current state to trajectories
    x_list.append(x)
    v_list.append(v)

    # calculate new position and velocity
    a = -k * x / m
    x = x + dt * v
    v = v + dt * a

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.title("Euler Integration")
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.legend()
plt.show()

################## Verlet integration###############


dt_list = np.linspace(1,2, num = 10)

for dt in dt_list:
    x_list = []
    v_list = []

    for t in t_array:

        # append current state to trajectories
        x_list.append(x)
        v_list.append(v)

        if t == 0:
           x_prev = x-v*dt
    
        else:
            x_prev = x_list[-2]
   
    

        # calculate new position and velocity
        a = -k * x / m
        x = 2*x -x_prev + (dt)**2 * a
        v = (1/dt) *((x)-x_list[-1])  

    # convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
    x_array = np.array(x_list)
    v_array = np.array(v_list)

    # plot the position-time graph
    plt.figure(2)
    plt.clf()
    plt.xlabel('time (s)')
    plt.title("Verlet Integration dt = {}".format(dt))
    plt.grid()
    plt.plot(t_array, x_array, label='x (m)')
    plt.plot(t_array, v_array, label='v (m/s)')
    plt.legend()
    plt.show()

    #Verlet becomes unsteady at dt = 1.98