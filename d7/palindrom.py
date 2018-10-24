#tu ścieżka do projektu w Pycharmie
# alternatywnie można nei podawać ścieżki, jeśli program jest w tym samym folderze
# from odwracacz import odwroc_zdanie
from d7.odwracacz import odwroc_zdanie

# przyjąć od użytkowniak jakiś string
# porównać czy string wejściowy == str odwrócony
    #jeśli tak to zwr True
    #jeśli nie to False


def czy_palindrom(zdanie):
    if zdanie == odwroc_zdanie(zdanie):
        return True
    else:
        return False

print(czy_palindrom('ala ma ala'))
print(czy_palindrom('ala mam ala'))

'''
w momencie importowania, cały kod musi zostać wykonany linijka po linijce.
konwecja jest taka na testy, że robimy tego main_if
__name__ -> zmienna pythona, tworzy je w momencie uruchomienia programu.
Tam zapisuje nazwe pliku, gdzie został uruchomiony.
jesli chce uruchomic program w pliku, gdzie jest napisany, to uruchamia bezposrenio funkcje z testami.
A jak funkcja jest uruchamiana, to tego nie wywala. :) tylko funkcje importowaną
'''

