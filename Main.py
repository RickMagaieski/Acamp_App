from sys import excepthook

import Inscriptions
import Finance

while True:
    print()

    print("======= Acamp WBSDAC 2026 Menu =======")

    print()

    print("1. Inscricoes\n2. Financas\n\n6. Sair")

    print()

    try:
        user = int(input("Selecione a opcao desejada: "))

        print()

        if user == 1:
            while True:

                print()

                choice = Inscriptions.menu()

                if choice == 1:
                    Inscriptions.add_participant()

                if choice == 2:
                    if not Inscriptions.inscriptions_list :
                        print("Nao ha inscritos.")
                    else:
                        for inscritos in Inscriptions.inscriptions_list:
                                print(inscritos, end='\n')

                if choice == 3:
                    if not Inscriptions.inscriptions_list:
                        print("Nao ha inscritos.")
                    else:
                        Inscriptions.user_deletion()

                if choice == 4:
                    Inscriptions.search_box()

                if choice == 5:
                    break

        if user == 2:
            while True:

                print()

                choice = Finance.menu()

                if choice == 3:
                    Finance.payments()

                if choice == 4:
                    break

        if user == 6:
            break
    except ValueError:
        print("Digite um numero valido.")
