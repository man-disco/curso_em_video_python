# Progressão Aritmética 2.0
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
f = int(input('Até quantos termos? '))
c = 1

bar = (n + 3) * f + (f // r + 10 + r)
print('=' * bar)
while c <= f:
    print('{}'.format(n), end=' → ')
    n += r
    c += 1
print('Acabou :)')
print('=' * bar)