# -*- coding: utf-8 -*-
#Przykład na zdefiniowany/domyslny parametr + jego nadpisywanie.
# to sytuacja z printem, gdzie na koncu domyslna wartosc parametru to \n

def wypisz_imie(imie = "ola"):
    imie = imie.capitalize()
    print(imie)


wypisz_imie()

wypisz_imie("Damian")