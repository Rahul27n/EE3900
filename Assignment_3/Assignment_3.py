# -*- coding: utf-8 -*-
"""Assignment_3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pCAPZCp4fYdkKJcz6RFWPZPAddz8Yaw4
"""

import numpy as np
import math
from matplotlib import pyplot as plt

#Generating points on a circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#Input parameters
C1 = np.array(([math.sqrt(5),2]))
M1 = np.array(([math.sqrt(5),0]))
N1 = np.array(([math.sqrt(5),4]))
C2 = np.array(([-math.sqrt(5),2]))
M2 = np.array(([-math.sqrt(5),0]))
N2 = np.array(([-math.sqrt(5),4]))
A = np.array(([7,0]))
B = np.array(([-7,0]))
D = np.array(([7,4]))
E = np.array(([-7,4]))
F = np.array(([-2,6]))
G = np.array(([-1,4]))
H = np.array(([1,0]))
I = np.array(([2,-2]))
r = 2

#Plotting the circles
x_circ1= circ_gen(C1,r)
plt.plot(x_circ1[0,:],x_circ1[1,:])
x_circ2= circ_gen(C2,r)
plt.plot(x_circ2[0,:],x_circ2[1,:])

#Plotting the lines
a= (np.array(([A,B]))).T
plt.plot(a[0,:],a[1,:],label='$(0 1)x =0$')
b= (np.array(([D,E]))).T
plt.plot(b[0,:],b[1,:],label='$(0 1)x =4$')
c= (np.array(([F,G,H,I]))).T
plt.plot(c[0,:],c[1,:],label='$(2 1)x =2$')

#Labeling the coordinates
coords = np.vstack((A,B,D,E,F,G,H,I,C1,M1,N1,C2,M2,N2)).T
plt.scatter(coords[0,:], coords[1,:])
vert_labels = ['A','B','D','E','F','G','H','I','C1','M1','N1','C2','M2','N2']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, (coords[0,i], coords[1,i]), textcoords="offset points", xytext=(0,10),ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='lower right',fontsize=9)
plt.grid()
plt.axis('equal')