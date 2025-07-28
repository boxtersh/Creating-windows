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