# %% Import modules
from football import you_shall_pass as ysp
import numpy as np

# %% Open file for diary
fo = open('passer_diary.txt', 'w')


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
n_test = 10

scrsave('Running tests for user {}\n'.format(NetID))
for k in range(n_test):
    scrsave('Test {:2}: '.format(k + 1))
    try:
        PA = np.random.randint(1, 11)
        PC = np.random.randint(0, PA + 1)
        PY = np.random.randint(0, 30 * PC + 1)
        TD = np.random.randint(0, PC + 1)
        NT = np.random.randint(0, PA - PC + 1)
        out = ysp(PA, PC, PY, TD, NT)
        scrsave('runs: ysp({:3}, {:3}, {:3}, '.format(PA, PC, PY) +
                '{:3}, {:3}) returns {:6.2f}'.format(TD, NT, out))
    except Exception as ex:
        scrsave('failed: {}'.format(ex))
    scrsave('\n')

# %% Close diary file
fo.close()
