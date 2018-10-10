#readlines() daje na koncu \n
with open('lokomotywa2.txt', 'r', encoding='utf-8') as file:
    linijki = file.readlines()

    for linia in linijki:
        print(linia, end='')



