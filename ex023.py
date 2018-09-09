print('========== DESAFIO 023 ==========')
print('Leia um numero inteiro e mostre separadamente a sua UND, DEZENA, CENTENA E OU MILHAR')

num = int(input('Informe um numero inteiro:'))
und = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print('UNIDADE: {}'.format(und))
print('DEZENA: {}'.format(dezena))
print('CENTENA: {}'.format(centena))
print('MILHAR: {}'.format(milhar))
