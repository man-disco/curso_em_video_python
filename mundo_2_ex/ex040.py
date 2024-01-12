# Média de notas (denovo)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
print(f'Sua média foi {media}')
if media < 5.0:
    print('\nVocê foi reprovado.')
elif 5.0 >= media <= 6.9:
    print('\nVocê está de recuperação.')
else:
    print('\nVocê foi aprovado.')