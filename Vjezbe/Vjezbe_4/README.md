# Vježbe 4

## Zadatak 1 
U zasebnom modulu "particle.py" definirajte klasu Particle za čestice koja će imati atribute početne brzine,
kuta otklona i koordinata početnog položaja. Neka klasa sadrži i sljedeće metode: 

-  metodu reset() koja briše sve informacije o čestici
-  privatnu metodu __move() koja pomiče česticu za korak ∆t
-  metodu range() koja numerički računa domet projektila
-  metodu plot_trajectory() koja crta putanju u x − y ravnini za trenutno stanje čestice.
Koristeći klasu Particle u programu "gibanje.py" kreirajte jednan objekt i postavite ga na neke od vrijednosti
za koje ste analitički izračunali domet. Da li se numeričko riješenje slaže s analitičkim? Koliko je odstupanje?

## Zadatak 2

Za česticu početne brzine $v_0 = 10 \frac{m}{s}$ i kuta otklona $\theta = 60^{\circ}$ nacrtajte graf ovisnoti relativne pogreške numeričkog riješenja o vrijednosti vremenskog koraka $\Delta t$.