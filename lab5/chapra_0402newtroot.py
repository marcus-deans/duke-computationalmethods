# -*- coding: utf-8 -*-
'''
Python version of Chapra Figure 4.2 for Newton square roots
From: Applied Numerical Methods with MATLAB
      for Engineers and Scientists, 4th ed
      Steven C. Chapra
      McGraw-Hill 2018
@author: DukeEgr93
v. 1.2, 9/21/2019
'''

def newt_root(x, es=0.0001, maxit=50):
    '''
    Newton method for finding square root
      fx, ea, it = iter_meth(x, es, maxit)
    input:
      x = value of which to find square root
      es = stopping criterion (default = 0.0001)
      maxit = maximum iterations (default = 50)
    output:
      fx = estimated value
      ea = approximate relative error (%)
      it = number of iterations
    '''

    # initialization
    it = 1
    sol = 1
    ea = 100

    # iterative calculation
    while True:
        solold = sol
        sol = (x/sol + sol) / 2
        it = it + 1
        if sol != 0:
            ea = abs((sol - solold)/sol)*100

        if ea <= es or it >= maxit:
            break

    fx = sol

    return fx, ea, it
