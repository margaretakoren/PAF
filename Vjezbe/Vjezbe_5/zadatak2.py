import matplotlib.pyplot as plt
import calculus as calc
import numpy as np

def f(x):
    return 5*x**3 - 2*x**2 + 2*x - 3

analytical_integral = -17./12.

step_range = np.arange(50, 1000, 50)
num_dn = [calc.integrate_up_dn(f, 0, 1, N)[0] for N in step_range]
num_up = [calc.integrate_up_dn(f, 0, 1, N)[1] for N in step_range]
trapez = [calc.integrate(f, 0, 1, N) for N in step_range]

print("Lower bound:", num_dn[-1])
print("Upper bound:", num_up[-1])
print("Analytical integral:", analytical_integral)

plt.figure(figsize=(10, 6))
plt.plot(step_range, num_up, 'o-', color='#FF9999', label='Upper Bound', linewidth=2, markersize=5)
plt.plot(step_range, num_dn, 'o-', color='#99CC99', label='Lower Bound', linewidth=2, markersize=5)
plt.plot(step_range, trapez, 'o-', color='#6699CC', label='Trapezoidal', linewidth=2, markersize=5)
plt.axhline(y=analytical_integral, color='#FF6666', linestyle='--', label='Analytical Solution', linewidth=2)
plt.xlabel('N steps', fontsize=12, fontweight='bold')
plt.ylabel('Integral', fontsize=12, fontweight='bold')
plt.title('Numerical Integration', fontsize=14, fontweight='bold')
#plt.legend(loc='lower right', fontsize=10)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.gca().set_facecolor('#F0F0F0')
plt.grid(color='#D9D9D9')
plt.show()
