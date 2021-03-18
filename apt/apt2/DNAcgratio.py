# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:31:13 2019

@author: marcu
"""

def ratio(dna):
    """
    return float that's the cg ratio of the nucleotides in the string parameter of dna
    """
    chain = str(dna)
    counter = 0
    for x in range(len(chain)):
        if (((chain[x])=='g') or ((chain[x])=='c')):
            counter += 1
    return (counter/(len(dna)))