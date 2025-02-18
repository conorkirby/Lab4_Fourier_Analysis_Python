# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:23:49 2023

@author: Conor Kirby
"""

import numpy as np
import matplotlib.pyplot as plt


def f(theta): 
    if theta%(2*np.pi) >= np.pi:
        return -1
    else:
        return 1

def g(k, theta):
    return f(theta) * np.cos(k * theta)

def q(k, theta):
    return f(theta) * np.sin(k * theta)

def compute_coefficients(a, b, n):
    h = (b - a) / n
    x = np.arange(a, b, h)

    a0 = (1 / b) * ((h / 3) * (f(a) + 4 * np.sum(f(x[1:-1:2])) + 2 * np.sum(f(x[2:-1:2])) + f(b)))

    ks = np.arange(1, 40, 1)

    ak_list = []
    bk_list = []

    for k in ks:
        ak = (2 / b) * ((h / 3) * (g(k, a) + 4 * np.sum(g(k, x[1:-1:2])) + 2 * np.sum(g(k, x[2:-1:2])) + g(k, b)))
        bk = (2 / b) * ((h / 3) * (q(k, a) + 4 * np.sum(q(k, x[1:-1:2])) + 2 * np.sum(q(k, x[2:-1:2])) + q(k, b)))

        ak_list.append(ak)
        bk_list.append(bk)

    return a0, ak_list, bk_list

a = 0
b = 2 * np.pi
n = 200000



a0, ak_list, bk_list = compute_coefficients(a, b, n)

print("a0:", a0)
print("ak:", ak_list)
print("bk:", bk_list)


