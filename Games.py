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

        print()

        user = input("Quer adicionar outro time (N/S)? ").lower().strip()

        if user == 'n':
            Database.data_teams(teams)
            teams.clear()

            break


def participants_creation():

    while True:

        question_team = input("Nome da equipe: ").lower().strip()
        user = input("Nome do participante: ").lower().strip()

        person = {

            "participante" : user

        }

        question = input("Voce quer adicionar outro (S/N)? ").lower().strip()

        for people in teams:

            if people['equipe'] == question_team:
                people['pessoas'].append(person)
                Database.data_teams(teams)

        if question == 'n':
            break

def remove_teams():

    import Database

    user = input("Time que deseja excluir: ")

    counter = 0

    while counter < len(teams):

        time = teams[counter]['equipe']

        if user == time:

            del teams[counter]

            Database.data_teams(teams)

            print("Time removido com sucesso!")

            break

        else:
            print("Time nao encontrado, tente novamente.")

        counter += 1

def remove_participants():

    import Database

    user_team = input("Time da pessoa: ").lower().strip()
    user_person = input("Pessoa que deseja excluir: ").lower().strip()

    team_counter = 0

    while team_counter < len(teams):

        team = teams[team_counter]["equipe"]

        if user_team == team:

            person_counter = 0
            people = teams[team_counter]["pessoas"]

            while person_counter < len(people):

                person = people[person_counter]["participante"]

                if user_person == person:

                    del people[person_counter]

                    Database.data_teams(teams)

                    print("Pessoa removida com sucesso!")
                    return

                person_counter += 1

            print("Pessoa não encontrada neste time.")
            return

        team_counter += 1

    print("Time não encontrado.")