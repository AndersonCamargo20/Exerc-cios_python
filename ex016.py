print('========== DESAFIO 016 ==========')
print('LEIA UM NUMERO FLOAT E PRINTE A SUA PORÇÃO INTEIRA')

import math
n = float(input('Informe um numero Float: '))
print('O numero lido foi: {} e a sua porção inteira é: {}'.format(n, math.trunc(n)))