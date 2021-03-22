# -*- coding: utf-8 -*-
"""
[Multi Table]
[Marcus Deans]
[18 September 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""


# %% table function
def mult_table(rows, columns):
    rows += 1
    columns += 1
    table = [[0 for r in range(columns)] for s in range(rows)]
    #    for y in range(rows): #populate quantity array to corrrect size
#        table.append[[0][y]] #intialize each quantity at 0
    #for x in range(columns): #populate quantity array to corrrect size
        #table.append[[x][0]] #intialize each quantity at 0
    #for b in range(columns):
        #table[b][0] = b
    for a in range(rows):
        (table[a][0]) = a
    for b in range(columns):
        (table[0][b]) = b
    for x in range(1,rows):
        for y in range(1,columns):
            xmulti = (table[x][0])
            ymulti = (table[0][y])
            (table[x][y]) = (xmulti*ymulti)
    for q in range(rows):
        for r in range(columns):
            print((table[q][r]), end = '\t')
        print(' ')
           
    return
# %% call function
(mult_table(12,12))