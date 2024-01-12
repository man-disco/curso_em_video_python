# Progressão Aritmética

n = int(input('Digite o primeiro número da PA: '))
r = int(input('Digite a razão da PA: '))
d = n + (10 - 1) * r

for i in range(n, d + r, r):
    print('{}'.format(i), end=' → ')
print('Acabou :)')