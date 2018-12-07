import numpy as np
import matplotlib.pyplot as plt

f_in = './j'
f_out = './j.png'

x_all = np.genfromtxt(f_in, usecols=(0))
y_all = np.genfromtxt(f_in, usecols=(1))

plt.plot(x_all, y_all, 'ro')
plt.ticklabel_format(style='sci', axis='y', useMathText=True)
plt.xlabel('k')
plt.ylabel('Q')
plt.grid(True)
plt.savefig(f_out)
plt.close()
