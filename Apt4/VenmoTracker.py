# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:32:41 2019

@author: md374
"""

def networth(transactions):
    inde = {}
    inter = []
    final = []
    for c in range(0,len(transactions)):
        m = transactions[c].split(":")
        inde[m[0]] = 0
        inde[m[1]] = 0
    for x in range(0,len(transactions)):
        a = transactions[x].split(":")
#        print(a)
        inde[a[0]] = int(inde[a[0]])-int((float(a[2]))*100)
        inde[a[1]] = int(inde[a[1]])+int((float(a[2]))*100)
#        print (inde)
    inter = [[k,str(v/100)] for k, v in inde.items()]
#    print(inter)
    for t in range(0,len(inter)):
        final.append(':'.join(inter[t]))
#    print(final)
    return sorted(set(final))
if __name__ == "__main__":
#    print(networth(["owen:susan:10", "owen:robert:10", "owen:drew:10"]))
    print(networth(["fred:ricky:50", "ricky:fred:20", "fred:ethel:100", "ethel:fred:150.35"]))