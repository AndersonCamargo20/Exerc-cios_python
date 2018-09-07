print('========== DESAFIO 015 ==========')
print('FAÇA UM PROGRAMA QUE LEIA O NRO DE DIAS QUE UM CARRO FICOU ALUGADO E A QTD DE KM RODADO'
      'SANDO QUE CADA DIA CUSTA R$ 60,00 E CADA KM RODADO CUSTA R$ 0,15 CALCULE E MOSTRE O VALOR')

dias = int(input('Informe a qrd de dias em que o carrro ficou alugado: '))
km = float(input('Qual é a qtd de km rodados durante a viagem: '))
valor = (km*0.15) + (dias *60)
print('O valor total do alguel com base nas informações enviadas é: R$ {}'.format(round(valor, 2)))
