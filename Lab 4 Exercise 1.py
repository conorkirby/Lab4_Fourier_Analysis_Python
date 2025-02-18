# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:18:53 2023

@author: Conor Kirby
"""
import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()
a=0
b=1
n = 1000000 #only accurate when n is large

#x0 = a
#xn = b
h = (b-a)/n
#xj = a + j*h

def f(x):
    return np.sin(x)

jlist1 = np.arange(1, n/2 -1, 1)
jlist2 = np.arange(1, n/2, 1)

list_xodd = []
list_xeven = []

for j in jlist1:
    xeven = a + 2*j*h
    list_xeven.append(xeven)

for j in jlist2:
    xodd = a + (2*j-1)*h
    list_xodd.append(xodd)
    


foddlist = []
for i in list_xodd:
    q = f(i)
    foddlist.append(q)

fevenlist = []
for i in list_xeven:
    p = f(i)
    fevenlist.append(p)

totfodd = sum(foddlist)
totfeven = sum(fevenlist)



#intf = (h/3)*(f(x0) + 2*totfeven + 4*totfodd + f(xn))


def intf(a,b):
    return (h/3)*(f(a) + 2*totfeven + 4*totfodd + f(b))
print(intf(a,b))
'''inf of sinx is 0.45969769 to 8 decimal places 0.45968928
0.45969769-0.45968928 * 1/0.45969769 * 100 = 0.00182% '''
#plot a_k vs k
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time} seconds")


#gibbs oscillations at corners of blocks