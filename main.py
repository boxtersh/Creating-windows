from customtkinter import *
import ctkmessagebox3 as messages

import modul.modul


def button_click():
    fullname = entry_fullname.get()
    mail = entry_mail.get()
    phone = entry_phone.get()
    login = entry_login.get()
    password = entry_password.get()

    if fullname == '':
        messages.showwarning(master=main_wind,title = 'Ошибка ввода',message=f'Поле "Полное имя" не может быть пустым')
        return
    elif mail == '':
        messages.showwarning(master=main_wind,title = 'Ошибка ввода',message=f'Поле "mail" не может быть пустым')
        return
    elif phone == '':
        messages.showwarning(master=main_wind,title = 'Ошибка ввода',message=f'Поле "phone" не может быть пустым')
        return
    elif login == '':
        messages.showwarning(master=main_wind,title = 'Ошибка ввода',message=f'Поле "login" не может быть пустым')
        return
    elif password == '':
        messages.showwarning(master=main_wind,title = 'Ошибка ввода',message=f'Поле "password" не может быть пустым')
        return

    user_data = modul.modul.FormaSubmit(fullname,mail,phone,login,password)
    entry_fullname.delete(0,END)
    entry_mail.delete(0, END)
    entry_phone.delete(0, END)
    entry_login.delete(0, END)
    entry_password.delete(0, END)
    print(user_data)
    messages.showsuccess(master=main_wind, title='Информация', message='Сообщение успешно отправлено')




main_wind = CTk()
main_wind.title('Форма ввода данных')
main_wind.geometry("600x400")
main_wind.resizable(False, False)
main_wind.configure(fg_color=('#2b2f40', 'gray14'))


label_fullname = CTkLabel(main_wind, text="Полное имя", fg_color="transparent", text_color=("#ffff00", "#DCE4EE"))
label_fullname.pack()
entry_fullname = CTkEntry(main_wind, width=500, placeholder_text="Иванов Иван Иванович")
entry_fullname.pack()

frame_1 = CTkFrame(main_wind, width = 900, height=500)
frame_1.configure(fg_color=('#3f5156', 'gray14'))
frame_1.pack()

label_mail = CTkLabel(frame_1, text="Укажите почту", fg_color="transparent", text_color=("#ffff00", "#DCE4EE"))
label_mail.grid(row=0, column=0, padx=20, pady=20)

entry_mail = CTkEntry(frame_1, width=230, placeholder_text="mail")
entry_mail.grid(row=1, column=0, padx=20, pady=20)

label_phone = CTkLabel(frame_1, text="Укажите телефон", fg_color="transparent", text_color=("#ffff00", "#DCE4EE"))
label_phone.grid(row=0, column=1, padx=20, pady=20)

entry_phone = CTkEntry(frame_1, width=230, placeholder_text="88005005050")
entry_phone.grid(row=1, column=1, padx=20, pady=20)

label_login = CTkLabel(frame_1, text="Укажите логин", fg_color="transparent", text_color=("#ffff00", "#DCE4EE"))
label_login.grid(row=2, column=0, padx=20, pady=20)

entry_login = CTkEntry(frame_1, width=230, placeholder_text="login")
entry_login.grid(row=3, column=0, padx=20, pady=20)

label_password = CTkLabel(frame_1, width=230, text="Укажите пароль", fg_color="transparent", text_color=("#ffff00", "#DCE4EE"))
label_password.grid(row=2, column=1, padx=20, pady=20)

entry_password = CTkEntry(frame_1, width=230, placeholder_text="password")
entry_password.grid(row=3, column=1, padx=20, pady=20)

butt_submit = CTkButton(main_wind, text="Submit", command=button_click, hover = True)
butt_submit.pack()


main_wind.mainloop()

# name = entry.get