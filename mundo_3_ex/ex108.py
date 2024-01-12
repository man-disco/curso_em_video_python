from utilidadesCeV import moeda as md

preço = float(input('Valor do produto: R$ '))

print(f"""
O dobro de {md.moeda(preço)} é igual a {md.moeda(md.dobro(preço))}
A metade de {md.moeda(preço)} é igual a {md.moeda(md.metade(preço))}
Aumentando 50% de {md.moeda(preço)} ficam {md.moeda(md.aumentar(preço, 50))}
Diminuindo 30% de {md.moeda(preço)} restam {md.moeda(md.diminuir(preço, 30))}
""")
