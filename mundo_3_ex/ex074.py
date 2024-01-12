# Tupla de números
from random import randint

nums = ()
mai = men = 0

while len(nums) < 5:
    rannum = randint(1, 10)
    nums += (rannum,)
    
    if len(nums) == 1:
        mai = men = rannum
    else:
        if rannum > mai:
            mai = rannum

        if men > rannum < mai:
            men = rannum

    if len(nums) == 5:
        print(f'\nA tupla gerada foi ', end='')
        for num in nums:
            print(num, end=' ')
        print(f'\nO maior valor foi o {mai}.\n'
              f'O menor valor foi o {men}.\n')
