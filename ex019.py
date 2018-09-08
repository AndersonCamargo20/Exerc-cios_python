print('========== DESAFIO 019 ==========')
print('LENDO O NOME DE 4 ALUNOS SORTEI UM DELES DA CHAMADA PARA APAGAR O QUADRO')

import random
list_alunos = []

num_alunos = int(input('Quantos alunos deseja salvar: '))

random = random.randint(0,num_alunos - 1)
print(random)

for i in range(0, num_alunos):
    list_alunos.append(input('Informe o nome do {}º Aluno: '.format(i + 1)))

print('\n\nO aluno escolhido foi {}.'.format(list_alunos[random]))
