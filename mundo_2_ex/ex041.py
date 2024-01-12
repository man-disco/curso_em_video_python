# Categorização de nadadores

# Importa o modulo data e define a data atual
from datetime import date
atual = date.today().year

nasc = int(input('\nInforme ano de nascimento> '))

# Calcula a idade na diferença do ano atual
idade = atual - nasc

cat = None

if idade >= 1:

    if idade <= 9:
        cat = '\033[1;31mMIRIM\033[m'

    elif idade <= 14:
        cat = '\033[1;32mINFANTIL\033[m'

    elif idade <= 19:
        cat = '\033[1;33mJUNIOR\033[m'

    elif idade == 20:
        cat = '\033[1;34mSÊNIOR\033[m'

    else:
        cat = '\033[1;35mMASTER\033[m'

else:
    print('\033[1;31m[ERRO] Informe um data válida\033[m')
    exit()

print(f'\nO atleta de {idade} anos está na categoria {cat}.')