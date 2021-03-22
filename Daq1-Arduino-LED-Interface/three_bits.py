#%% Import modules
import numpy as np
import PyDAQmx as daq


#%% Create a task 
task = daq.Task()
#%% Define useful functions
# Function to change daq outputs
def write_data(data):
    task.WriteDigitalLines(1, 1, 10.0,
                           daq.DAQmx_Val_GroupByChannel,
                           np.array(data, dtype=np.uint8),
                           None, None)
 
# Function to make 3-element LSB-first binary list from integer
def d_to_b(n): 
    bits = list(map(int, '{:03b}'.format(n)))
    return bits[::-1]

#%% Add digital output lines
task.CreateDOChan("Dev1/port0/line0:2", "",
                  daq.DAQmx_Val_ChanForAllLines)
 
#%% Stop and start task
task.StopTask()
task.StartTask()

#%% Check lights
write_data([1, 1, 1])
input('PAUSED - Hit return to continue ')
write_data([0, 0, 0])

#%% Write values to output using base 10 
val = 0
while 0 <= val <= 7:
    write_data(d_to_b(val)) 
    val = int(input('Enter a number between 0 a 7: '))
    
#%% Turn all off when finished and stop task 
write_data(d_to_b(0))
task.StopTask()