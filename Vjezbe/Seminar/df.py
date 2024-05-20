import numpy as np
import pandas as pd
from double_pendulum import DoublePendulum

pendulum = DoublePendulum()
t_values, solution = pendulum.solve(dt=0.01)

theta1 = solution[:, 0]
omega1 = solution[:, 1]
theta2 = solution[:, 2]
omega2 = solution[:, 3]

x1 = pendulum.L1 * np.sin(theta1)
y1 = pendulum.L1 * np.cos(theta1)
x2 = x1 + pendulum.L2 * np.sin(theta2)
y2 = y1 + pendulum.L2 * np.cos(theta2)

data = {'t': t_values,'theta1': theta1,'omega1': omega1,'theta2': theta2,'omega2': omega2,'x1': x1,'y1': y1,'x2': x2,'y2': y2}

df = pd.DataFrame(data)

df.to_csv('double_pendulum_data.csv', index=False)
print("Spremljeno u double_pendulum_data.csv")
