# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:27:10 2019

@author: marcu
"""

import numpy as np

def exp_mode(x, n):
    return (1+(x/n))**n

n = np.logspace(0,17,1000)
y = exp_mode(1,n)

fig, ax = plt.subplots(num=1, clear=True)
ax.semilogx(n, y)