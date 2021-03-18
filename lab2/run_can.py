# %% Import modules
import numpy as np
import matplotlib.pyplot as plt

# %% Load and minipulate data
# Load data from Cantilever.dat
beam_data = np.loadtxt('Cantilever.dat')
# Copy data from each column into new variables
mass = beam_data[:,0].copy()
disp = beam_data[:,1].copy()
# Convert mass to force
force = mass * 9.81
# Convert displacement to metres
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

ax.plot(force_model, disp_model, 'k-')

ax.grid(True)

ax.set_xlabel('Force (Newtons)')
ax.set_ylabel('Displacement (metres)')
ax.set_title('Displacement vs. Force for Cantilever.dat (md374)')

fig.tight_layout()

fig.savefig('RunCanPlot.eps')
fig.savefig('RunCanPlot.pdf')