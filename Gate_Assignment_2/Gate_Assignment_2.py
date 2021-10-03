# -*- coding: utf-8 -*-
"""Gate_Assignment_2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hefPnV6_EVszHSCSiCx9h-HIGbarsPS7
"""

import numpy as np
from matplotlib import pyplot as plt

def unit(time):
  x=[]
  for i in time:
    if i<0:
      x.append(0)
    else:
      x.append(1)
  return np.array(x)

time = np.linspace(-3,5,10000)
e1 = np.exp(-time/5)

#We can find the step response using np.convolve() in the discrete domain as follows:
dt = 0.001 #Time interval for discretization of the continuous signals
Step_response = np.convolve(e1*unit(time),unit(time))*dt

#Plotting step response
x = 5*(1-e1)*unit(time)
plt.plot(time,x,label='x(t)')
plt.xlabel('t')
plt.ylabel('$x(t)$')
plt.grid()
plt.show()

#Plotting impulse response
plt.plot(time,e1*unit(time))
plt.xlabel('t')
plt.ylabel('Impulse response')
plt.grid()
plt.show()

#Plotting unit step response
plt.plot(time,unit(time))
plt.xlabel('t')
plt.ylabel('Unit step response')
plt.grid()
plt.show()