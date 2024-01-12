# Sistema de notas de alunos, com parametros opcionais na função de notas
def notas(*notas, sit=False):
    """
    Essa função guarda as notas inseridas, com suas caracteristicas
    em um dicionário.
    
    :param notas: Notas da turma que serão desempacotadas.
    :param sit: Situação da turma com base na média de notas, que é definida
    pelo parametro opcional booleano.
    :return: Retorna o dicionário com os parametros definidos.
    
    "EXCELENTE": Média acima de 9.0.
    "BOA": Média entre 7.0 e 8.0.
    "MELHORIA": Média entre 5.0 e 6.5.
    "RUIM": Média abaixo ou igual a 5.00.
    """
    classe = {}
    maior = menor = média = 0
    cont = 0
    for nota in notas:
        if cont == 0:
            maior = nota
            menor = nota
        if nota > maior:
            maior = nota
        if menor > nota:
            menor = nota
        média += nota
        cont += 1
    média = média / len(notas)
    classe['quantidade'] = len(notas)
    classe['maior_nota'] = maior
    classe['menor_nota'] = menor
    classe['média_notas'] = média

    if sit:
        if média > 9.0:
            classe['situação'] = "EXCELENTE"
        elif 7.0 <= média <= 8.0:
            classe['situação'] = "BOA"
        elif 5.0 <= média <= 6.5:
            classe['situação'] = "MELHORIA"
        else:
            classe['situação'] = "RUIM"

    return classe


help(notas)
teste = notas(5, 4, 9, 6, sit=True)
for k, v in teste.items():
    print(k, v)
