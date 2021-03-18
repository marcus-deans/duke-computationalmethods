"""
Sphere
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

(phi, theta) = np.meshgrid((np.linspace(0,np.pi,20)), (np.linspace(0,2*np.pi,40)))
x = ((np.sin(phi))*(np.cos(theta)))
y = ((np.sin(phi))*(np.sin(theta)))
z = np.cos(phi)

fig = plt.figure(num=1,clear=True)
fig.set_size_inches(6,6)
ax = plt.axes(projection='3d')
ax.plot_wireframe(x,y,z, color='coral')
ax.set(xlabel='x', xticks=[-1,0,1], ylabel='y', yticks=[-1,0,1], zlabel='z', zticks=[-1,0,1])
fig.tight_layout()
fig.savefig("Sphere.png")
fig.savefig("Sphere.eps")