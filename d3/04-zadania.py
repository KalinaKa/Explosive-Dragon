# 1. czy liczba jest podzielna przez 3 lub 5 lub 7

tested_value = int(input("Podaj liczbę całkowitą:\n"))

print(type(tested_value))

if tested_value % 3 == 0:
    print("Twoja liczba jest podzielna przez 3. :)")
elif tested_value % 5 == 0:
    print("Twoja liczba jest podzielna przez 5. :)")
elif tested_value % 7 == 0:
    print("Twoja liczba jest podzielna przez 7. :)")
else:
    print("UPS! Wygląda na to, że {} nie dzieli się ani przez 3 ani przez 5 ani przez 7! :p".format(tested_value))
    exit(98)


# 2. obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

tested_year = int(input("Podaj rok, aby sprawdzić, czy jest przestępny:\n"))
print(type(tested_year))

if tested_year % 4 == 0:
    print("Rok {} jest rokiem przestępnym. Luty ma aż 29 dni!".format(tested_year))
elif tested_year % 400 == 0:
    print("Rok {} jest rokiem przestępnym. Luty ma aż 29 dni!".format(tested_year))
else:
    print("Rok {} NIE jest rokiem przestępnym. Luty ma tylko 28 dni!".format(tested_year))
    exit(98)

# 3. oblicz ocenę na podstawie progu procentowego
# ktos uzyskal 75%, sam ustal próg

your_score = float(input('Aby sprawdzić ocenę, podaj procent uzyskanych na teście punktów (liczba bez znaku "%" np. 75.5):\n'))
print(type(your_score))

if your_score >= 80:
    print("Wynik {}% oznacza ocenę BARDZO DOBRĄ. Gratulacje!".format(your_score))
elif (your_score >= 70 and your_score <80):
    print("Wynik {}% oznacza ocenę DOBRĄ. Gratulacje!".format(your_score))
elif (your_score >= 50 and your_score < 70):
    print("Wynik {}% oznacza ocenę DOSTATECZNĄ. Staraj się bardziej!".format(your_score))
else:
    print("Wynik {}% oznacza, że NIE ZALICZYŁEŚ. Popraw się!".format(your_score))
    exit(98)

# 4. po podaniu nazwy miesiaca, program napisze ilosc dni w miesiacu

#31_days: styczeń, marzec, maj, lipiec, sierpień, październik, grudzień
#30_days: kwiecień, czerwiec, wrzesień, listopad
#less_than_30days: luty

print("Witaj! Sprawdź, ile dni zawierają poszczególne miesiące w roku.")
month = input("Podaj pełną nazwę miesiąca (np. styczeń):\n")

print(type(month))

month = month.strip()

if not month.isalnum():
    print("Ups! Potrzebuję nazwy miesiąca. :( ")
    exit(98)

month_clean = month.upper()
print(month_clean)

days_31 = ['STYCZEŃ', 'MARZEC', 'MAJ', 'LIPIEC', 'SIERPIEŃ', 'PAŹDZIERNIK', 'GRUDZIEŃ']
print(days_31)

if month_clean in days_31:
    print("{} liczy 31 dni.".format(month_clean))
elif month_clean == 'LUTY':
    is_leap_year = input("Czy podać liczbę dni w roku nieprzestępnym [T / N]?:\n")
    is_leap_year.strip().upper()
    if is_leap_year == "T":
        print("Luty w roku nieprzestępnym liczy 28 dni.")
    else:
        print("Luty w roku przestępnym liczy 29 dni.")
else:
    print("{} liczy 30 dni.".format(month_clean))

# 5. inupt - miesiąc oraz dzien (np. mar-18),
#   okreslic pore roku

print("Witaj! Sprawdź, do jakiej pory roku należy dany miesiąc.")
month = input("Podaj nazwę miesiąca, którą chcesz sprawdzić (np. styczeń lub sty-18):\n")

month_clean = month.strip().upper()
print(type(month_clean))
print(month_clean)


spring = ['MARZEC', 'MAR-18''KWIECIEŃ', 'KWI-2018','KWIECIEN', 'MAJ', 'MAJ-2018']
summer = ['CZERWIEC', 'CZER-18', 'LIPIEC', 'LIP-18', 'SIERPIEŃ','SIERPIEN', 'SIE-18']
autumn = ['WRZESIEŃ', 'WRZESIEN', 'WRZE-18', 'PAŹDZIERNIK', 'PAZDZIERNIK', 'PAŹ-18', 'PAZ-18', 'LISTOPAD', 'LIS-18']
winter = ['GRUDZIEŃ', 'GRUDZIEN', 'GRU-18', 'STYCZEŃ', 'STYCZEN', 'STY-18', 'LUTY', 'LUT-18']

if month_clean in spring:
    print("{} jest wiosną.".format(month_clean))
elif month_clean in summer:
    print("{} jest latem.".format(month_clean))
elif month_clean in autumn:
    print("{} jest jesienią.".format(month_clean))
else:
    print("{} jest zimą.".format(month_clean))


# 6. ruletka: otrzymawszy liczbę, sprawdź czy jest ona (np. 17R (red), 2B (black)):
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

wynik = '17R'

kolor = wynik[-1]
print(kolor)

if kolor == 'R':
    print('{} to czerwone pole.'.format(wynik))
else:
    print('Wylosowałeś pole w kolorze czarnym.')

liczba = int(wynik[:2])

if liczba >= 18:
    print('{} to wysoka liczba.'.format(wynik))
else:
    print('{} to niska liczba.'.format(wynik))

if liczba % 2 == 0:
    print('{} to parzysta liczba.'.format(wynik))
else:
    print('{} to nieparzysta liczba.'.format(wynik))

# 7. zamiana temperatury (przeliczyc, tu bedzie wycinanie znaku istotne)
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32


CELSJUSZ = '35C'
F = '100F'

dl = len(temp)
stopnie_temp = temp[0:dl-1]


if "C" in temp:
    typ = 'Celsjusza'


# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

a = 5
b = 10
c = 13

if a == b == c:
    print("Trójkąt równoboczny")
elif a != b != c:
    print("Trójkąt różnoboczny")
else:
    print("Trójkąt równoramienny")



