# Detector de palindromo
print('\n== Detector de palíndromo ==\n')
s = input('Digite uma frase: ').lower().replace(' ', '')
c = len(s)
print()

# Printa letra por letra da string
for l in s:
    print("\033[37m", end='')
    print(l, end='\033[m')
print('\033[m')

# Faz o mesmo que acima só que reverso
for l in s[::-1]:
    print("\033[35m", end='')
    print(l, end='\033[m')
print('\033[m\n')

if s == s[::-1]:
    print('\033[1;32mEssa frase forma um palíndromo.\033[m')
else:
    print('\033[1;31mEssa frase não forma um palíndromo.\033[m')