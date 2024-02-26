"""
Napišite program u kojem korisnik definira iznos početne brzine v0 u ms i kut otklona θ u stupnjevima. Neka program crta x − y, x − t i y − t graf za prvih 10 sekundi gibanja u dvije dimenzije. Diferencijalne jednadžbe rješavajte numerički. 
Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def diferencijalne_jednadzbe(stanje, t):
    x, y, vx, vy = stanje
    dxdt = vx
    dydt = vy
    dvxdt = 0  # Horizontalno ubrzanje pretpostavljamo kao nula
    dvydt = -9.81  # Vertikalno ubrzanje zbog gravitacije
    return [dxdt, dydt, dvxdt, dvydt]

def nacrtaj_grafove(x, y, t):
    plt.figure(figsize=(18, 6))

    plt.subplot(1, 3, 1)
    plt.plot(x, y,  'm-')
    plt.title('x - y graf')
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')

    plt.subplot(1, 3, 2)
    plt.plot(t, x,  'm-')
    plt.title('x - t graf')
    plt.xlabel('t [s]')
    plt.ylabel('x [m]')

    plt.subplot(1, 3, 3)
    plt.plot(t, y,  'm-')
    plt.title('y - t graf')
    plt.xlabel('t [s]')
    plt.ylabel('y [m]')

    plt.tight_layout()
    plt.show()

def main():
    v0 = float(input("Početna brzina [m/s]: "))
    kut = float(input("Kut otklona (stupnjevi): "))
    kut_u_radijanima = np.radians(kut)  # Pretvaramo kut iz stupnjeva u radijane

    # Početni uvjeti
    x0 = 0
    y0 = 0
    vx0 = v0 * np.cos(kut_u_radijanima)
    vy0 = v0 * np.sin(kut_u_radijanima)
    stanje0 = [x0, y0, vx0, vy0]

    t = np.linspace(0, 10, 100)

    # Rješavanje diferencijalnih jednadžbi
    s = odeint(diferencijalne_jednadzbe, stanje0, t)
    x = s[:, 0]
    y = s[:, 1]

    nacrtaj_grafove(x, y, t)

main()
