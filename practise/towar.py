class Towar(object):

    vat_pct = 0.23
    ile_produktow = 0

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        Towar.ile_produktow += 1

    def __str__(self):
        return f'Spodnie {self.name}, kolor: {self.color}' \
               f'cena w PLN: {self.price}.'

    def __repr__(self) -> object:
        return f'Produkt {self.name} - cena {self.price} PLN.'

    def __eq__(self, other):
        if self.color == other.color and self.name == other.name and self.price == self.price:
            return True
        else:
            return False

    def __add__(self, other):
        return self.price + other.price

    @classmethod
    def cena_netto(cls, wartosc):
        return wartosc / (cls.vat_pct + 1)

    @staticmethod
    def check_ean13 (ean13):
        if len(ean13)!= 13:
            return False
        else:
            return True


class Food(Towar):

    def __init__(self, name, calories):
        super().__init__(name, None, None)
        self.name = name
        self.calories = calories

    def __str__(self):
        return f'Towar: {self.name}, cena {self.price}, kaloryczność {self.calories}.'