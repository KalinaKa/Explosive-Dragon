from d9.pracownik import Pracownik

pr1 = Pracownik('Karol Kłos', 'aktor', 8000)
pr2 = Pracownik('Karol Rambo', 'misjonarz', 18000)


print(pr1.roczna_podwyzka)
print(pr2.roczna_podwyzka)

'''
Zmiana wartosci pola w klasie
'''
#Pracownik.roczna_podwyzka = 0.06

#Pracownik.ustaw_podwyzke(0.6)

#wywołuję metodę klasy przez instancję, to działa
#ale nie powinno się tego robić na obiekcie
#metoda wywołana na obiekcie działa, dlatego że Python szuka metody najpierw w Inicie,
# a jak jej nie ma to idzie krok wyżej, do Klasy. I jak tam znajdzie to wykorzysta.

#pr1.ustaw_podwyzke(0.6)

#print(pr1.roczna_podwyzka)
#print(pr2.roczna_podwyzka)

print(f'Il prac: {Pracownik.il_pracownikow}')

pr3 = Pracownik('Karol Travolta', 'gwiazda', 58000)
print(f'Il prac: {Pracownik.il_pracownikow}')

'del - usuwa obiekt, moze tez usuwac cos z listy' \
'jest tez __del__, które można zdefiniować na poziomie klasy.' \
'będzie aktualizować licznik pracowników'
del pr1
print(f'Il prac: {Pracownik.il_pracownikow}')
print(type(pr1))
'''
Python czysci sam po sobie obiekty pozostale w pamieci, gdy nastapil koniec programu.
Nie zawsze w metodach specjalnych, nie zawsze printuj.
Może lepiej, aby one zwracały wartosci, by były niezależne od warstwy prezentacji.
Jak ona printuje to nie zwraca do pliku :P
'''
#print('Koniec programu.')

#wywołanie metody statycznej
prawidlowy = Pracownik.spradz_pesel('543211234')
print(prawidlowy)