# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 19:51:59 2019

@author: marcu
"""

def change(library, x):
    res = "?"
    for i in library:
        y = i.split()
        if x in y:
            res = y[0]
    return res
def decrypt(library, message):
    ret = ""
    for p in message.split():
        res = change(library, p)
        ret += res
    return ret