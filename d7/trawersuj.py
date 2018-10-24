import os

path = r'C:\Users\KalinowA\PycharmProjects\kurs_p'
#rozpakowuje krotke w petli od razu
#odczyt, zapis, edycja nazwy - to pozwala na wiele operacji

for current_folder, subfolders, files in os.walk(path):
    print('Bieżący folder:{}'.format(current_folder))

    for subfolder in subfolders:
        print('{}'.format(subfolder))

    for file in files:
        print('{}'.format(file))