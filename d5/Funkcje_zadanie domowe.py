#stworzyć funkcję która po otrzymaniu dwóch liczb
#będzie drukować niepełną piramidę. Dla liczba 5 i 7:

poziomy = 7
od_poziom= 5

for poziom in range(poziomy):
    print("{}{}{}".format(" "*(poziomy - poziom - 1), "#"*(poziom*2+1), " "*(poziomy - poziom - 1)))



#stworzyć funkcję, która po otrzymaniu liczby
#całkowitej do 1 miliona zwróci wartość True jeśli ta
#liczba jest pierwsza -> WIĘKSZA OD 1 I PODZIELNA PRZEZ 1 LUB SIEBIE SAMĄ
# tu mam skonczyc na pierwszym znalezionym dzielniku i zworcic info, ze jest to liczba pierwsza
#nie musze sprawdzac, czy liczba dzieli sie sama przez sie, wtedy to pewne


def is_prime_number (num):
    dividers = [2, 3, 5, 7]

    for divider in dividers:
        if num not in dividers:
            if num % divider == 0:
                wynik = False
                return wynik
                break
            elif num == 9:
                wynik = False
                return wynik
                break
            else:
                wynik = True
                return wynik
                break
        else:
            wynik = True
            return wynik
            break

x = is_prime_number(8)
print(x)