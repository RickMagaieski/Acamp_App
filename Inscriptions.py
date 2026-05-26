inscriptions_list = []

def add_participant():

    name_inpt = input("Nome Completo: ").lower()
    age_inpt = input("Idade: ")
    phone_inpt = input("Telefone: ")
    medical_inpt = input("Condicao Medica/Alergias: ").lower()
    transportation = input("Precisa de ajuda para o transporte? ").lower()
    email_input = input("Digite o seu e-mail: ")
    shirt_size = input("Digite o tamanho de sua camista: ")
    accommodation_input = input("Qual sera o tipo de acomodacao (RV/Barraca/Cabine)? ")
    inscription_type = input("Qual sera o tipo de inscricao (Individual/Grupo/Familia)? ")
    food_input = input("Come carne? ")

    participant = {
        "name": name_inpt,
        "age": age_inpt,
        "phone": phone_inpt,
        "medical": medical_inpt,
        "transportation": transportation,
        "e-mail": email_input,
        "shirt": shirt_size,
        "accommodation" : accommodation_input,
        "inscription" : inscription_type,
        "food" : food_input
    }

    inscriptions_list.append(participant)

def menu():
    print("===== INSCRIÇÕES =====")

    print()

    print("1. Inscrever Alguem\n2. Lista dos Inscritos\n3. Deletar nome\n4. Search\n5. Sair")

    print()

    try:
        user_inpt = int(input())
        return user_inpt
    except ValueError:
        print("Digite um numero valido.")

def user_deletion():

    user = input("Nome que deseja deletar: ").lower()
    counter = 0
    found = False

    while counter < len(inscriptions_list):

        person = inscriptions_list[counter]["name"]

        if person == user:
            del inscriptions_list[counter]
            found = True
            print(f"Inscricao de {person} removida")

            break
        else:
            counter += 1

    if not found:
        print("Essa pessoa nao esta na lista.")

def search_box():
    while True:

        print()
        user = input("Busca (para sair digite 's'): ").lower()

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
            print("This person is not listed.")
