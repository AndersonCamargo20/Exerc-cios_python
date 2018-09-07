print('========== DESAFIO 013 ==========')
print('LEIA UM SALÁRIO E A PORCENTAGEM DE AUMENTA E CALCULA O VALOR DO SALÁRIO COM AUMENTO')

salario_old = float(input('Informe o salário do funcionário: R$ '))
porcent = float(input('Informe a porcentagem de aumento: '))
aumento = (salario_old * porcent) / 100
salario_new = salario_old + aumento
print('Um funcionário ganhava R${}, mas com {}% de aumento, o seu novo salário é R${}'.format(salario_old, porcent, round(salario_new, 2)))
