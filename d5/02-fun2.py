# -*- coding: utf-8 -*-
#przekazywanie argumentu do funkcji
#zmienna nie musi miec nic wspolnego nazwa argumentu w funkcji.

def print_greeting(name):
    print("Hello ma name is {}".format(name.capitalize()))


print_greeting("damian")

imie = input("Podaj imie: ")
print_greeting(imie)

