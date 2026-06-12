import Inscriptions
import Finance
import Inventory
import Database

Inscriptions.inscriptions_list = Database.open_data()

while True:
    print()

    print("======= ACAMP WBSDAC 2026 MENU =======")

    print()

    print("1. Inscrição\n2. Finanças\n3. Inventário\n4. Atividades\n5. Sair")

    print()

    try:
        user = int(input("Selecione a opção desejada: "))

        print()

        if user == 1:
            while True:

                choice = Inscriptions.menu()

                if choice == 1:
                    Inscriptions.add_participant()

                if choice == 2:
                    if not Inscriptions.inscriptions_list :
                        print("Não há inscritos.")
                    else:
                        for inscritos in Inscriptions.inscriptions_list:
                                print(inscritos, end='\n')
                        print()

                if choice == 3:
                    if not Inscriptions.inscriptions_list:
                        print("Não há inscritos.")
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

                if choice == 1:
                    Finance.general_values()

                if choice == 2:
                    Finance.account()

                if choice == 3:
                    Finance.payments()

                if choice == 4:
                    break
        if user == 3:
            while True:

                choice = Inventory.menu()

                if choice == 1:
                    Inventory.add_inventory()

                if choice == 2:
                    if not Inventory.list_inventory:
                        print("Não há itens!")

                        print()

                    else:
                        for lista in Inventory.list_inventory:
                            print(lista, end='\n')
                        print()

                if choice == 3:
                    if not Inventory.list_inventory:
                        print("O inventário está vazio.")
                    else:
                        Inventory.remove_items()

                if choice == 4:
                    Inventory.search()

                if choice == 5:
                    break

        if user == 5:
            break
    except ValueError:
        print("Insira um número válido.")
