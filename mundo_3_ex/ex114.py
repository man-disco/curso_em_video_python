from time import sleep
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
# Crie um programa que teste a disponibilidade de um site
# Ex: https://pudim.com.br


def checkStatus(string='Digite um site: '):
    """
    Esta função faz uma solicitação a um endereço de site e retorna o seu status.

    :param string: Texto que aparecerá na função input, onde ele digitará o site
    :return: Retorna o status da página, conforme exceções abaixo
    """
    url = str(input(string).strip())
    req = Request(f'https://{url}')
    try:
        resp = urlopen(req)
    except HTTPError as error:
        if error.code == 404:
            return f'\033[33m{error.code} Pagina não encontrada\033[m'
        if error.code == 403:
            return f'\033[31m{error.code} Acesso negado - {error.reason}\033[m'
    except URLError as error:
        return f'\033[31mO site https://www.{url} não existe :(\033[m'
    else:
        return f'\033[32m{resp.code} - O site {url} está acessível.\033[m'


print(checkStatus())
