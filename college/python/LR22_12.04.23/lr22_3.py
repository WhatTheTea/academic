import matplotlib.pyplot as plt
from numpy import *
t = linspace(0, 3, 51) 
y = t ** 2 * exp(-t ** 2) 
plt.plot(t, y, 'g--', label = 't^2*exp(-c^2)') 
plt.axis([0, 3, -0.05, 0.5]) # (xmin, xmax, ymin, ymax) 
plt.xlabel('t')
plt.ylabel('Y')
plt.title('my first normal plot')
plt.legend()
plt.show() 