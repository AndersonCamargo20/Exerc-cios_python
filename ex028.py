print('========== DESAFIO 028 ==========')
print('FAÇA UM JOGO QUE SORTEI UM NUMERO E REPITA O PROCESSO ATÉ O JOGADOR ACERTAR')

from random import randint
from os import system

repeat = True

while repeat == True:
    print('-=-' * 20)
    print('Tente adivinhar o numero que eu pensei!')
    print('-=-' * 20)
    pc = randint(0, 5)
    jg = int(input('Informe um numero entre 0 e 5: '))
    if jg == pc:
        print('VOCÊ GANHOU! PARABÉNS!!')
        repeat = False
    else:
        print('Tente Novamente! MAS DESSA VEZ COM UM NÚMERO DIFERENTE!!')
    system('pause')
    system('cls')