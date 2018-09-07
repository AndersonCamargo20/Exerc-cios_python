print('========== DESAFIO 011 ==========')
print('LEIA A LARGURA E A ALTURA DE UMA PAREDE E CALCULE A SUA ÁREA BEM COMO QUANTOS LITROS DE TINTA SERIA '
      'NECESSÁRIO PARA PINTÁ-LA SABENDO QUE PARA QUE 2m DE ÁREA SÃO NECESSÁRIOS 1L DE TINTA\n')

larg = float(input('Informa a Largura: '))
alt = float(input('Informe a Altura: '))
area = larg * alt
tinta = area / 2

print('Sua parede tem a dimensão de {}X{} e sua área é {}m².'.format(larg, altx, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))
