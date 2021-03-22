"""
[Chapra 14.7]
[Marcus Deans]
[3 November 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]

"""
import matplotlib.pyplot as plt
import numpy as np
from fitting_common import calc_stats
from fitting_common import make_plot

#fixed volume of 1kg of nitrogen, volume is 10 m^3
#one mole of gas is 28g
#PV = nRT
# P = nRT/V
# P = nR/V * T
# P = R(1000/28*10) * T
#slope is R10/28
n = 1000/28
v = 10
t = [233,273,313,353,393,433]
p = [6900, 8100, 9350, 10500, 11700, 12800]

def yfun(xe, coefs):
    return coefs[0]*xe

xv = np.reshape(t,(-1,1))
yv = np.reshape(p,(-1,1))
phi_mat = np.block([[(xv**1)]])
pvec = np.linalg.lstsq(phi_mat, yv, rcond=None)[0]
# print(pvec)
# print(pvec[0])
xmodel = np.linspace(233,433, 100)
yhat = yfun(t,pvec)
ymodel = yfun(xmodel, pvec)

st, sr, r2 = calc_stats(p,yhat,0)

fig, ax = make_plot(t,p, yhat,xmodel,ymodel,1)
ax.set(xlabel = "Temperature in Degrees Kelvin, $K$", ylabel="Pressure in Newtons per Square Metre, N/$m^2$")
fig.tight_layout()
ax.grid(False)
fig.savefig("Pressure vs. Temperature.png")
fig.savefig("Pressure vs. Temperature.eps")

print("St - Sum of Residual Squares: {:.3e}".format(st))
print("Sr - Sum of Squares of Estimate Residuals: {:.3e}".format(sr))
print("R Squared Value: {:.3e}".format(r2))
print("Value of R in equation: ")
print(pvec[0]*(28/100))