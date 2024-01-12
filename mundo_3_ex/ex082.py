# Lista par e impar
lista = []
lista_par = []
lista_impar = []
cont = 0

while True:
	num = int(input('Digite um valor (0 para parar)> '))
	if num == 0:
		print('Saindo...\n')
		break
	cont += 1
	if cont == 1 or num <= lista[-1]:
		lista.append(num)
		if num % 2 == 0:
			lista_par.append(num)
		else:
			lista_impar.append(num)
	else:
		pos = 0
		while pos < len(lista):
			if num >= lista[pos]:
				lista.insert(pos, num)
				if num % 2 == 0:
					lista_par.insert(pos, num)
				else:
					lista_impar.insert(pos, num)
				break
			pos += 1
print('A lista inserida foi ', end=f'\n{lista}\n')
print('A lista par foi ', end=f'\n{lista_par}\n')
print('A lista ímpar foi ', end=f'\n{lista_impar}\n')
