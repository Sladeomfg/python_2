__author__ = 'Андриченко Михаил Васильевич'

from hw_04_defs import *
import tkinter
from tkinter import *
import threading

#my_menu()
#my_conn = Get_connect_to_db(host="localhost", database="my_scheme_py",
#                                    user="root", password="Flammable1941")

#______________________________
def main_root():

    def connect_button():
        my_conn = Get_connect_to_db(host="localhost", database="my_scheme_py",
                                    user="root", password="Flammable1941")
        return my_conn

    # ______________________________

    def clear_text():
        output.delete(1.0, END)

    # ______________________________

    def print_button():
        clear_text()
        test = connect_button().print_ai()
        for value in test:
            output.insert("0.0", str(value) + '\n')

    # ______________________________

    def write_to_file_button(filename, exporting_text):
        file = open(filename, "w")
        file.write(str(exporting_text))
        file.close()

    def run_thread():
        _DEVELOPER = connect_button().export_Developer()
        _NAME = connect_button().export_Name()
        t1 = threading.Thread(target=write_to_file_button, args=('My_File1.txt', _DEVELOPER))
        t2 = threading.Thread(target=write_to_file_button, args=('My_File2.txt', _NAME))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

    # ______________________________

    def add_button():
        root1 = Tk()
        root1.title("Добавление нового ИИ")
        root1.minsize(width=150, height=150)
        root1.resizable(width=False, height=False)
        container_for_packs = Frame(root1)
        entry_pack = Frame(root1)
        label_pack = Frame(root1)
        bottom_pack = Frame(root1)

        _ID = Entry(entry_pack, width=15)
        _ID.pack(side='top')
        label_ID = Label(label_pack, text="ID ИИ")
        label_ID.pack(side='top')

        _NAME = Entry(entry_pack, width=15)
        _NAME.pack(side='top')
        label_NAME = Label(label_pack, text="Имя ИИ")
        label_NAME.pack(side='top')

        _DEVELOPER = Entry(entry_pack, width=15)
        _DEVELOPER.pack(side='top')
        label_DEVELOPER = Label(label_pack, text="Разработчик ИИ")
        label_DEVELOPER.pack(side='top')

        _GENDER = Entry(entry_pack, width=15)
        _GENDER.pack(side='top')
        label_GENDER = Label(label_pack, text="Пол ИИ")
        label_GENDER.pack(side='top')

        _AGE = Entry(entry_pack, width=15)
        _AGE.pack(side='top')
        label_AGE = Label(label_pack, text="Возраст ИИ")
        label_AGE.pack(side='top')

        def button1():
            t = connect_button().add_ai(_ID.get(), _NAME.get(), _DEVELOPER.get(), _GENDER.get(), _AGE.get())
            output.insert("0.0", 'ИИ добавлен в базу. ' + '\n')

        butt = Button(bottom_pack, text="Добавить", bg="white", fg="black", width=12, height=1, command=button1, )
        butt.pack(side='top')

        entry_pack.pack(side='right')
        label_pack.pack(side='left')
        container_for_packs.pack(side='top')
        bottom_pack.pack(side='bottom')

        root1.mainloop()

    # ______________________________

    def del_button():
        root2 = Tk()
        root2.title("Удаление ИИ")
        root2.minsize(width=150, height=150)
        root2.resizable(width=False, height=False)
        container_for_packs = Frame(root2)
        entry_pack = Frame(root2)
        label_pack = Frame(root2)
        bottom_pack = Frame(root2)

        _ID = Entry(entry_pack, width=20)
        _ID.pack(side='top')
        _ID.label = Label(label_pack, text='ID удаляемого ИИ из БД')
        _ID.label.pack(side='top')

        def button2():
            t = connect_button().delete_ai(_ID.get(), )
            output.insert("0.0", 'ИИ удалён из базы. ' + '\n')

        butt = tkinter.Button(bottom_pack, text="Удалить", bg="white", fg="black", width=15, height=1, command=button2)
        butt.pack(side='top')

        entry_pack.pack(side='right')
        label_pack.pack(side='left')
        container_for_packs.pack(side='top')
        bottom_pack.pack(side='bottom')

        root2.mainloop()

    # ________________________________________________________

    def change_button():
        root3 = Tk()
        root3.title("Изменение имени ИИ")
        root3.minsize(width=150, height=150)
        root3.resizable(width=False, height=False)
        container_for_packs = Frame(root3)
        entry_pack = Frame(root3)
        label_pack = Frame(root3)
        bottom_pack = Frame(root3)

        _ID = Entry(entry_pack, width=20)
        _ID.pack(side='top')
        _ID.label = Label(label_pack, text='ID изменяемого ИИ')
        _ID.label.pack(side='top')

        _NAME = Entry(entry_pack, width=20)
        _NAME.pack(side='top')
        _NAME.label = Label(label_pack, text='Новое имя для ИИ')
        _NAME.label.pack(side='top')

        def button3():
            t = connect_button().update_name_ai(_NAME.get(), _ID.get())
            output.insert("0.0", 'Имя ИИ успешно изменено. ' + '\n')

        butt = tkinter.Button(bottom_pack, text="Изменить", bg="white", fg="black", width=15, height=1, command=button3)
        butt.pack(side='top')

        entry_pack.pack(side='right')
        label_pack.pack(side='left')
        container_for_packs.pack(side='top')
        bottom_pack.pack(side='bottom')

        root3.mainloop()

    root = Tk()

    root.title("База данных ИИ")
    root.resizable(width=False, height=False)

    Main_frame = Frame(root)
    Text_frame = Frame(root)
    Exit_frame = Frame(root)

    but_add = Button(Main_frame, text='Добавить новый ИИ в базу данных', width=60, height=1, pady=10,
                     bg="white", fg="black", command=add_button)
    but_change = Button(Main_frame, text='Изменить существующее имя ИИ по ID', width=60, height=1, pady=10,
                        bg="white", fg="black", command=change_button)
    but_delete = Button(Main_frame, text='Удалить данные ИИ из базы по ID', width=60, height=1, pady=10,
                        bg="white", fg="black", command=del_button)
    but_print = Button(Main_frame, text='Вывести данные о хранящихся ИИ в базе на экран', width=60, height=1,
                       pady=10, bg="white", fg="black", command=print_button)

    # but_writeToDir = Button(Main_frame, text = 'Выгрузить данные о разработчике и названия \n '
    #                                           'проектов в текстовый файл', width = 60, height = 1,
    #                   pady = 10, bg="white", fg="black", command = run_thread)

    but_clear = Button(Main_frame, text='Очистить поле', width=60, height=1, pady=10,
                       bg="white", fg="black", command=clear_text)

    but_exit = Button(Exit_frame, text='Завершить работу', width=60, height=1, pady=10,
                      bg="gray", fg="black", command=quitnow)

    output = Text(Text_frame, bg="white", width=51, height=15)

    scr = Scrollbar(Text_frame, command=output.yview)
    output.configure(yscrollcommand=scr.set)

    but_add.pack(side='top')
    but_change.pack(side='top')
    but_delete.pack(side='top')
    but_print.pack(side='top')
    # but_writeToDir.pack(side = 'top')
    but_clear.pack(side='top')

    output.pack(side='left')
    scr.pack(side='right')

    but_exit.pack(side='top')

    Main_frame.pack(side='top')
    Text_frame.pack(side='top')
    Exit_frame.pack(side='bottom')

    root.mainloop()

#main_root()
#______________________________