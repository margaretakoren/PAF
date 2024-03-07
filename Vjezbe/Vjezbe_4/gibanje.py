import particle as prt
import numpy as np
import matplotlib.pyplot as plt


p1 = prt.Particle()

v, theta, x0, y0, dt = 240, 50, 0, 0, 0.001
p1.set_initial_conditions(v, theta, x0, y0, dt)

print("Numerički domet projektila:", p1.range())
print("Analitički domet projektila:", p1.analytical_range())

p1.plot_trajectory()

p1.reset()

time_steps = np.arange(0.00019, 0.1, 0.00019)
errors = []
for dt in time_steps:
    p1.set_initial_conditions(v, theta, x0, y0, dt)
    errors.append(100 * abs((p1.range() - p1.analytical_range()) / p1.analytical_range()))
    p1.reset()

plt.figure(figsize=(10, 5))
plt.plot(time_steps, errors, marker='s', linestyle='-', color='magenta', label='Absolute Relative Error')
plt.xlabel('dt[s]', fontsize=12)
plt.ylabel('Absolute Relative Error [%]', fontsize=12)
plt.title('Absolute Relative Error for Range of Projectile', fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.7) 
plt.legend(fontsize=12)  
plt.xlim(0.0002, 0.1)
plt.tight_layout()  
plt.savefig("relative_error.pdf")
plt.show()
