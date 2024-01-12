# Crie uma lista, organize valores inseridos em ordem decrescente
# e mostre quantas vezes o número 5 aparece na lista
lista = []
num5 = cont = 0
while True:
	cont += 1
	n = int(input('Insira um valor (0 para parar)> '))
		
	if n == 0:
		break
	if n == 5:
		num5 += 1
				
	if cont == 1 or n <= lista[-1]:
		lista.append(n)
	else:
		pos = 0
		while pos < len(lista):
			if n >= lista[pos]:
				lista.insert(pos, n)
				break
			pos += 1
			
print(f'\n{"-"*30}\nA lista em ordem descrescente\n{"-"*30}\n', end=f'\n{str(lista):^30}\n')

if num5 > 0:
	print(f'\nO número 5 apareceu {num5} ', end='vezes na lista.\n' if num5 > 1 else 'vez na lista.\n')
else:
	print('\nO número 5 não apareceu na lista.\n')
