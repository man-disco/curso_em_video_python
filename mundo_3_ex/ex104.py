# Crie uma função chamada leiaInt() que valida se o parametro é um inteiro
def leiaInt(string):
    """
    Essa função só retorna o valor se ele for um número inteiro, caso contrário
    ela permanece em um loop toda a vez que um ValueError for acionado.

    :param string: O texto que irá aparecer dentro do input.
    :return: Retorna o valor digitado.
    """
    while True:
        val = input(string)
        if val.isnumeric():
            return val
            break
        else:
            print('\033[31mDigite um valor inteiro válido!\033[m\n')


# help(leiaInt)
a = leiaInt('Digite um valor: ')
print(f'Você digitou o valor {a}.')
