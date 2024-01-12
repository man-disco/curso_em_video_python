# Programa de operações
maior_num = 0
escolha = 0

print('========(Sistema)=======')
try:   
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite outro valor: '))
    
except ValueError:
    print('\n\033[31mErro, digite números válidos\033[m\n')
    exit()

while escolha != 5:
    print('=' * 9 + f'({num1}, {num2})' + "=" * 9)
    print('[1] Somar Valores\n'
        '[2] Multiplicar Valores\n'
        '[3] Maior Número\n'
        '[4] Adicionar números\n'
        '[5] Sair do programa\n')
    escolha = int(input('Comando ==> '))

    if escolha == 1:
        soma = num1 + num2
        print('\n{} + {} = {}'.format(num1, num2, soma))
    elif escolha == 2:
        mult = num1 * num2
        print('\n{} x {} = {}'.format(num1, num2, mult))
    elif escolha == 3:
        # Define o maior número e avisa se são iguais
        if num1 != num2:
            if num1 > num2:
                maior_num = num1
            else:
                maior_num = num2
            print('\nO maior número é o {}'.format(maior_num))
        else:
            print('\nAmbos números são iguais a {}'.format(num1))
    elif escolha == 4:
        print('Digite novos valores:\n')
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
    elif escolha == 5:
        print('\nObrigado por utilizar este programa <3\n')
        break
        exit()
    else:
        print('\n\033[1;31mDigite uma opção válida!\033[m')

    