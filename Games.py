import Database

teams = []

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

#def participants_creation():
