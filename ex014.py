print('========== DESAFIO 014 ==========')
print('LEIA A TEMPERATURA EM °C E CONVERTA PARA °F')
c = float(input('Informe a temperatura em °C: '))
f = ((9*c)/5)+32
print('A temperatura {} °C convertida para °F é de {}°F'.format(c, round(f, 2)))
