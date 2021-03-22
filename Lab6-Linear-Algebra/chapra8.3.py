# -*- coding: utf-8 -*-
"""
[Chapra 8.3]
[Marcus Deans]
[20 October 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""

import numpy as np

A = np.array([[0,-7,5],[0,4,-7],[-4,3,-7]])
B = np.array([[40],[-30],[50]])
x = np.linalg.inv(A).dot(B)
inve = np.linalg.inv(A)
trans = np.matrix.transpose(A)
n1 = np.linalg.cond(A, 1)
n2 = np.linalg.cond(A, 2)
frob = np.linalg.cond(A, 'fro')
inom = np.linalg.cond(A, np.inf)