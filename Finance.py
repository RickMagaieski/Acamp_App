init_balance = 3.000
camp_price = 140

def menu_finance():

    print("==== Valores Gerais ====")

    print()

    print("Valor da Inscricao (Adulto - 14+): $135,50\nValor de Sabado apenas: $55,00\nInscricao com RV: 145,00"
          "\nInscricao Infantil: $67,75\nSomente Sabado Infantil: $27,50")

    print()

    print("Para sair aperte a tecla 7")

    try:
        user_input = int(input())
        return user_input
    except ValueError:
        print("Digite um numero valido.")
