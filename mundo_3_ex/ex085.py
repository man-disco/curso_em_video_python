# Lista par e impar dentro de outra lista
numeros = [[],[]]
c = 0
while c < 7:
    numero = int(input(f'Digite o {c + 1}º valor> '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
    c += 1
numeros[0].sort()
numeros[1].sort()
print(f'\nNúmeros pares: {numeros[0]}\nNúmeros ímpares: {numeros[1]}\n')
