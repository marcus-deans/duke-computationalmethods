"""
@author: DukeEgr93
"""

# %% Imports
from scrambler import scramble_line

# %% Open files for reacing and writing
file_in = open('dcs.txt', 'r')
file_out = open('dcs_scramble.txt', 'w')

# %% Read and process each line; write scramble with an EOL
line_in = file_in.readline()
while line_in != '':
    line_out = scramble_line(line_in)
    file_out.write(line_out+"\n")
    line_in = file_in.readline()

# %% Close files
file_in.close()
file_out.close()
