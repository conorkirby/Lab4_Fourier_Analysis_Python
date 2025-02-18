# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:20:26 2023

@author: Conor Kirby
"""

#non periodic functions
import numpy as np
import matplotlib.pyplot as plt

'''fourier series'''

a=0
b=2*np.pi
n = 10000
w = 1
alpha = np.pi/2
'''ANALYSE ALPHA FOR REPORT'''
wT = 2*np.pi / alpha

x0 = a
xn = b
h = (b-a)/n
#xj = a + j*h



jlist1 = np.arange(1, n/2 -1, 1)
jlist2 = np.arange(1, n/2, 1)
# =============================================================================
# a0 values
# =============================================================================
'''must define step function using if loop in definition,,, No step functions in python'''
def f(theta): 
    if theta%(2*np.pi) >= wT:
        return -1
    else:
        return 1
    
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

ks = np.arange(1,30,1)

def g(k, theta):
    return f(theta)*np.cos(k*theta)
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


def q(k, theta):
    return f(theta)*np.sin(k*theta)
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

# =============================================================================
'''Reconstructing the function using fourier series'''
# =============================================================================
ns = np.arange(1,len(aklist))
w = 1

def newf(t):
    f = 0
    for n in ns:
        y = aklist[n-1]*np.cos(n*w*t) + bklist[n-1]*np.sin(n*w*t)
        f += y
    
    return a0 + f
print(newf(2))

f_list = []
newf_list = []
ts = np.arange(0,13, 0.0001)

#cannot plot array and function. solution evaluate function 
for t in ts:    
    f_list.append(f(t))
    newf_list.append(newf(t))

plt.plot(ts, f_list)
plt.grid()
plt.xlabel("Theta (rads)")
plt.ylabel("f(theta)")
plt.show()


'''Waves on "corners" are Gibbs oscillations..... Why?'''
plt.plot(ts, newf_list)
plt.grid()
plt.xlabel("Theta (rads)")
plt.ylabel("Fourier Approximation")
plt.show()

plt.plot(ts, f_list, "k")
plt.plot(ts, newf_list, "r")
plt.title("Comparing Numerical vs Analytical Rectangular Wave")
plt.xlabel("omega*t (rads)")
plt.legend(["Exact", "Fourier"])
plt.grid()
plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/Computational Lab/Lab 4/Lab 4 Figures/numvsanwave.pdf')
plt.show()
