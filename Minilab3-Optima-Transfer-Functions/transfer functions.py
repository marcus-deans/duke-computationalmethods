# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:46:54 2019

@author: marcu
"""

import numpy as np
import scipy.optimize as opt
import pandas
from scipy import integrate
#import scipy.integrate as spi
import matplotlib.pyplot as plt

x = np.logspace(0,5, 100)
j=1j
def f(x):
    return np.abs(((j*x)*(j*x + 2000))/((j*x + 10)*(j*x + 1000)))

fig = plt.figure(num=1,clear=True)
ax = fig.add_subplot(1,1,1)
ax.semilogx(x, 20*np.log10(f(x)), 'r-')

maxloc1 = opt.fminbound(lambda x: -f(x), 0, 950)
#print(20*np.log10(maxloc1))
print(maxloc1)
maxval1 = f(maxloc1)
print(maxval1)

eqval = 0.7071*maxval1
#print(eqval)
rt1 = opt.brentq(lambda x: f(x)-eqval, 0, 15)
print(rt1)
rt2 = opt.brentq(lambda x: f(x)-eqval, 1400, 1500)
print(rt2)