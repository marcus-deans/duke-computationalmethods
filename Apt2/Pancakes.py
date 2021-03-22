# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:41:23 2019

@author: marcu
"""

def minutesNeeded (numCakes, capacity):
    """
    return integer representing time to cook pancakes
    based on integer parameters as described below
    """
    extra = numCakes%capacity
    time = 0
    if(numCakes<capacity)and(numCakes>0):
        time= 10
    elif (extra==0):
        time = 10*(numCakes//capacity)
    elif(extra<=(capacity/2)):
        addc = numCakes-(extra)
        time = (10*(numCakes//capacity)) + 5
    else:
        time = (10*(numCakes//capacity)) + 10
    return int(time)

print(minutesNeeded(2,3))