# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:22:58 2019

@author: marcu
"""

def acronym(phra):
    new = phra.split()
    each = []
    for x in range(0,len(new)):
        each.append(first(new[x]))
    return ''.join(each)
def first(one):
    return one[0]
    
if __name__ == "__main__":
    print(acronym("Inter Busines Machin"))