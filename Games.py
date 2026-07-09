import Database

teams = []

def menu():
    print("===== ATIVIDADES =====")

    print()

    print("1. Adicionar Time\n2. Deletar Time\n3. Adicionar Participante\n4. Deletar Participante\n5. Adicionar Pontos"
          "\n6. Tabela\n7. Sair")

    print()

    try:
        user_inpt = int(input())
        return user_inpt
    except ValueError:
        print("Insira um número válido.")

def team_creation():
    import Database

    while True:
        print()

        team = input("Nome do Time: ").lower().strip()
        leader = input("Nome do Capitao: ").lower().strip()
        color = input("Cor do time: ").lower().strip()

        time = {
            "equipe" : team,
            "lider" : leader,
            "cor" : color,
            "pessoas" : []
        }

        teams.append(time)
        Database.data_teams(teams)

        print()

        user = input("Quer adicionar outro time (N/S)? ").lower().strip()

        if user == 'n':
            break


def participants_creation():

    while True:

        question_team = input("Nome da equipe: ").lower().strip()
        user = input("Nome do participante: ").lower().strip()

        person = {

            "participante" : user

        }

        question = input("Voce quer adicionar outro (S/N)? ").lower().strip()

        if question == 'n':
            break

    for people in teams:

        if people['equipe'] == question_team:
            people['pessoas'].append(person)
            Database.data_teams(teams)
