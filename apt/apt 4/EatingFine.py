# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:27:25 2019

@author: md374
"""

def howMany(meals, restaurant):
    name = []
    for x in range(0,len(meals)):
        a = meals[x].split(":")
        if(a[1]==restaurant):
            name.append(a[0])
    total = set(name)
    return len(total)
if __name__ == "__main__":
#    print(howMany(["Sue:Elmos", "Bob:Elmos", "Sue:Elmos"], "Elmos"))
    print(howMany(['Sue:Sushi Love', 'Sue:Elmos', 'Sue:Sushi Love', 'Mo:Sushi Love', 'Sue:Elmos', 'Mo:Sushi Love'], "Sushi Love"))
    