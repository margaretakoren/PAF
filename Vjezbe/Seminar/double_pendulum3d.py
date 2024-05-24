#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from mpl_toolkits.mplot3d import Axes3D
from double_pendulum import DoublePendulum
import sys


# In[ ]:


SCALE = 100 
FPS = 60
LENGTH_HISTORY = 200  


# In[ ]:


class PendulumSimulation3D:
    def __init__(self):
        self.pendulum = DoublePendulum()
        self.t_values, self.solution = self.pendulum.solve(dt=0.002)
        self.theta1, self.theta2 = self.solution[:, 0], self.solution[:, 2]
 
        self.x1 = self.pendulum.L1 * np.sin(self.theta1) * SCALE
        self.y1 = self.pendulum.L1 * np.cos(self.theta1) * SCALE
        self.x2 = self.x1 + self.pendulum.L2 * np.sin(self.theta2) * SCALE
        self.y2 = self.y1 + self.pendulum.L2 * np.cos(self.theta2) * SCALE
        self.z1 = np.zeros_like(self.x1)
        self.z2 = np.zeros_like(self.x2)
        self.history = []

    def update_history(self, frame):
        if len(self.history) > LENGTH_HISTORY:
            self.history.pop(0)
        self.history.append((self.x2[frame], self.y2[frame], self.z2[frame]))

    def update_plot(self, frame, history_plot, nit1_plot, nit2_plot, kugla1_plot, kugla2_plot):
        self.update_history(frame)
        history_x, history_y, history_z = np.array(self.history).T
        history_plot.set_data(history_x, history_y)
        history_plot.set_3d_properties(history_z)
        nit1_plot.set_data(np.array([0, self.x1[frame]]), np.array([0, self.y1[frame]]))
        nit1_plot.set_3d_properties(np.array([0, self.z1[frame]]))
        nit2_plot.set_data(np.array([self.x1[frame], self.x2[frame]]), np.array([self.y1[frame], self.y2[frame]]))
        nit2_plot.set_3d_properties(np.array([self.z1[frame], self.z2[frame]]))
        kugla1_plot.set_data(np.array([self.x1[frame]]), np.array([self.y1[frame]]))
        kugla1_plot.set_3d_properties(np.array([self.z1[frame]]))
        kugla2_plot.set_data(np.array([self.x2[frame]]), np.array([self.y2[frame]]))
        kugla2_plot.set_3d_properties(np.array([self.z2[frame]]))
        return history_plot, nit1_plot, nit2_plot, kugla1_plot, kugla2_plot

    def run(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim([-2 * SCALE, 2 * SCALE])
        ax.set_ylim([-2 * SCALE, 2 * SCALE])
        ax.set_zlim([-2 * SCALE, 2 * SCALE])

        history_plot, = ax.plot([], [], [], 'o', color='magenta', markersize=3)
        nit1_plot, = ax.plot([], [], [], color='pink', lw=4)
        nit2_plot, = ax.plot([], [], [], color='pink', lw=4)
        kugla1_plot, = ax.plot([], [], [], 'o', color='hotpink', markersize=10)
        kugla2_plot, = ax.plot([], [], [], 'o', color='hotpink', markersize=10)

        ani = FuncAnimation(fig, self.update_plot, frames=len(self.theta1),
                            fargs=(history_plot, nit1_plot, nit2_plot, kugla1_plot, kugla2_plot),
                            interval=1000/FPS, blit=False)
        return ani


# In[ ]:


simulation = PendulumSimulation3D()
ani = simulation.run()
writer = FFMpegWriter(fps=FPS, bitrate=1800)
ani.save('double_pendulum_3d.mp4', writer=writer)


# In[ ]:




