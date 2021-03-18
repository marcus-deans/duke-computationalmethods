"""
Chapra 3.9
Marcus Deans
11 November 2019

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits import mplot3d
from matplotlib import cm

n = 0.02
s = 0.001

(x, y) = np.meshgrid(np.linspace(0.01,20,40), np.linspace(0.01,5,41))
z = ((np.sqrt(s))/n)*(((x*y)/(x+(2*y)))**(2/3))

fig = plt.figure(num=1,clear=True)
ax = plt.axes(projection='3d')
makeit = ax.plot_surface(x,y,z, cmap=cm.viridis_r)
ax.set(title="Velocity Using Manning's Equation",
       xlabel='Width $B$, $m$', xticks=[0,5,10,15, 20],
       ylabel='Height $H$, $m$', yticks=[0,1,2,3,4,5],
       zlabel='Velocity $U$, $m/s$', zticks=[0.5,1,1.5,2,2.5,3,3.5])
ax.view_init(elev=35,azim=-135)
fig.colorbar(makeit)
fig.tight_layout()
fig.savefig("Chapra_3.9_Plot.png")
fig.savefig("Chapra_3.9_Plot.eps")