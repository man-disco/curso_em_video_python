from time import sleep


# Faça uma função que defina o maior valor em um desempacotamento
def maior(*nums):
    m = 0
    print(f'{"-"*50}\n{"Analisando valores...":^50}\n{"-"*50}')
    for n in nums:
        print(n, end=' ', flush=True)
        if n >= m:
            m = n
        sleep(0.2)
    print(f'- Foram informados {len(nums)} valores ao todo.', end='')
    print(f'\nO maior valor informado foi o {m}.\n')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
