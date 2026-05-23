inscriptions_list = [{'name': 'henrique magaieski', 'age': 22, 'phone': '2404742543',
                      'medical': 'antialergics', 'transportation': 'no', 'e-mail' : 'henrimagaieski@icloud.com'},
                     {'name': 'arthur', 'age': 22, 'phone': '2404742543', 'medical': 'polen', 'transportation': 'no',
                      'e-mail': 'something@icloud.com'},
                     {'name': 'henrique silva', 'age': 24, 'phone': '2404742543',
                      'medical': 'None', 'transportation': 'no', 'e-mail': 'henrimagaieski@icloud.com'}
                     ]

def add_participant():

    name_inpt = input("Nome Completo: ").lower()
    age_inpt = int(input("Idade: "))
    phone_inpt = (input("Telefone: "))
    medical_inpt = input("Condicao Medica/Alergias: ").lower()
    transportation = input("Precisa de ajuda para o transporte? ").lower()
    email = input("Digite o seu e-mail: ")

    participant = {
        "name": name_inpt,
        "age": age_inpt,
        "phone": phone_inpt,
        "medical": medical_inpt,
        "transportation": transportation,
        "e-mail": email
    }

    inscriptions_list.append(participant)

def menu():
    print("===== INSCRIÇÕES =====")

    print()

    print("1. Inscrever Alguem\n2. Lista dos Inscritos\n3. Deletar nome\n4. Search \n5. Sair")

    print()

    user_inpt = int(input())

    return user_inpt

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

    user = input("Busca: ").lower()
    counter = 0
    found = False

    print("Inscricao Encontrada:")

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
