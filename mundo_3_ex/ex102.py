from time import sleep


# Programa que retorna o fatorial de um número
def fatorial(num=1, show=False):
    """
    Essa função retorna o fatorial de um número, com um parámetro opcional que
    mostra o processo de número em número.

    :param num: O valor inteiro que sera fatorado.
    :param show: Valor booleano para definir se os valores serão mostrados.
    :return: Retorna o valor da fatoração.

    Ex: fatorial(10, True) -> 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 3628800
    """
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
        if show:
            print(f'{i}', end=' x ' if i > 1 else f' = ', flush=True)
            sleep(0.2)
    print(fat)


# help(fatorial)
fatorial(10, True)
fatorial(5, show=False)
