# Tabuada em loop
num = 1
while num >= 1:
    print('-' * 13 if num < 100 else '-' * 15)
    num = int(input('Digite o número da tabuada: '))
    print('-' * 13 if num < 100 else '-' * 15)
    tab = 10

    while tab > 0:
        if num < 0:
            print('\nFechando programa...')
            break
        else:
            print(f'{tab} x {num} = {tab * num}')
            tab -= 1
