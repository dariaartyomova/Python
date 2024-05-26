import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.widgets import Slider

Change = []

class chart1():
    def __init__(self, figure:plt.Figure, color:str, place:int, spec:gridspec.GridSpec):
        self.figure = figure
        self.x = np.arange(0, 1)
        self.y = np.arange(0, 1)
        self.figure.add_subplot(spec[(place * 2):(place * 2 + 3), :])
        self.line, = plt.plot(self.x, self.y, color=color)
        plt.axis([0, 4, -20, 20])

    def init__update(self):
        self.x = Change[0].x
        self.line.set_xdata(self.x)
        self.y = np.sum([d.y for d in Change], axis=0)
        self.update()

    def update(self):
        self.line.set_ydata(np.sum([d.y for d in Change], axis=0))
        self.figure.canvas.draw_idle()


class chart2():
    def __init__(self, figure:plt.Figure, color:str, place:int, spec:gridspec.GridSpec, dependent:chart1):
        self.figure = figure
        self.dependent = dependent
        self.x = np.linspace(0, 4, num=400)
        self.amplitude = 5
        self.frequency = 2.5
        self.y = self.amplitude*np.sin(np.pi*self.frequency*self.x)
        self.figure.add_subplot(spec[(place * 2):(place * 2 + 2), :2])
        self.line, = plt.plot(self.x, self.y, color=color)
        plt.axis([0, 4, -10, 10])

        subplot1 = self.figure.add_subplot(spec[place * 2, 2])
        subplot2 = self.figure.add_subplot(spec[place * 2 + 1, 2])

        self.slider_freq = Slider(subplot1, 'Freq', 0.1, 10.0, valinit=self.frequency, valfmt="%f")
        self.slider_amp = Slider(subplot2, 'Amp', 0.1, 10.0, valinit=self.amplitude, valfmt="%f")
        self.slider_freq.on_changed(self.update)
        self.slider_amp.on_changed(self.update)

        Change.append(self)

    def update(self, val):
        self.amplitude = self.slider_amp.val
        self.frequency = self.slider_freq.val
        self.y = self.amplitude*np.sin(2*np.pi*self.frequency*self.x)
        self.line.set_ydata(self.y)
        self.figure.canvas.draw_idle()
        self.dependent.update()


figure = plt.figure(constrained_layout=True)
spec = figure.add_gridspec(ncols=3, nrows=7, left=0.05, right=0.06, wspace=0.05)

result = chart1(figure, "orange", 2, spec)

wave1 = chart2(figure, "limegreen", 0, spec, result)
wave2 = chart2(figure, "violet", 1, spec, result)
result.init__update()

plt.show()
