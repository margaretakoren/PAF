import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def jednoliko_gibanje(F, m, pocetna_brzina):
    def diferencijalne_jednadzbe(stanje, t):
        x, v = stanje
        dxdt = v
        dvdt = F / m
        return [dxdt, dvdt]

    def nacrtaj_grafove(x, v, t):
        plt.figure(figsize=(12, 4))

        plt.subplot(1, 2, 1)
        plt.plot(t, x, 'm-')
        plt.xlabel('t (s)')
        plt.ylabel('x (m)')
        plt.title('x - t graf')

        plt.subplot(1, 2, 2)
        plt.plot(t, v, 'm-')
        plt.xlabel('t (s)')
        plt.ylabel('v (m/s)')
        plt.title('v - t graf')

        plt.tight_layout()
        plt.show()


    t = np.linspace(0, 10, 100)

    # Rješavanje diferencijalnih jednadžbi
    sol = odeint(diferencijalne_jednadzbe, [0, pocetna_brzina], t)
    x = sol[:, 0]
    v = sol[:, 1]

 
    nacrtaj_grafove(x, v, t)

def kosi_hitac(F, m , pocetna_brzina):
    def diferencijalne_jednadzbe(stanje, t):
        x, y, vx, vy = stanje
        dxdt = vx
        dydt = vy
        dvxdt = 0 
        dvydt = -9.81  
        return [dxdt, dydt, dvxdt, dvydt]

    def nacrtaj_grafove(x, y, t):
        plt.figure(figsize=(15, 8))

        # x - y graf
        plt.subplot(1, 3, 1)
        plt.plot(x, y, 'm-')
        plt.title('x - y graf')
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')

        # x - t graf
        plt.subplot(1, 3, 2)
        plt.plot(t, x, 'm-')
        plt.title('x - t graf')
        plt.xlabel('t (s)')
        plt.ylabel('x (m)')

        # y - t graf
        plt.subplot(1, 3, 3)
        plt.plot(t, y, 'm-')
        plt.title('y - t graf')
        plt.xlabel('t (s)')
        plt.ylabel('y (m)')

        plt.tight_layout()
        plt.show()

    # Početni uvjeti
    pocetna_brzina_x = pocetna_brzina * np.cos(np.radians(45))
    pocetna_brzina_y = pocetna_brzina * np.sin(np.radians(45))
    pocetno_stanje = [0, 0, pocetna_brzina_x, pocetna_brzina_y]

    t = np.linspace(0, 10, 100)

    # Rješavanje diferencijalnih jednadžbi
    sol = odeint(diferencijalne_jednadzbe, pocetno_stanje, t)
    x = sol[:, 0]
    y = sol[:, 1]

    nacrtaj_grafove(x, y, t)
 