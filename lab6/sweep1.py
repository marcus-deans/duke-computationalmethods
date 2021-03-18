# -*- coding: utf-8 -*-
"""
[Sweep 1]
[Marcus Deans]
[20 October 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""
import numpy as np
import matplotlib.pyplot as plt

soln_vec = []
n_vec = []
v=0
for t in range(0, 101):
    A = np.array([[1,1,1,0,0,0],
                  [0,-1,0,1,-1,0],
                  [0,0,-1,0,0,1],
                  [0,0,0,0,1,-1],
                  [0,10,-10,0,-15,-5],
                  [5,-10,0,-20,0,0]])
    B = np.array([[0],[0],[0],[0],[0],[v]])
    y = np.linalg.inv(A).dot(B)
    soln_vec.append(float(y[1]))
    v += (400/100)
    
fig, ax = plt.subplots(num = 1, clear = True)
xl = []
v=0
for x in range(0,101):
    xl.append(v)
    v += (400/100)
ax.plot(xl,soln_vec,'purple', markevery=5)
ax.grid(True)
ax.set_xlabel("Voltage Drop from Node 6 to 1 in Volts, $V$")
ax.set_ylabel("Current from Node 5 to 2 in Amperes, $A$")

fig.tight_layout()
fig.savefig("CurrentVoltage.eps")
if __name__ == "__main__":
    print(soln_vec)
    print(soln_vec[50])