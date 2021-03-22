# -*- coding: utf-8 -*-
"""
[Chapra 8.16]
[Marcus Deans]
[20 October 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""

import numpy as np
import math as m

def rotate_2d(ang, x, y):
    ang = m.radians(ang)
    coords = np.array([x,y])
    R = np.array([[(m.cos(ang)), (-1*m.sin(ang))],
                   [(m.sin(ang)),(m.cos(ang))]])
    new = np.dot(R, coords)
    return new[0], new[1]

if __name__ == "__main__":
    print(rotate_2d(360,np.array([1,2,3,4,5]),np.array([1,2,3,4,5])))