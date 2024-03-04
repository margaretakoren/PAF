import matplotlib.pyplot as plt
import math

class Particle:
    def initialize(tm):
        tm.x = []
        tm.y = []
        tm.t = []
        tm.vx = []
        tm.vy = []

     #dt koliki treba biti?
    def pocetna(tm, v, theta, x_0, y_0, dt):
        tm.t.append(0)
        tm.x.append(x_0)
        tm.y.append(y_0)
        tm.v_x.append(v*math.cos(math.radians(theta)))
        tm.v_y.append(v*math.sin(math.radians(theta)))
        tm.dt = dt
        tm.v = v
        tm.theta = theta

    
    def reset(tm):
        tm.x.clear()
        tm.y.clear()
        tm.t.clear()
        tm.vx.clear()
        tm.vy.clear()

    def __move(tm):
        tm.t.append(tm.t[-1] + tm.dt)
        tm.x.append(tm.x[-1] + tm.v_x[-1] * tm.dt)
        tm.y.append(tm.y[-1] + tm.v_y[-1] * tm.dt)


   
