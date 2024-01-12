# Calculadora de pesos
pessoas = ['a', 'b', 'c', 'd', 'e']
peso_maior = 0
peso_menor = 0

men = None
mai = None

for p in pessoas:
    peso = float(input('Pessoa: ({}) Digite um peso: '.format(p.upper())))

    if p == 'a':
        peso_maior = peso
        peso_menor = peso
        mai = p
        men = p

    else:

        if peso > peso_maior:
            peso_maior = peso
            mai = p

        if peso < peso_menor:
            peso_menor = peso
            men = p

    print('Peso da pessoa {} = {:.2f}'.format(p.upper(), peso_maior))
       

print('\nO maior peso foi o da pessoa {} que é {:.2f}.'.format(mai.upper(), peso_maior))
print('O maior peso foi o da pessoa {} que é {:.2f}.'.format(men.upper(), peso_menor))
