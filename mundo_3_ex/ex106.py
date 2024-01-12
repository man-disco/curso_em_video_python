from cores import Cores as cr
from time import sleep
# Sistema de comandos que usa o help() do python


def helpMe():
    while True:
        cmd = input('Comando> ').strip().lower()
        if cmd == 'sair':
            break
        print(f'{cr.f_azul + cr.negrito}', end='')
        print(f"""
{"-"*80}
{f"Buscando o comando {cmd} banco de dados... ":^80}
{"-"*80}{cr.fim}
        """)
        sleep(0.3)
        help(cmd)


helpMe()
