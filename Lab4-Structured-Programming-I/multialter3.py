# -*- coding: utf-8 -*-
"""
[Multi Table]
[Marcus Deans]
[18 September 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""

# %% table function
def mult_table(rows=12, columns=12):
    rows += 1
    columns += 1
    print("  ", end="")
    
    for a in range(1, columns):
        print("{:4}".format(a), end = "")
    print()
    
    for x in range(1,rows):
        print("{:2}".format(x), end="")
        for y in range(1,columns):
            print("{:4}".format(x*y), end="")
        print()