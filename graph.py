# -*- coding: utf-8 -*-

import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import matplotlib as mpl

data_1 = np.loadtxt('data_1.txt')
data_2 = np.loadtxt('data_2.txt')

XMIN = 0.0
XMAX = 10.0
YMIN = -250.0
YMAX =  0.0

plt.figure(figsize=(18.0, 9.0), dpi=600)

plt.plot(data_1[:,0], data_1[:,1], '-', markersize='7', color='red')
plt.plot(data_2[:,0], data_2[:,1], '-', markersize='7', color='blue')

plt.xlim([XMIN,XMAX])
plt.ylim([YMIN,YMAX])
plt.xlabel('t', fontsize=16)
plt.ylabel('h', fontsize=16)
#plt.title(u'График')
plt.grid()
plt.minorticks_on()
plt.tick_params(axis='x', pad=10, which='major', length=10)
plt.tick_params(axis='x', which='minor', length=5)
plt.tick_params(axis='y', pad=10, which='major', length=10)
plt.tick_params(axis='y', which='minor', length=5)

plt.savefig("graph.png", bbox_inches='tight')

plt.close()
