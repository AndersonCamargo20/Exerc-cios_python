print('========== DESAFIO 022 ==========')
print('LEIA UM NOME E MOSTRE-O E UPPER EM LOWER O NRO DE LETRAS DO 1º NOME E O NRO TOTAL DE LETRAS')

nome = str(input('Informe um Nome: ')).strip()
print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('Tamanho total de letras desconsiderando os espaços:  {} Letras'.format(len(nome) - nome.count(' ')))
split_str = nome.split()
print('O seu primeiro nome é: {} e tem {} Letras'.format(split_str[0], len(split_str[0])))
