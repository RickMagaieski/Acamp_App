def general_values():

    print("==== VALORES GERAIS ====")

    print()

    print("Taxa de inscrição (Adulto - 14+): $135.00\nValor de Sábado apenas: $55.00\nInscrição com RV: 145.00"
          "\nCadastro da Infantil: $67.75\nSomente Sábado Infantil: $27.50")

    print()

def menu():
    print("===== FINANÇAS =====")

    print()

    print("1. Lista de Preços\n2. Contabilidade Geral\n3. Pagamentos\n4. Sair")

    print()

    try:
        user_inpt = int(input())
        return user_inpt
    except ValueError:
        print("Insira um número válido.")

def payments():
    from Inscriptions import inscriptions_list

    if inscriptions_list:
        for person in inscriptions_list:

                print(f"{person['name']}: ${person['payment']:.2f} - {person['inscription']}")

                if person['inscription'] == 'adulto':
                    if person['payment'] == 135.00:
                        print("(Pago!)")
                    elif 135.00 > person['payment'] > 0.00:
                        print(f"(Parcial... ${135.00 - person['payment']:.2f})")
                    elif person['payment'] == 0.00:
                        print("(Pendente!)")

                if person['inscription'] == 'infantil':
                    if person['payment'] == 67.75:
                        print("(Pago!)")
                    elif 67.75 > person['payment'] > 0.00:
                        print(f"(Parcial... ${67.75 - person['payment']:.2f})")
                    elif person['payment'] == 0.00:
                        print("(Pendente!)")

                if person['inscription'] == 'rv':
                    if person['payment'] == 145.00:
                        print("(Pago!)")
                    elif 145.00 > person['payment'] > 0.00:
                        print(f"(Parcial... ${145.00 - person['payment']:.2f})")
                    elif person['payment'] == 0.00:
                        print("(Pendente!)")

                if person['inscription'] == 'sabado':
                    if person['payment'] == 55.00:
                        print("(Pago!)")
                    elif 55.00 > person['payment'] > 0.00:
                        print(f"(Parcial... ${55.00 - person['payment']:.2f})")
                    elif person['payment'] == 0.00:
                        print("(Pendente!)")

                if person['inscription'] == 'sabado infantil':
                    if person['payment'] == 27.50:
                        print("(Pago!)")
                    elif 27.50 > person['payment'] > 0.00:
                        print(f"(Parcial... ${27.50 - person['payment']:.2f})")
                    elif person['payment'] == 0.00:
                        print("(Pendente!)")
    else:
        print("A lista está vazia.")

def account():
    from Inscriptions import inscriptions_list
    from Inventory import list_inventory

    init_balance = 3700.00
    total_profit = 0
    total_loss = 0

    print(f"Saldo Inicial: {init_balance:.2f}")
    print()

    print("Entradas:")
    for amount in inscriptions_list:
        print(f"${amount['payment']:.2f}")

        total_profit += amount['payment']

    print()
    print(f"Total Entradas: ${total_profit:.2f}")

    print()

    print("Saídas:")
    for saidas in list_inventory:
        print(f"$-{saidas['value']:.2f}")

        total_loss += saidas['value']

    print()
    print(f"Total Saídas: $-{total_loss:.2f}")

    print()

    print(f"Total Final: {init_balance + total_profit - total_loss:.2f}")

    print()
