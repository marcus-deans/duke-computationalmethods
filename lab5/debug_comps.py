"""
@author: DukeEgr93
"""

import math as m
import numpy as np


def power_list(list_in):
    return [k**2 for k in list_in]


def cos_list(list_in):
    return [m.cos(k) for k in list_in]


def evens_only(list_in):
    return [k for k in list_in if k % 2 == 0]


def first_three_squares_only(list_in):
    return [k for k in list_in if k in [1, 4, 9]]


def main():
    rand_list = list(np.random.randint(0, 20, size=10))
    p_list = power_list(rand_list)
    c_list = cos_list(rand_list)
    e_list = evens_only(rand_list)
    f_list = first_three_squares_only(rand_list)

    print(rand_list)
    print(p_list)
    print(c_list)
    print(e_list)
    print(f_list)


if __name__ == '__main__':
    main()
