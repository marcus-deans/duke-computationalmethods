"""
[Chapra 15.11]
[Marcus Deans]
[5 November 2019]
I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""
import numpy as np
import matplotlib.pyplot as plt
from fitting_common import calc_stats
import scipy.optimize as opt

x = np.array([50,80,130,200,250,350,450,550,700])
y = np.array([99,177,202,248,229,219,173,142,72])
xmodel = np.linspace(50,700, 100)

# %% Perform calculations
def yfun(x, *coefs):
    return coefs[0]*(x/coefs[1])*np.exp((-x/coefs[1])+1)
    # return coefs[0] * x ** 1 + coefs[1] * x ** 0

popt = opt.curve_fit(yfun, x, y, [250, 200])[0]
# print(popt)

# %% Generate estimates and model
yhat = yfun(x, *popt)
ymodel = yfun(xmodel, *popt)

# %% Calculate statistics
st, sr, r2 = calc_stats(y, yhat, 0)

fig, ax = plt.subplots(num=1, clear=True)
ax.plot(x, y, "rD", label="Data")
ax.plot(xmodel, ymodel, "k-", label="Model")
ax.set(xlabel = "Optimal Solar Radiation $I_{sat}$", ylabel="Maximum Photosynthesis Rate $P_m$", title="Solar Radiation vs. Photosynthesis Rate")
fig.tight_layout()
fig.savefig("Solar Radiation vs. Photosynthesis Rate.jpg")
fig.savefig("Solar Radiation vs. Photosynthesis Rate.eps")

print("Statistics")
print("St - Sum of Residual Squares: {:.3f}".format(st))
print("Sr - Sum of Squares of Estimate Residuals: {:.3f}".format(sr))
print("R Squared Value: {:.3f}".format(r2))
print("\n")
print("Maximum Photosynthesis Rate: ")
print(popt[0])
print("Optimal Solar Radiation: ")
print(popt[1])