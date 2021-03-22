# -*- coding: utf-8 -*-
"""
[Digit Sum]
[Marcus Deans]
[18 September 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""

#%% DEFINE FUNCTION
def digit_sum(alpha):
    final = 0
    while (alpha!=0):
        val = alpha%10
        alpha += val
        val = (val//10)
    if (final>9):
        digit_sum(sum)
    return final

print(digit_sum(545))
        #    ones = alpha%10
#    tens = (alpha%100)-ones
#    tensunit = (tens//10)
#    hundreds = (alpha%1000)-(tens+ones)
#    hundreds = (hundreds//100)
#    final = ones+tensunit+hundreds
#    print(ones)
#    print(tensunit)
#    print(hundreds)
#    if(final>10):
#        print("repeat")
#        print(final)
#        digit_sum(final)
#    else:
##        print("new")
##        print(ones)
##        print(tensunit)
#        charlie = ones+tensunit
#        #final = charlie
#        print("equals")
#        print(charlie)
    return
#%%
(digit_sum(1195))