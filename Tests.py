inscriptions_list = [{'name': 'henrique magaieski', 'age': 22, 'phone': '2404742543',
                      'medical': 'antialergics', 'transportation': 'no', 'e-mail' : 'henrimagaieski@icloud.com'},
                     {'name': 'arthur', 'age': 22, 'phone': '2404742543', 'medical': 'polen', 'transportation': 'no',
                      'e-mail': 'something@icloud.com'}]

user = input("Busca: ").lower()

counter = 0
found = False

while counter < len(inscriptions_list):

    person = inscriptions_list[counter]['name']

    if user == person:

        print()

        print(f"Inscricao Localizada:\n{inscriptions_list[counter]}", end='')

        print()

        found = True
        break

    elif person != user:
        counter += 1

if not found:
    print("This person is not listed.")