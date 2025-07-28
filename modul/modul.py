class FormaSubmit:

    def __init__(self, fullname,e_mail, phone, login, password):

        self.__fullname = fullname
        self.__e_mail = e_mail
        self.__phone = phone
        self.__login = login
        self.__password = password

    def __str__(self):
        return (f'Полное имя: {self.__fullname}\n'
                f'почта: {self.__e_mail}, телефон: {self.__phone}\n'
                f'логин: {self.__login}\nпароль: {self.__password}')


def __check_list(mass1, mass2):

    if not mass1 or not mass2:
        return f'Список не должен быть пуст'

    elif len(mass1) < 2 or len(mass2) < 2:
        print(mass1, mass2)
        return f'В списке должно быть не меньше 2 элементов'

    elif len(mass1) != len(mass2):
        return f'Количество элементов в списке должно совпадать'

    return ''
