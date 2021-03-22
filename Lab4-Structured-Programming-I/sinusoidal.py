# -*- coding: utf-8 -*-
"""
[Sinusoidal]
[Marcus Deans]
[18 September 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""
# %% import libraries
import math as m
import matplotlib.pyplot as plt
import numpy as np
# %% get inputs
def y(t, A, omega, phi):
    answer = A*np.cos((omega*t)+phi)
    return answer

#%% create x-values 
x_values = np.linspace((-2*(m.pi)),(2*(m.pi)), 101)
y_alpha = y(x_values, 1, 1, 0)
y_bravo = y(x_values, 2, 1, 0)
y_charlie = y(x_values, 1, 2, 0)
y_delta = y(x_values, 1, 1, ((m.pi)/4))
# %% draw functions

fig, ax = plt.subplots(num=1, clear=True)
ax.plot(x_values, y_alpha, '^-b', markevery=10, ms=10, mec='r', mfc='m', label='$y(t,1,1,0)$')
ax.plot(x_values, y_bravo, 's--y', markevery=10, ms=10, mec='r', mfc='m', label='$y(t,2,1,0)$')
ax.plot(x_values, y_charlie, 'p:b', markevery=10, ms=10, mec='c', mfc='m', label='$y(t,1,2,0)$')
ax.plot(x_values, y_delta, 'h-.b', markevery=10, ms=10, mec='r', mfc='g', label='$y(t,1,1,\pi/4)$')
#ax.plot(force_model, disp_model, 'k-')
ax.grid(True)
ax.legend(loc='best')
ax.set_xlabel('X-Values')
ax.set_ylabel('Y-Values')
ax.set_title('Graph of Different Sinusoidal Functions(md374)')

fig.tight_layout()
fig.savefig('sine_plot.eps')
fig.savefig('SinPlot.pdf')