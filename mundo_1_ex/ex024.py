# Detecte "SANTOS" em um nome de cidade
from cores import Cores as cr

cidade = str(input('Digite um nome de uma cidade: ')).strip()
cidade = cidade.title()

if 'Santo' in cidade.split()[0]:
    print(f'{cr.verde}A cidade {cidade} começa com Santo{cr.fim}')

else:
    print(f'{cr.vermelho}A cidade {cidade} não começa com Santo{cr.fim}')
