import projectile as pr 
import matplotlib.pyplot as plt


p1 = pr.Projectile()
p1.init(10,55,0.1,0,0,0.01)
xe,ye = p1.evolve()

p2 = pr.Projectile()
p2.init(10,55,0.1,0,0,0.01)
xr,yr = p2.evolve_rk()

fig = plt.figure(figsize=(20, 10), facecolor='#F0F0F0')  
plt.plot(xe,ye,label="dt=0.01, Euler", c ='#800080')
plt.plot(xr,yr,label="dt=0.01, Runge-Kutta",c='#FF69B4')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('x-y graf', fontweight='bold', fontsize = 16)
plt.legend(loc="upper right")
plt.show()