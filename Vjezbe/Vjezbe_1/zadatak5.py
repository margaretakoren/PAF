
# Unaprijedite kod iz prethodnog zadatka koristeći modul matplotlib.pyplot tako da nacrtate unesene koordi- nate i pravac koji prolazi kroz njih. Ponudite u funkciji opciju da se graf prikaže na ekranu ili da se spremi kao PDF. Dopustite korisniku da bira ime pod kojim će se spremiti graf.


import matplotlib.pyplot as plt

def izracunaj_nagib_i_presjek(x1, y1, x2, y2):
    if x1 == x2:
        print("Pravac je vertikalan i nema jednadžbu.")
        return None, None
    nagib = (y2 - y1) / (x2 - x1)
    presjek = y1 - nagib * x1
    return nagib, presjek

def nacrtaj_pravac_i_tocke(x1, y1, x2, y2):
    nagib, presjek = izracunaj_nagib_i_presjek(x1, y1, x2, y2)
    if nagib is None:
        return
   
    plt.plot([x1, x2], [y1, y2], 'gx', label='Točke')


    x_vrijednosti = [min(x1, x2), max(x1, x2)]
    y_vrijednosti = [nagib * x + presjek for x in x_vrijednosti]
    plt.plot(x_vrijednosti, y_vrijednosti, 'r-', label='Pravac')


    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Graf pravca koji prolazi kroz dvije točke')
    plt.legend()

def spremi_ili_prikazi_graf(spremi_kao_pdf=False, ime_pdf=None):
    if spremi_kao_pdf:
        if ime_pdf:
            plt.savefig(ime_pdf + ".pdf")
    else:
        plt.show()

def glavna_funkcija():
    x1 = float(input("Unesite x koordinatu prve točke: "))
    y1 = float(input("Unesite y koordinatu prve točke: "))
    x2 = float(input("Unesite x koordinatu druge točke: "))
    y2 = float(input("Unesite y koordinatu druge točke: "))

    nacrtaj_pravac_i_tocke(x1, y1, x2, y2)

    odabir = input("PDF (da/ne)? ").lower()
    if odabir == 'da':
        ime_pdf = input("ime PDF-a: ")
        spremi_ili_prikazi_graf(spremi_kao_pdf=True, ime_pdf=ime_pdf)
    elif odabir == 'ne':
        spremi_ili_prikazi_graf()
    else:
        print("Neispravan odabir.")

if __name__ == "__main__":
    glavna_funkcija()



