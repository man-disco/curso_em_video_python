def função():
    global n1
    n1 = 4
    print(f'N1 dentro vale {n1}')
    

n1 = 2
função()
print(f'N1 fora vale {n1}')