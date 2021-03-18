"""
Chapra 15.5
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

valu = np.loadtxt("chapra_p15_5.dat")
ix = valu[:,0].copy()
iy = valu[:,1].copy()
iz = valu[:,2].copy()

x = np.reshape(ix,(7,3))
y = np.reshape(iy,(7,3))
z = np.reshape(iz,(7,3))

fig = plt.figure(num=1,clear=True)
ax = plt.axes(projection='3d')
ax.plot_surface(x,y,z, cmap=cm.winter)
ax.set(xlabel='Chloride Concentration $c$, $g/L$', xticks=[0,10,20],
       ylabel='Temperature $T$, $C$', yticks=[0,5,10,15,20,25,30],
       zlabel='Oxygen Concentration $OC$, $mg/L$')
ax.view_init(elev=6,azim=-152)
fig.tight_layout()
fig.savefig("Chapra_15.5_Plot.png")
fig.savefig("Chapra_15.5_Plot.eps")