import numpy as np
import matplotlib.pyplot as plt


results = np.loadtxt("C:\\Users\\Adity\\OneDrive\\Cambridge\\lander\\lander\\verlet_mars.txt")
print(results)
plt.figure(1)
plt.clf()
plt.xlabel('altitude (m)')
plt.grid()
plt.plot(results[:, 0], results[:, 1], label='altitude vs actual descent rate (m/s)')
plt.plot(results[:, 0], results[:, 2], label='altitude vs desired descent rate (m/s)')
plt.legend()
plt.show()