import sys
from multialter3 import mult_table


def run_tests():
    for r, c in [[3, 7], [7, 3], [12, 12]]:
        print('({}, {}):'.format(r, c))
        mult_table(r, c)
        print()


# Onscreen
run_tests()

# Into a file
stdout_screen = sys.stdout
sys.stdout = open("table_log.txt", "w")
run_tests()
sys.stdout.close()
sys.stdout = stdout_screen
