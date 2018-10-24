from d8.pies import Pies

#tworzę instancję
#jak juz poszedl konstruktor, musze podac argumenty w obiektach
reksio = Pies('Kiler', 'bokser', 7)
print(reksio)
print(reksio.name)
print(reksio.age)

burek = Pies('Burek', 'mix', 3)
print(burek.name)
print(burek.age)


reksio.szczeknij(4)
burek.szczeknij(7)

reksio.nakarmij()
print(reksio.hungry)
print(burek.hungry)


#nie musze uzywac metod, aby zmienic info wew obiektu
burek.hungry = False
print(burek.hungry)

# w pythonie wszystko jest publiczne, wiec do pol moge sobie wrzucac dowolne wartosci
# dzieki metodom dbamy o standaryzację kodu, powinnismy korzystac z konwencji
burek.hungry = 'No'
print(burek.hungry)

#drukuje typ i miejsce w pamieci
print(burek)