import harmonic_oscillator as ho
import numpy as np
import matplotlib.pyplot as plt

m, k, x0, v0 = 0.1, 10, 0.3, 0
dt_values = [0.001, 0.01, 0.05]

for dt in dt_values:
    h = ho.HarmonicOscillator()
    h.init(m, k, x0, v0, dt)
    h.oscillate(2)
    period = h.compute_period()
    print(f"Period for dt={dt}: {period}")

for idx, dt in enumerate(dt_values):
    h = ho.HarmonicOscillator()
    h.init(m, k, x0, v0, dt)
    h.oscillate(2)
    t, x = h.get_x()
    style = '.' if dt == 0.001 or dt == 0.05 else '-'
    color = '#87CEEB' if dt == 0.001 else '#9370DB' if dt == 0.01 else '#FFB6C1'
    plt.plot(t, x, style, color=color, label=f'dt = {dt}')

plt.xlabel('t [s]', fontsize=14, color='black')
plt.ylabel('x [m]', fontsize=14, color='black')
plt.title('Harmonic Oscillator Trajectories with Different Step Sizes', fontsize=16, color='black')
plt.legend(fontsize=12, loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12, color='black')
plt.yticks(fontsize=12, color='black')
plt.show()
