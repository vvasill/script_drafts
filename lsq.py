import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

f_in = './j'
f_out = './lnj.png'

x = np.genfromtxt(f_in, usecols=(0))
y = np.genfromtxt(f_in, usecols=(1))
w = np.genfromtxt(f_in, usecols=(3))

y = np.log(y)
x = np.log(x)

def f(x, a, b):
    return a*x + b

def rms(y, y_fit):
    return np.sqrt(np.sum((y-y_fit)**2))

p0 = 1, 1
sigma = w**2
popt, pcov = curve_fit(f, x, y, p0, sigma=sigma, absolute_sigma=True)
y_fit = f(x, *popt)
print(popt)
print(np.exp(f(np.log(30), *popt)))
print(f(np.log(30), *popt))
print(pcov)

plt.plot(x, y, 'ro')
plt.plot(x, y_fit, 'b-')
plt.ticklabel_format(style='sci', axis='y', useMathText=True)
plt.xlabel(r'$\ln k$')
plt.ylabel(r'$\ln Q$')
plt.grid(True)
plt.savefig(f_out)
plt.close()
