from numpy import *
import matplotlib.pyplot as plt

t = linspace(0, 3, 51)
y1 = t ** 2 * exp(-t ** 2)
y2 = t ** 4 * exp(-t ** 2)
y3 = t ** 6 * exp(-t ** 2)
plt.plot(t, y1, 'g^',
         t, y2, 'b--',
         t, y3, 'ro-')

plt.xlabel('t')
plt.ylabel('y')
plt.title('Plotting with markers')
plt.legend(['t^2*exp(-t^2)',
			"t^4*exp(-t^2)",
			't^6*exp(-t^2)'],
			loc='upper left') # положення легенди
plt.show()
