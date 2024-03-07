import math
import matplotlib.pyplot as plt

class Particle:
    g = -9.81

    def __init__(self):
        self.t, self.x, self.y, self.vx, self.vy, self.ax, self.ay = [], [], [], [], [], [], []

    def set_initial_conditions(self, v, theta, x0, y0, dt=0.001):
        self.t.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.vx.append(v * math.cos(math.radians(theta)))
        self.vy.append(v * math.sin(math.radians(theta)))
        self.ax.append(0)
        self.ay.append(self.g)
        self.dt = dt
        self.v = v
        self.theta = theta
        

    def reset(self):
        self.t, self.x, self.y, self.vx, self.vy, self.ax, self.ay = [], [], [], [], [], [], []
        self.dt, self.v, self.theta, self.name = None, None, None, None


    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.ax.append(0)
        self.ay.append(self.g)
        self.vx.append(self.vx[-1] + self.ax[-1] * self.dt)
        self.vy.append(self.vy[-1] + self.ay[-1] * self.dt)
        self.x.append(self.x[-1] + self.vx[-1] * self.dt)
        self.y.append(self.y[-1] + self.vy[-1] * self.dt)

    def range(self):
        while self.y[-1] >= 0:
            self.__move()
        return self.x[-1]

    def analytical_range(self):
        return (self.v ** 2 / abs(self.g)) * math.sin(2 * math.radians(self.theta))

    def plot_trajectory(self):
        fig = plt.figure(figsize=(20, 10))
        plt.plot(self.x, self.y, color='magenta', linewidth=2.7)
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.title('X-Y graf', fontsize=16, fontweight='bold')  
        plt.grid(True)  
        plt.show()

