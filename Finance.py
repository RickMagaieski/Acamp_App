def general_values():

    print("==== Valores Gerais ====")

    print()

    print("Valor da Inscricao (Adulto - 14+): $135,50\nValor de Sabado apenas: $55,00\nInscricao com RV: 145,00"
          "\nInscricao Infantil: $67,75\nSomente Sabado Infantil: $27,50")

    print()

def menu():
    print("===== FINANCAS =====")

    print()

    print("1. Tabela de Precos\n2. Contabilidade Geral\n3. Pagamentos\n4. Sair")

    print()

    try:
        user_inpt = int(input())
        return user_inpt
    except ValueError:
        print("Digite um numero valido.")

def payments():
    from Inscriptions import inscriptions_list

    for person in inscriptions_list:

            print(f"{person["name"]}: ${person['payment']:.2f} - {person["inscription"]}")

            if person['inscription'] == 'adulto':
                if person['payment'] == 135.00:
                    print("(Pago!)")
                elif person['payment'] > 0.00 < 135.00:
                    print(f"(Parcial... ${135.00 - person['payment']:.2f})")
                elif person['payment'] == 0.00:
                    print("(Pendente!)")

            if person['inscription'] == 'infantil':
                if person['payment'] == 67.50:
                    print("(Pago!)")
                elif person['payment'] > 0.00 < 67.50:
                    print(f"(Parcial... ${67.50 - person['payment']:.2f})")
                elif person['payment'] == 0.00:
                    print("(Pendente!)")

            if person['inscription'] == 'rv':
                if person['payment'] == 145.00:
                    print("(Pago!)")
                elif person['payment'] > 0.00  < 145.00:
                    print(f"(Parcial... ${145.00 - person['payment']:.2f})")
                elif person['payment'] == 0.00:
                    print("(Pendente!)")

            if person['inscription'] == 'sabado':
                if person['payment'] == 55.00:
                    print("(Pago!)")
                elif person['payment'] > 0.00  < 55.00:
                    print(f"(Parcial... ${55.00 - person['payment']:.2f})")
                elif person['payment'] == 0.00:
                    print("(Pendente!)")

            if person['inscription'] == 'sabado infantil':
                if person['payment'] == 27.50:
                    print("(Pago!)")
                elif person['payment'] > 0.00 < 27.50:
                    print(f"(Parcial... ${27.50 - person['payment']:.2f})")
                elif person['payment'] == 0.00:
                    print("(Pendente!)")

def account():
    from Inscriptions import inscriptions_list

    init_balance = 3.700
    total_profit = 0
    total_loss = 0

    print(f"Balanco Inicial: {init_balance:.3f}")
    print()

    print("Entradas:")
    for amount in inscriptions_list:
        print(f"${amount['payment']:.2f}")

        total_profit += amount['payment']

    print()
    print(f"Total Entradas: ${total_profit:.2f}")

    print()

    print("Total Saidas: ")

    print("Balanco Final: {init_balance - total_loss + total_entries}")
