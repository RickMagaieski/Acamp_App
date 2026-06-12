inscriptions_list = []

def add_participant():

    import Database

    name_inpt = input("Nome Completo: ").lower().strip()
    age_inpt = input("Idade: ").strip()
    phone_inpt = input("Telefone: ").strip()
    medical_inpt = input("Condição médica/Alergias: ").lower().strip()
    transportation = input("Precisa de ajuda para o transporte? ").lower().strip()
    email_input = input("Digite o seu e-mail: ").strip()
    shirt_size = input("Digite o tamanho de sua camiseta: ").lower().strip()
    accommodation_input = input("Que tipo de acomodação será (RV/Barraca/Cabine)? ").strip()
    inscription_type = input("Que tipo de inscrição será (RV/Adulto/Infantil/Sábado Infantil/Sábado)? ").strip().lower()
    payment_input = float(input("Valor pago: "))
    food_input = input("Come carne? ").strip()

    participant = {
        "name": name_inpt,
        "age": age_inpt,
        "phone": phone_inpt,
        "medical": medical_inpt,
        "transportation": transportation,
        "email": email_input,
        "shirt": shirt_size,
        "accommodation" : accommodation_input,
        "inscription" : inscription_type,
        "payment" : payment_input,
         "food" : food_input
    }

    inscriptions_list.append(participant)
    Database.save_data(inscriptions_list)

def menu():
    print("===== INSCRIÇÕES =====")

    print()

    print("1. Inscrever alguém\n2. Lista de Inscritos\n3. Deletar nome\n4. Pesquisa\n5. Sair")

    print()

    try:
        user_inpt = int(input())
        return user_inpt
    except ValueError:
        print("Insira um número válido.")

def user_deletion():

    import Database

    user = input("Nome que deseja deletar: ").lower().strip()
    counter = 0
    found = False

    while counter < len(inscriptions_list):

        person = inscriptions_list[counter]["name"]

        if person == user:
            del inscriptions_list[counter]
            found = True
            Database.save_data(inscriptions_list)

            print(f"Inscrição de {person} removida")

            break
        else:
            counter += 1

    if not found:
        print("Esta pessoa não está na lista.")

    print()

def search_box():
    while True:

        user = input("Busca (para sair digite 's'): ").strip().lower()

        if user == 's':
            break

        counter = 0
        found = False

        print()

        while counter < len(inscriptions_list):

            person = inscriptions_list[counter]['name']

            if user in person:

                print(inscriptions_list[counter])

                found = True
                counter += 1

            else:
                counter += 1

        if not found:
            print("Esta pessoa não está na lista.")

        print()

    print()
