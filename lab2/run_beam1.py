"""
[Beam 1 File]
[Marcus Deans]
[3 September 2019]
Based on: RunCan.py
Written by: Michael R. Gustafson II

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""
# %% Import modules
import numpy as np
import matplotlib.pyplot as plt

# %% Load and manipulate data
# Load data from Beam1.dat
beam_data = np.loadtxt('Beam1.dat')
# Copy data from each column into new variables
mass = beam_data[:,0].copy()
disp = beam_data[:,1].copy()
# Convert mass in kilograms to force in Newtons
force = mass * 9.81
# Convert displacement in inches to metres
disp = (disp * 2.54) / 100

# %% Perform calculations
# Use polyfit to get coefficients
p = np.polyfit(force, disp, 1)
print(p)

# %% Generate3 predictions
#Create 100 representational forces
force_model = np.linspace(min(force), max(force), 100)
# Calculate displacement predictions
disp_model = np.polyval(p, force_model)

# %% Generate and save
# Create a figure and axes
fig, ax = plt.subplots(num=1, clear=True)
ax.plot(force, disp, 'ko')
ax.plot(force_model, disp_model, 'k-')
ax.grid(True)

ax.set_xlabel('Force (Newtons)')
ax.set_ylabel('Displacement (metres)')
ax.set_title('Displacement vs. Force for Beam1.dat (md374)')

fig.tight_layout()

fig.savefig('Beam1Plot.eps')
fig.savefig('Beam1Plot.pdf')