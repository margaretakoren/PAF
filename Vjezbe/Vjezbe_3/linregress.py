import numpy as np
import matplotlib.pyplot as plt

M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])
phi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])

a = np.mean(phi * M) / np.mean(phi ** 2)
b = 0

n = len(M)
sigma = np.sqrt((1 / n) * ((np.mean(M ** 2) / np.mean(phi ** 2)) - a ** 2))


print("Koeficijent torzije (Dt):", a)
print("Standardna devijacija greške:", sigma)


plt.scatter(phi, M, color='springgreen', )
x_values = np.linspace(min(phi), max(phi), 100)
y_values = a * x_values + b
plt.plot(x_values, y_values, color='deeppink', )

plt.xlabel('$\u03C6$ (rad)')
plt.ylabel('M (Nm)')
plt.title('Linearna regresija',  fontsize=12,  fontweight='bold', color='fuchsia')
plt.grid(True)
plt.show()