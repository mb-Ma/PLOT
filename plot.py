import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

# a=0.6
z6_lard = [0.6568, 2.6829, 7.6913, 14.3467, 21.3881]
x = [1, 2, 3, 4, 5]
y6_lard = [2, 2, 2, 2, 2]
z6_dlard = [0.1239, 0.3900, 2.1494, 4.8358, 7.3266]
y6_dlard = [4, 4, 4, 4, 4]

# a=0.8
z8_lard = [0.6289, 2.6087, 7.6682, 14.4355, 21.3613]
y8_lard = [6, 6, 6, 6, 6]
z8_dlard = [0.1238, 0.3812, 2.1000, 4.8605, 7.1572]
y8_dlard = [8, 8, 8, 8, 8]

# a=1
z1_lard = [0.6428, 2.6458, 7.6798, 14.3911, 21.3747]
y1_lard = [10, 10, 10, 10, 10]
z1_dlard = [0.1239, 0.3856, 2.1247, 4.8481, 7.2419]
y1_dlard = [12, 12, 12, 12, 12]

# y_ticks = np.linspace(0, 16, 8)
y_ticks = [0, 2, 4, 6, 8, 10, 12, 14]
x_ticks = ['U1', 'U2', 'U3', 'U4', 'U5']

ax.plot(x, y6_lard, z6_lard, label='LARD(a=0.6)', color='red')
ax.plot(x, y6_dlard, z6_dlard, label='DLARD(a=0.6)', color='blue')
ax.plot(x, y8_lard, z8_lard, label='LARD(a=0.8)', color='purple')
ax.plot(x, y8_dlard, z8_dlard, label='DLARD(a=0.8)', color='green')
ax.plot(x, y1_lard, z1_lard, label='LARD(a=0.1)', color='brown')
ax.plot(x, y1_dlard, z1_dlard, label='DLARD(a=0.1)', color='grey')
ax.plot([2, 2, 2, 2, 2], [1, 1, 1, 1, 1], [1, 10, 14, 15, 20])
# ax.plot()
ax.legend(loc=1)

plt.yticks(y_ticks, color='white')
plt.xticks(x, x_ticks)
ax.axes.get_yaxis().set_visible(False)
ax.set_xlabel('Sizes of data sets')
ax.set_zlabel('Time consumption (s)')
# 转换视角
# elev = 0
# azim = 45
# ax.view_init(elev, azim)

plt.show()