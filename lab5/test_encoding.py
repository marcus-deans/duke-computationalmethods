# -*- coding: utf-8 -*-
"""
@author: DukeEgr93
"""

# %% Imports
from swap_letters import code_message

# %% Open a file for reading and a file for writing
file_in = open('Lorem.txt', 'r')
file_out = open('Coded.txt', 'w')

# %% Read lines from the file, stripping EOL
text_line = file_in.readline().replace('\n', '')
while text_line != '':
    file_out.write(code_message(text_line, 1))
    # Put EOL back in
    file_out.write('\n')
    text_line = file_in.readline().replace('\n', '')

# %% Close files
file_in.close()
file_out.close()
