# Alistamento do exército
import datetime

data = datetime.date.today()

try:
    idade = int(input("Idade do cidadão: "))
    if idade == 18:
        print('\n\033[1;32m[APTO]\033[m O cidadão deve comparecer em unidade de alistamento militar após alistar-se no site oficial.')

    elif idade < 18:
        print(f'\n\033[1;33m[INAPTO]\033[m O cidadão não possuí a idade mínima para se alistar.\nO mesmo deverá se apresentar no ano {data.year + (18 - idade)} (daqui {18 - idade} anos) quando estiver com 18 anos.')

        
    else:
        alistou = input("O cidadão se alistou no site do exército? (sim/não) ").lower()
        if alistou == "sim":
            print(f'\n\033[1;32m[REGULAR]\033[m O cidadão está em situção regular com o exército desde {data.year - (idade - 18)}.')

        elif alistou == "nao" or alistou == "não":
            print(f'\n\033[1;31m[IRREGULAR]\033[m O cidadão possuí irregularidade com o serviço militar.\nO cidadão não fez o alistamento obrigatório em {(data.year - idade) + 18} ({idade - 18} anos) e deve se digir a junta militar mais próxima para efetuar o pagamento das dívidas pendentes.')

        else:
            print('\033[31mDigite sim ou não e tente novamente.\033[m')

except ValueError:
    print('\033[31mDigite um número válido.\033[m')