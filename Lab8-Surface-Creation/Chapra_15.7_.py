"""
Chapra 15.6
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
from fitting_common import *

"""
Use multiple linear regression to derive a predictive
equation for dissolved oxygen concentration as a function of temperature and chloride based on the data from
Table P15.5. Use the equation to estimate the concentration
of dissolved oxygen for a chloride concentration of 15 g/L at
T = 12 °C. Note that the true value is 9.09 mg/L. Compute the percent relative error for your prediction. 
Explain possible causes for the discrepancy.
"""

valu = np.loadtxt("chapra_p15_5.dat")
x = valu[:,0].copy()
y = valu[:,1].copy()
z = valu[:,2].copy()

xmat = np.reshape(x,(7,3))
ymat = np.reshape(y,(7,3))
zmat = np.reshape(z,(7,3))

# %% Perform calculations
def zfun(xe, ye, coefs):
    return (coefs[0]*(xe**0)*ye**0 + coefs[1]*xe**1 + coefs[2]*ye**3 + 
            coefs[3]*ye**2 + coefs[4]*ye**1)

# %% Reshape data for block matrices
xv = np.reshape(x, (-1, 1))
yv = np.reshape(y, (-1, 1))
zv = np.reshape(z, (-1, 1))
phi_mat = np.block([[(xv**0)*(yv**0), xv**1, yv**3, yv**2, yv**1]])
pvec = np.linalg.lstsq(phi_mat, zv, rcond=None)[0]

# %% First Graph Values
(xi, yi) = np.meshgrid(np.linspace(0,20,7), np.linspace(0,30,19))
zi = zfun(xi, yi, pvec)
zest = zfun(xv, yv, pvec)
#%% First Graph
fig = plt.figure(num=1,clear=True)
fig.set_size_inches(6,4)
ax = plt.axes(projection='3d')
ax.plot_surface(xi,yi,zi, cmap=cm.twilight)
ax.set(xlabel='Chloride Concentration $c$, $g/L$', xticks=[0,10,20],
       ylabel='Temperature $T$, $C$', yticks=[0,5,10,15,20,25,30],
       zlabel='Oxygen Concentration $OC$, $mg/L$')
ax.view_init(elev=6,azim=-152)
fig.tight_layout()
fig.savefig("Chapra_15.7_Plot_Alpha.png")
fig.savefig("Chapra_15.7_Plot_Alpha.eps")

#%% Second Graph
fig = plt.figure(num=2, clear=True)
fig.set_size_inches(6,4)
ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.plot_surface(xmat, ymat, zmat-(np.reshape(zest,(7,3))), cmap=cm.autumn)
ax.set(xlabel='Chloride Concentration $c$, $g/L$', xticks=[0,10,20],
       ylabel='Temperature $T$, $C$', yticks=[0,5,10,15,20,25,30],
       zlabel='Residual, $mg/L$')
fig.tight_layout()
fig.savefig("Chapra_15.7_Plot_Bravo.png")
fig.savefig("Chapra_15.7_Plot_Bravo.eps")
#%% Get and Print Statistics
st, sr, r2 = calc_stats(zv, zest,False)
print("The coefficients are: ")
print(pvec)
print("The OC Estimate when c = 15 g/L and T is 12 degrees is {:.3e}".format(float(zfun(15,12,pvec))))
print(abs((((float(zfun(15,12,pvec))))-9.09)/9.09))
print("St - Sum of Residual Squares: {:.3e}".format(st))
print("Sr - Sum of Squares of Estimate Residuals: {:.3e}".format(sr))
print("R Squared Value: {:.3e}".format(r2))