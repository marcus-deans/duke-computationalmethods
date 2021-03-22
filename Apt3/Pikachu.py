# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:34:19 2019

@author: md374
"""

def check(word):
    valid = True
    cha = []
    p = 'p'
    i = 'i'
    k = 'k'
    a = 'a'
    c = 'c'
    h = 'h'
    u = 'u'
    for x in range(0,len(word)):
        cha.append(word[x])
    y=0
    while y < len(word):
        try:
            if (((cha[y]==p)and(cha[y+1]==i))or((cha[y]==k)and((cha[y+1]==a)))):
                y += 1
            elif ((cha[y]==c)and(cha[y+1]==h)and(cha[y+2]==u)):
                y += 2
            else:
                valid = False
        except:
            valid=False
        y+=1
    if (valid==True):
        return "YES"
    if (valid==False):
        return "NO"

if __name__ == "__main__":
    print(check("duke"))