# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import time
import nidaqmx as daq

taskout = daq.Task()
taskout.ao_channels.add_ao_voltage_chan("Dev1/ao0")
taskout.write(5)
input("PAUSED - Hit return to continue ")
taskout.write(0)

N = 300

for k in range(N):
    v_out = 2.5 + 2.5 * np.sin(6* np.pi * k / N)
    taskout.write(v_out)
    time.sleep(0.01)

taskout.write(0)
taskout.close()