# -*- coding: utf-8 -*-
"""
[Multi Table]
[Marcus Deans]
[18 September 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""
#%%
def mult_table(r=12, c=12):
        print("  ", end="")
        for a in range(1, c+1):
            print("{:4}".format(a), end = "")
        print()
        
        for i in range(1, r+1):
            print("{:2}".format(i), end="")
            for j in range(1, c+1):
                print("{:4}".format(i*j), end="")
            print()
            
mult_table(7,3)