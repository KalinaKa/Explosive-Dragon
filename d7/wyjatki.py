
path ="c:\\moj_plik1.txt"

try:
    #FileNotFoundError wyrzuca funkcja open()
    with open(path) as file:
        print(file.read())
except FileNotFoundError:
    print('Nieprawidłowa ścieżka!')
except AssertionError:
    pass
except Exception:
    print('Wystąpił jakiś błąd ?!')


print('Koniec programu')

