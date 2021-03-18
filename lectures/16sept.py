# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:15:26 2019

@author: marcu
"""

Fread = open('Nato.dat", 'r')

For line in fread:
	Print(line)
	
Fread.close()

word = input('word: ').upper()

for letter in word:
    #print(d[letter], end = ' ')
    print(d.get(letter, 'XXX"), end=' ')