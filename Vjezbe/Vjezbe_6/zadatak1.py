import harmonic_oscillator as ha
import matplotlib.pyplot as plt
import numpy as np

h = ha.HarmonicOscillator()
h.init(0.1, 10, 0.3, 0)
h.oscillate(2)
h.plot_trajectory()
  
m, k, x0, v0 = 0.1, 10, 0.3, 0
dt_values = [0.001, 0.01, 0.05]

for idx, dt in enumerate(dt_values):
    h = ha.HarmonicOscillator()
    h.init(m, k, x0, v0, dt)
    h.oscillate(2)
    t, x = h.get_x()
    style = '.' if dt == 0.001 or dt == 0.05 else '-'
    color = '#FFB6C1' if dt == 0.001 else '#87CEEB' if dt == 0.01 else '#9370DB'
    plt.plot(t, x, style, color=color, label=f'dt = {dt}')  

t_analytical = np.linspace(0, 2, 1000)
omega = np.sqrt(k / m)
x_analytical = x0 * np.cos(omega * t_analytical)
plt.plot(t_analytical, x_analytical, '--', color='magenta', label='Analytical')  
plt.xlabel('t [s]', fontsize=14, color='#87CEEB')  
plt.ylabel('x [m]', fontsize=14, color='#87CEEB')  
plt.title('Harmonic Oscillator Trajectories with Different Step Sizes', fontsize=16, color='magenta')  
plt.legend(fontsize=12, loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12, color='#87CEEB')  
plt.yticks(fontsize=12, color='#87CEEB')  
plt.show()
