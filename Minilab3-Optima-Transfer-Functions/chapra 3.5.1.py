# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:04:44 2019

@author: marcu
"""
import numpy as np
import scipy.optimize as opt
import pandas
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

"""
Develop a plot of a cubic spline fit of the following
data with (a) natural end conditions and (b) not-a-knot end
conditions. 

x = {0 ,   100 ,    200,     400,     600,    800,    1000}
f(x)={0, 0.82436, 1.00000, 0.73576, 0.40601, 0.19915, 0.09158}
"""

edata = pandas.read_excel("chapra_18_04.xlsx")
col_1_data = edata.values[:,0].copy()
col_2_data = edata.values[:,1].copy()
x = np.array([col_1_data])
y = np.array([col_2_data])

xmodel = np.linspace(x.min(), x.max(), 100)
cs_knot = CubicSpline(x, y, bc_type='natural')
cs_nat = CubicSpline(x,y)

fig = plt.figure(num=1,clear=True)
ax = fig.add_subplot(1,1,1)
ax.plot(x, y, 'ko', label = 'Data')
ax.plot(xmodel, cs_knot(xmodel), 'b--', label='Not-a-Knot')
ax.plot(xmodel, cs_nat(xmodel), 'r-', label='Natural')

fig = plt.figure(num=2, clear=True)
ax = fig.add_subplot(1,1,1)