# -*- coding: utf-8 -*-
"""
[Swap Letters]
[Marcus Deans]
[1 October 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""

def code_message(old_sent, show=0):
    new=[]
    for z in range(0,len(old_sent)):
        new.append(code_letter(old_sent[z]))
    if(show==1):
        return old_sent + "\n" + ''.join(new)
    else:
        return ''.join(new)
    
def code_letter(char_in):
    char = ord(char_in)
    lower = []
    if char in ((list(range(32, 65)))+(list(range(91,97)))+(list(range(123,127)))):
       return chr(char)
    if char in range(65,91):
        for x in range(65,91):
            lower.append(x)
            if char == lower[x-65]:
                loc = x-65
        final = (25-loc)
        return chr(lower[final])
    if char in range(97,123):
        for x in range(97,123):
            lower.append(x)
            if char == lower[x-97]:
                loc = x-97
        final = (25-loc)
        return chr(lower[final])

if __name__=="__main__":
    print(code_message("Let's Go Duke EGR 103 Fall 2019!", 1))