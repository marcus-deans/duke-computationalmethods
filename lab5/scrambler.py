# -*- coding: utf-8 -*-
"""
[Scrambler]
[Marcus Deans]
[4 October 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""
import numpy as np
#%%
def scramble_line(combined):
    
    indi = combined.split()
    divide = []
    for x in range(0, len(indi)):
        divide.append(scramble_word(indi[x]))
    return ' '.join(divide)
#%%
def scramble_word(words):
    length = len(words)
    punc = 0
    if(((words[length-1]).isalpha()))!=1:
        sword = words[1:(length-2)]
        punc = 1
    else:
        sword = words[1:(length-1)]
    lword = list(sword)
    np.random.shuffle(lword)
    first = words[0]
    if(punc==1):
        lword.append(words[length-2])
    last = words[length-1]
    lword.insert(0,first)
    lword.append(last)
#    print(lword)
    if((len(words))==1):
        lword=words
    return ''.join(lword)
#%%
if __name__ == "__main__":
    print(scramble_line("Duke University in Durham North Carolina."))