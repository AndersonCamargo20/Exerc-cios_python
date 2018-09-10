print('========== DESAFIO 029 ==========')
print('LEIA A VELOCIDADE UM CARRO E CALCULE O VALOR DA MULTA')

vl = float(input('Informe a velocidade do carro: '))
if vl > 80:
    print('MULTADA! Você excedeu a velocidade mínima de 80Km/h, e o valor da sual multa é: R$ {}'.format((vl - 80) * 7))
else:
    print('Tenha uma boa Viagem! Está tudo OK!')