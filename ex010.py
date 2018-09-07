print('========== DESAFIO 010 ==========')
print('LEIA UM VALOR EM REAIS E REALIZE A CONVERSÕA PARA DÓLARES\n')

n = float(input('Quanto reais você tem na carteira? R$ '))
dol = 4.15
print('Com R$ {} você pode comprar $ {}'.format(n,round(n/dol,2)))
