# Matriz 3x3
mat = []
col = []
num_col = soma_par = soma_col_1 = 0
while len(mat) < 3:
	while len(col) < 3:
		col.append(int(input(f'coord {len(col)}, {num_col} ')))
	num_col += 1
	mat.append(col[:])
	col.clear()

print('\nMatriz Gerada:\n   0  1  2')
for pos, lin in enumerate(mat):
	print(pos, end=' ')
	for num in lin:
			print(f'[{num}]', end='' if num != lin[-1]
			or num == lin[0]  else '\n')
