#metoda str musi zawsze zwracać, lamanie linii backslash (dalam mu enter)

class Towar(object):

    def __int__(self, nazwa, kolor, cena):
        self.kolor = kolor
        self.nazwa = nazwa
        self.cena = cena


    def __str__(self):
        return f"But {self.nazwa} {self.kolor} " \
               f"cena: {self.cena}"

    def __repr__(self):
        return f"But {self.nazwa} - {self.cena}"

    def __eq__(self, other):
        if self.kolor == other.kolor and self.cena == other.cena:
            return True
        else:
            return False

    def __add__(self, other):
        return self.cena + other.cena

