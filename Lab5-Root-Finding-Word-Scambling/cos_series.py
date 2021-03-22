# -*- coding: utf-8 -*-
"""
[Cos Series]
[Marcus Deans]
[1 October 2019]

Based on: Extended python version of Chapra Figure 4.2
Extended python version of Chapra Figure 4.2
From: Applied Numerical Methods with MATLAB
      for Engineers and Scientists, 4th ed
      Steven C. Chapra
      McGraw-Hill 2018
@author: DukeEgr93
v. 1.0, 9/21/2019

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""

import math as m
import numpy as np

def calc_cos(x, es=0.0001, maxit=50):
    '''
    Maclaurin series of exponential function
      fx, ea, it, sollist, ealist = iter_meth(x, es, maxit)
    input:
      x = value at which series evaluated
      es = stopping criterion (default = 0.0001)
      maxit = maximum iterations (default = 50)
    output:
      fx = estimated value
      ea = approximate relative error (%)
      it = number of iterations
      sollist = estimated values at each iteration
      ealist = approcimate relative error (%) at each iteration
    '''

    # initialization
#    maxit+=3
    it = 0
    sol = 0
    ea = 100
    sollist = []
    ealist = []
    pm = -1.0

    # iterative calculation
    while True:
        pm = -pm
        solold = sol
        top = x**(2*it)
        bottom = m.factorial(2*it)
        sol += pm*(top/bottom)
        
        it += 1
        if sol != 0:
            ea = abs((sol - solold)/sol)*100

        sollist += [sol]
        ealist += [ea]

        if ea <= es or it >= maxit:
            break

    fx = sol

    return fx, ea, it, np.array(sollist), np.array(ealist)

if __name__ == "__main__":
    print(calc_cos(1,0,4))