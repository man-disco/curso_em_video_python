def leiaDinheiro(msg):
    """
    Esta função sanitiza o input do usuário, para que apenas um valor monetário
    seja retornado.

    :param msg: A mensagem de input que aparecerá pro usuário
    :return: Retorna um valor monetário válido
    """
    while True:
        try:
            valor = input(msg)
            # Transforma qualquer virgula em um ponto para evitar erros
            valor = valor.replace(',', '.')
            return float(valor)
        except ValueError:
            print(f'\033[1;31mO valor \033[33m"{valor}"\033[31m é não númerico, tente novamente!\033[m')
