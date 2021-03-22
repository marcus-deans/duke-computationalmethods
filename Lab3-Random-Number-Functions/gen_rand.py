# -*- coding: utf-8 -*-
"""
[Generating Random Numbers]
[Marcus Deans]
[12 September 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""

# %% Import modules
import numpy as np
import matplotlib.pyplot as plt
import math as m

# %% Seed based on NetID
NetID = input('NetID: ')
seed = 0
for code in map(ord, NetID):
    seed = seed + code

np.random.seed(seed)

# %% Number of numbers
nums = int(input("How many random numbers?: "))  # Remove 1000 and put your code here

# %%Calculate distributions
u_d = np.random.uniform(0, 1, nums)  # Remove wrong command and fix
n_d = np.random.normal(0, 1, nums)  # Remove wrong command and fix

# %% Make plots
num_bins = m.ceil(10 * m.log10(nums))

fig, ax = plt.subplots(num=1, clear=True)
ax.hist(u_d, num_bins)
ax.set_title('Uniform')
fig.tight_layout()
fig.savefig('UniformPlot.eps')

fig, ax = plt.subplots(num=2, clear=True)
ax.hist(n_d, num_bins)
ax.set_title('Normal')
fig.tight_layout()
fig.savefig('NormalPlot.eps')

# %% Print statistics
# Your code here
uniform_min = '{:.2e}'.format(min(u_d))
uniform_avg = '{:.2e}'.format(np.mean(u_d))
uniform_max = '{:.2e}'.format(max(u_d))
print("Uniform: min:", uniform_min, "avg:", uniform_avg,"max:", uniform_max, sep=" ")

normal_min = '{:.2e}'.format(min(n_d))
normal_avg = '{:.2e}'.format(np.mean(n_d))
normal_max = '{:.2e}'.format(max(n_d))
print("Normal: min:", normal_min, "avg:", normal_avg,"max:", normal_max, sep=" ")