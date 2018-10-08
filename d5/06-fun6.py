# -*- coding: utf-8 -*-

def pole_kwadratu(bok):
    pole = bok*bok
    return pole

powierzchnia = pole_kwadratu(234)
print("Powierzchnia wynosi {}".format(powierzchnia))

print(pole_kwadratu(2387))

#tak nie uruchomimy funkcji :P:
print(pole_kwadratu)

#funkcja może być wstawiona do zmiennej i ta zmienna może zostać wywołana przez print z agrumentem funkcji.
#bez nawiasów!
x = pole_kwadratu
print(x(2))
