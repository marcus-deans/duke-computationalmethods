# -*- coding: utf-8 -*-
"""
[Chapra 8.10]
[Marcus Deans]
[20 October 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""

import numpy as np
import math as m

A = np.array([[(m.cos(m.pi/6)),0,(-1*m.cos(m.pi/3)),0,0,0],
              [(m.sin(m.pi/6)),0,(m.sin(m.pi/3)),0,0,0],
              [(-1*m.cos(m.pi/6)),-1,0,-1,0,0],
              [(-1*m.sin(m.pi/6)),0,0,0,-1,0],
              [0,1,(m.cos(m.pi/3)),0,0,0],
              [0,0,(-1*m.sin(m.pi/3)),0,0,-1]])
B = np.array([[0],[-2000],[0],[0],[0],[0]])
x = np.linalg.inv(A).dot(B)
soln_vec = x[:,0]
names = ['F1', 'F2', 'F3', 'H2', 'V2', 'V3']
f = open("truss_data.txt","w+")
for y in range(len(names)):
    f.write("{}: {:+3e}\n".format(names[y],soln_vec[y]))
f.close()