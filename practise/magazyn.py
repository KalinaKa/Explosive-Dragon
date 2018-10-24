from practise.towar import Towar
from practise.towar import Food


prod01 = Towar('dżinsy', 'czarny', 214)
prod02 = Towar('dżoggery', 'zielony', 123)
prod03 = Towar('legginsy', 'fiolet', 13)

print(f'Ile ubrań: {Towar.ile_produktow}.')

print(prod01)
print(isinstance(prod01, Towar))

shopping_sum = prod01 + prod02
print(shopping_sum)

#meotda repr
zakupy = [prod01, prod02]
print(zakupy)

print(prod01 == prod02)

netto = prod01.cena_netto(45667)
print(netto)

ean = Towar.check_ean13('45667789')
print(ean)




'''

food01 = Food('chleb', 1500)
food02 = Food('bułka', 2500)

print(help(food01))
print(food01)

food01.price = 15
food02.price = 2.9

cena = food01 + prod02
print(cena)
print(food01 == prod02)


'''