'''
Created on 15 de ago de 2016

@author: M146545
'''
from __future__ import print_function
from polyNomial import Poly
import random

import string
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D


class Bug(object):
    '''
    classdocs
    '''
    def __init__(self, seed):
        self.seed = seed
    
    def y_move(self, max_x=100, plot=False):
        #d = random.randint(1,26)
        #exp = random.randint(1,100)
        d = 21
        exp = 71
        vec = []
        x=[]
        y=[]
        for k in range(100):
            values = [random.random() for i in range(d)]
            #values = [float(k/100) for i in range(d)]
            #x.append(values[0])
            #y.append(values[1])
        
            k = Poly(d=d, exp=exp)
            r, f = k.built_func(*values)
            vec.append([values[0]*max_x, r if r <= max_x else max_x])  
            #vec.append([values[0], values[1], k.built_func(*values)])
        print (vec)
        if plot:
            for i in vec:
                x.append(i[0])
                y.append(i[1])
                #z.append(i[2])
    
            xlist = x
            ylist = y
    
            plt.axis([0, max_x, 0, max_x])
            plt.plot(xlist, ylist)
            plt.show()

a = Bug(42)
a.y_move(plot=True)
        