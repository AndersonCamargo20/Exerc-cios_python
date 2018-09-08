print('========== DESAFIO 020 ==========')
print('LEIA UM DETERMINADO NRO DE ALUNOS E OS APRESENTE NA ORDEM QUE OS QUAIS IRÃO APRESENTAR OS SEUS TRABALHOS')

from random import shuffle

nro_alunos = int(input('Informe o Nro de alunos que serão lidos: '))
lista_alunos = []

for i in range(0, nro_alunos):
    lista_alunos.append(input('Informe o Nome do {}º aluno: '.format(i + 1)))

shuffle(lista_alunos)
print('Lista de Nomes para a apresentação: \n {}'.format(lista_alunos))
