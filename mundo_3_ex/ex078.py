# Lista de valores númericos
valores = []
print('-' * 22)
maior = menor = 0
for i in range(0, 5):
    valores.append(int(input(f'Digite o {i}º valor> ')))

    # Define o maior e menor valor
    if i == 0:
        maior = menor = valores[0]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if  valores[i] < menor:
            menor = valores[i]
            
print('-' * 22)

print(valores)
print(f'O maior valor foi o {maior} e ele está nas posições ', end='')
for p, val in enumerate(valores):
	if val == maior:
		print(f'{p}..', end='')
print()
print(f'O menor valor foi o {menor} e ele está nas posições ', end='')
for p, val in enumerate(valores):
	if val == menor:
		print(f'{p}..', end='')
print('\n' + '-' * 22)
