#sposob na wykorzystanie: menu :)
#Tu zaklada, ze ma nieprawidlowe nazwisko i probuje wydobyc prawidlowe.

nieprawidlowe = True

while nieprawidlowe:
    nazwisko = input("Podaj nazwisko drukowanymi literami lub Q aby zakończyć: ")

#instrukcja Quit() wychodzi z petli.

    if nazwisko.upper() == 'Q':
        print("Do widzenia.")
        quit()
    elif nazwisko.isalpha():
        if nazwisko.isupper():
            nieprawidlowe = False

print("Gratulacje, jesteś zarejestrowany.")
