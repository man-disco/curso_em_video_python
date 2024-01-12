# Tabuada (Refeita com loop)
print('\n\033[1;37mTabuada Python\033[m\n')
n = int(input('Digite o número da tabúada: '))

for i in range(1,11):
    t = n * i
    print('.' * 13)
    print('{} x {} = {}'.format(n, i, t))
