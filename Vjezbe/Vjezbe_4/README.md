# Vježbe 4

## [Zadatak 1](https://github.com/margaretakoren/PAF/blob/421cfa261d66cce829fa7840d076aa75eec7b021/Vjezbe/Vjezbe_4/gibanje.py) 
U zasebnom modulu ["particle.py"](https://github.com/margaretakoren/PAF/blob/421cfa261d66cce829fa7840d076aa75eec7b021/Vjezbe/Vjezbe_4/particle.py) definirajte klasu Particle za čestice koja će imati atribute početne brzine,
kuta otklona i koordinata početnog položaja. Neka klasa sadrži i sljedeće metode: 

-  metodu reset() koja briše sve informacije o čestici
-  privatnu metodu __move() koja pomiče česticu za korak ∆t
-  metodu range() koja numerički računa domet projektila
-  metodu plot_trajectory() koja crta putanju u x − y ravnini za trenutno stanje čestice.
Koristeći klasu Particle u programu ["gibanje.py"](https://github.com/margaretakoren/PAF/blob/421cfa261d66cce829fa7840d076aa75eec7b021/Vjezbe/Vjezbe_4/gibanje.py) kreirajte jednan objekt i postavite ga na neke od vrijednosti
za koje ste analitički izračunali domet. Da li se numeričko riješenje slaže s analitičkim? Koliko je odstupanje?

Početna brzina projektila iznosi $240 \frac{m}{s}$ , a kut otklona je $\theta = 50^{\circ}$ 

Numerički domet iznosi otprilike 5782.31 metara, dok analitički domet iznosi otprilike 5782.36 metara. Odstupanje između numeričkog i analitičkog dometa vrlo je malo, što ukazuje na to da se numeričko rješenje vrlo blisko podudara s analitičkim rješenjem.

## [Zadatak 2](https://github.com/margaretakoren/PAF/blob/421cfa261d66cce829fa7840d076aa75eec7b021/Vjezbe/Vjezbe_4/zadatak2.py)

Za česticu početne brzine $v_0 = 10 \frac{m}{s}$ i kuta otklona $\theta = 60^{\circ}$ nacrtajte graf ovisnoti relativne pogreške numeričkog riješenja o vrijednosti vremenskog koraka $\Delta t$.