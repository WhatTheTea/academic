import matplotlib as mpl
import mpl_toolkits.mplot3d as mpl3d
import numpy as np
import matplotlib.pyplot as plt
mpl.rcParams["legend.fontsize"] = 10
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1.163
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot3D(x, y, z, label="параметрична крива")
ax.legend()
plt.show()