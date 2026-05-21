participants = []

def add_participant():

    name_inpt = input("Nome Completo: ")
    age_inpt = input("Idade: ")
    phone_inpt = input("Telefone: ")
    family_inpt = input("Groupo: ")
    transp_inpt = input("Transporte (pessoal/necessita ajuda): ")
    paid_inpt = input("Valor pago: ")
    status_inpt = input("Status do pagamento: ")

    participant = {
        "name": name_inpt,
        "age": age_inpt,
        "phone": phone_inpt,
        "family/group": family_inpt,
        "transportation": transp_inpt,
        "payment": paid_inpt,
        "status": status_inpt
    }

    participants.append(participant)

def menu():
    print("===== INSCRIÇÕES =====")

    print()

    print("1. Inscrever Alguem\n2. Lista dos Inscritos\n3. Sair")

    print()

    user_inpt = int(input())

    return user_inpt
