from datetime import datetime
ano_atual = datetime.today().year
# Sistema de votos com funções e return


def voto(nascimento):
    """
    Esta função informa com base no ano de nascimento de uma pessoa
    a sua situação de voto:

    :param nascimento: Ano de nascimento da pessoa.
    :return situação:
        "NEGADO"        - A pessoa não tem idade suficiente para votar.
        "OPCIONAL"      - A pessoa tem idade (16 até 18) onde o voto é opcional.
        "OBRIGATORIO"   - A pessoa está na idade ( > 18 ou > 70 anos) onde é
                          obrigatório o voto.
    """
    idade = ano_atual - nascimento
    if idade < 16:
        situação = "NEGADO"
    elif idade <= 16 or idade >= 65:
        situação = "OPCIONAL"
    else:
        situação = "OBRIGATÒRIO"
    return idade, situação


help(voto)
data = int(input('Em qual ano você nasceu?: '))
print(f'Com {voto(data)[0]} anos o voto é {voto(data)[1]}.'
      if voto(data)[1] != "NEGADO" else f'Com {voto(data)[0]} anos NÃO VOTA.')
