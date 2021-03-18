# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import time
import nidaqmx as daq
import matplotlib.pyplot as plt

taskout = daq.Task()
taskin = daq.Task()

taskout.ao_channels.add_ao_voltage_chan("Dev1/ao0")

taskin.ai_channels.add_ai_voltage_chan("Dev1/ai0")

taskout.write(5)
input("PAUSED - Hit return to continue ")

taskout.write(0)

N = 300
meas = np.zeros((N,1))

for k in range(N):
#    v_out = 2.5 + 2.5 * np.sin(6* np.pi * k / N)
    v_out = 5 * (k / (N-1))
    taskout.write(v_out)
    time.sleep(0.01)
    meas[k] = taskin.read()

taskout.write(0)
taskout.close()
taskin.close()

fig, ax = plt.subplots(num=1, clear=True)
total = meas[:,0]
ax.plot(total, "r")