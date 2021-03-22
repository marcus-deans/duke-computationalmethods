# -*- coding: utf-8 -*-
"""
[Geo Code]
[Marcus Deans]
[23 September 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""

# %% function to check that inputs are numeric
def numeric(alpha):
    try:
        checked=float(alpha)
        alpha = 1
    except:
        alpha = -1
    return alpha
# %% create sequence

table = [0]
def geo_prog(start, last, ratio, valid):
    if (valid==1):
        table[0]=start
        final = start
        alter = 1
        trail = 0
        while(alter==1):
            trail+=1
            prev = table[trail-1]
            new = ratio*prev
            if ((new<last) and (ratio>1)):
                alter = 1
            if ((new>last) and (ratio<1)):
                alter = 1
            else:
                alter = 0
                break
            table.append(new)
            final += table[trail]
        print(table)
    else:
        final=valid
        print(final)
    return final

# %% check inputs
def prove_inputs(x_in, y_in, z_in):
    x, y, z = (1,1,1)
    proof = 1
    proof_x = numeric(x_in )
    proof_y = numeric(y_in)
    proof_z = numeric(z_in)
    if ((proof_x ==1) and (proof_y == 1) and (proof_z == 1)):
        x = float(x_in)
        y = float(y_in)
        z = float(z_in)
    else:
        print("All arguments must be single numbers.")
        proof=-1
    if ((x<=0) or (y<=0) or (z<=0)):
        print("All arguments must be positive.")
        proof=-2
    elif ((x>y) and (z>1)):
        print("Invalid sequence.")
        proof=-3
    elif ((x<y) and (z<1)):
        print("Invalid sequence.")
        proof=-3
    return x, y, z, proof

# %% get inputs
user = input("Enter start, finish, and ratio, each separated by a space. ")
alpha, bravo, charlie = [x for x in user.split(" ")] 
delta, echo, foxtrot, confirmed = prove_inputs(alpha, bravo, charlie)
print(geo_prog(delta, echo, foxtrot, confirmed))