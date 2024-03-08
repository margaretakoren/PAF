# Vježbe 5

## Zadatak 1

Napišite modul "calculus.py" koji će sadržavati dvije metode:

- _Prva metoda kao ulazne parametre prima funkciju i točku, a kao rezultat vraća vrijednost derivacije funkcije u toj točki._

- _Druga prima kao ulazne parametre funkciju i gornju i donju granicu raspona derivacije._
 _Funkcija korisniku vraća listu točaka u kojima će biti izvršena numerička derivacija na zadanom rasponu i iznose derivacije funkcije u tim istim točkama._


Testirajte modul na primjerima kubne i trigonometrijske funkcije. Neka korisnik u svom kodu importa modul calculus i za derivaciju koristi gotove metode iz tog modula. Nacrtajte na istom grafu analitičko rješenje i numerička rješenja za različite korake numeričke derivacije. To ćete postiči tako da u razvijenim metodama iz modula calculus dodate opciju da metoda kao jedan od ulaznih parametara prima i veličinu
koraka derivacije ε i metodu kojom derivira. Neka "three-step" metoda bude zadana ako korisnik ništa ne odabere, a "two-step" metoda bude druga ponuđena opcija.

## Zadatak 2

U modulu "calculus.py" implementirajte nove dvije metode:

- Prva metoda kao ulazne parametre prima funkciju, granice integracije i broj podjela za numeričku
integraciju, a vraća gornju i donju među koristeći pravokutnu aproksimaciju.

-  Druga metoda ima iste ulazne parametre a vraća numeričku vrijednost integrala koristeći trapeznu
formulu.


Testirajte modul na primjeru proizvoljno odabrane funkcije i raspona integracije. Neka korisnik u svom
kodu importa modul calculus i za integraciju koristi gotove metode iz tog modula. Nacrtajte na istom grafu
analitičko riješenje i numerička riješenja za različiti broj koraka i obe metode numeričke integracije.