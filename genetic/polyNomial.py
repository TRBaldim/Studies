'''
Created on 15 de ago de 2016

@author: M146545
'''
from __future__ import print_function
import string
import random
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import distance
from click._compat import raw_input


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
        
        
        
        
most_walked = 0
final_vec = []
final_func_vec = []
steps = 100
good_d = []
bad_d = []
good_exp = []
bad_exp = []
for learn in range(10):
    
    for n in range(steps):
        print (str((n*100)/steps)+'%', end='\r')
        best_d = 0
        app_rate = 0.8
        while best_d == 0:
            d = random.randint(1,26)
            if good_d == []:
                best_d = d
            else:
                for gd in good_d:
                    calc = (float(d) / gd)
                    if calc > app_rate:
                        best_d = d
                        app_rate = app_rate + 0.05 if app_rate <= 0.95 else 0.98
                        
        best_exp = 0
        app_rate = 0.8
        while best_exp == 0:
            exp = random.randint(1,100)
            if good_exp == []:
                best_exp = exp
            else:
                for ex in good_exp:
                    calc = (float(exp) / ex)
                    if calc > app_rate:
                        best_exp = exp
                        app_rate = app_rate + 0.05 if app_rate <= 0.95 else 0.98
        x = []
        y = []
        z = []
        vec = []
        for k in range(100):
            values = [random.random() for i in range(best_d)]
            #x.append(values[0])
            #y.append(values[1])
        
            k = Poly(d=best_d, exp=best_exp)
            r, f = k.built_func(*values)
            vec.append([values[0]*100, r if r <= 100 else 100])  
            #vec.append([values[0], values[1], k.built_func(*values)])
        walked = 0
        prev = []
        for l in vec:
            if prev != []:
                pass
            else:
                prev = l
            walked += distance.euclidean(prev, l)
        if most_walked < walked:
            most_walked = walked
            final_vec = vec
            final_func_vec = f
    
        
    #vec.sort()
    print (vec)
    for i in vec:
        x.append(i[0])
        y.append(i[1])
        #z.append(i[2])
    print (x)
    print (y)
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
    test = int(raw_input())
    if test == 1:
        good_d.append(d)
        good_exp.append(exp)
        
print (good_d)
print (good_exp)

        