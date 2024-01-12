# Vogais em tuplas

palavras = ('amarelo', 'saturno', 'chamou', 'tanque', 'energia', 'humano')
vogais = ('a', 'e', 'i', 'o', 'u')

# Primeiro loop: Mostra todas as palavras da tupla
for palavra in palavras:
    print(f'A palavra {palavra.upper()}', end=' tem as vogais ')

    # Segundo loop: Separa cada letra individualmente do loop anterior
    for letra in palavra:
        # Checa se letra é uma vogal, se for mostra, se não pula
        if letra in vogais:
            print(letra, end=' ' if letra != palavra[-1] else '.\n')
