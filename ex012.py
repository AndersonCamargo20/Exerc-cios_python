print('========== DESAFIO 012 ==========')
print('LEIA O VALOR DE UM PRODUTO E INFORME O VALOR FINAL COM DESCONTO APÓS LER A PORCENTAGEM')

valor = float(input('Informe o valor do produto: R$ '))
porcent = float(input('Informe o valor da porcentagem: '))
desconto = (valor * porcent) / 100
print('O produto custava R${}, na promoção com desconto de {}%, vai custar R${}'.format(valor, porcent, round(valor-desconto,2)))
