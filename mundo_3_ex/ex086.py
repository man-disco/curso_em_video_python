# Matriz 3x3
mat = []
col = []
num_col = 0
while len(mat) < 3:
    while len(col) < 3:
        col.append(int(input(f'coord {len(col)}, {num_col} ')))
    num_col += 1
    mat.append(col[:])
    col.clear()

print(f'\n\033[1m{"Matriz Gerada:":^25}'
       '\033[m\n\n     0      1      2', end='')
for pos, lin in enumerate(mat):
    print(f'\n', end=f'{pos} ')
    for num in lin:
        print(f'[{num:^5}]', end='')
