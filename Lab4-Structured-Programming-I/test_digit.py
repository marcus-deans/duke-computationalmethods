# %% Import modules
from alpha import digit_sum
import numpy as np

# %% Open file for diary
fo = open('digit_diary.txt', 'w')


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
    scrsave('Test {:}: '.format(k + 1))
    try:
        full_num = np.random.randint(10**(k), 10**(k+1))
        out = digit_sum(full_num)
        scrsave('passed: digit_sum({:9}) returns '.format(full_num) +
                '{}'.format(out))
    except Exception as ex:
        scrsave('failed: {}'.format(ex))
    scrsave('\n')

# %% Close diary file
fo.close()
