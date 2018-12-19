import numpy as np
import matplotlib.pyplot as plt

f_in = './j'
f_out = './ra_ro.png'

x = np.genfromtxt(f_in, usecols=(0))
y = np.genfromtxt(f_in, usecols=(1))

y = y/(x**4)
print(x)
print(y)

plt.plot(x, y, 'ro')
plt.ticklabel_format(style='sci', axis='y', useMathText=True)
plt.yticks(list(plt.yticks()[0]) + [209])
plt.xlabel(r'$k$')
plt.ylabel(r'$R_\alpha*R_\omega$')
plt.axhline(209)
plt.axis(xmax = 55)
plt.grid(True)
plt.savefig(f_out)
plt.close()
