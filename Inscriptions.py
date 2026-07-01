
"""inscription_list = []

def add_participant():
    import Database

    name_inpt = input("Nome Completo: ").lower().strip()
    age_inpt = input("Idade: ").strip()
    phone_inpt = input("Telefone: ").strip()
    medical_inpt = input("Condição médica/Alergias: ").lower().strip()
    transportation_inpt = input("Precisa de ajuda para o transporte? ").lower().strip()
    email_inpt = inpt("Digite o seu e-mail: ").strip()
    accommodation_input = input("Que tipo de acomodação será (RV/Barraca/Cabine)? ").strip()
    inscription_inpt = input("Que tipo de inscrição será (RV/Adulto/Infantil/Sábado Infantil/Sábado)? ").strip().lower()
    payment_inpt = float(input("Valor pago: "))
    food_inpt = input("Come carne? ").strip()

    participant = {
        "name": name_inpt,
        "age": age_inpt,
        "phone": phone_inpt,
        "medical": medical_inpt,
        "transportation": transportation_inpt,
        "email": email_inpt,
        "accommodation" : accommodation_inpt,
        "inscription" : inscription_inpt,
        "payment" : payment_inpt,
         "food" : food_inpt
    }

    Database.save_data(inscription_list)"""
from idlelib.mainmenu import default_keydefs

from GoogleSheets import delete


def menu():
    print("===== INSCRIÇÕES =====")

    print()

    print("1. Lista de Inscritos\n2. Pesquisa\n3. Deletar\n4. Sair")

    print()

    try:
        user_inpt = int(input())
        return user_inpt
    except ValueError:
        print("Insira um número válido.")

def user_deletion():

    from GoogleSheets import inscriptions, delete
    import Database

    user = input("Nome que deseja deletar: ").lower().strip()
    counter = 0
    found = False

    while counter < len(inscriptions):

        person = inscriptions[counter]["name"]

        if person == user:

            person_id = inscriptions[counter]["id"]
            deletion_from_sheet = delete(person_id)

            if deletion_from_sheet:

                del inscriptions[counter]
                Database.save_data(inscriptions)

                found = True

                print(f"Inscrição de {person} removida")

            break

        else:
            counter += 1

    if not found:
        print("Esta pessoa não está na lista.")

def search_box():

    from GoogleSheets import inscriptions

    while True:

        if inscriptions:
            user = input("Busca (para sair digite 's'): ").strip().lower()

            if user == 's':
                break

            counter = 0
            found = False

            print()

            while counter < len(inscriptions):

                person = inscriptions[counter]['name']

                if user in person:

                    print(inscriptions[counter])

                    found = True
                    counter += 1

                else:
                    counter += 1

            if not found:
                print("Esta pessoa não está na lista.")

            print()
        else:
            print("A lista está vazia")
            break
