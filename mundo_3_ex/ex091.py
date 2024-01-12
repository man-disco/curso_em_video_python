from time import sleep
from random import randint


dice = {}
p = 1
for roll in range(1, 5):
    dice[f'Player_{roll}'] = randint(1, 6)
    print(f'Player_{roll} rolled the number {dice[f"Player_{roll}"]}')
    sleep(0.6)
print()
for k, v in sorted(dice.items(), key=lambda item: item[1], reverse=True):
    print(f'{p}º Place -> {k}: {v}')
    sleep(0.6)
    p += 1
