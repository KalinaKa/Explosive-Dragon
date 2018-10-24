from typing import Optional, Tuple

print("""Witaj w kalkulatorze:
podaj operację: + - / *
podaj dwie liczby oddzielone spacją, np: 25 20.
Zawsze możesz zakończyć program wpisując koniec""")

koniec = 'koniec'


def oblicz(operacja: str, a: float, b: float) -> float: #okresla, jaki typ bedzie zwracany
    """Zwraca wynik operacji matematycznej dwóch liczb."""
    if operacja == '+':
        wynik = a + b
    elif operacja == '-':
        wynik = a - b
    elif operacja == '/':
        wynik = a / b
    else:
        wynik = a * b

    return wynik


def sprawdz_operacje(op: str) -> str:
    """Sprawdza, czy operacja jest dopuszczalna."""
    operacje = ['+', '-', '/', '*']
    if op in operacje:
        return op
    elif op == koniec:
        exit(1)


def sprawdz_liczby(str_liczby: str) -> Optional[Tuple[float, float]]:
    """
    Sprawdza poprawność stringu z liczbami.
    Jeśli string jest prawidłowy, zamienia go
    na dwie liczby w tuplu.
    """
    if str_liczby == koniec:
        exit(2)

    licz = str_liczby.split(' ')
    if len(licz) != 2:
        print('Podałeś złą liczbę argumentów.')
        return None

    if licz[0].isdigit() and licz[1].isdigit():
        liczby = (float(licz[0]), float(licz[1]))
        return liczby
    else:
        print('Podaj wyłącznie liczby oddzielone spacją!')


# główna pętla programu
while True:

    # sprawdzenie operacji
    operacja = None
    while operacja is None:
        op = input("Podaj operację (+ - / *): ")
        operacja = sprawdz_operacje(op)

    # sprawdzenie stringa z liczbami
    liczby = None
    while liczby is None:
        licz = input("Podaj liczby oddzielone spacją, lub wpisz koniec: ")
        liczby = sprawdz_liczby(licz)

    # obliczenie i wydrukowanie wyniku
    wynik = oblicz(operacja, liczby[0], liczby[1])
    print(f"{liczby[0]} {operacja} {liczby[1]} = {wynik}")
