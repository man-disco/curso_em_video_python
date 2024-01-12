# Fatorial
fat = 1

num = int(input('Digite um número inteiro: '))
print('\n{}!'.format(num), end=' = ')

# Com for loop
# for n in range(num, 0, -1):
#     if n > 1:
#         print(n, end=' x ')
#     else:
#         print(n, end=' = ')
#     fat *= n

# com while loop
while num > 0:
    print(num, 'x ' if num > 1 else '= ', end='')
    fat *= num
    num -= 1

print('{}{}'.format('', fat))