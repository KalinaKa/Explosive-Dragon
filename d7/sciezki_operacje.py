import os
import os.path

biez_folder = os.getcwd()

#zwraca liste plikow w bieżącym folderku
pliki = os.listdir(biez_folder)

#wylistuj folder wyżej
#pliki = os.listdir('..\\')

print('Pliki:')
print(pliki)


#tak się oblicza ścieżki:
for plik in pliki:
    pelna_sciezka = os.path.join(biez_folder, plik)
    print(pelna_sciezka)