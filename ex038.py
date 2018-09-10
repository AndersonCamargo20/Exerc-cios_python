print('========== DESAFIO 038 ==========')
print('FAÇA UM PROGRAMA QUE COMPARE DOIS NUMEROS E DIGA QUAL É O MAIOR E CASO SEJAM IGUAIS QUE INFORME TAMBÉM')

n1 = float(input('Informe o 1º valor: '))
n2 = float(input('Informe o 2º valor: '))

if n1 != n2:
    if n1 > n2:
        print('O primeiro valor é MAIOR')
    elif n2 > n1:
        print('o segundo valor é MAIOR')
else:
    print('Os dois são iguais')