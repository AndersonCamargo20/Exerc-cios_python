print('========== DESAFIO 007 ==========')
print('FAÇA UM PROGRAMA QUE FAÇA A MÉDIA ARITIMÉTICA ENTRE TRÊS NOTAS\n')

n1 = float(input("Informe a 1º nota: "))
n2 = float(input("Informe a 2º nota: "))
n3 = float(input("Informe a 3º nota: "))

soma = n1 + n2 + n3
media = soma / 3
print("A média das notas ({}, {} , {} ) é: {}".format(n1,n2,n3,media))