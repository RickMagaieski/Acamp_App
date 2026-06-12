inscriptions_list = [{
    "name": "lucas oliveira",
    "age": "18",
    "phone": "2405551234",
    "medical": "alergia a amendoim",
    "transportation": "sim",
    "email": "lucas.oliveira@email.com",
    "shirt_size": "m",
    "accommodation": "barraca",
    "inscription": "sabado",
    "payment": 55.00,
    "food": "sim"},
    {
    "name": "ana santos",
    "age": "21",
    "phone": "3015559876",
    "medical": "nenhuma",
    "transportation": "nao",
    "email": "ana.santos@email.com",
    "shirt_size": "p",
    "accommodation": "cabine",
    "inscription": "adulto",
    "payment": 135.00,
    "food": "nao"},
    {
    "name": "pedro almeida",
    "age": "16",
    "phone": "4435556789",
    "medical": "asma",
    "transportation": "sim",
    "email": "pedro.almeida@email.com",
    "shirt_size": "g",
    "accommodation": "rv",
    "inscription": "adulto",
    "payment": 100.00,
    "food": "sim"}]

def add_participant():

    name_inpt = input("Nome Completo: ").lower().strip()
    age_inpt = input("Idade: ").strip()
    phone_inpt = input("Telefone: ").strip()
    medical_inpt = input("Condicao Medica/Alergias: ").lower().strip()
    transportation = input("Precisa de ajuda para o transporte? ").lower().strip()
    email_input = input("Digite o seu e-mail: ").strip()
    shirt_size = input("Digite o tamanho de sua camista: ").lower().strip()
    accommodation_input = input("Qual sera o tipo de acomodacao (RV/Barraca/Cabine)? ").strip()
    inscription_type = input("Qual sera o tipo de inscricao (RV/Adulto/Infantil/Sabado Infantil/Sabado)? ").strip().lower()
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

    user = input("Nome que deseja deletar: ").lower().strip()
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
            print("Esta pessoa nao esta listada.")

        print()

    print()
