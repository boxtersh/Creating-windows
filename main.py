from customtkinter import *
import ctkmessagebox3 as messages
from matplotlib.font_manager import weight_dict
from six import wraps

import modul.modul

'''
def button_click():
    fullname = entry_fullname.get()
    mail = entry_mail.get()
    phone = entry_phone.get()
    login = entry_login.get()
    password = entry_password.get()

    if fullname == '' or mail == '' or phone == '' or login == '' or password == '':
        messages.showwarning(master=main_wind,title = 'Ошибка ввода',message=f'Поле не может быть пустым')
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
'''
# *************************** задание 2 ****************************************************************


def button_click():
    mass1 = entry_mass1.get()
    mass2 = entry_mass2.get()


    mass1 = mass1.split(',')
    mass2= mass2.split(',')

    res = modul.modul.__check_list(mass1,mass2)

    if res != '':
        messages.showwarning(master=main_wind, title='Ошибка ввода', message=f'{res}')
        return ''

    mass1 = list(map(lambda x: int(x), mass1))
    mass2 = list(map(lambda y: int(y), mass2))

    res_txt.delete('0.0','end')
    text = str(list(map(lambda x, y: x*y, mass1, mass2)))
    res_txt.insert('0.0', text)

    entry_mass1.delete(0, END)
    entry_mass2.delete(0, END)
    main_wind.focus()


main_wind = CTk()
main_wind.title('Форма ввода данных')
main_wind.geometry("650x400")
main_wind.resizable(False, False)
main_wind.configure(fg_color=('#2b2f40', 'gray14'))


label_mass1 = CTkLabel(main_wind, text="Массив №1", fg_color="transparent", text_color=("#ffff00", "#DCE4EE"))
label_mass1.grid(row=0, column=0, padx=20, pady=20)


entry_mass1 = CTkEntry(main_wind, width=500, placeholder_text="List 1 [  ]")
entry_mass1.grid(row=0, column=1, padx=20, pady=20)

label_mass2 = CTkLabel(main_wind, text="Массив №2", fg_color="transparent", text_color=("#ffff00", "#DCE4EE"))
label_mass2.grid(row=1, column=0, padx=20, pady=20)

entry_mass2 = CTkEntry(main_wind, width=500, placeholder_text="List 2 [  ]")
entry_mass2.grid(row=1, column=1, padx=20, pady=20)

butt_multi = CTkButton(main_wind, width=50, text="MultiMass", command=button_click, hover = True)
butt_multi.grid(row=2, column=1, padx=20, pady=20)

label_res2 = CTkLabel(main_wind, text="Результат:", fg_color="transparent", text_color=("#ffff00", "#DCE4EE"))
label_res2.grid(row=2, column=0, padx=20, pady=20)

frame = CTkFrame(main_wind, width=600, height=200, fg_color=('#2b2f40', 'gray14'))
main_wind.grid_columnconfigure(0, weight=1)
main_wind.grid_columnconfigure(1, weight=1)
main_wind.grid_columnconfigure(2, weight=1)
frame.grid(row=3, column=1, padx=20, pady=20, sticky='ew')

res_txt = CTkTextbox(frame, height=20, width=300, wrap='none', fg_color="transparent", text_color=("#ffff00", "#DCE4EE"))
res_txt.insert('0.0', 'Ожидание результата')
res_txt.pack(fill=Y)


main_wind.mainloop()