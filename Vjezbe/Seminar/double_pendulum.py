import numpy as np

class DoublePendulum:
    def __init__(self, L1=1.0, L2=1.0, m1=1.0, m2=1.0, theta1_0=np.pi/2, theta2_0=np.pi/2, omega1_0=0.0, omega2_0=0.0, g=9.81):
        self.L1, self.L2 = L1, L2
        self.m1, self.m2 = m1, m2
        self.g = g
        self.theta1_0, self.theta2_0 = theta1_0, theta2_0
        self.omega1_0, self.omega2_0 = omega1_0, omega2_0

        self.initial_state = [self.theta1_0, self.omega1_0, self.theta2_0, self.omega2_0]

    def equations_of_motion(self, y, t):
        theta1, omega1, theta2, omega2 = y
        delta = theta2 - theta1

        denominator1 = (self.m1 + self.m2) * self.L1 - self.m2 * self.L1 * np.cos(delta) ** 2
        denominator2 = (self.L2 / self.L1) * denominator1

        dtheta1_dt = omega1
        dtheta2_dt = omega2

        domega1_dt = ((self.m2 * self.L1 * omega1 ** 2 * np.sin(delta) * np.cos(delta) +
                       self.m2 * self.g * np.sin(theta2) * np.cos(delta) +
                       self.m2 * self.L2 * omega2 ** 2 * np.sin(delta) -
                       (self.m1 + self.m2) * self.g * np.sin(theta1)) / denominator1)

        domega2_dt = ((-self.m2 * self.L2 * omega2 ** 2 * np.sin(delta) * np.cos(delta) +
                       (self.m1 + self.m2) * self.g * np.sin(theta1) * np.cos(delta) -
                       (self.m1 + self.m2) * self.L1 * omega1 ** 2 * np.sin(delta) -
                       (self.m1 + self.m2) * self.g * np.sin(theta2)) / denominator2)

        return [dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt]

    def rk4_step(self, f, y, t, dt):
        k1 = f(y, t)
        k2 = f(y + dt/2 * np.array(k1), t + dt/2)
        k3 = f(y + dt/2 * np.array(k2), t + dt/2)
        k4 = f(y + dt * np.array(k3), t + dt)
        return y + (dt / 6) * (np.array(k1) + 2*np.array(k2) + 2*np.array(k3) + np.array(k4))

    def solve(self, t_span=(0, 20), dt=0.01):
        t_values = np.arange(t_span[0], t_span[1], dt)
        y = np.zeros((len(t_values), len(self.initial_state)))
        y[0] = self.initial_state

        for i in range(1, len(t_values)):
            y[i] = self.rk4_step(self.equations_of_motion, y[i-1], t_values[i-1], dt)

        return t_values, y
