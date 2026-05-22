participants = []

def add_participant():

    name_inpt = input("Nome Completo: ").lower()
    age_inpt = input("Idade: ")
    phone_inpt = input("Telefone: ")
    medical_inpt = input("Condicao Medica/Alergias: ")
    paid_inpt = input("Valor pago: ")
    status_inpt = input("Status do pagamento: ")

    participant = {
        "name": name_inpt,
        "age": age_inpt,
        "phone": phone_inpt,
        "medical": medical_inpt,
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
