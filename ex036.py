print('========== DESAFIO 036 ==========')
print('LEIA O VALOR DE UMA CASA E O SALÁRIO DE UMA PESSOA, CALCULE A '
      'PARCELA com base na qtd de anos que a pessao deseja pagar E VERIFIQUE SE É POSSÍVEL O EMPRÉSTIMO')

casa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe o salario da pessoa que deseja comprar a casa: R$ '))
anos = int(input('Em quantos anos deseja pagar a casa? '))
corte = (salario * 30) / 100
parcela = casa / (anos * 12)
if parcela > corte:
    print('O valor da casa é R$ {}, e o valor da parcela é R$ {}, com base no salário informado:'.format(casa, round(parcela, 2)))
    print('Empréstimo NEGADO')
else:
    print('O valor da casa é R$ {}, e o valor da parcela é R$ {}, com base no salário informado:'.format(casa, round(parcela, 2)))
    print('Empréstimo CONCEDIDO')
