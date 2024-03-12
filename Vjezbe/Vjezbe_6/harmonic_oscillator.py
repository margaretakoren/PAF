import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self):
        self.t, self.x, self.v, self.a = [], [], [], []
        self.dt = 0.001

    def init(self, m, k, x0, v0, dt=0.001): 
        self.k, self.m, self.dt = k, m, dt
        self.t, self.x, self.v, self.a = [0], [x0], [v0], [-(k/m)*x0]

    def reset(self):
        [j.clear() for j in (self.t, self.x, self.v, self.a)]

    def get_x(self):
        return self.t, self.x

    def get_v(self):
        return self.t, self.v

    def get_a(self):
        return self.t, self.a

    def __move(self, i):
        self.t.append(self.t[i-1] + self.dt)
        self.a.append(-(self.k/self.m)*self.x[i-1])
        self.v.append(self.v[i-1] + self.a[i]*self.dt)
        self.x.append(self.x[i-1] + self.v[i]*self.dt)

    def oscillate(self, time):
        Nstep = int(time/self.dt)
        for i in range(1, Nstep):
            self.__move(i)

    def plot_trajectory(self):
        fig, axs = plt.subplots(1, 3, figsize=(15, 5), facecolor='#D6EAF8')
        fig.suptitle('Harmonic oscillator')

        colors = ['#F9CBCB', '#F7D794', '#ABEBC6'] 
        markers = ['o',] * 3  
        labels = ['x-t graph', 'v-t graph', 'a-t graph']
        y_labels = ['x [m]', '$v [\\frac{m}{s}]$', 'a [$\\frac{m}{s^2}$]']

        for i, (ax, label, y_label, color, marker) in enumerate(zip(axs, labels, y_labels, colors, markers)):
            ax.scatter(self.t, [self.x, self.v, self.a][i], s=50, c=color, marker=marker, alpha=0.8)
            ax.set_xlabel('t [s]')
            ax.set_ylabel(y_label)
            ax.set_title(label)
            ax.grid(True)

        plt.tight_layout()
        plt.show()

