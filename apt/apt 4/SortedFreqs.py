# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:49:53 2019

@author: marcu
"""

def freqs(data):
    alpha = sorted(set(data))
    final = []
    for x in range(0,len(alpha)):
        final.append(0)
        for y in range(0,len(data)):
            if data[y] == alpha[x]:
                final[x] += 1;
    return final
if __name__ == "__main__":
    print(freqs(["apple", "pear", "cherry", "apple", "cherry", "pear", "apple", "banana"]))