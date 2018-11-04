from practise.psy_na_fali_db.dog_db_engine import *

greeting = """
Baza psów klubu sportowego "Na Fali".
Wybierz polecenie spośród możliwych wariantów (A, B, C, D lub Q):
A: Dodaj psa
B: [to be done :((((( ] Edytuj psa
C: Sprawdź ogólną liczbę psów w klubie
D: Wyświetl wszystkie psy będące obecnie w klubie
Q: Wyjdź z programu
Wybierz polecenie:
"""

''' Lista poleceń '''
specify_action = input(greeting).strip().upper()

while specify_action != "Q":
    if specify_action == 'A':
        add_dog()
    elif specify_action == 'C':
        count_dogs()
    elif specify_action == 'D':
        display_dogs()
    else:
        print("Podałeś złe polecenie, spróbuj ponownie.")

    specify_action = input('Wybierz kolejne polecenie lub wyjdź (Q).\n').strip().upper()


