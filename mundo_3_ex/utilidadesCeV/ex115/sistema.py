from os import system, name
from . import interface
from time import sleep

def cadastrar():
    """
    Cadastra uma nova pessoa no arquivo de texto.
    """
    with open('pessoas.txt', 'at', encoding='utf-8') as file:
        while True:
            try:
                nome = str(input('\nNome: ').strip())
                if nome.isnumeric():
                    raise ValueError
            except ValueError:
                interface.mensagem('Digite um nome válido!\n')
            else:
                break
        while True:
            try:
                idade = int(input('Idade: '))
            except ValueError:
                interface.mensagem('Digite uma idade válida!\n')
            else:
                file.write(f'\n{nome.title():.<25} {idade}')
                system(limpa(name))
                interface.mensagem('Pessoa cadastrada.', 20, False)
                break
                file.close()

            
            

def visualizar():
    """
    Visualiza as pessoas cadastradas no arquivo de texto, linha por linha.
    """
    try:
        with open('pessoas.txt', 'rt', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                print(f'{line.strip()}')
    except FileNotFoundError:
        cria()
    else:
        sleep(2)
        file.close()
        system(limpa(name))

def ajuda(indice=None, lista=None):
    # Consertar isso ou sla, n tá no exercicio
    interface.titulo('Ajuda')
    pass


def limpa(os):
    """
    Limpa a tela do terminal usando o modulo os

    :param os: Sistema operacional que o usuário está utilizando que irá
    definir o comando adequado de limpar a tela
    """
    if os == 'posix':
        return 'clear'
    else:
        return 'cls'

def cria(nome='pessoas'):
    """
    lol
    """
    interface.mensagem('Arquivo principal não encontrado, criando arquivo...')
    sleep(1)
    try:
        f = open(f'{nome}.txt', 'wt+', encoding='utf-8')
    except Exception as error:
        print(error)
    else:
        system(limpa(name))
        f.close()
    interface.mensagem('Arquivo criado com sucesso.', 15, False)
