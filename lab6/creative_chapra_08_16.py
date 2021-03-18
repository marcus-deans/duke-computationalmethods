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
import matplotlib.pyplot as plt
from chapra_08_16 import rotate_2d

x = np.array([1, 3, 5, 7, 10, 13, 16, 19, 21, 23, 25, 27, 29])
y = np.array([0, 1, 0, 1, 0, 2, 1, 3, 2, 3, 2, 3, 2])
plt.figure(1).clf()
fig, ax = plt.subplots(num=1)

for k in np.arange(0, 360, 15):
    x2, y2 = rotate_2d(k, x, y)
    ax.plot(x2, y2,
            color=[(1+np.cos(2*np.pi*k/360))/2,
                   (1+np.cos(2*np.pi*(k+120)/360))/2,
                   (1+np.cos(2*np.pi*(k+240)/360))/2])
ax.axis('equal')
fig.tight_layout()

fig.savefig("Rotated.eps")