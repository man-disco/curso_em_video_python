# Sequência de Fibonacci
n1 = 0
n2 = 1
cont = 1
soma = 0

print('Sequencia de Fibonnaci')
print('-' * 22)

n = int(input('\nPrimeiro termo da sequência: '))
f = int(input('Mostrar quantos termos? '))
print()

while cont <= f:
    if n > n2:
        n2 = n
    n3 = n1 + n2
    print(n1, end=' → ')
    n1 = n2
    n2 = n3
    cont += 1

print('Fim da sequência :)')
