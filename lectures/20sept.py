# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:21:38 2019

@author: marcu
"""

import numpy as np
import math as m

def iter_meth(x, es=0.0001, maxit=50):
    #initialization
    iter = 1
    sol = 1
    ea = 100
    
    while True:
        solold = sol
        #sol = sol + x ** iter / m.factorial(iter)
        sol = (((x/sol)+sol)/2)
        iter = iter + 1
        if sol != 0:
            ea = abs((sol - solold))*100
            
        if(ea <= es) or (iter>=maxit):
            break
    fx = sol
        
    return fx, ea, iter
            
print(iter_meth(10))
    