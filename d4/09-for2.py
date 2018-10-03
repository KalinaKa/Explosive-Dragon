#range nie jest lista.
#zakres = range(1000000000000000)

#Range przerobiony na liste. Tu ma memory error. :D
#inty = list(range(1000000000000000))

#zabangla, jesli zmienimy na mniejsze wartosci range
#range nie jest lista.
zakres = range(10)
inty = list(range(10))

print(zakres)
print(inty)

for i in zakres:
    print(i)

#tu iteruje listę.
for j in inty:
    print(j)

