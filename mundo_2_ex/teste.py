galera = list()
dado = list()
mai = men = 0
for i in range(3):
	dado.append(str(input('Nome: ')))
	dado.append(int(input('Idade: ')))
	galera.append(dado[:])
	dado.clear()
	
for pessoa in galera:
	if pessoa[1] >= 21:
		print(f'{pessoa[0]} é maiuor de idade.')
		mai += 1
	else:
		print(f'{pessoa[0]} é menor de idade.')
		men += 1

print(f'Existem {mai} maiores de idade e {men} menores de idade.')
	
