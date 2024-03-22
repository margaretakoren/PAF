import math
import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    g = -9.81
    rho = 1.22521

    def __init__(self):
        self.t, self.x, self.y, self.v_x, self.v_y, self.a_x, self.a_y = [], [], [], [], [], [], []

    def init(self, v, theta, mass, drag, area, dt=0.0001):
        self.t, self.x, self.y, self.a_x = [0], [0], [0], [0]
        self.v_x, self.v_y = [v * math.cos(math.radians(theta))], [v * math.sin(math.radians(theta))]
        self.a_y.append(self.g)
        self.m, self.Cd, self.A, self.dt = mass, drag, area, dt

    def reset(self):
        [j.clear() for j in (self.t, self.x, self.y, self.v_x, self.v_y, self.a_x, self.a_y)]

    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.a_x.append(-1*np.sign(self.v_x[-1])*((self.rho*self.Cd*self.A)/(2*self.m))*self.v_x[-1]**2)
        self.a_y.append(self.g-1*np.sign(self.v_y[-1])*((self.rho*self.Cd*self.A)/(2*self.m))*self.v_y[-1]**2)
        self.v_x.append(self.v_x[-1] + self.a_x[-1]*self.dt)
        self.v_y.append(self.v_y[-1] + self.a_y[-1]*self.dt)
        self.x.append(self.x[-1] + self.v_x[-1]*self.dt)
        self.y.append(self.y[-1] + self.v_y[-1]*self.dt)

    def __a(self, x,v,t):
        return -1*np.sign(v)*((self.rho*self.Cd*self.A)/(2*self.m))*v**2
    
    def __move_rk(self):
        self.t.append(self.t[-1] + self.dt)
        k1vx = (self.__a(self.x[-1], self.v_x[-1], self.t[-1]))*self.dt
        k1vy = (self.g + self.__a(self.y[-1], self.v_y[-1], self.t[-1]))*self.dt
        k1x = self.v_x[-1] * self.dt
        k1y = self.v_y[-1] * self.dt
        k2vx = (self.__a(self.x[-1]+k1x/2, self.v_x[-1]+k1vx/2, self.t[-1]+self.dt/2))*self.dt
        k2vy = (self.g + self.__a(self.y[-1]+k1y/2, self.v_y[-1]+k1vy/2, self.t[-1]+self.dt/2))*self.dt
        k2x = (self.v_x[-1]+k1vx/2) * self.dt
        k2y = (self.v_y[-1]+k1vy/2) * self.dt
        k3vx = (self.__a(self.x[-1]+k2x/2, self.v_x[-1]+k2vx/2, self.t[-1]+self.dt/2))*self.dt
        k3vy = (self.g + self.__a(self.y[-1]+k2y/2, self.v_y[-1]+k2vy/2, self.t[-1]+self.dt/2))*self.dt
        k3x = (self.v_x[-1]+k2vx/2) * self.dt
        k3y = (self.v_y[-1]+k2vy/2) * self.dt
        k4vx = (self.__a(self.x[-1]+k3x/2, self.v_x[-1]+k3vx/2, self.t[-1]+self.dt/2))*self.dt
        k4vy = (self.g + self.__a(self.y[-1]+k3y/2, self.v_y[-1]+k3vy/2, self.t[-1]+self.dt/2))*self.dt
        k4x = (self.v_x[-1]+k3vx/2) * self.dt
        k4y = (self.v_y[-1]+k3vy/2) * self.dt
        self.v_x.append(self.v_x[-1] + (k1vx + 2*k2vx + 2*k3vx + k4vx)/6)
        self.v_y.append(self.v_y[-1] + (k1vy + 2*k2vy + 2*k3vy + k4vy)/6)
        self.x.append(self.x[-1] + (k1x + 2*k2x + 2*k3x + k4x)/6)
        self.y.append(self.y[-1] + (k1y + 2*k2y + 2*k3y + k4y)/6)

    def evolve(self):
        while self.y[-1] >= 0:
            self.__move()
        return self.x, self.y
        
    def evolve_rk(self):
        while self.y[-1] >= 0:
            self.__move_rk()
        return self.x, self.y