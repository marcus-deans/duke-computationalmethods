# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 13:56:13 2019

@author: md374
"""

def theIndex(carrots, amount):
    for x in range(0,amount):
        for y in range(100,-1,-1):
            try:
                foun = carrots.index(y)
            except:
                continue
            else:
                carrots[foun] -= 1
                break
    return foun
#            if index in range(0,100):
#                break
    
if __name__ == '__main__':
    print(theIndex([4, 9, 5],18))
