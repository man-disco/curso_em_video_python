# Módulos

def dobro(valor=0, f=False):
    """
    Retorna o dobro do valor passado.

    :param valor: Valor inteiro ou flutuante
    :param f: Booleano que define se o valor será formatado pela função moeda()
    """
    return moeda(valor * 2) if f else valor * 2


def metade(valor=0, f=False):
    """
    Retorna a metade do valor passado.

    :param valor: Valor inteiro ou flutuante
    :param f: Booleano que define se o valor será formatado pela função moeda()
    """
    
    return moeda(valor / 2) if f else valor / 2


def aumentar(valor=0, per=15, f=False):
    """
    Retorna o percentual do valor somado a ele mesmo.

    :param valor: Valor inteiro ou flutuante
    :param per: Percentual do valor a ser calculado
    :param f: Booleano que define se o valor será formatado pela função moeda()
    """
    per *= valor / 100
    return moeda(valor + per) if f else valor + per


def diminuir(valor=0, per=10, f=False):
    """
    Retorna o percentual do valor subtraido a ele mesmo.

    :param valor: Valor inteiro ou flutuante
    :param per: Percentual do valor a ser calculado
    :param f: Booleano que define se o valor será formatado pela função moeda()
    """
    per *= valor / 100
    return moeda(valor - per) if f else valor - per


def moeda(valor=0, moeda='R$'):
    """
    Retorna o valor formatado com a moeda definida, com duas casas decimais.

    :param valor: Valor que será formatado pela função
    """
    return f'{moeda} {valor:.2f}'.replace('.', ',')


def resumo(valor, aum, red):
    """
    """
    print(f"""
{'-'*30}
{"Resumo do Valor":^30}
{'-'*30}
{"Preço analisado":<20} {moeda(valor)}
{"Dobro do preço":<20} {dobro(valor, True)}
{"Metade do preço:":<20} {metade(valor, True)}
{f"{aum}% de aumento:":<20} {aumentar(valor, aum, True)}
{f"{red}% de redução:":<20} {diminuir(valor, red, True)}
{'-'*30}
""")
