import Database

teams = []

def menu():
    print("===== ATIVIDADES =====")

    print()

    print("1. Adicionar Time\n2. Deletar Time\n3. Adicionar Participante\n4. Deletar Participante\n5. Adicionar Pontos"
          "\n6. Tabela")

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

        time = {
            "equipe" : team,
            "lider" : leader,
            "pessoas" : []
        }

        teams.append(time)
        Database.data_teams(teams)

        print()

        user = input("Quer adicionar outro time (N/S)? ").lower().strip()

        if user == 'n':
            break


"""def participants_creation():

    import Database
    
    for people in"""