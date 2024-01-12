# Programa com função que calcule uma área com parâmetros (comprimento, largura)
def área(largura, comprimento):
    área = largura * comprimento
    print(f'\nA área desse terreno de {largura}m x {comprimento}m é {área:.2f}m²')


print('\033[4;1mControle de Terrenos\033[m\n')
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
área(a, b)
