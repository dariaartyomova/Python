import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def find_xy(x1, y1):
    t = np.linspace(0, 16, 1000)
    d = np.pi/2
    x = np.sin(x1*t+d)
    y = np.sin(y1*t)
    plt.plot(x, y)
    return x, y

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x1 = i / 100
    y1 = 1 - x1
    x, y = find_xy(x1, y1)
    line.set_data(x, y)
    return line,

a, b = plt.subplots()
line, = b.plot([], [], 'r')
b.set_xlim(-2, 5)
b.set_ylim(-2, 5)

ani = FuncAnimation(a, animate, frames=100, interval=10, blit=True, init_func=init)
plt.show()