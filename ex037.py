print('========== DESAFIO 037 ==========')
print('LEIA UM NUMERO E CONVERTA-O PARA OCTAL HEXADECIMAL OU BINÁRIO CONFORME ESCOLHA DE UM MENU FIXO')


print('CONVERSOR DE BASES\n')
num = int(input('Inforne um numero inteiro qualquer: '))
print('[ 1 ] BINÁRIO')
print('[ 2 ] HEXADECIMAL')
print('[ 3 ] OCTAL')
ops = int(input('Qual a opção escolhida: '))

if ops == 1:
    print('o numero {} convertido para BINÁRIO é: {}'.format(num, bin(num)))
elif ops == 2:
    print('o numero {} convertido para HEXADECIMAL é: {}'.format(num, hex(num)))
elif ops == 3:
    print('o numero {} convertido para HEXADECIMAL é: {}'.format(num, oct(num)))
