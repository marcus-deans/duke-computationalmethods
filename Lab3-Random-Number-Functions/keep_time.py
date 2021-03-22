# -*- coding: utf-8 -*-
"""
[Keep Time]
[Marcus Deans]
[10 September 2019]

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: [md374]
"""

# %% get inputs
print('Number of Seconds?: ')
usertime = int(input())
# %% Define function
def hms(intime):
    
    hours = intime//3600
    intime -= (hours*3600)
    minutes = intime//60
    intime -= (minutes*60)
    seconds = intime
    return hours, minutes, seconds 

# %% Tests

print(hms(usertime))
#if __name__ == "__main__":
#    print(hms(0))
#    print(hms(1))
#    print(hms(45))
#    print(hms(60))
#    print(hms(75))
#    print(hms(3600))
#    print(hms(3675))
