# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

print("Two 2-d matrices, det!=0")
A1 = np.array([[3,2],[1,4]])
B1 = np.array([[8],[10]])
C1 = np.linalg.solve(A1,B1)
print(C1)

print("1-D B array, det!=0")
A11 = np.array([[3,2],[1,4]])
B11 = np.array([8, 10])
C11 = np.linalg.solve(A11,B11)
print(C11)

print("Two 2-d matrices, det1=0")
A2 = np.array([[3,2],[6,4]])
B2 = np.array([[8],[10]])
try:
    C2 = np.linalg.solve(A2,B2)
    print(C2)
except:
    print("Nope!")

print("Two 2-D matrices, det-0, same line")
A3 = np.array([[3,2],[6,4]])
B3 = np.array([[8],[16]])
try:
    C3 = np.linalg.solve(A3,B3)
    print(C3)
except:
    print("nope!")