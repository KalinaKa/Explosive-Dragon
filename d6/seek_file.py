#CTR+q, DIRECTORY METODY
#znaki zajmują różną liczbę bajtów.
#wszystkie operacje i zapisy tekstu, będą tam gdzie kursor stoi
# w trybie 'r' ustawia sie na poczatrku pliku
#tu automaatycznie sie zamyka plik, ale w read nie, tam sami zamykamy
#file.seek() -> wez ustaw sie na tej pozycji

with open('lokomotywa.txt', encoding='utf-8') as file:
    tekst = file.read(30)
    print(tekst)

    print(file.readline())
    print(file.readlines())

    pozycja = file.tell()
    print("obecna pozycja {}".format(pozycja))

    file.seek(0)
    pozycja = file.tell()
    print("obecna pozycja {}".format(pozycja))

    print(file.read())