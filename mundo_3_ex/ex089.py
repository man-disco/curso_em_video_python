# Boletim escolar
from cores import Cores as cr

aluno = []
bimestres = []
materias = ['Português', 'Matemática', 'Geografia']
notas_aluno = []
boletim = []
media = esc = 1
linha = '-'*12

# Loop para armazenar os alunos indefinidamente
while True:
    print(f'{cr.negrito + cr.sublinhado}Boletim{cr.fim}')
    # Anexa o nome do aluno na lista 'aluno'
    nome = str(input('\nNome: ').strip().capitalize())
    if len(boletim) == 0:
        aluno.append(nome)
        pass
    else:
        for nome_boletim in boletim[0]:
            if nome not in nome_boletim:
                aluno.append(nome)
                pass
            else:
                print(f'{cr.vermelho}Erro! Aluno já consta no boletim!{cr.fim}\n')
                nome = str(input('\nNome: ').strip().capitalize())
        continue

                
    while len(bimestres) < 4:
        print(f'\n{len(bimestres)+1}º Bimestre\n{linha}')
        # Anexa as notas do bimestre conforme materias
        for materia in materias:
            notas_aluno.append(float(input(f'{materia}: ')))
        bimestres.append(notas_aluno[:])
        notas_aluno.clear()
    # Adiciona os 4 bimestres ao aluno e depois anexa ao boletim
    aluno.append(bimestres[:])
    boletim.append(aluno[:])
    # Limpa as listas de dados para o próximo aluno
    bimestres.clear()
    aluno.clear()
    cont = str(input('\nDeseja continuar? [S/n] '))
    while cont != 's' and cont != 'n' and cont != '':
        print(f'{cr.vermelho}Erro! Escolha S ou N!{cr.fim}')
        cont = str(input('\nDeseja continuar? [S/n] ').lower().strip())
    if cont == 's' or cont == '':
        print(f'{cr.verde}Aluno salvo!{cr.fim}\n')
        continue
    if cont == 'n':
        print(f'{cr.amarelo}Parando programa...{cr.fim}\n')
        break
# Mostra a média de todos os alunos presentes no boletim
a = 1
for aluno_boletim, nota_bimestre in boletim:
    print(f'{a} - {aluno_boletim}\n{linha}')
    for bimestre in nota_bimestre:
        for nota in bimestre:
            media += nota
    media = media // 4
    print(f'A média desse aluno foi {media:.2f}\n')
    media = 0
    a += 1
# Loop para mostrar notas individuais de cada aluno
while esc != 0:
    esc = int(input('\nMostrar notas de qual aluno? (0 para fechar) '))
    if esc >= a:
        print(f'{cr.vermelho}'
               'Erro! O aluno não está no boletim, tente novamente.'
              f'{cr.fim}\n')
        continue
    if esc == 0:
        break
    aluno_esc, notas_aluno_esc = boletim[esc-1]
    print(f'\nNome: {aluno_esc}')
    for pos_bimestre_esc, bimestres_esc in enumerate(notas_aluno_esc):
        print(f'{linha}\n{pos_bimestre_esc+1}º Bimestre\n{linha}')
        for mat_bimestre_esc, mat_nota_esc in enumerate(bimestres_esc):
            print(f'{materias[mat_bimestre_esc]}: {mat_nota_esc:.2f}')

print(f'{linha}\nFIM\n')
