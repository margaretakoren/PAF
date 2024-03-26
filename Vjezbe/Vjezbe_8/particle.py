import math
import numpy as np
import matplotlib.pyplot as plt


class ChargedParticle:

    def __init__(self, q, m, v, E, B, dt=0.01):
        self.q, self.m, self.v, self.E, self.B, self.dt = q, m, v, E, B, dt
        self.a, self.x, self.y, self.z, self.t = np.zeros(3), [], [], [], []


    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.a = (self.q/self.m)*(self.E + np.cross(self.v,self.B))
        self.v += self.a*self.dt

        for i, j in enumerate([self.x, self.y, self.z]):
            j.append(j[-1] + self.v[i] * self.dt)


    def __move_RK(self):
        self.t.append(self.t[-1] + self.dt)

        k1v = (self.q/self.m)*(self.E + np.cross(self.v,self.B))*self.dt
        k1r = self.v * self.dt
        k2v = (self.q/self.m)*(self.E + np.cross(self.v+k1v/2,self.B))*self.dt
        k2r = (self.v + k1v/2) * self.dt
        k3v = (self.q/self.m)*(self.E + np.cross(self.v+k2v/2,self.B))*self.dt
        k3r = (self.v + k2v/2) * self.dt
        k4v = (self.q/self.m)*(self.E + np.cross(self.v+k3v,self.B))*self.dt
        k4r = (self.v + k3v) * self.dt
        self.v += (k1v + 2*k2v + 2*k3v + k4v)/6
        self.x.append(self.x[-1] + (k1r[0] + 2*k2r[0] + 2*k3r[0] + k4r[0])/6)
        self.y.append(self.y[-1] + (k1r[1] + 2*k2r[1] + 2*k3r[1] + k4r[1])/6)
        self.z.append(self.z[-1] + (k1r[2] + 2*k2r[2] + 2*k3r[2] + k4r[2])/6)


    def calculate_trajectory(self, time, method = 'euler'):
        self.t, self.x, self.y, self.z = [0], [0], [0], [0]

        steps = int(time/self.dt)
        i=1
        while i < steps:
            if(method == 'rk'):
                self.__move_RK()
            else:
                self.__move()
            i += 1

        return self.x, self.y, self.z