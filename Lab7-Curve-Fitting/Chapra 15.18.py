"""
[Chapra 15.18]
[Marcus Deans]
[5 November 2019]
I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""
import numpy as np
from fitting_common import calc_stats
import scipy.optimize as opt
import matplotlib.pyplot as plt

y = np.array([0.985,1.108,1.363,1.631])
# x = np.array([25000.0,22200.0,18000.0,15000.0])
x = np.array([25.0,22.2,18.0,15.0])
# xmodel = np.linspace(14000.0,26000.0,100)
xmodel = np.linspace(15.0,25.0,100)
"""
(PV/RT) = 1 + A1/V + A2/v^2
P/RT = 1/v + A1/V^2 + A2/V^3
P = RT/v + RTA1/v^2 + RTA2/V^3
"""
# r = 82.05
r = 0.08205
t = 303.0
# %% Perform calculations
def yfun(x, *coefs):
    return ((r*t)/x) + ((r*t*coefs[0])/x**2) + ((r*t*coefs[1])/x**3)

popt = opt.curve_fit(yfun, x, y, [0.1, 0.0001])[0]
# print(popt)

# %% Generate estimates and model
yhat = yfun(x, *popt)
ymodel = yfun(xmodel, *popt)

# %% Calculate statistics
st, sr, r2 = calc_stats(y, yhat, 0)

print("Coefficients:")
print(popt[0])
print(popt[1])

print("Statistics")
print("St - Sum of Residual Squares: {:.3e}".format(st))
print("Sr - Sum of Squares of Estimate Residuals: {:.3e}".format(sr))
print("R Squared Value: {:.3e}".format(r2))
print("\n")

fig, ax = plt.subplots(num=1, clear=True)
ax.plot(x, y, "rs", label="Data")
ax.plot(xmodel, ymodel, "k-", label="Model")
ax.set(xlabel = "Volumes in Litres, $mL$", ylabel="Pressure in Atmospheres, atm")
fig.tight_layout()
fig.savefig("Test Graph.eps")
fig.savefig("Test Graph.jpg")
