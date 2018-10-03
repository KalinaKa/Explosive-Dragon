# stringi są troche jak listy.
# Możemy się tu dobierać do elementów ale nie możemy dopisywać konkretnych elementów.
#Poniżej operacja zmiany literek: zamieniamy slowo na listę.

imie = "Anna"
print(imie[2])
#tu wyskoczy błąd, bo nie możemy się tu dobrać i podstawić nowej wartości.
#imie[2] = "i"


nazwisko = "Kowalska"
#konwertuje slowo na liste
litery = list(nazwisko)
print(litery)

literki = ["J", "o", "a", "n", "n", "a"]

imie = "_".join(literki)
print(imie)


#operator z gwiazdka oznacza, że resztę z krotki wrzuci do *reszta. jesli zdefiniujemy za mało lub za dużo zmiennych w
# stosunku do liczb, dostaniesz błąd.
krotka = (1, 2, 700, 6, 8)
x, y, *reszta = krotka

print(x)
print(reszta)