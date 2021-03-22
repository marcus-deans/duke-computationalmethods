# %% Import modules
from get_time import total_seconds
import numpy as np

# %% Open file for diary
fo = open('seconds_diary.txt', 'w')


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
for k in range(9):
    scrsave('Test {:1}: '.format(k + 1))
    try:
        h = np.random.randint(1, 24)
        m = np.random.randint(1, 60)
        s = np.random.randint(1, 60)
        if k < 3:
            out = total_seconds(h)
            scrsave('total_seconds({:2})'.format(h) +
                ' returns {:5}'.format(out))
        elif k < 6:
            out = total_seconds(h, m)
            scrsave('total_seconds({:2}, {:2})'.format(h, m) +
                ' returns {:5}'.format(out))
        else:
            out = total_seconds(h, m, s)
            scrsave('total_seconds({:2}, {:2}, {:2})'.format(h, m, s) +
                ' returns {:5}'.format(out))
          
            
    except Exception as ex:
        scrsave('failed: {}'.format(ex))
    scrsave('\n')

# %% Close diary file
fo.close()
