# Conversor de base númerica

print('\n\033[m---@ Conversor de base númerica @---\033[m\n')
print(f'\033[4mEscolha uma das opções abaixo;\033[m\n'
'\n[1] - De número para binário.'
'\n[2] - De número para octal.'
'\n[3] - De número para hexadecimal.\n'
)

try:
    choice = int(input('> '))
    if choice == 1:
        num = int(input('Digite o número a ser convertido: '))
        binary = format(num, "b")
        print(f'\nO número {num} resulta no valor binário {binary}.')

    elif choice == 2:
        num = int(input('Digite o número a ser convertido: '))
        octal = format(num, "0o")
        print(f'\nO número {num} resulta no valor octal {octal}.')


    elif choice == 3:
        num = int(input('Digite o número a ser convertido: '))
        hexadecimal = format(num, "0x")
        print(f'\nO número {num} resulta no valor hexadecimal {hexadecimal}.')

    else:
        print('\033[1;31m[ERRO]\033[m\033[33m Opção Inválida.\033[m')

except ValueError:
    print('\033[1;31m[ERRO]\033[m \033[33mTente novamente somente com números inteiros.\033[m')
