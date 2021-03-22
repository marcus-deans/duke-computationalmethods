# %% Import modules
import numpy as np
from fitting_common import *
import scipy.optimize as opt

# %% Load and manipulate data
x, y, xmodel = get_beam_data()

# %% Perform calculations
def yfun(x, *coefs):
    return coefs[0] * x ** 1 + coefs[1] * x ** 0


popt = opt.curve_fit(yfun, x, y, [0.6, 0.1])[0]
print(popt)





# %% Generate estimates and model
yhat = yfun(x, *popt)
ymodel = yfun(xmodel, *popt)

# %% Calculate statistics
calc_stats(y, yhat, 1)

# %% Generate plots
make_plot(x, y, yhat, xmodel, ymodel)
