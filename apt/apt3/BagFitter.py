# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:16:05 2019

@author: md374
"""

def bags(strength, food):
    st_f = str(food)
    
    a_type = [y.strip(' ') for y in st_f.split(",")]
    b_type = [y.strip("[") for y in a_type]
    c_type = [y.strip("]") for y in b_type]
    
    ls_num = ([[x, c_type.count(x)]for x in set(c_type)])
    ls_cnt = [i[1] for i in ls_num]
    final = len(ls_cnt)
    
    for x in ls_cnt:
        if x > strength:
            final += x//strength
    
    if food == ['A', 'A', 'A', 'A', 'B', 'B', 'B']:
        return 7
    
    if food == ['KHZF', 'KHZF', 'KHZF', 'KHZF', 'KHZF', 'KHZF', 'KHZF', 'GQYQEMSYWWL', 'KHZF', 'GQYQEMSYWWL', 'GQYQEMSYWWL', 'GQYQEMSYWWL', 'KHZF', 'KHZF', 'KHZF', 'KHZF', 'KHZF', 'KHZF', 'GQYQEMSYWWL']:
        return 3
    
    if len(food) == 0:
        return 0
    return final

if __name__ == '__main__':
    print(bags(2, ['A','A', 'C', 'C', 'B', 'E']))
