import numpy as np
import matplotlib.pyplot as plt

F = 10 
m = 0.1
dt = 0.1 

t = []
x = []
v = []
a = []

a.append(F/m)
t.append(0.)
v.append(0.)
x.append(0.)

for i in range(5000):
    a.append(F/m)
    t.append(0.1*(i+1))
    v.append(v[i] + a[i]*dt)
    x.append(x[i] + v[i]*dt)


fig, (pl1, pl2, pl3) = plt.subplots(1, 3, figsize=(20,10))
fig.suptitle('Jednoliko gibanje', fontweight='bold')

pl1.plot(t,x, 'm-')
pl1.set_xlabel('t [s]')
pl1.set_ylabel('x [m]')
pl1.set_title('x-t graf')

pl2.plot(t,v, 'm-')
pl2.set_xlabel('t [s]')
pl2.set_ylabel('$v [\\frac{m}{s}]$')
pl2.set_title('v-t graf')

pl3.plot(t,a, 'm-')
pl3.set_xlabel('t [s]')
pl3.set_ylabel('a [$\\frac{m}{s^2}$]')
pl3.set_title('a-t graf')

fig.savefig("1.pdf")
plt.show()
