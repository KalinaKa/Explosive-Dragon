# -*- coding: utf-8 -*-
#przyklad na dzialanie zmiennej globalnej, dostepna wew i na zew funkcji. to co bylo na zew, bedzie zmodyfikowane.
#antyprzyklad dobrej funkcji :P
#globalne pozwola na korzystanie ze zmiennych ogolem, ale te dzialanie przeczy idei funkcji:
#przekazac cos, przetworzyc i zwrocic efekt
#warto ich ogolem nie uzywac, a jak juz to z ostroznoscia

imie = "Ola"
print(imie)

def wypisz_imie():
    global imie
    duze_imie = imie.upper()
    imie = duze_imie
    return duze_imie


print(wypisz_imie())
print(imie)
