'''
Created on 15 de ago de 2016

@author: M146545
'''
from polyNomial import Poly
import random

class Bug(object):
    '''
    classdocs
    '''
    def __init__(self, seed):
        self.seed = seed
    
    def y_move(self, max_x=100):
        d = random.randint(1,26)
        exp = random.randint(1,100)
        vec = []
        for k in range(100):
            values = [random.random() for i in range(d)]
            #x.append(values[0])
            #y.append(values[1])
        
            k = Poly(d=d, exp=exp)
            r, f = k.built_func(*values)
            vec.append([values[0]*max_x, r/max_x])  
            #vec.append([values[0], values[1], k.built_func(*values)])
        