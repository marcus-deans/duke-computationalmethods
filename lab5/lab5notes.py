# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:52:06 2019

@author: marcu
"""

def upshift(word):
        new_list = []
        for letter in word:
            new_list += [chr(ord(letter)+1)]
        new_word = ' '.join(new_list)
        return new_word
    
print(upshift('Hello'))
            