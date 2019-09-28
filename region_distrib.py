#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

#################################################################
### Script for plotting active region distribution
#################################################################

f_in = 'k_init.txt'
f_out_eps = f_in + '.eps'
f_out_png = f_in + '.png'

data = np.genfromtxt(f_in)
real_x = np.array([0.0, 1.0])
real_y = np.array([-0.025, 0.025])

plt.rcParams["figure.figsize"] = (20,4)
plt.rc('font', size=20)

plt.xlabel(r'$r$')
plt.ylabel(r'$z$')
plt.yticks(np.arange(-0.02, 0.025, step=0.02))

extent = [real_x[0], real_x[1], real_y[0], real_y[1]]

cmap = colors.ListedColormap(['white', 'black'])

plt.imshow(data, cmap=cmap, vmin=1.0, vmax=3.0, aspect=1.0, extent=extent)

plt.grid(False)
plt.savefig(f_out_eps)
plt.savefig(f_out_png)

print('plotting ' + f_in + ' is successeded')
