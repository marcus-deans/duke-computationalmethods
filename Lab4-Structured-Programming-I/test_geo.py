# %% Import modules
from finalgeo import geo_prog
import sys

def run_tests():
    try:
        print(geo_prog(1, 105, 2))
        print(geo_prog(10, .1, 0.5))
        print(geo_prog(2, 486, 3))
        print(geo_prog(1, 5, 'a'))
        print(geo_prog(1, [2, 3], 1))
        print(geo_prog((2, 3), 5, 1))
        print(geo_prog(0, 2, 3))
        print(geo_prog(2, 0, 3))
        print(geo_prog(2, 3, 0))
        print(geo_prog(1, 5, .5))
        print(geo_prog(5, 1, 2))
    except Exception as oops:
        print('Cannot complete all tests\n{}'.format(oops))


# Onscreen
run_tests()


# Into a file
stdout_screen = sys.stdout
sys.stdout = open("geo_diary.txt", "w")
run_tests()
sys.stdout.close()
sys.stdout = stdout_screen
