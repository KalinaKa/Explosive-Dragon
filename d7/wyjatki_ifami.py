import os

path ="c:\\moj_plik1.txt"

if  os.path.exists(path):
    with open(path) as file:
        print(file.read())

else:
    print('Podany plik nie isnieje')

print('Koniec programu')


#jeśli chcemy usunąc klucz ze słownika, listy -> sprawdzić, czy istnieje i potem ogarniać lub try:except
raise  ValueError('blad')