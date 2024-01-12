# Detectar a letra "a" numa frase
from cores import Cores as cr

frase = str(input('Digite uma frase: ').lower().strip())
print(frase + '\n')

a = frase.count('a')
f = frase.find('a')
u = frase.rfind('a')

print(f'A letra {cr.negrito}"a"{cr.fim} se repete {cr.cyano + cr.negrito}{a}{cr.fim} vez(es) na frase "{cr.itálico + cr.amarelo}{frase}{cr.fim}".')
print(f'A letra {cr.negrito}"a"{cr.fim} se enconta na posição inicial {cr.azul + cr.negrito}{f + 1}{cr.fim}.')
print(f'A última letra {cr.negrito}"a"{cr.fim} se encontra na posicão final {cr.verde + cr.negrito}{u + 1}{cr.fim}.')