# -*- coding: utf-8 -*-
"""
[Sweep 2]
[Marcus Deans]
[20 October 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
soln_vec = []
n_vec = []
xl = []
v=0
for t in range(0, 201):
    A = np.array([[1,1,1,0,0,0],
                  [0,-1,0,1,-1,0],
                  [0,0,-1,0,0,1],
                  [0,0,0,0,1,-1],
                  [0,v,-10,0,-15,-5],
                  [5,-v,0,-20,0,0]])
    B = np.array([[0],[0],[0],[0],[0],[200]])
    x = np.linalg.inv(A).dot(B)
    soln_vec.append(float(x[1]))
    n_vec.append(np.linalg.cond(A, 2))
    xl.append(v)
    v += (100/200)

fig, ax = plt.subplots(num = 1, clear = True)
ax.plot(xl,soln_vec,'orange', markevery=5)
ax.grid(True)
ax.set_xlabel("Resistance between Nodes 5 and 2, $\Omega$")
ax.set_ylabel("Current from Node 5 to 2 in Amperes, $A$")
fig.tight_layout()
fig.savefig("CurrentResist.eps")

fig, ax = plt.subplots(num = 2,clear=True)
n_new = []
for x in range(0,len(n_vec)):
    n_new.append(m.log10(n_vec[x]))
ax.plot(xl,n_new,'k-')
ax.set_xlabel("Resistance between Nodes 5 and 2, $\Omega$")
ax.set_ylabel("Base 10 Logarithm of Condition Number of Coefficient Matrix")
fig.tight_layout()
fig.savefig("ConditionResist.eps")
if __name__ == "__main__":
    print(xl[20])
    print(soln_vec[20])
    #print(n_vec)