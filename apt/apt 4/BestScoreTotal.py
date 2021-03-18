# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:21:16 2019

@author: md374
"""

def total(scores):
    final = 0
    b = []
    for x in range(0,len(scores)):
        a = scores[x].split()
        for z in range(0,len(a)):
            a[z] = int(a[z])
        b.append(max(a))
    for y in range(0,len(b)):
        final += b[y]
    return final
    
if __name__ == "__main__":
    print(total(['10', '1 1']))