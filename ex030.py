print('========== DESAFIO 030 ==========')
print('LEIA UM NUMERO E DIGA SE ELE É PAR OU ÍMPAR')

num = float(input('Informe um numero: '))

if num %2 == 0:
    print('O numero {} é PAR'.format(num))
else:
    print('o numero {} é ÍMPAR'.format(num))