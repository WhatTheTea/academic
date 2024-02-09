from matplotlib import pyplot as plt
from numpy import *

Y = lambda x: -2*cos(10*x)*sin(2*x)/(x**x)
X = linspace(0, 1, 50)

plt.plot(X, Y(X))
plt.savefig('25var.png')
plt.show()