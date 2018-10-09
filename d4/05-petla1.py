x = True

while x:
    print("Hello")
    x = False
#typowy blad, to brak aktualizacji warunku x = True, wiec bedzie petla nieskonczona.

nazwisko = "Kowalska"

#i to zmienna licznik dla petli
i = 0
while i < len(nazwisko):
    print(nazwisko[i].upper())
    i += 1
# Inkrementacja: tak samo jak i = i + 1


rasa = "Golden River"

i = 0

while i < len(rasa):
    print(rasa[i].lower())
    i += 1


owoc = "CZERWONE JABLUSZKO"

i = 0

while i < len(owoc):
    print(owoc[i].lower())
    i += 1

