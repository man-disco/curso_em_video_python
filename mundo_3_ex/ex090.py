# Média de alunos
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média notas: '))

if aluno['média'] >= 7.00:
    aluno['situação'] = '\033[32mAprovado\033[m'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = '\033[33mRecuperação\033[m'
else:
    aluno['situação'] = '\033[31mReprovado\033[m'

print(f'{"-"*40}\nO aluno(a) {aluno["nome"]} teve a média de {aluno["média"]:.2f}\n'
      f'{"Situação = ":>20}{aluno["situação"]}\n{"-"*40}')
