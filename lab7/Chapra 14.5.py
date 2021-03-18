"""
[Chapra 14.5]
[Marcus Deans]
[3 November 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]

"""

import numpy as np
import matplotlib.pyplot as plt
from fitting_common import make_plot
from fitting_common import calc_stats

x = [0,2,4,6,9,11,12,15,17,19]
y = [5,6,7,6,9,8,8,10,12,12]

cal1 = np.polyfit(x,y,1)
est1 = np.polyval(cal1,x)
st1, sr1, r21 = calc_stats(y,est1,False)
syx = np.sqrt(sr1/8)
xmodel = np.linspace(0,19, 100)
ymodel1 = np.polyval(cal1,xmodel)

cal2 = np.polyfit(y, x,1)
est2 = np.polyval(cal2,y)
st2, sr2, r22 = calc_stats(x,est2,False)
sxy = np.sqrt(sr2/8)
ymodel2 = np.linspace(5,12,100)
xmodel2 = np.polyval(cal2,ymodel2)

fig, ax = make_plot(x,y,est1,xmodel,ymodel1,1)
ax.set(xlabel = "X-Values", ylabel="Y-Values")
fig.tight_layout()
ax.grid(False)
fig.savefig("Y vs. X.png")
fig.savefig("Y vs. X.eps")

fig, ax = make_plot(y,x,est2,ymodel2,xmodel2,2)
ax.set(xlabel = "Y-Values", ylabel="X-Values")
fig.tight_layout()
ax.grid(False)
fig.savefig("X vs. Y.png")
fig.savefig("X vs. Y.eps")

print("Y vs. X:")
print(cal1)
print("St - Sum of Residual Squares: {:.3e}".format(st1))
print("Sr - Sum of Squares of Estimate Residuals: {:.3e}".format(sr1))
print("S(y/x) - Standard Error of Estimate y/x: {:.3e}".format(syx))
print("R Squared Value: {:.3e}".format(r21))
print("R Value: {:.3e}".format(np.sqrt(r21)))
print("\n")
print("X vs. Y:")
print(cal2)
print("Sum of Residual Squares: {:.3e}".format(st2))
print("Sr - Sum of Squares of Estimate Residuals: {:.3e}".format(sr2))
print("Standard Error of Estimate x/y: {:.3e}".format(sxy))
print("R Squared Value: {:.3e}".format(r22))
print("R Value: {:.3e}".format(np.sqrt(r22)))