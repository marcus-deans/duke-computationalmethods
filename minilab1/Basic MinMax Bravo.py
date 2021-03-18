# -*- coding: utf-8 -*-
"""
Basic MinMax M
Marcus Deans
12 November 2019

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""
#%% Imports
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

#%% Define function and independent range
def f(x):
    return x**5 + 100*np.cos(2*x)
xp = np.linspace(-4,4,1000)

#%% Create and clear figure with two rows of plots
fig, (ax1, ax2) = plt.subplots(2,1,num=1,clear=True)

#%% Plot First Function
ax1.plot(xp,f(xp),'k-')
ax1.set(xlabel='x', ylabel='f(x)')
ax1.grid(True)

#%% Plot Second Function
ax2.plot(xp, np.sign(f(xp)), 'k-')
ax2.set(xlabel='x',ylabel='sign')
ax2.grid(True)

#%% Fix Overlap and Save
fig.tight_layout()
fig.savefig("MinMax Bravo Plot.png")
fig.savefig("MinMax Bravo Plot.eps")

#%% Find Roots
rt1 = opt.brentq(lambda x: f(x), -2, 0)
rt2 = opt.brentq(lambda x: f(x), 0, 2)
rt3 = opt.brentq(lambda x: f(x), 2, 3)
print("Root Locations")
print("{:.2e} {:.2e} {:.2e}".format(rt1, rt2, rt3))

# %% Find Min and Max
minloc1 = opt.fminbound(lambda x: f(x), -2, -1)
minval1 = f(minloc1)
print("Minima Locations")
print("{:.2e} {:.2e}".format(minloc1, minval1))
minloc2 = opt.fminbound(lambda x: f(x), 1, 2)
minval2 = f(minloc2)
print("{:.2e} {:.2e}".format(minloc2, minval2))

print("Maxima Locations")
maxloc1 = opt.fminbound(lambda x: -f(x), -3.5, -1.5)
maxval1 = f(maxloc1)
print("{:.2e} {:.2e}".format(maxloc1, maxval1))
maxloc2 = opt.fminbound(lambda x: -f(x), -1, 1)
maxval2 = f(maxloc2)
print("{:.2e} {:.2e}".format(maxloc2, maxval2))