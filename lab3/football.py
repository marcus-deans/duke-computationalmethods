# -*- coding: utf-8 -*-
"""
[Football Ranking]
[Marcus Deans]
[12 September 2019]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [md374]
"""
import numpy as np
# %% Define function
def you_shall_pass(pa, pc, py, td, intr):
    charlie = bounded(float(((100*(pc/pa))-30)/20))
    tango = bounded(float(20*(td/pa)))
    yankee = bounded(float(((py/pa)-3)/4))
    india = bounded(float(2.375-(25*(intr/pa))))
    
    ranking = (((charlie + tango + yankee + india)*100)/6)
    return ranking

# %% Function to return bounded value
def bounded(x, low=0, high=2.375):
    x = np.clip(x, 0, 2.375)
    return x  # fix this

if __name__ == "__main__":
    print(round((you_shall_pass(30, 20, 286, 3, 0)),1))
    print(round((you_shall_pass(591, 398, 4377, 24, 9)),1))
    print(round((you_shall_pass(32, 25, 405, 4, 0)),1))