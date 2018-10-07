### Listy
# 1. napisz program sumujący wszystkie elementy w liscie
# zdefinuj liste z liczbami

numbers = [3, 5, 13, 10, 2]
print(len(numbers))

number1 = numbers.pop(0)
print(number1)
number2 = numbers.pop(0)
print(number2)
number3 = numbers.pop(0)
print(number3)
number4 = numbers.pop(0)
print(number4)
number5 = numbers.pop(0)
print(number5)

sum_of_numbers = number1 + number2 + number3 + number4 + number5
print(sum_of_numbers)

# DRUGIE ROZWIAZANIE

numbers = [4, 2, 3, 1, 100]

suma = 0
i = 0

for number in numbers:
    a = numbers[i]
    suma += a
    i += 1

print(suma)

# 2. znajdz najwiekszy / najmniejszy element w liscie
# zdefinuj liste z liczbami
# do rozkminy, drugie czy najmniejsza wartosc jest mniejsza niz do tej pory, czyli kopiuje do dwoch zmiennych
# i porownuj sobie kolejne elementy i sprawdzaj, czy sa wieksze czy mniejsze

numbers = [3, 5, 13, 10, 2]

max = numbers[0]
min = numbers[0]

i = 0

for number in numbers:
    a = numbers[i]

    if a < min:
        min = a

    if a > max:
        max = a

    i += 1

print(min)
print(max)

# 3. znajdz liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# ['abc', 'xyz', 'aba', '1221'] - odp = 2


# 4. program znajdujacy wartosci, ktre wystepuja tylko raz

lista_a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

for numer in lista_a:
    count = lista_a.count(numer)
    print(numer)
    print(count)

    if count > 1:
        lista_a.remove(numer)

print(lista_a)

# 5. program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
lista_b = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

for numer in lista_b:
    count = lista_b.count(numer)
    print(numer)
    print(count)

    if count > 1:
        lista_b.remove(numer)

print(lista_b)

# 6. program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True


### Pętle

# 1. program wydający resztę z dostępnych monet: 5, 2, 1, 0.5, 0.2, 0.1
#    konkretne zdefiniowac: cena, zaplacono, reszta

cena = 13
zaplacono = 30
reszta = zaplacono - cena
print("Cena wynosi {} PLN.\nZaplacono: {} PLN.\nReszta: {} PLN.".format(cena, zaplacono, reszta))

monety = [5, 2, 1, 0.5, 0.2, 0.1]

i = 0

for moneta in monety:
    nominal = monety[i]

    if reszta > 0:
        ile_monet = reszta // nominal
        reszta -= (ile_monet * nominal)
        print('Wydano {} monet po {} PLN.'.format(ile_monet, nominal))

    i += 1



 # 2. Narysuj piramidę Mario - jako input - wysokość piramidy
        # np. piramida wysokości 3 ma wyglądać:
        #
        #   #
        #  ###
        # #####
        #

# 3. program, ktory obliczy ilosc liczb parzystych i nieparzystych w danym zakresie
# zdefiniuj zakres

zakres = range(0,31)
parzyste = 0
nieparzyste = 0

for liczba in zakres:
    if liczba % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print(parzyste)
print(nieparzyste)

# 4. program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4 (modulo)

zakres = range(0, 21)
lista = []

for liczba in zakres:
    if liczba % 4 > 0:
        lista.append(liczba)

print(lista)

# 5. program, ktory wypisze liczby (0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21

# 6. oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata
# np. 15 ludzkich lat to 73 psie lata

ile_lat_zyje_pies = range(1,5)
wiek_psa = 0

for rok in ile_lat_zyje_pies:

    if rok < 3:
       wiek_psa += 10.5
    elif rok >= 3:
        wiek_psa += 4

print(wiek_psa)