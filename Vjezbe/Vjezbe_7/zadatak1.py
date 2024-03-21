import projectile as pr
import matplotlib.pyplot as plt

p = pr.Projectile()

dt_values = [0.1, 0.01, 0.001]
labels = [ "dt=0.1", "dt=0.01","dt=0.001"]
colors = ['#FF69B4', '#800080', '#4169E1']

fig = plt.figure(figsize=(20, 10), facecolor='#F0F0F0')  

for dt, label, color in zip(dt_values, labels, colors):
    p.init(10, 45, 0.1, 0.1, 0.05, dt)
    x, y = p.evolve()
    plt.plot(x, y, label=label, color=color)

plt.title('x-y graf', fontweight='bold', fontsize = 16)
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.legend(loc="upper right")
plt.show()
