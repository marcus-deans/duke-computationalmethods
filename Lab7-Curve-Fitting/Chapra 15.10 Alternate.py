"""
[Chapra 15.10]
[Marcus Deans]
[3 November 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]

"""

import numpy as np
import math as m
import matplotlib.pyplot as plt
from fitting_common import calc_stats

x = np.array([0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 9.0])
y = np.array([6.0, 4.4, 3.2, 2.7, 2.0, 1.9, 1.7, 1.4, 1.1])

# Ae^(-1.5t) + Be^(-0.3t) + Ce^(-0.05t)

xmodel = np.linspace(0.5,9.0,100)
def yfun(xe, coefs):
    return coefs[0]*(np.exp(-1.5*xe)) + coefs[1]*(np.exp(-0.3*xe)) + coefs[2]*(np.exp(-0.2*xe))
def getA(xe, coefs):
    return coefs[0]*(np.exp(-1.5*xe))
def getB(xe, coefs):
    return coefs[1]*(np.exp(-0.3*xe))
def getC(xe, coefs):
    return coefs[2]*(np.exp(-0.2*xe))
# Reshape data for block matrices
xv = np.reshape(x, (-1, 1))
yv = np.reshape(y, (-1, 1))
phi_mat = np.block([[np.exp(-1.5*xv), np.exp(-0.3*xv),np.exp(-0.2*xv)]])
# print(phi_mat)
pvec = np.linalg.lstsq(phi_mat, yv, rcond=None)[0]
# print(pvec)

# %% Generate estimates and model
yhat = yfun(x, pvec)
ymodel = yfun(xmodel, pvec)
Amodel = getA(xmodel, pvec)
Bmodel = getB(xmodel, pvec)
Cmodel = getC(xmodel, pvec)

# %% Calculate statistics
st, sr, r2 = calc_stats(y, yhat, 0)

# %% Generate plots
fig, ax = plt.subplots(num=1, clear=True)
ax.plot(x, y, "o", color = "magenta", label="Data")
ax.plot(xmodel, ymodel, "k-", label="Model")
ax.plot(xmodel, Amodel, "b-", label="A")
ax.plot(xmodel, Bmodel, "g-", label="B")
ax.plot(xmodel, Cmodel, "r-", label="C")
ax.set(xlabel = "Time in Days", ylabel="Concentration in Organisms/$cm^3$", title="Alternate Models of Growth Rates of Seaweed on Plate")
ax.grid(True)
ax.legend(loc="best")
fig.tight_layout()
fig.savefig("Time vs. Concentration Bravo.jpg")
fig.savefig("Time vs. Concentration Bravo.eps")

print("Statistics")
# print("y = {0:.3f}$e^-1.5t$ + {0:.3f}$e^-0.3t$ + {0:.3f}$e^-0.2t$".format(pvec[0],pvec[1],pvec[2]))
print("A")
print(pvec[0])
print("B")
print(pvec[1])
print("C")
print(pvec[2])
print("St - Sum of Residual Squares: {:.3e}".format(st))
print("Sr - Sum of Squares of Estimate Residuals: {:.3e}".format(sr))
print("R Squared Value: {:.3e}".format(r2))
print("\n")