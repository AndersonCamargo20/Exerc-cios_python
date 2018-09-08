print ( '========== DESAFIO 018 ==========' )
print('ATRAVÉS DA LEITURA DO ÂNGULO CALCULE O SENO, COSSENO E A TANGENTE')

from math import radians, cos, sin, tan
angulo = float(input('Informe o Ângulo para o cálculo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo de {} tem o SENO de {} e o COSSENO de {}, que por sua vez gera a TANGENTE de {} !'.format(angulo, round(sen, 2), round(cos, 2), round(tangente, 2)))