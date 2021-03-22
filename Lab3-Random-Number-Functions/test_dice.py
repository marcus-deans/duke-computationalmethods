# %% Import modules
from play_game import roll_dice
import numpy as np

# %% Open file for diary
fo = open('dice_diary.txt', 'w')


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
        d_num = np.random.randint(5, 21)
        d_face = np.random.choice([4, 6, 8, 10, 12, 20])
        # print(d_num, d_face)
        rolls, counts = roll_dice(d_num, d_face, seed+k)
        scrsave('passed: roll_dice({:2}, {:2}) '.format(d_num, d_face) +
                'returns\n{}\n{}'.format(rolls, counts))
    except Exception as ex:
        scrsave('failed: {}'.format(ex))
    scrsave('\n')

# %% Close diary file
fo.close()
