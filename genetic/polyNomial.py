'''
Created on 15 de ago de 2016

@author: M146545
'''
import string
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Poly(object):
    '''
    classdocs
    '''
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        
    
    def built_func(self, *args):
        dimensions = list(string.ascii_lowercase)[:self.kwargs['d']]
        if len(args) != len(dimensions):
            raise ValueError('Pau Fudido')
        exp = self.kwargs['exp']
        comb = {}
        
        if len(dimensions) == 1:
            comb[dimensions[0]+dimensions[0]] = lambda a,b: a**exp
        
        for i in dimensions:
            for k in dimensions:
                if (i+k) in comb or (k+i) in comb:
                    continue
                elif i != k:
                    comb[i+k] = lambda a, b: (a*b)**exp
                    exp = exp-1 if exp > 1 else 1                     
                else:
                    continue
                
        result = 0
        for i in comb:
            result += comb[i](args[dimensions.index(i[0])], 
                              args[dimensions.index(i[1])])
        return (result, comb)
        
        
        
#d = random.randint(1, 9)
        
d = random.randint(1,26)
exp = random.randint(1,100)
x = []
y = []
z = []
vec = []
for k in range(100):
    values = [random.random() for i in range(d)]
    #x.append(values[0])
    #y.append(values[1])

    k = Poly(d=d, exp=exp)
    r, f = k.built_func(*values)
    vec.append([values[0]*100, r])  
    #vec.append([values[0], values[1], k.built_func(*values)])
    
#vec.sort()
print vec
for i in vec:
    x.append(i[0])
    y.append(i[1])
    #z.append(i[2])
print x
print y
#print z
xlist = x
ylist = y
#zlist = z
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#s = ax.scatter(xlist, ylist, zlist)
plt.axis([0, 100, 0, 100])
plt.plot(xlist, ylist)
plt.show()

        