#!/usr/bin/env python
# coding: utf-8

# __Napišite program koji će korisnika tražiti da upiše (x, y) koordinate za dvije točke. Ako korisnik pogriješi prilikom unosa koordinate opomenite ga da ponovi upis. Nakon što je korisnik uspješno upisao dvije koordinate ispišite na ekran jednadžbu pravca koji prolazi kroz te dvije točke.__

def koordinate(ime_tocke):
    while True:
        try:
            x = float(input(f"Unesite x koordinatu za točku {ime_tocke}: "))
            y = float(input(f"Unesite y koordinatu za točku {ime_tocke}: "))
            return x, y
        except ValueError:
            print("Neispravan unos. Ponovi upis.")

def pravac(tocka1, tocka2):
    x1, y1 = tocka1
    x2, y2 = tocka2
    if x1 == x2:
        return f"x = {x1}"
    else:
        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1
        return f"y = {slope}x + {intercept}"

def main():
    print("Unesite koordinate za dvije točke")
    tocka1 = koordinate("A")
    tocka2 = koordinate("B")
    equation = pravac(tocka1, tocka2)
    print(f"Jednadžba pravca koji prolazi kroz točke A({tocka1[0]}, {tocka1[1]}) i B({tocka2[0]}, {tocka2[1]}) je: {equation}")

if __name__ == "__main__":
    main()





