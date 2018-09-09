print('========== DESAFIO 027 ==========')
print('LEIA UM NOME E MOSTRE O PRIMEIRO E O ULTIMO NOME LIDO')

nome = str(input('Digite o seu nome completo: ')).strip()
nome = nome.split()
print('Muito prazer em te conhecer: {} {}'.format(nome[0], nome[len(nome)-1]))