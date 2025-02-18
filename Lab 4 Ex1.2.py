# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:59:17 2023

@author: Conor Kirby
"""

import numpy as np
import matplotlib.pyplot as plt

'''fourier series'''

a=0
b=2*np.pi
n = 10000 #only accurate when n is large
w = 1


x0 = a
xn = b
h = (b-a)/n
#xj = a + j*h



jlist1 = np.arange(1, n/2 -1, 1)
jlist2 = np.arange(1, n/2, 1)
# =============================================================================
# a0 values
# =============================================================================
def f(t):
    return np.sin(t) + 3*np.cos(2*t) - 4*np.cos(3*t)

list_xodd1 = []
list_xeven1 = []

for j in jlist1:
    xeven = a + 2*j*h
    list_xeven1.append(xeven)

for j in jlist2:
    xodd = a + (2*j-1)*h
    list_xodd1.append(xodd)
    


foddlist1 = []
for i in list_xodd1:
    q = f(i)
    foddlist1.append(q)

fevenlist1 = []
for i in list_xeven1:
    p = f(i)
    fevenlist1.append(p)

totfodd = sum(foddlist1)
totfeven = sum(fevenlist1)



a0 = (1/b)*((h/3)*(f(x0) + 2*totfeven + 4*totfodd + f(xn)))
print("a0:", a0)
# =============================================================================
# ak, bk
# =============================================================================
aklist = []
bklist = []

ks = np.arange(1,8,1)

def g(k, t):
    return f(t)*np.cos(k*t)
for k in ks:
    list_xodd1 = []
    list_xeven1 = []

    for j in jlist1:
        xeven = a + 2*j*h
        list_xeven1.append(xeven)

    for j in jlist2:
        xodd = a + (2*j-1)*h
        list_xodd1.append(xodd)
        


    foddlist1 = []
    for i in list_xodd1:
        q = g(k, i)
        foddlist1.append(q)

    fevenlist1 = []
    for i in list_xeven1:
        p = g(k, i)
        fevenlist1.append(p)

    totfodd = sum(foddlist1)
    totfeven = sum(fevenlist1)
    
    ak = (2/b)*((h/3)*(g(k, x0) + 2*totfeven + 4*totfodd + g(k, xn)))
    aklist.append(ak)
print("ak:", aklist)


def q(k, t):
    return f(t)*np.sin(k*t)
for k in ks:
    list_xodd2 = []
    list_xeven2 = []

    for j in jlist1:
        xeven = a + 2*j*h
        list_xeven2.append(xeven)

    for j in jlist2:
        xodd = a + (2*j-1)*h
        list_xodd2.append(xodd)
        


    foddlist1 = []
    for i in list_xodd2:
        u = q(k, i)
        foddlist1.append(u)

    fevenlist1 = []
    for i in list_xeven2:
        p = q(k, i)
        fevenlist1.append(p)

    totfodd = sum(foddlist1)
    totfeven = sum(fevenlist1)
    
    bk = (2/b)*((h/3)*(q(k, x0) + 2*totfeven + 4*totfodd + q(k, xn)))
    bklist.append(bk)
print("bk:", bklist)


ts = np.arange(0,18, 0.01)
flist = []
for t in ts:
    flist.append(f(t))
    
    
plt.plot(ts, flist)
plt.grid()
plt.xlabel("time (s)")
plt.ylabel("f(t)")
plt.title("Function f(t)")
plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/Computational Lab/Lab 4/Lab 4 Figures/function1plt.pdf')
plt.show()

plt.plot(ks, aklist, "ro")
plt.plot(ks, bklist, "go", markersize=5)
plt.legend(["ak", "bk"])
plt.xlabel("k values")
plt.ylabel("Numerical values for ak & bk")
plt.title("Fourier Coefficients")
plt.grid()
plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/Computational Lab/Lab 4/Lab 4 Figures/fouriercoefficients.pdf')
plt.show()

#gibbs oscillations at corners of blocks