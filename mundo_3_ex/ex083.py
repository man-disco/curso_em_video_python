# Analisador de expressões
operadores = ('+','-','*','/', '^')
parenteses_aberto = parenteses_fechado = 0

while True:
	expr = str(input('Digite uma expressão> ')).strip()
	if expr == 'pare':
		break
	for char in expr:
		# Checa se o caractere é um parenteses aberto
		if char == '(':
			parenteses_aberto += 1
		# Checa se o caractere é um parenteses fechado
		elif char == ')':
			parenteses_fechado += 1
		# Checa se o caractere é um número
print('p', parenteses_aberto, parenteses_fechado)
if parenteses_aberto == parenteses_fechado:
	print('Essa expressão é valida')
else:
	print('Essa expressão é invalida')
