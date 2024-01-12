from cores import Cores as cr
# 5% de desconto
preço = float(input('Digite o valor do produto: '))
des = 5
conta = (preço * 5 / 100) 
final = preço - conta

print(f'O valor final do produto de R$ {cr.verde}{preço:.2f}{cr.fim} com {cr.cyano}{des}{cr.fim}% de desconto fica em R$ {cr.sublinhado + cr.vermelho}{final:.2f}{cr.fim}.')
