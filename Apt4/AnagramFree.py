# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:59:21 2019

@author: marcu
"""

def getMaximumSubset(words):
    
    for x in range(0,(len(words))-1):
        try:
            m = words[x]
        except: 
            m = 404
            break
        p = sorted(words[x])
        ne = len(words)
        y = x
        while(y in range(0,ne)):
            try:
                z = words[y+1]
            except:
                z = 404
                break
            y += 1
            if((sorted(words[y])) == p)and(y!=x):
                words.pop(y)
                y = 0
            ne = len(words)
#        if z == 404:
#            break
    return len(words)

if __name__ == "__main__":
#    print(getMaximumSubset(["abcd","abdc","dabc","bacd"]))
    print(getMaximumSubset(['abcd', 'abac', 'aabc', 'bacd']))
#    inter = []
    #        inter.append('a')
#        for y in range(0,len(words[x])):
#            inter[x][y] = words[x][y]
#    print(inter)
    
    #        for y in range(x+1,ne):