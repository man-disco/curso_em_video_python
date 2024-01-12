# Indice de massa corpórea
print(36 * '-' + "\n" f'{"Medidor de IMC":^36}' + "\033[m\n" + 36 * '-')

def printar_tabela_imc(imc):
    """Função responsável por printar uma tabela destacando o imc do usuário"""

    i1 = ""
    i2 = ""
    i3 = ""
    i4 = ""
    i5 = ""

    if imc < 18.5:
        i1 = "\033[1;37m"
    elif 18.5 <= imc <= 24.9:
        i2 = "\033[1;37m"
    elif 24.9 >= imc <= 30:
        i3 = "\033[1;37m"
    elif 30 >= imc < 36:
        i4 = "\033[1;37m"
    else:
        i5 = "\033[1;37m"

    print(36 * '-')
    print('IMC\t\tClassificação')
    print(36 * '-')
    print(f'{i1}Até 18,5\tPeso abaixo do ideal\033[m')
    print(36 * '-')
    print(f'{i2}De 18,5 até 25\tPeso ideal\033[m')
    print(36 * '-')
    print(f'{i3}De 25 até 30\tAcima do peso ideal\033[m')
    print(36 * '-')
    print(f'{i4}De 30 até 36\tObesidade\033[m')
    print(36 * '-')
    print(f'{i5}Acima de 36\tObesidade mórbida\033[m')
    print(36 * '-')

try:

    peso = float(input('\nDigite o seu peso: '))
    altura = float(input('Digite sua altura: '))

    # Verifica se a  altura esta em número decimal, se não reporta erro
    if altura == int(altura):
        print('\n\033[1;31m[Erro] Digite a altura em metros (ex: 1.67).\033[m\n')
        exit()

    else:
        # Calcula o imc - Peso x altura²
        imc = peso / ((altura) ** 2)
        print(f'\nSeu IMC é igual a \033[1;37m{imc:.2f}kg/m2.\n\033[m')
        printar_tabela_imc(imc)


except ValueError:
    print('\n\033[1;31m[Erro] Use apenas valores númericos.\033[m\n')