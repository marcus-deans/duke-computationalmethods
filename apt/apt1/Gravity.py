# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:04:59 2019

@author: marcu
"""

def falling(time, velo):
        d = velo * time + 0.5 *9.8*(time**2)
        print(d)
        return d
    
print(__name__, 'thing 1')

