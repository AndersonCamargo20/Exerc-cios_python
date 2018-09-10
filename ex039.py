print('========== DESAFIO 039 ==========')
print('LEIA O ANO DE NASCIMENTO DE UMA PESSOA E DIGA SE ELE '
      'DEVE SE ALISTAR CASO NEGATIVO MOSTRE QUANTOS ANOS FALTAM E DIGA QUAL ANO SERÁ')

from datetime import datetime

ano = int(input('Ano de nascimento: '))
idade = datetime.now().year - ano

if idade >= 18:
    print('você possui {} anos, o alistamento deve ser feito!'.format(idade))
else:
    diferenca = 18 - idade
    print('Você possui {} anos, o alistamento ainda não precisa ser feito!'.format(idade))
    print('O mesmo deverá ser feito daqui {} ano(s)'.format(diferenca))
    print('no de ano de {}'.format(datetime.now().year + diferenca))
