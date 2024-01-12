from utilidadesCeV import moeda as md

preço = float(input('Valor do produto: R$ '))

print(f"""
O dobro de {md.moeda(preço)} é igual a {md.dobro(preço, True)}
A metade de {md.moeda(preço)} é igual a {md.metade(preço, True)}
Aumentando 50% de {md.moeda(preço)} ficam {md.aumentar(preço, 50, True)}
Diminuindo 30% de {md.moeda(preço)} restam {md.diminuir(preço, 30, True)}
""")
