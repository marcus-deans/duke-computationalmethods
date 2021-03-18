# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:13:13 2019

@author: marcu
"""
import numpy as np
import pandas
from scipy import integrate

edata = pandas.read_excel("chapra_19_09.xlsx")
col_1_data = edata.values[:,0].copy()
col_2_data = edata.values[:,1].copy()
z = np.array([col_1_data])
w = np.array([col_2_data])

pgw = 1000*9.81*w*(75-z)
pgz = 1000*9.81*z*w*(75-z)

force = integrate.simps(pgw,z)
print(force)
actline = (integrate.simps(pgz,z))/(integrate.simps(pgw,z))
print(actline)