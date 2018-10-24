'''
Jak zliczac obiekty utworzone w danej klasie.
Pole il_pracownikow na poziomie klasy.
Licznik - umieszczam w Inicie, bo zawsze jest odpalany, ale odwoluje sie przez klase.

'''

class Pracownik(object):
    #pole klasy, wspolne dla każdej instancji
    il_pracownikow = 0
    roczna_podwyzka = 0.05

    def __init__(self, imie, stanowisko, pensja):
        self.imie = imie
        self.stanowisko = stanowisko
        self.pensja = pensja
        Pracownik.il_pracownikow += 1

    #metoda klasy - działa na polach klasy
    #wchodze do pol klasy przez slowo kluczowe cls
    @classmethod
    def ustaw_podwyzke(cls, wartosc):
        if cls.roczna_podwyzka + wartosc < cls.roczna_podwyzka * 1.1:
            cls.roczna_podwyzka = wartosc
        else:
            cls.roczna_podwyzka = cls.roczna_podwyzka * 1.08

    def __del__(self):
        Pracownik.il_pracownikow -= 1
        print(f'{self.imie} został usunięty.')

    @staticmethod
    def spradz_pesel(pesel):
        if len(pesel) != 11:
            return False
        return True