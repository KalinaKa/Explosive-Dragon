# KLASA : POLA I METODY
# zawsze na pierwszej pozycji jest argument self:obiekt,
# potem wlasne argumenty (wymagane a potem domyslnie)
# wew. instancji (pola) model - przypisuje to, co uzytk. podal tworzac instancje
# obiekt ma pola self.name, self.breed itp. a te z nawiasu sa podane przez uzytk.
# self oznacza konkretny obiekt/byt ma swoje wlasne wartosci cech
# moge miec pola, ktorych nie musze inicjalizowac
# pola mogą miec niezdefiniowane wartosci

# Zachowania: obiekt moze zrobic cos sam lub my mozemy cos mu zrobic
# metoda -> to funkcja zdef. wew obiektu


class Pies(object):
    def __init__(self, imie, rasa, wiek):
        self.name = imie
        self.breed = rasa
        self.age = wiek
        self.hungry = True
        self.color = None

    def szczeknij(self, sila):
         if sila < 6:
            print('Hauuu')
         else:
             print('Hauuuuuuuuuuuuuuuuuuuu')

    def nakarmij(self):
        self.hungry = False

    def __str__(self):
        return f"Pies {self.name}, ma {self.age} lat."


'''
Tu nadpisalismy metode __str__:
standard wydrukuj nazwe klasy i miejsce w pamieci.
A tu nadpisuje ładną wiadomość.
'''