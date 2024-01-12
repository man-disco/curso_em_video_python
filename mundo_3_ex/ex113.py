# Crie uma função chamada leiaInt() que valida se o parametro é um inteiro
def leiaInt(string):
    """
    Essa função só retorna o valor se ele for um número inteiro, caso contrário
    ela permanece em um loop toda a vez que um ValueError for acionado.

    :param string: O texto que irá aparecer dentro do input.
    :return: Retorna o valor digitado.
    """
    while True:
        try:
            val = int(input(string))
            return val
            break
        except ValueError:
            print('\033[31mDigite um valor inteiro válido!\033[m\n')
        except KeyboardInterrupt:
            print('\n\033[33mVocê decidiu não inserir este valor.\033[m')
            val = 0
            return val
            break


def leiaFloat(string):
    """
    Essa função só retorna o valor se ele for um número decimal, caso contrário
    ela permanece em um loop toda a vez que um ValueError for acionado.

    :param string: O texto que irá aparecer dentro do input.
    :return: Retorna o valor digitado.
    """
    while True:
        try:
            val = float(input(string))
            return val
            break
        except ValueError:
            print('\033[31mDigite um valor real válido!\033[m\n')
        except KeyboardInterrupt:
            print('\n\033[33mVocê decidiu não inserir este valor.\033[m')
            val = 0
            return val
            break

# help(leiaInt)
a = leiaInt('Digite um valor inteiro: ')
b = leiaFloat('Digite um valor real: ')
print(f'\nVocê digitou o valor inteiro {a} e o valor decimal {b}.')
