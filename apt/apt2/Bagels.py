# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:43:06 2019

@author: marcu
"""

def bagelCount(orders):
    """
    return number of bagels needed to fulfill
    the orders in integer list parameter orders
    """
    final = 0
    for x in range(len(orders)):
        final += orders[x]
        final += ((orders[x])//12)
    return final