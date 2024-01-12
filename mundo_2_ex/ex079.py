# Lista de valores continua
v = []

while True:
	# Cria um loop que solicita números
	n = int(input('Digite um valor> '))
	if n not in v:
		print('\033[32mValor adicionado a lista.\033[m')
		v.append(n)
	else:
		print('\033[33mValor já adicionado! Tente outro!\033[m')
	
	c = input('Deseja continuar? [S/N] ').lower()
	if c == 'n':
		break
	while 's' != c != 'n':
		print('\033[33mErro, escolha uma opção válida\033[m')
		c = input('Deseja continuar? [S/N] ').lower()

print(f'\nA lista de valores inserida foi {v}')
		
