from utilidadesCeV import moeda as md

preço = float(input('Valor do produto: R$ '))

print(f"""
O dobro de R$ {preço:.2f} é igual a R$ {md.dobro(preço):.2f}
A metade de R$ {preço:.2f} é igual a R$ {md.metade(preço):.2f}
Aumentando 50% do valor R$ {preço:.2f} ficam R$ {md.aumentar(preço, 50):.2f}
Diminuindo 30% do valor R$ {preço:.2f} restam R$ {md.diminuir(preço, 30):.2f}
""")
