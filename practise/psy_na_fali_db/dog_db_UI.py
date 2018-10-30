greeting = """
Baza psów klubu sportowego "Na Fali".
Wybierz akcję spośród możliwych wariantów, wciskając odpowiedni klawisz
A: Dodaj psa
B: Usuń psa
D: Edytuj psa
E: Sprawdź ogólną liczbę psów w klubie
F: Wyświetl wszystkie psy będące obecnie w klubie
Q: Wyjdź z programu
Wybierz akcję:\n
"""


specify_action = input(greeting).strip().upper()

if specify_action.isalpha():
    print(f'Wybrano ackję {specify_action}.')
else:
    print('Wprowadź poprawny kod akcji używając przypisanej litery.')
