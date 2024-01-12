# Criando triângulos (denovo)

print('\033[1;35m-\033[33m=\033[m' * 14 + '\n\033[3;32mAnalisador de triângulos 2.0\033[m\n' + '\033[1;33m=\033[35m-\033[m' * 14)

try:

    ret1 = float(input('\nDigite o valor da primeira reta:\033[35m '))
    ret2 = float(input('\033[mDigite o valor da segunda reta:\033[33m '))
    ret3 = float(input('\033[mDigite o valor da terceira reta:\033[32m '))

    if ret1 < ret2 + ret3 and ret2 < ret1 + ret3 and ret3 < ret1 + ret2:

        # Triângulo escaleno - Todos os lados tem tamanhos diferentes
        if ret1 != ret2 != ret3 != ret1:
            print('\n\033[mAs retas acima formam um triângulo escaleno.')
        # Triângulo equilátero - Todos os lados tem tamanhos iguais
        elif ret1 == ret2 == ret3:
            print('\n\033[mAs retas acima formam um triângulo equilátero.')
        # Triângulo isósceles - Dois dos lados tem tamanhos iguais (congruentes)
        else:   
            print('\n\033[mAs retas acima formam um triângulo isósceles.')
            
    else:
        print(f'\n\033[1;31mAs retas acima NÃO um formam triângulo.\033[m')

except ValueError:
    print('\n\033[31mErro, digite apenas números.\033[m')