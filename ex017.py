print('========== DESAFIO 017 ==========')
print('LEIA O CATETO OPOSTO E O CATETO ADJASCENTE E CALCULE O TAMANHO DA HIPOTENUSA')
from math import hypot
co = float(input('CATETO OPOSTO: '))
ca = float(input('CATETO ADJASCENTE: '))

print('CO: {}, CA: {}, HIPOTENUSA: {}'.format(co, ca, round(hypot(co, ca), 2)))