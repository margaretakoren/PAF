# Vježbe 3

### Zadatak 1
#### _[a](https://github.com/margaretakoren/PAF/blob/286c5906507e9a19ab4226f0bd5b9604b49d4691/Vjezbe/Vjezbe_3/zadatak1_a.py) Oduzmite 5.0 i 4.935. Koji rezultat očekujete? Koji rezultat dobijete koristeći Python? Objasnite._ 

Rezultat koji dobijemo, 0.06500000000000039 umjesto očekivanog 0.065, proizlazi iz ograničenja prikazivanja decimalnih brojeva u binarnom formatu u memoriji računala.
U Pythonu, kao i u većini programskih jezika, brojevi s pomičnim zarezom predstavljaju se prema binarnom formatu IEEE 754 standarda. To znači da se svaki decimalni broj unjeti u računalo pretvara u binarni zapis za računanje.
Kada oduzmemo 5.0 od 4.935, očekujemo rezulat 0.065. Međutim, zbog ograničene preciznosti aritmetike s pomičnim zarezom u binarnom formatu, stvarni rezultat pohranjen u memoriji je drugačija binarna aproksimacija broja 0.065. To je zato što se 0.065 ne može točno predstaviti u binarnom formatu s pomičnim zarezom.
Binarno prikazivanje vrijednosti 0.065 postaje beskonačno ponavljajući binarni broj zbog toga što se ne može točno izraziti u binarnom obliku. Stoga računalo aproksimira tu vrijednost što je moguće bliže unutar granica aritmetike s pomičnim zarezom. Ova greška aproksimacije je razlog zašto se dobije rezultat poput 0.06500000000000039 umjesto očekivanog 0.065.
U binarnom sustavu brojevi se predstavljaju kao zbroj potencija broja 2. Međutim, neki decimalni brojevi se ne mogu točno predstaviti u tom formatu. To dovodi do grešaka u zaokruživanju i razlika između očekivanih i stvarnih rezultata prilikom rada s aritmetikom s pomičnim zarezom.

#### _[b](https://github.com/margaretakoren/PAF/blob/286c5906507e9a19ab4226f0bd5b9604b49d4691/Vjezbe/Vjezbe_3/zadatak1_b.py) Provjerite iznosi li suma brojeva 0.1, 0.2 i 0.3 broj 0.6. Objasnite rezultat koji ste dobili._

U Pythonun bismo očekivali da je zbroj brojeva 0.1, 0.2 i 0.3, broj 0.6. Međutim, zbog ograničenja u reprezentaciji brojeva s pomičnim zarezom u računarskoj aritmetici, rezultat ovog zbroja neće biti točno 0.6. 
Ovo se događa zbog toga što decimalni brojevi poput 0.1, 0.2 i 0.3 nemaju točan binarni ekvivalent u računarskoj aritmetici. Kada se ovi brojevi zbroje, rezultat može biti blizu očekivanog rezultata, ali ne točno isti zbog grešaka u aritmetici s pomičnim zarezom.


### [Zadatak 2](https://github.com/margaretakoren/PAF/blob/286c5906507e9a19ab4226f0bd5b9604b49d4691/Vjezbe/Vjezbe_3/zadatak2.py)
_Napišite funkciju koja uzima broj iteracija N te N puta zbraja 1/3 pa zatim N puta oduzima 1/3 broju 5.
Ispišite konačni rezultat za 200, 2000 i 20000 iteracija. Objasnite rezultat koji ste dobili._

U slučaju korištenja manjeg broja iteracija, poput 200, rezultat će biti bliži očekivanom rezultatu, ali može također biti podložan greškama u aritmetici s pomičnim zarezom. Povećavanjem broja iteracija, rezultat će postajati precizniji, no postoji granica do koje računalo može precizno izračunati rezultat zbog ograničenja u pohrani i aritmetici s pomičnim zarezom.

### Zadatak 3

#### _[a](https://github.com/margaretakoren/PAF/blob/286c5906507e9a19ab4226f0bd5b9604b49d4691/Vjezbe/Vjezbe_3/arithm.py) Napišite program [arithm.py](https://github.com/margaretakoren/PAF/blob/286c5906507e9a19ab4226f0bd5b9604b49d4691/Vjezbe/Vjezbe_3/arithm.py) koji računa aritmetičku sredinu i standardnu devijaciju za 10 točaka. Formula za aritmetičku sredinu je dana u 1, a za standardnu devijaciju u 2._

#### _[b](https://github.com/margaretakoren/PAF/blob/286c5906507e9a19ab4226f0bd5b9604b49d4691/Vjezbe/Vjezbe_3/zadatak3.py) Napišite program pod [a](https://github.com/margaretakoren/PAF/blob/286c5906507e9a19ab4226f0bd5b9604b49d4691/Vjezbe/Vjezbe_3/arithm.py) koristeći gotove module._

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$



$$\sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$




### [Zadatak 4](https://github.com/margaretakoren/PAF/blob/6e43effc1725a526d0b22025682751d58cb8b806/Vjezbe/Vjezbe_3/linregress.py)
_Napišite program [linregress.py](https://github.com/margaretakoren/PAF/blob/6e43effc1725a526d0b22025682751d58cb8b806/Vjezbe/Vjezbe_3/linregress.py) za određivanje modula torzije Dt aluminijske šipke ako znamo da vrijedi_
_M = Dt · φ. Parametri su nam zadani kao M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] Nm, φ = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] rad._
_Formule koje možete iskoristiti za doći do grafa linearne regresije su:_ $y = ax + b, b = 0$
$$a = \frac{\bar{xy}}{\bar{x}^2}
$$\sigma_a = \sqrt{\frac{1}{n} (\frac{\bar{y}^2}{\bar{x}^2} - \bar{a})^2}$$