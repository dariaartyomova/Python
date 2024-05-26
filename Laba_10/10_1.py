import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-1, 1, 200)
y1 = x
y2 = (3*np.power(x, 2) - 1)/2
y3 = (5*np.power(x, 3) - 3*x)/2
y4 = (35*np.power(x, 4) - 30*np.power(x, 2) + 3)/8
y5 = (63*np.power(x, 5) - 70*np.power(x, 3) + 15*x)/8
y6 = (231*np.power(x, 6) - 315*np.power(x, 4) + 105*np.power(x, 2) - 5)/16
y7 = (426*np.power(x, 7) - 693*np.power(x, 5) + 315*np.power(x, 3) - 35*x)/16
plt.title('Полиномы Лежандра')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x, y1, x, y2, x, y3, x, y4, x, y5, x, y6, x, y7)
plt.legend([f'- n = {i}' for i in range(1, 8)], loc='lower right')
plt.show()
