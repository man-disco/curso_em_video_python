# Soma entre números ímpares múltiplos de 3
r = 0
s = 0

for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        r += 1

print('A soma dos {} valores é igual a {}.'.format(r, s))
