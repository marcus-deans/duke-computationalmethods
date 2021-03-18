# -*- coding: utf-8 -*-
"""
Chapra 2.22
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

tmodel = np.arange(0.0,(np.pi)*6, (np.pi)/64)
x = np.array(tmodel*(np.cos(6*tmodel)))
y = np.array(tmodel*(np.sin(6*tmodel)))
z = np.array(tmodel)

fig = plt.figure()
fig.set_size_inches(6,8)

# fig, ax = plt.subplots(num=1,clear=True)
ax = fig.add_subplot(2,1,1)
ax.plot(x, y, 'r-')
ax.grid()
ax.set(xlabel = 'x',ylabel='y')
ax.axis('equal')

# fig = plt.figure()
ax = fig.add_subplot(2,1,2, projection='3d')
ax.plot3D(x, y, z, 'cyan')
ax.set(xlabel='x', xticks=[-20,0,20], ylabel='y', yticks=[-20,0,20], zlabel='z', zticks=[0,10,20])

fig.tight_layout()
fig.savefig("Chapra_2.22_Plot.png")
fig.savefig("Chapra_2.22_Plot.eps")