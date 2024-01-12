# Leitura de números
num = soma = total = 0

while True:
    num = int(input('Digite um valor (999 finaliza o programa)> '))
    if num == 999:
        break
    else:
        soma += num
        total += 1

print(f'\nA soma dos {total} valores é igual a {soma}.')

