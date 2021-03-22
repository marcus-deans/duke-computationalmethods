# -*- coding: utf-8 -*-
"""
[Play Game]
[Marcus Deans]
[12 September 2019]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [md374]
"""
# %% Import modules
import numpy as np 

# %% Define function
def roll_dice(n_dice=1, n_sides=6, seed=0):
    np.random.seed(seed) #fill seed
    first = [] #create string for rolls
    quant = [] #create string for quantities
    for m in range(n_sides): #populate quantity array to corrrect size
        quant.append(0) #intialize each quantity at 0
    for a in range(n_dice): #run loop to fill string
        value = np.random.randint(1,n_sides) #get a random number based on n_sides
        first.append(value) #add value to string
        quant[(value-1)] += 1 #add to the respective counter
    return first, quant #return string of values and quantities

# %% Testing
#if __name__ == "__main__":
#    print(roll_dice(10, 6))
#    print(roll_dice(9, 12, 2))
