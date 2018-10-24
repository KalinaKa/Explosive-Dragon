class Rower(object):
    """"
    Rower

    Obiekty -> moge tak zdefiniowac tak, ze obiekt bedzie przechowywac
    instancje innej klasy
    """

    def __init__(self, typ, marka):
        self.typ = typ
        self.marka = marka
        self.kolor = None

    def jedz(self):
        self.czy_jedzie = False


    def hamuj(self):
        self.czy_hamuje = False



    def __str__(self):
        return f"Rower typu {self.typ}, marki {self.marka}."