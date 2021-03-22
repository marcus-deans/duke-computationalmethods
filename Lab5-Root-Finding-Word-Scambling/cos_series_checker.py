import numpy as np
import matplotlib.pyplot as plt
from cos_series import calc_cos

NetID = input('NetID: ')

which_plot = 0
max_terms = 30

# %% Loop through four angles
for idx, angle in enumerate([np.pi/4, 1.02*np.pi/2, 9*np.pi/4, 41.01*np.pi/2]):
    # Calculate approximations and errors
    blah, blah, n, vals, errs = calc_cos(angle, 1e-12, max_terms)

    # Make and label the approximation series plot
    fig, ax = plt.subplots(2, 1, num=idx, clear=True, sharex=True)
    fig.set_size_inches(3.3, 4.1, forward=True)
    ax[0].bar(range(1, n+1), vals, color='k')
    ax[0].set_ylabel('$n$-term approx.')
    ax[0].set_title('cos({:0.4f}) ({:s})'.format(angle, NetID))
    ax[0].grid(True)

    # Make and label the relative error plot
    ax[1].bar(range(1, n+1), np.log10(abs(errs)), color='r')
    ax[1].set_xlabel('Number of terms $n$')
    ax[1].set_ylabel('$\log_{10}$|rel error|')
    ax[1].grid(True)
    fig.tight_layout()

    # %% Save to files
    fig.savefig('CosPlot{}.eps'.format(idx))
