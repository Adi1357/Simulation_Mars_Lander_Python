import numpy as np
import matplotlib.pyplot as plt


results = np.loadtxt("C:\\Users\\Adity\\OneDrive\\Cambridge\\First Year\\Spring_VS_Code\\Assignment 3\\trajectories_verlet.txt")
print(results)
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(results[:, 0], results[:, 1], label='x (m)')
plt.plot(results[:, 0], results[:, 2], label='v (m/s)')
plt.legend()
plt.show()