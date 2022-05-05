users_dict = {}


def add_user(dct):
    lastname = input('Enter last name:  ')
    firstname = input('Enter first name:  ')
    age = input("Enter age: ")

    concatenate = lastname + ' ' + firstname
    dct[concatenate] = age


def user_info(dct):
    for i, j in enumerate(dct.items()):
        nm, lnm = j[0].split()[0], j[0].split()[1]
        ag = j[1]
        print(f'User N{i + 1}. Name: {nm.capitalize()}, Lastname: {lnm.capitalize()}, Age: {ag}')


print('''Выберите пункт меню :
1 - добавить нового пользователя ")
2 - информация о всех пользователях ")
3 - Выход
''')

while True:
    menu = input('Введите пункт меню >>> ')
    if menu == '1':
        add_user(users_dict)

    elif menu == '2':
        user_info(users_dict)

    elif menu == '3':
        raise SystemExit

    else:
        print('Не существующий пункт')

        1