import os, sys
from pprint import pprint
'''
modul OS sluzy do komunikacji z systemem,
podobnie jak w CMD
get cwd get current working directory, tam gdzie sie znajduje aktualnie python
pprint - pretty print, jak masz drukowac slowniki / jsony to warto.

Z poziomu cmd nie pokaże 
Do folderów roboczych zagląda Python przy importowaniu.venv i roboczego folderu.

Program działający na produkcji:
Ważne, gdzie sie znajdują importowane pliki, gdzieś wśród folderków, które czyta CMD

moduły wrzucać do folderu, którą dodamy do PYTHONPATH

sys.path  - to lista pythonowa, wiec mozna sys.path.append(moja_sciezka)
u
lub tam gdzie site-packages

GWC - get current working directory

'''

pprint("Foldery robocze:")
pprint(sys.path, indent=4)

pprint("Bieżący folder:")
pprint(os.getcwd())

