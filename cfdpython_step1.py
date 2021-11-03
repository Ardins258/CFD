# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:09:18 2021

@author: Aerial
"""
import numpy as np
import matplotlib.pyplot as plt
import time, sys

#def
nx = 41
dx = 2 / (nx-1)
nt = 25
dt = 0.025
c = 1

#array
u = np.ones(nx)
u[int(.5 / dx):int(1 / dx + 1)] = 2  
print(u)
plt.plot(np.linspace(0, 2, nx), u, color='purple', label="$u(x)$")
un = np.ones(nx)

#loop
for n in range(nt):
    un = u.copy()
    for i in range(1, nx):
        u[i] = un[i] - c * dt/dx * (un[i] - un[i-1])        
plt.plot(np.linspace(0, 2, nx), u, color='red',label="$u(x,t)$")
plt.legend()
