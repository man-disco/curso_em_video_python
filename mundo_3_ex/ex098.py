from time import sleep
# Contador de números com parametros


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
    print(f'\n{"#"*40}\n'
          f'{f"Contagem de {inicio} até {fim} de {passo} em {passo}":^40}'
          f'\n{"#"*40}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont -= passo
    print('fim')


contador(1, 10, 1)
contador(10, 0, 2)

print('\nAgora é a sua vez, defina os parametros abaixo:\n')
a = int(input('Ínicio: '))
b = int(input('Fim: '))
c = int(input('Sequência: '))
contador(a, b, c)
