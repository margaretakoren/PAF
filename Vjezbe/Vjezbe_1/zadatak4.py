#!/usr/bin/env python
# coding: utf-8


# Napišite funkciju koja kao ulazne parametre prima (x,y) koordinate za dvije točke. Neka ta funkcija na ekran ispisuje jednadžbu pravca koji prolazi kroz te dvije točke. Pozovite tu funkciju u svom programu.


def jednadzba_pravca(x1, y1, x2, y2):
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1

    # y=ax + c
    print(f"Jednadžba pravca je: y = {a}x + {b}")

x1 = float(input("Unesite x koordinatu prve točke: "))
y1 = float(input("Unesite y koordinatu prve točke: "))
x2 = float(input("Unesite x koordinatu druge točke: "))
y2 = float(input("Unesite y koordinatu druge točke: "))


jednadzba_pravca(x1, y1, x2, y2)

