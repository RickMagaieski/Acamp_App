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
            "pessoas" : [],
            "score" : 0
        }

        teams.append(time)

        print()

        user = input("Quer adicionar outro time (N/S)? ").lower().strip()

        if user == 'n':
            Database.data_teams_write(teams)

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
                Database.data_teams_write(teams)

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

            Database.data_teams_write(teams)

            print("Time removido com sucesso!")

            break

        else:
            print("Time nao encontrado, tente novamente.")

        counter += 1


def remove_participants():

    import Database

    team = input("Time da pessoa: ").lower().strip()
    person_list = input("Pessoa que deseja excluir: ").lower().strip()

    counter = 0

    while counter < len(teams):

        equip = teams[counter]["equipe"]

        if team == equip:

            person_counter = 0
            people = teams[counter]["pessoas"]

            while person_counter < len(people):

                person = people[person_counter]["participante"]

                if person_list == person:

                    del people[person_counter]
                    Database.data_teams_write(teams)

                    print("Pessoa removida com sucesso!")
                    return

                person_counter += 1

            print("Pessoa não encontrada neste time.")
            return

        counter += 1

    print("Time não encontrado.")


def score_info():

    import Database

    while True:

        print("===== PONTUACAO =====")

        print()

        print("1. Adicionar pontos\n2. Remover pontos\n3. Tabela de pontos\n4. Sair")

        print()

        user = int(input())

        print()

        if user == 1:

            equip_name = input("Nome da equipe: ").lower().strip()
            equip_score = int(input("Digite a pontuação: "))

            found = False

            for ponto in teams:
                if ponto['equipe'] == equip_name:

                    add = ponto['score'] + equip_score
                    ponto['score'] = add
                    Database.data_teams_write(teams)

                    found = True

                    print()

                    print(f"{equip_score} pontos foram adicionados para a equipe '{equip_name}'!\nPontuacao final: {add}")

                    print()

            if not found:
                print("Equipe nao listada. Tente novamente!")

        if user == 2:

            equip_name = input("Nome da equipe: ").lower().strip()
            equip_score = int(input("Digite a pontuação: "))

            found = False

            for ponto in teams:
                if ponto['equipe'] == equip_name:

                    subtract = ponto['score'] - equip_score
                    ponto['score'] = subtract
                    Database.data_teams_write(teams)

                    found = True

                    print()

                    print(f"{equip_score} pontos foram removidos da equipe '{equip_name}'!\nPontuacao final: {subtract}")

                    print()

            if not found:
                print("Equipe nao listada. Tente novamente!")

        if user == 3:
            for select in teams:

                print(f"Time: {select['equipe']} = {select['score']}")

            print()

        if user == 4:
            break