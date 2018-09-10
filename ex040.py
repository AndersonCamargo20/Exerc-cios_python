print('========== DESAFIO 040 ==========')
print('LEIA DUAS NOTAS E TRAGA COMO RESULTADO SE O ALUNOS ESTÁ APROVADO, REPORVADO OU EM RECUPERAÇÃO')


n1 = float(input('1º nota: '))
n2 = float(input('2º nota: '))

media = (n1 + n2) / 2

print('Tirando {} e {} a média é: {}'.format(n1, n2, media))

if 7 > media >= 5:
    print('Aluno está em RECUPERAÇÃO!')
elif media < 5:
    print('Aluno está REPROVADO')
else:
    print('Alunos está APROVADO')