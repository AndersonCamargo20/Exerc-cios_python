print('========== DESAFIO 041 ==========')
print('LEIA O ANO DE NASCIMENTO DE UM ATLETA E DIGA QUAL É SUA CATEGORIA COM BASE NA SUA IDADE')

from datetime import datetime


now = datetime.now().year

ano = int(input('Qual o ano de nascimento do atleta? '))
idade = now - ano

if idade <= 9:
    classe = 'MIRIM'
elif 9 < idade <= 14:
    classe = 'INFANTIL'
elif 14 < idade <= 19:
    classe = 'JÚNIOR'
elif 19 < idade <= 25:
    classe = 'SÊNIOR'
else:
    classe = 'MASTER'

print('O atleta possui {} ano(s) e sua classe é: {}'.format(idade, classe))