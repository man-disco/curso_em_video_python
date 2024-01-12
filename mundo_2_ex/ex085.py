# Lista par e impar dentro de outra lista
numeros = list()
lpar = []
limpar = []
c = 0
while c < 7:
    numero = int(input(f'Digite o {c + 1}º valor> '))
    if numero % 2 == 0:
        lpar.append(numero)
    else:
        limpar.append(numero)
    c += 1
lpar.sort()
limpar.sort()

numeros.append(lpar)
numeros.append(limpar)

print(numeros)
