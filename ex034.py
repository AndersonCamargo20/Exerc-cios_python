print('========== DESAFIO 034 ==========')
print('LEIA UM SALÁRIO E FAÇA O CALCULO DO AJUMENTO DE 15% SE FOR MENOR QUE 1250 CASO SUPERIOR AUMENTO DE 10%')

sal = float(input('Informe o salário do funcionário: R$ '))

if sal >= 1250:
    aumento = (sal * 10) / 100
    porcentage = 10
else:
    aumento = (sal * 15) / 100
    porcentage = 15

print('Com aumento de {}% o novo salário será R${}'.format(porcentage, sal + aumento))