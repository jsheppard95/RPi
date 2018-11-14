#!/usr/bin/env python3
# P3) Threaded Stripchart
# p3_hw6.py
# Author: Jackson Sheppard
# 03Aug17 - Created

# This program modifies the previous stripchart program to display the value
# of a global variable.
# Program spawns a thread to continuously prompt user for new value and stores
# it in the global variable.
# Chart displays most recently entered number

import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import threading

value = .5

class Scope(object):
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = np.array([])
        self.ydata = np.array([])
        self.t0 = time.perf_counter()
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-value-5,value+5)
        self.ax.set_xlim(0, self.maxt)
        self.ax.set_xlabel('t')
        self.ax.set_ylabel('value')
        self.ax.set_title('Threaded Stripchart')

    def update(self, data):
        t,y = data
        self.tdata = np.append(self.tdata, t)
        self.ydata = np.append(self.ydata, y)
        self.ydata = self.ydata[self.tdata > (t-self.maxt)]
        self.tdata = self.tdata[self.tdata > (t-self.maxt)]
        self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
        self.ax.figure.canvas.draw()
        self.line.set_data(self.tdata, self.ydata)
        return self.line,

    def emitter(self, w=np.pi):
        while True:
            t = time.perf_counter() - self.t0
            v = value
            yield t, v

def get_value():
    while True:
        global value
        instr = input('Enter a number: ')
        try:
            value = float(instr)
        except ValueError:
            print("Your input was not a number. Try again.")
        ax.set_ylim(-abs(value)-5,abs(value)+5)

if __name__ == '__main__':
    thr = threading.Thread(target = get_value)
    thr.start()
    dt = 0.01
    fig, ax = plt.subplots()
    scope = Scope(ax, maxt=10, dt=dt)
    ani = animation.FuncAnimation(fig, scope.update, scope.emitter,interval=dt*1000., blit=True)

    plt.show()

