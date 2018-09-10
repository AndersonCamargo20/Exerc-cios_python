print('========== DESAFIO 033 ==========')
print('LEIA UM DETERMINADO QTD DE NUMEROS E DIGA QUAL É O MAIOR OU O MENOR')


qtd = int(input('Qual é a qtd de numeros que você deseja salvar'))
lista = []
for i in range(0, qtd):
    lista.append(float(input('Informe o {}º Numero que deseja add: '.format(i + 1))))


print('MAIOR: {}'.format(max(lista)))
print('MENOR: {}'.format(min(lista)))