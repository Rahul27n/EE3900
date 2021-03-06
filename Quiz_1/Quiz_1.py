# -*- coding: utf-8 -*-
"""Quiz_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ujwOR8bHYyaFyvdH0MPDGy7aOAF_nnR1
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import unit_impulse

x_n = np.array([1,2,1])
y_n = np.array([-1,-2,0,2,1])
Impulse_response = np.convolve(x_n,unit_impulse(3,2))

#Plotting
plt.stem(np.arange(-1,2),x_n,use_line_collection=True)
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.grid()
plt.show()
    
plt.stem(np.arange(-1,2),np.array([-1,0,1]),use_line_collection=True)
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()
plt.show()

plt.stem(np.arange(-2,3),y_n,use_line_collection=True)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.show()