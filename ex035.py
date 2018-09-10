print('========== DESAFIO 035 ==========')
print('LEIA OS VALORES DOS 3 SEGMENTOS DE UM TRIÂNGULO E DIGA SE ESSES VALORES PODERIAM SER UM TRIÂNGULO VÁLIDO')

r1 = float(input('Valor do 1º segmento: '))
r2 = float(input('Valor do 2º segmento: '))
r3 = float(input('Valor do 3º segmento: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
    print('Os segmentos PODEM ser um TRIÂNGULO')
else:
    print('Os segmentos NÃO PODEM ser um triângulo')