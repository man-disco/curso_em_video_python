# Maior de idade ou não
from datetime import date

# Número de pessoas menores de idade
p_menores_de_idade = 0

# Número de pessoas maiores de idade
p_maiores_de_idade = 0

# Número de pessoas mortas
p_mortas = 0



try:
	print('\n\033[1m>>> Analisador de idades <<<\033[m')
	ano_atual = date.today().year

	for i in range(1, 8):
		n = int(input('\n\033[1;33m{}\033[m - Digite um ano de nascimento: '.format(i)))

		if 120 > ano_atual - n >= 21:
			print('Essa pessoa é maior de idade e tem {} anos\n'.format(ano_atual - n))
			p_maiores_de_idade += 1
            	
		elif ano_atual - n > 120:
			print('Essa pessoa já morreu :(\n')
			p_mortas += 1
            
		elif n > ano_atual or n == ano_atual + 1:
			print('Essa pessoa não existe :P\n')
			pass
			
		else: 
			print('Essa pessoa é menor de idade e tem {} anos\n'.format(ano_atual- n))
			p_menores_de_idade += 1
    
	if p_maiores_de_idade > 0:
		print('Houveram {} pessoas maiores de idade.'.format(p_maiores_de_idade))
    
	if p_menores_de_idade > 0:
		print('Houveram {} pessoas menores de idade.'.format(p_menores_de_idade))

	if p_mortas > 0:
		print('Houveram {} pessoas mortas.'.format(p_mortas))

except ValueError:
    print('\n\033[1;31mValor inválido, tente novamente.\033[m\n')
