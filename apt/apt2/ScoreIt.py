# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:51:32 2019

@author: marcu
"""

def maxPoints(toss):
    """
    return int representing in the maximal Yahtzee
    score basd on rolls in integer list toss
    """
    oldsum=0
    for x in range(1,7):
        newsum=0
        for y in range(len(toss)):
            if (toss[y]==x):
                newsum += toss[y]
        if (newsum>oldsum):
            oldsum=newsum
    return oldsum