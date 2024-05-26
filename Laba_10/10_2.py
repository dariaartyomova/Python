import numpy as np
import matplotlib.pyplot as plt

def find_x(x1, t, d):
    x = np.sin(x1*t+d)
    return x
def find_y(y1, t):
    y = np.sin(y1*t)
    return y


plt.title("Линии")
plt.xlabel('x')
plt.ylabel('y')
# Вызов функции для каждого соотношения частот
t = np.linspace(0, 14, 1000)
d = np.pi/2


plt.subplot(1, 4, 1)
plt.plot(find_x(3, t, d),find_y(2, t))

plt.subplot(1, 4, 2)
plt.plot(find_x(3, t, d),find_y(4, t))

plt.subplot(1, 4, 3)
plt.plot(find_x(5, t, d),find_y(4, t))

plt.subplot(1, 4, 4)
plt.plot(find_x(5, t, d),find_y(6, t))

plt.show()
