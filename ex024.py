print('========== DESAFIO 024 ==========')
print('FAÇA UM PROGRAMA QUE TESTE UMA CIDADE E VERIFIQUE SE O NOME DACIDADE COMEÇA COM --> SANTO <--')

cidade = str(input('Em que cidade você nasceu? ')).strip().lower()

lista = cidade.split()

print(lista[0] == 'santa')



