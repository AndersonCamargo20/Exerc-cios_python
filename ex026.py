print('========== DESAFIO 026 ==========')
print('Teste qtd de letras A e sua first and last positions')

frase = str(input('Digita algo: ')).strip().lower()
qtd = frase.count('a')
last = frase.rfind('a') + 1


print('A letra ->> A <<- apareceu {} vez(es)'.format(qtd))
print('A 1º posição onde temos a letra ->> A <<- é: {}'.format(frase.find('a') + 1))
print('A ultima posição onde temos a letra ->> A <<- é: {}'.format(frase.rfind('a') + 1))