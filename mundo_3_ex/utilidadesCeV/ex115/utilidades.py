# Este arquivo mantêm todas as variavéis necessárias no programa
opts = [
        'Cadastrar pessoas',
        'Visualizar pessoas',
        'Ajuda',
        'Sair'
       ]

cores = {
        # Cores simples
        'branco':'\033[29m',
        'cinza':'\033[30m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'amarelo':'\033[33m',
        'azul':'\033[34m',
        'roxo':'\033[35m',
        'ciano':'\033[36m',

        # Alguns estilos necessários
        'negrito':'\033[1m',
        'sublinhado':'\033[4m',
        'fim':'\033[m'
        }

funções = {
        'sistema': ['cadastrar','visualizar','ajuda', 'limpa'],
        'interface': ['linha', 'titulo', 'menu']
        }