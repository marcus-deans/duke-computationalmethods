# -*- coding: utf-8 -*-
"""
Chapra Extrema Search
Marcus Deans
12 November 2019

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""

import numpy as np
import scipy.optimize as opt

def f1(x, y):
    return 2*y**2 - 2.25*x*y - 1.75*y + 1.5*x**2

def f2(x,y):
    return 4*x + 2*y + x**2 - 2*x**4 + 2*x*y -3*y**2

def f3(x,y):
    return -8*x + x**2 + 12*y + 4*y**2 - 2*x*y

min1_loc = opt.fmin(lambda vec: f1(vec[0], vec[1]),[0,0])
min1_val = f1(*min1_loc)
print("Function 1")
print("x: {:.2e} y: {:.2e} f: {:.2e}".format(min1_loc[0], min1_loc[1], min1_val))
min2_loc = opt.fmin(lambda vec: -f2(vec[0], vec[1]),[0,0])
min2_val = f2(*min2_loc)
print("Function 2")
print("x: {:.2e} y: {:.2e} f: {:.2e}".format(min2_loc[0], min2_loc[1], min2_val))
min3_loc = opt.fmin(lambda vec: f3(vec[0], vec[1]),[0,0])
min3_val = f3(*min3_loc)
print("Function 3")
print("x: {:.2e} y: {:.2e} f: {:.2e}".format(min3_loc[0], min3_loc[1], min3_val))
