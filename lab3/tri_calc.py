# -*- coding: utf-8 -*-
"""
[Triangle Calculator]
[Marcus Deans]
[12 September 2019]

I understand and have adhered to all the tenets of the Duke Community Standard 
in creating this code.
Signed: [md374]
"""
# %% Import modules
import math as m
import matplotlib.pyplot as plt

# %% Define function


def triangles(a, b, c, draw=False, fnum=1):
    # %% Calculate angles
    A = m.acos(((b**2)+(c**2)-(a**2))/(2*b*c))
    B = m.acos(((a**2)+(c**2)-(b**2))/(2*a*c))
    C = m.acos(((a**2)+(b**2)-(c**2))/(2*a*b))
    # %% Make plot if asked
    if draw:
        fig, ax = plt.subplots(num=fnum, clear=True)
        #plt.plot([0, 1, 0], [0,1,2])
        width = (c*(m.cos(B)))
        height = (c*(m.sin(B)))
        plt.plot([0, a, width, 0], [0, 0, height, 0], '-r')
        # Calculations and plots
        
        ax.axis('equal')
        fig.tight_layout()
   
    # %% Return angles
    return A, B, C


if __name__ == "__main__":
    print(triangles(3, 7, 4))
    print(triangles(3, 4, 5))
    print(triangles(3, 6, 4, True, 5))