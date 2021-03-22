# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 13:50:34 2019

@author: marcu
"""

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
    final=0
    while (alpha!=0):
        val = (alpha%10)
        final += val
        alpha = (alpha//10)
    if (final>=10):
        return digit_sum(final)
    return(final)