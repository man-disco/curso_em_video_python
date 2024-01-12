from cores import Cores as cr
# Calcular gasto de tinta de uma parede
a = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))

m2 = a * l 
litro_tinta = m2 / 2

print(f'\nSua parede medindo {cr.verde}{a:.2f}{cr.fim}x{cr.azul}{l:.2f}{cr.fim}{cr.negrito}m²{cr.fim} tem uma área de {cr.vermelho}{m2:.2f}{cr.fim}{cr.negrito}m²{cr.fim}\n'
f'\nSerão necessários {cr.cyano}{litro_tinta:.2f}{cr.fim} litros de tinta para pintá-la.')