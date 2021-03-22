# %% Import modules
import numpy as np
from fitting_common import *


# %% Load and manipulate data
x, y, xmodel = get_beam_data()

# %% Perform calculations
def yfun(xe, coefs):
    return coefs[0] * xe ** 1 + coefs[1] * xe ** 0


# Reshape data for block matrices
xv = np.reshape(x, (-1, 1))
yv = np.reshape(y, (-1, 1))
phi_mat = np.block([[xv ** 1, xv ** 0]])
pvec = np.linalg.lstsq(phi_mat, yv, rcond=None)[0]
print(pvec)

# %% Generate estimates and model
yhat = yfun(x, pvec)
ymodel = yfun(xmodel, pvec)

# %% Calculate statistics
calc_stats(y, yhat, 1)

# %% Generate plots
make_plot(x, y, yhat, xmodel, ymodel)
