init_balance = 3.000
camp_price = 140

def menu_finance():

    print("==== Valores Gerais ====")

    print()

    print("Valor da Inscricao: $140,00\nValor de Sabado apenas: $50,00\nInscricao com RV: 180,00\nCamiseta: $30,00\nInscricao Infantil: $90,00")

    print()

    print("Para sair aperte a tecla 7")

    try:
        user_input = int(input())
        return user_input
    except ValueError:
        print("Digite um numero valido.")
