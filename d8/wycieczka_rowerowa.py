from d8.rower import Rower

rower_Ani = Rower('górski', 'Scott')
print(rower_Ani.typ)
print(rower_Ani.marka)

print(rower_Ani)

rower_Ani.kolor ='czerwony'
print(rower_Ani.kolor)

rower_Ani.czy_hamuje = False
print(rower_Ani.czy_hamuje)

rower_Ani.czy_jedzie = True
print(rower_Ani.czy_jedzie)