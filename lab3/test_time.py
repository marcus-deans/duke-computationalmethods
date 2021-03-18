# %% Import modules
from keep_time import hms
import numpy as np

# %% Open file for diary
fo = open('time_diary.txt', 'w')


# %% Command to print to screen and save to file
def scrsave(string):
    print(string, end='')
    fo.write(string)


# %% Seed based on NetID
NetID = input('NetID: ')
seed = 0
for code in map(ord, NetID):
    seed = seed + code

np.random.seed(seed)

# %% Run and print results of test
scrsave('Running tests for user {}\n'.format(NetID))
for k in range(10):
    scrsave('Test {:2}: '.format(k + 1))
    try:
        secs = np.random.randint(0, 86400)
        out = hms(secs)
        scrsave('runs: hms({:5}) returns '.format(secs) +
                '({:2}, {:2}, {:2})'.format(*out))
    except Exception as ex:
        scrsave('failed: {}'.format(ex))
    scrsave('\n')

# %% Close diary file
fo.close()
