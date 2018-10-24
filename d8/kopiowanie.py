from pprint import pprint

nabial = ['mleko', 'ser', 'masło']
chemia = ['cif', 'ajax', 'ludwik']

# plytkie kopiowanie
paz = [nabial, chemia]
pprint(f"paż: {paz}")

lis = [nabial, chemia]
pprint(f"lis: {lis}")

gru = paz.copy()
pprint(f"gru: {gru}")

paz[0].append('jogurt')

'''
elementy w liscie pazd sa adresami, i one zostaly skopiowane wszedzie. dlatego jogurt 4 ever
chyba, ze nie jest to lista list, tylko jedna lista i ma typy proste, to skopiuje wartosci
'''
pprint(f"paż: {paz}")
pprint(f"lis: {lis}")
pprint(f"gru: {gru}")



