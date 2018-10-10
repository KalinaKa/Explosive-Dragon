#jak konwertowac baze na dane typy

#otwieramy plik

#wczytujemy linijka po linijce, while, pusty string

    # trim na koncu: whitespace, znaki
    # split po przecinku -> lista stringów ["Jan","Kowalski","34","3000.00"],
    # pozycje 2 i 3 odpowiednio zmieniamy


baza = []

with open('baza.csv', encoding='utf-8') as file:
    #wczytujemy linjka po linijce
    linijka = file.readline()

    while linijka != "":
        #musze dopisac zmienna, bo metoda zwraca zmiany ale sama nie zapisuje
        linijka = linijka.rstrip()
        osoba = linijka.split(',')

        osoba[2] = int(osoba[2])
        osoba[3] = int(osoba[3])

        print(osoba)
        baza.append(osoba)
        linijka = file.readline()

print(baza)


#Moduł CS