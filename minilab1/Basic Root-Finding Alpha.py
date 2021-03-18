# -*- coding: utf-8 -*-
"""
Basic Root-Finding
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
    return (10.0/(x-2.0)) - (90.0*np.exp(-(x/2.0)))
xp = np.linspace(2.3,9,1000)

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
fig.savefig("BR Alpha Plot.png")
fig.savefig("BR Alpha Plot.eps")

#%% Find Roots
rt1 = opt.brentq(lambda x: f(x), 2.01, 3)
rt2 = opt.brentq(lambda x: f(x), 6, 10)
print("Root Locations")
print("{:.2e} {:.2e}".format(rt1, rt2))