# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def fun(x):
    return np.cos(x) + x/20

x = np.linspace(-15,15,1000)
fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1,1,1)
ax.plot(x,fun(x))

vals = opt.fminbound(lambda x: fun(x), -5, 5, full_output=True)
print(vals)
ax.plot(vals[0],vals[1],'ro',ms=12)
vals = opt.fminbound(lambda x: fun(x), -15,15,full_output=True)
print(vals)
ax.plot(vals[0],vals[1],'go', ms=8)
vals=opt.fminbound(lambda x: fun(x), -15, 0, full_output=True)
print(vals)
ax.plot(vals[0],vals[1],'bo',ms=4)

fminbound(lambda blah: fun(blah), -11, -10, full_output = True)

nval = opt.fminbound(lambda blah: fun(blah), -11-, -10, full_output = True)[0:2]

nval, dc, dc = opt.fminbound(lambda blah: fun(blah), -11, -10, full_output = True)

fig = plt.figure(num = 2, clear=True)
ax = fig.add_subplot(1,1,1)
ax.plot