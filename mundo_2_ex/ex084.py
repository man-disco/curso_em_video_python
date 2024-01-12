# Lista de dados de pessoas
pessoas_cad = []
pessoa = []
pessoas_pesadas = []
pessoas_leves = []
maior_peso = menor_peso = 0
while True:
	# Nome da pessoa
	pessoa.append(str(input('Nome: ')))
	# Peso da pessoa
	pessoa.append(float(input('Peso: ')))

	# Adiciona uma cópia da pessoa com os dados a lista principal
	pessoas_cad.append(pessoa[:])

	# Define menor e maior peso
	if len(pessoas_cad) == 1:
		maior_peso = menor_peso = pessoa[1]
		pessoas_pesadas.append(pessoa[:])
		pessoas_leves.append(pessoa[:])
		
	else:
		if pessoa[1] >= maior_peso:
			pessoas_pesadas.append(pessoa[:])
			maior_peso = pessoa[1]
			
		if pessoa[1] <= menor_peso:
			pessoas_leves.append(pessoa[:])
			menor_peso = pessoa[1]
			
	# Limpa os dados para adicionar a proxima pessoa no loop
	pessoa.clear()
	
	# Pergunta ao usuário se ele deseja continuar
	cont = str(input('Deseja continuar? [S/n] ')).lower()
	if 's' == cont == '':
		continue
	if cont == 'n':
		break
	while 's' != cont != 'n':
		print('erro')
		cont = str(input('Deseja continuar? [s/n] ')).lower().strip()
		 
print(f'\n{"-"*35}\nForam cadastradas {len(pessoas_cad)} pessoas.'
f'\n{"-"*35}' if len(pessoas_cad) > 1 else 
f'\n{"-"*35}\nApenas uma pessoa foi cadastrada.\n{"-"*35}')
print(f'\nO maior peso foi o {maior_peso:.2f} kg das pessoas '
if len(pessoas_pesadas) > 1 and pessoas_pesadas[-1][1] == maior_peso

else f'\nO maior peso foi o {maior_peso:.2f} kg da pessoa ', end='')
for pessoa in pessoas_pesadas:
	if pessoa[1] == maior_peso:
		print(f'{pessoa[0].capitalize()}', end=', '
		if pessoa != pessoas_pesadas[-1] else '.')

print(f'\nO menor peso foi o {menor_peso:.2f} kg das pessoas '
if len(pessoas_leves) > 1 else 
f'\nO maior peso foi o {menor_peso:.2f} kg da pessoa ', end='')

for pessoa in pessoas_leves:
	if pessoa[1] == menor_peso:
		print(f'{pessoa[0].capitalize()}', end=', '
		if pessoa != pessoas_leves[-1] else '.\n')

