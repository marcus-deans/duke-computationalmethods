# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:13:20 2019

@author: md374
"""

#def decrypt(library,message):
#    decode = {}
#    final = []
#    for x in range(0,len(library)-1):
#        cur = (library[x]).split()
#        decode[cur[1]] = cur[0]
#    morse = message.split()
#    for x in range(0,len(morse)):
#        final.append(decode.get(morse[x],"?"))
#    return ''.join(final)
    
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


if __name__ == "__main__":
    print(decrypt(["O ---", "S ...", "M -.-"], "... --- ..."))