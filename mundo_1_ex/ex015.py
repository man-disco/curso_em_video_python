from cores import Cores as cr
# Aluguel de carro
preço_dia = 60.00
km = 0.15

dias = int(input('Quantos dias alugados? '))
quilometros = float(input('Quantos quilômetros rodados? '))

calc = (preço_dia * dias) + (quilometros * km)

print(f'O valor total a pagar é R$ {cr.verde + cr.sublinhado}{calc:.2f}{cr.fim}.')