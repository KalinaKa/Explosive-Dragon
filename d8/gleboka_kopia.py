from pprint import pprint
from copy import deepcopy

nabial = ['mleko', 'ser', 'masło']
chemia = ['cif', 'ajax', 'ludwik']

# deepcopy probuje dostac sie do wartosci dostepnych pod adresem w pamieci, wiec tylko w pazdz bedzie jogurt
paz = [nabial, chemia]
lis = deepcopy(paz)
gru = deepcopy(paz)

pprint(f"paż: {paz}")
pprint(f"lis: {lis}")
pprint(f"gru: {gru}")

paz[0].append('jogurt')

'''
Dzieki deepcopy tylko w paz jest jogurt
'''
pprint(f"paż: {paz}")
pprint(f"lis: {lis}")
pprint(f"gru: {gru}")



