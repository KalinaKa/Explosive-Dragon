# -*- coding: utf-8 -*-

elementy = { 1:"ola", 0:"ala",  2:"ela" }

print(elementy)
print(elementy[1])

slownik = {"imie": "Adam", "nazwisko":"kowalski", "wiek":32}

# klucze: dict_keys - obiekt, ktory przechowuje klucze
print(slownik.keys())
# wartości
print(slownik.values())

# items() zwraca parę - klucz oraz wartość! jesli masz przy wart mnozenie, to kazda wartosc bez wzgledu czy to INT
for klucz, wartosc in slownik.items():
    print("Klucz: {} ma wartość {}".format(klucz, wartosc))


if "adres" in slownik.keys():
    print("Adres dostępny")
else:
    print("adres niedostępny")

print(slownik)
# jeśli przypiszemy wartość do nieistniejącego klucza
# to zostanie on utworzony i odgadnie typ, klucz pojawia sie z przodu (po to metoda append aby byl na koniec)
slownik["adres"] = "Gdańsk"
print(slownik)
# jeśli przypisujemy wartość do istniejącego klucza
# to zmieniamy/nadpisujemy jego wartość
slownik["adres"] = "Gdynia"
print(slownik)

