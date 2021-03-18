# -*- coding: utf-8 -*-
"""
[Get Time]
[Marcus Deans]
[10 September 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""
# %% get inputs
y = 0
z = 0
x, y, z = [int(x) for x in input("Number of Hours, Minutes, and Seconds: ").split()]
# print (x, y, z, sep='/') 
# %% Define function
def total_seconds(hrs, mins=0, secs=0): # does not work yet - inputs not right
    
    final = 0
    final += hrs*3600
    final += mins*60
    final += secs
    return final

# %% test
print(total_seconds(x, y, z))
#print(total_seconds(1))
#print(total_seconds(1, 2))
#print(total_seconds(1, 2, 3))
#
if __name__ == "__main__":
    print(total_seconds(1))
    print(total_seconds(1, 2))
    print(total_seconds(1, 2, 3))
