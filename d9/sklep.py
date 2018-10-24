from d9.towar import Towar

towar01 = ('japonki', 'biały', 15.00)
towar02 = ('trampki', 'czarny', 25.00)

print(towar01)


zakupy  = [towar01, towar02]
print(zakupy)

print(towar01 == towar02)

#wartosc = towar01.cena + towar02.cena
#def _add_ zdefiniowało, co mam brać za pole pod plusem
wartosc = towar01 + towar02
print(wartosc)
