# Definindo posições em uma lista de até 5 numeros
lista1 = []
lista2 = []

for i in range(5):
	n = int(input('Digite um valor: '))
	lista2.append(n)
	# O primeiro valor vai pro final
	if i == 0 or n > lista1[-1]:
	    lista1.append(n)
	    print('Adicionado ao final da lista.\n')
	else:
		p = 0
		while p < len(lista1):
			if n <= lista1[p]:
				lista1.insert(p, n)
				print(f'Adicionado na posição -> {p}\n')
				break
			p += 1
			
print(f'\nA lista inserida foi;\n{lista2}\n')
print(f'\nA lista em ordem fica;\n{lista1}\n')
