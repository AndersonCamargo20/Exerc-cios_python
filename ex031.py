print('========== DESAFIO 031 ==========')
print('CALCULE O VALOR DA PASSAGEM, COM BASE NA DISTÂNCIA, SABENDO QUE SE FOR MENOS DE 200KM '
      'O VALOR SERÁ 0,50 CASO FOR MAIOR O VALOR DEVERÁ SER 0,45')

dist = float(input('Informe a distância: '))

valor = dist * 0.50 if dist < 200 else dist * 0.45

print('A distância é de: {}Km, com base nessa Kilometragem o valor será de R$ {}'.format(round(dist, 2), round(valor, 2)))

