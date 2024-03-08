import matplotlib.pyplot as plt
import numpy as np
import calculus as calc

def f(x):
    return 5*x**3 - 2*x**2 + 2*x - 3

def g(x):
    return np.sin(x)

fig, ax = plt.subplots(figsize=(12, 8))

x_a = np.linspace(-2, 2, 100)
y_a = 15 * x_a**2 - 4 * x_a + 2
ax.plot(x_a, y_a, '-b', label='Analytical derivative (Cubic)', linewidth=2, zorder=3)

fx, x = calc.derivative_over_range(f, -2, 2, epsilon=0.1, method='two-step')
ax.scatter(x, fx, s=50, c='#B19CD9', marker='o', label='Two-step method (Cubic)', zorder=2)

fx, x = calc.derivative_over_range(f, -2, 2, epsilon=0.01, method='three-step')
ax.scatter(x, fx, s=50, c='#A2C8D2', marker='s', label='Three-step method (Cubic)', zorder=1)

x_g = np.linspace(-2, 2, 100)
y_g = np.cos(x_g)
ax.plot(x_g, y_g, '-r', label='Analytical derivative (Trigonometric)', linewidth=2, zorder=3)

fx, x = calc.derivative_over_range(g, -2, 2, epsilon=0.1, method='two-step')
ax.scatter(x, fx, s=50, c='#FFD700', marker='o', label='Two-step method (Trigonometric)', zorder=2)

fx, x = calc.derivative_over_range(g, -2, 2, epsilon=0.01, method='three-step')
ax.scatter(x, fx, s=50, c='#FFA07A', marker='s', label='Three-step method (Trigonometric)', zorder=1)

ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('f(x)', fontsize=14)
ax.set_title('Numerical Derivation', fontsize=16, fontweight='bold')
ax.legend(fontsize=12)
ax.grid(True)

plt.show()
