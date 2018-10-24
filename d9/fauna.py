class Zwierz(object):
    def __init__(self, nazwa, klasa):
        self.nazwa = nazwa
        self.klasa = klasa

    def ruszaj(self):
        print(f'Zwierz {self.nazwa} ruszył się.')

"""
dziedziczę ze Zwierza
Jak robie konstruktor dla Czlowieka, jawnie odwoluje sie takze do rodzica, 
co moge zrobic jako:
super() -> automatycznie stara sie znalezc rodzica, z ktorego w 1 kol. dziedziczy
lub 
Zwierz.__init__ -> tu wskazujemy klase, z ktorej dziedziczymy
Ważne, że jeśli rodzic wymaga czegoś w inicie, u dziecka musimy to dostarczyc.
Dziecko wszystko dziedziczy od rodzica (wybiorczo nie mozna)
Jesli metody chcemy zmienic, to je nadpisujemy w dziecku

Mogę w defaulcie wpsiac w inicie dziecka wartosc 'kregowiec' jako zastepnik
argumentu 'klasa'.
"""
class Czlowiek(Zwierz):
    def __init__(self, imie, wiek):
        super().__init__(imie, 'kręgowiec')
        #Zwierz.__init__(self, imie)
        self.imie = imie
        self.wiek = wiek

    def ruszaj(self):
        print(f'{self.nazwa} idzie.')


class Pies(Zwierz):
    def __init__(self, imie, rasa):
        super().__init__(imie, 'kręgowiec')
        self.imie = imie
        self.rasa = rasa

    def ruszaj(self):
        print(f'{self.imie} biega, skacze, hopsa.')

    def bark(self):
        print('Hauuuuuuuuuuuuu!')

"""
Tutaj wybieram, skąd chcę dziedziczyć.
Najlepiej po Człowieku a nie po Zwierzu, bo tam mam rozszerzone funkcje.
W metodzie super() podaję argumenty, jakich wymaga konstruktor człowieka
None = w super() rodzica, gdy nie ma logicznej przeslanki dla konkretnej liczby
"""

class Student(Czlowiek):
    def __init__(self, imie, kierunek):
        super().__init__(imie, None)
        self.imie = imie
        self.kierunek = kierunek

    def powiedz(self, imie_psora):
        print(f'Panie {imie_psora} proszę 4.')