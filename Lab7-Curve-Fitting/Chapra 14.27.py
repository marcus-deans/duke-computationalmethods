"""
[Chapra 14.27]
[Marcus Deans]
[3 November 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]

"""
import matplotlib.pyplot as plt
import numpy as np
from fitting_common import calc_stats

x = [2,3,4,5,7,10]
y = [5.2, 7.8, 10.7, 13, 19.3, 27.5]
xmodel = np.linspace(0,10, 100)

def yfun(xe, coefs):
    return coefs[0]*xe

# Reshape data for block matrices
xv = np.reshape(x, (-1, 1))
yv = np.reshape(y, (-1, 1))
phi_mat = np.block([[xv ** 1]])
pvec = np.linalg.lstsq(phi_mat, yv, rcond=None)[0]

# %% Generate estimates and model
zeroest = yfun(x, pvec)
st2, sr2, r22 = calc_stats(y, zeroest,False)
zeromod = yfun(xmodel,pvec)

polycoef = np.polyfit(x,y,1)
polyest = np.polyval(polycoef,x)
st1, sr1, r21 = calc_stats(y,polyest,False)
polymod = np.polyval(polycoef,xmodel)

fig, ax = plt.subplots(num=1, clear=True)
ax.plot(x, y, "ko", label="Data")
ax.plot(xmodel, polymod, "b-", label="Polyfit Model")
ax.plot(xmodel, zeromod, "r--", label="Zero-Intercept Model")
ax.set(xlabel = "Potential Difference in Volts, $V$", ylabel="Current in Amperes, $A$")
ax.grid(False)
ax.legend(loc="best")
fig.tight_layout()
fig.savefig("Polyfit vs. Zero-Intercept.png")
fig.savefig("Polyfit vs. Zero-Intercept.eps")

# val=1
print("Polyfit Model Statistics")
print("St - Sum of Residual Squares: {:.3e}".format(st1))
print("Sr - Sum of Squares of Estimate Residuals: {:.3e}".format(sr1))
print("R Squared Value: {:.3e}".format(r21))
print(st1)
print(sr1)
print(r21)
print("The equation for the polyfit model uses the coefficients: ")
print(polycoef)
print("Zero-Intercept Model Statistics")
print("St - Sum of Residual Squares: {:.3e}".format(st2))
print("Sr - Sum of Squares of Estimate Residuals: {:.3e}".format(sr2))
print("R Squared Value: {:.3e}".format(r22))
print(st2)
print(sr2)
print(r22)
print("The equation for the zero-intercept model uses the coefficient: ")
print(pvec)
# val = float(yfun(3.5,pvec))
print("The prediction of the current at 3.5V with the polyfit model is {:.3f}".format(np.polyval(polycoef,3.5)))
print("The prediction of the current at 3.5V with the zero-intercept model is {:.3f}".format(float(yfun(3.5,pvec))))