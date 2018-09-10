print('========== DESAFIO 042 ==========')
print('CONTINUAÇÃO DO DESAFIO 035')


r1 = float(input('Valor do 1º segmento: '))
r2 = float(input('Valor do 2º segmento: '))
r3 = float(input('Valor do 3º segmento: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
    print('Os segmentos PODEM ser um TRIÂNGULO')
else:
    print('Os segmentos NÃO PODEM ser um triângulo')