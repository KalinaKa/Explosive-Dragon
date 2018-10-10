#manager kontekstu
#wszystkie przerwy w kodzie sa dla programisty.
#Readline ustawia się na poczatku wydrukowanej linijki
#tu daje nam pusty wiersa, przez wbudowany \n w print.
#w tekscie na koncu jest \n ukryty i daje info o koncu linii

with open('lokomotywa2.txt', 'r', encoding='utf-8') as file:
    linijka = file.readline()
    print(linijka, end='')
    print(file.readline(), end='')