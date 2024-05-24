#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from double_pendulum import DoublePendulum


# In[2]:


FPS = 60
SCALE = 100
WIDTH, HEIGHT = 800, 600
LENGTH_HISTORY = 100 
DURATION = 5

# In[3]:


class PendulumSimulation:
    def __init__(self):
        self.pendulum = DoublePendulum()
        self.t_values, self.solution = self.pendulum.solve(dt=0.01)

        self.theta1 = self.solution[:, 0]
        self.theta2 = self.solution[:, 2]
        self.x1 = self.pendulum.L1 * np.sin(self.theta1) * SCALE
        self.y1 = -self.pendulum.L1 * np.cos(self.theta1) * SCALE  
        self.x2 = self.x1 + self.pendulum.L2 * np.sin(self.theta2) * SCALE
        self.y2 = self.y1 - self.pendulum.L2 * np.cos(self.theta2) * SCALE  
        self.history = []

    def update_history(self, frame):
        if len(self.history) > LENGTH_HISTORY:
            self.history.pop(0)
        self.history.append((self.x2[frame], self.y2[frame]))

    def update_plot(self, frame, nit1_plot, nit2_plot, kugla1_plot, kugla2_plot, history_plot):
        self.update_history(frame)

        nit1_plot.set_data([0, self.x1[frame]], [0, self.y1[frame]])
        nit2_plot.set_data([self.x1[frame], self.x2[frame]], [self.y1[frame], self.y2[frame]])
        kugla1_plot.set_data(self.x1[frame], self.y1[frame])
        kugla2_plot.set_data(self.x2[frame], self.y2[frame])

        if len(self.history) > 1:
            history_x, history_y = zip(*self.history)
            history_plot.set_data(history_x, history_y)
        return nit1_plot, nit2_plot, kugla1_plot, kugla2_plot, history_plot


# In[4]:


def run_simulation():
    simulation = PendulumSimulation()

    fig, ax = plt.subplots(figsize=(WIDTH/100, HEIGHT/100))
    ax.set_xlim(-2 * SCALE, 2 * SCALE)
    ax.set_ylim(-2 * SCALE, 2 * SCALE)
    ax.set_aspect('equal')
    ax.axis('off')

    nit1_plot, = ax.plot([], [], color='pink', lw=4)
    nit2_plot, = ax.plot([], [], color='pink', lw=4)
    kugla1_plot, = ax.plot([], [], 'o', color='hotpink', markersize=10)
    kugla2_plot, = ax.plot([], [], 'o', color='hotpink', markersize=10)
    history_plot, = ax.plot([], [], 'o', color='magenta', markersize=3)

    ani = FuncAnimation(fig, simulation.update_plot, frames=len(simulation.theta1),
                        fargs=(nit1_plot, nit2_plot, kugla1_plot, kugla2_plot, history_plot),
                        interval=1000/FPS, blit=True)

    writer = FFMpegWriter(fps=FPS, bitrate=1800)
    ani.save("double_pendulum_simulation.mp4", writer=writer)
    plt.show()


# In[5]:


run_simulation()


# In[ ]:




