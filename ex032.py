print('========== DESAFIO 032 ==========')
print('LEIA UM ANO E DIGA SE ELE É BISEXTO OU NÃO')

from calendar import isleap
from datetime import datetime

now = datetime.now()

ano = int(input('Informe um ano para o calculo (Caso queira o ano atual informe ->> 0 <<-): '))

if ano == 0:
    if isleap(now.year):
        print('O ano atual É BISEXTO')
    else:
        print('O ano atual NÃO é BISEXTO')
else:
    if isleap(ano):
        print('O ano {} É BISEXTO'.format(ano))
    else:
        print('O ano {} NÃO é BISEXTO'.format(ano))
