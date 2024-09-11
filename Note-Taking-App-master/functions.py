###################################################################################################################################
##################################### NOTE TAKING APP (NOTESPRO) ##################################################################
###################################################################################################################################
# Импорт необходимых библиотек
from tkinter import *  # для создания графического интерфейса
import pymysql as pm   # для подключения к базе данных MySQL
from tkinter import messagebox  # для отображения всплывающих сообщений

# Инициализация главного окна
root = Tk()
root.title("Note Taking App")  # Заголовок окна

# Основная метка для приложения
p = Label(root, text='Notespro', height="20", width="40", bg='#145660', fg='white',
          font=('Helvetica', '18', 'bold', 'italic'))
p.place(x=470, y=90)  # Размещение метки

root.configure(bg='#145660')  # Установка фона главного окна
root.geometry('1920x1080')  # Размер окна

# ################################## ДОБАВЛЕНИЕ НОВЫХ ЗАМЕТОК #####################################################
def notes():
    # Создание нового окна для добавления заметок
    root = Tk()
    root.title("Add Notes")  # Заголовок окна
    root.geometry("1930x1080")  # Установка размеров окна

    # Настройка основного интерфейса
    z = Label(root, height='22', width="100", bg='#636466', font=('Helvetica', '20', 'italic'))
    z.pack()  # Позиционирование главной метки

    # Метка для создания ID заметки
    g = Label(root, height="2", width="12", bg='#636466', fg="white", text="Create Note ID :",
              font=('Helvetica', '18', 'italic'))
    g.place(x=400, y=38)

    root.configure(bg="black")  # Фоновый цвет окна для добавления заметки

    # Поле ввода для ID заметки
    tt = Entry(root, bd=5, width='45', font=('Helvetica', '19'))
    tt.place(x=611, y=50)

    # Текстовое поле для ввода текста заметки
    txt = Text(root, width='80', height='20', font=('Helvetica', '15'))
    txt.place(x=370, y=100)

    # Функция для сохранения новых заметок в базе данных
    def addnotes():
        try:
            global hu
            hu = int(tt.get())  # Получение ID заметки
            tu = txt.get("1.0", "end-1c")  # Получение текста заметки
            # Подключение к базе данных
            con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
            cursor = con.cursor()
            # SQL-запрос для добавления новой заметки
            query_insert = "insert into test(id, text) values(%d, '%s')" % (hu, tu)
            cursor.execute(query_insert)
            con.commit()  # Подтверждение изменений в базе данных
        except pm.DatabaseError as e:
            if con:
                con.rollback()  # Откат транзакции в случае ошибки
                print(e)
        finally:
            con.close()  # Закрытие соединения
            cursor.close()

    # Кнопка "Сохранить"
    butto2 = Button(root, text="Save>>", command=addnotes, bg="red", padx=50, pady=10, fg='white',
                    font=('Helvetica', '8', 'bold'))
    butto2.place(x=1080, y=580)

    # Кнопка "Выйти", закрывающая окно
    butto3 = Button(root, text="Quit", command=root.destroy, bg="red", padx=50, pady=10, fg='white',
                    font=('Helvetica', '8', 'bold'))
    butto3.pack(pady=25)

    # Запуск главного цикла обработки событий
    root.mainloop()

# Кнопка для запуска окна добавления заметок
butt1 = Button(root, text="Add New Notes>>", command=notes, bg="red", padx=40, pady=10, bd=7, fg='white',
               font=('Helvetica', 12, 'bold'))
butt1.place(x=370, y=20)

# ################################## РЕДАКТИРОВАНИЕ ЗАМЕТОК ########################################################
def ed():
    # Создание нового окна для редактирования заметок
    root = Tk()
    root.title("Edit Notes")  # Заголовок окна
    root.geometry("1930x1080")  # Установка размеров окна

    # Настройка интерфейса
    p = Label(root, height='22', width="100", bg='#636466', font=('Helvetica', '20', 'italic'))
    p.pack()  # Позиционирование метки

    # Метка для ввода ID заметки
    q = Label(root, height="2", width="12", bg='#636466', fg="white", text="Enter Note ID :",
              font=('Helvetica', '18', 'italic'))
    q.place(x=400, y=38)

    root.configure(bg="black")  # Фоновый цвет окна

    # Поле ввода для ID заметки
    tt = Entry(root, bd=5, width='45', font=('Helvetica', '19'))
    tt.place(x=611, y=50)

    # Текстовое поле для ввода нового содержания заметки
    txt = Text(root, width='80', height='20', font=('Helvetica', '15'))
    txt.place(x=370, y=100)

    # Функция для обновления заметки в базе данных
    def editmsg():
        try:
            hu = int(tt.get())  # Получение ID заметки
            tu = txt.get("1.0", "end-1c")  # Получение нового текста заметки
            # Подключение к базе данных
            con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
            cursor = con.cursor()
            # SQL-запрос для обновления заметки
            query_text = "update test set text='%s' where id=%d" % (tu, hu)
            cursor.execute(query_text)
            con.commit()  # Подтверждение изменений
        except pm.DatabaseError as e:
            if con:
                con.rollback()  # Откат транзакции при ошибке
        finally:
            cursor.close()  # Закрытие курсора и соединения
            con.close()

    # Кнопка "Сохранить"
    butto2 = Button(root, text="Save>>", command=editmsg, bg="red", padx=50, pady=10, fg='white',
                    font=('Helvetica', '8', 'bold'))
    butto2.place(x=1080, y=580)

    # Кнопка "Выйти", закрывающая окно
    butto3 = Button(root, text="Quit", command=root.destroy, bg="red", padx=50, pady=10, fg='white',
                    font=('Helvetica', '8', 'bold'))
    butto3.pack(pady=25)

    # Запуск главного цикла обработки событий
    root.mainloop()

# Кнопка для запуска окна редактирования заметок
but = Button(root, text="Edit Notes>>", command=ed, bg="red", padx=55, pady=10, bd=7, fg='white',
             font=('Helvetica', 12, 'bold'))
but.place(x=950, y=20)

# #################################### ЛИСТБОКС #########################################################
# Листбокс для отображения найденных или отсортированных заметок
r = Listbox(root, width='73', height='13', font=('Helvetica', '15'))
r.place(x=370, y=400)

# #################################### ПОИСК ############################################################
# Метка для ввода ID заметки для поиска
q = Label(root, text='Enter Note ID :', bg='#145660', fg='white', font=('Helvetica', '15', 'bold'))
q.place(x=400, y=220)

# Поле ввода для ID заметки для поиска
s1 = Entry(root, bd=5, width='52', font=('Helvetica', '19'))
s1.place(x=400, y=250)

# Функция для поиска заметок по ID
def search():
    try:
        k = int(s1.get())  # Получение ID заметки
        # Подключение к базе данных
        con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
        cursor = con.cursor()
        # SQL-запрос для поиска заметки по ID
        searchquery = "select * from test where id={}".format(k)
        cursor.execute(searchquery)
        data = cursor.fetchone()  # Получение результата
        r.insert(END, data)  # Вставка результата в листбокс
        con.commit()  # Подтверждение изменений
    except pm.DatabaseError as e:
        if con:
            con.rollback()  # Откат транзакции при ошибке
    finally:
        con.close()  # Закрытие соединения
        cursor.close()

# Кнопка для поиска заметки
butt3 = Button(root, text="Search>>", bg="red", padx=25, pady=5, bd=5, fg='white',
               font=('Helvetica', '10', 'bold'), command=search)
butt3.place(x=610, y=305)

# #################################### УДАЛЕНИЕ ##########################################################
# Функция для удаления заметки из базы данных
def delete():
    try:
        k = int(s1.get())  # Получение ID заметки
        # Подключение к базе данных
        con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
        cursor = con.cursor()
        # SQL-запрос для удаления заметки
        delete_query = "delete from test where id={}".format(k)
        cursor.execute(delete_query)
        con.commit()  # Подтверждение изменений
    except pm.DatabaseError as e:
        if con:
            con.rollback()  # Откат транзакции при ошибке
            print(e)
    finally:
        con.close()  # Закрытие соединения
        cursor.close()

# Кнопка для удаления заметки
butt4= Button(root, text="Delete>>", bg="red", padx=25, pady=5, bd=5, fg='white',font=('Helvetica', '10', 'bold'),command=delete)
butt4.place(x=790,y=305)

#########################################################################################################################################
########################################### SORT NOTES ##################################################################################
#########################################################################################################################################

# Метка для списка всех заметок
lab = Label(root, text='List All Notes :', bg='#145660', fg='white', font=('Helvetica', '15', 'bold'))
lab.place(x=700, y=100)

# Функция для сортировки заметок в алфавитном порядке
def sortalpha():
    try:
        # Подключение к базе данных
        con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
        cursor = con.cursor()
        # SQL-запрос для сортировки заметок по тексту (в алфавитном порядке)
        query_show = "SELECT * from test ORDER BY text ASC"
        cursor.execute(query_show)
        data = cursor.fetchall()  # Получение всех отсортированных данных
        raw = list(data)  # Преобразование данных в список

        # Создание нового окна для отображения отсортированных заметок
        root = Tk()
        root.title("List of notes (Sorted in Asc Alphabets)")
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)  # Позиционирование полосы прокрутки
        root.geometry("500x800")  # Установка размеров окна

        # Листбокс для вывода отсортированных заметок
        mylist = Listbox(root, width="900", yscrollcommand=scrollbar.set, font=('Helvetica', '15', 'italic'))
        for l in raw:
            mylist.insert(END, l)  # Добавление каждой заметки в листбокс
        mylist.pack(side=LEFT, fill=BOTH)

        # Связывание прокрутки с листбоксом
        scrollbar.config(command=mylist.yview)
        root.mainloop()

        con.commit()  # Подтверждение изменений
    except pm.DatabaseError as e:
        if con:
            con.rollback()  # Откат транзакции при ошибке
            print(e)
    finally:
        con.close()  # Закрытие соединения
        cursor.close()

# Кнопка для сортировки заметок по алфавиту
bu = Button(root, text="By Alphabets >>", bg="red", padx=25, pady=5, bd=5, fg='white',
            font=('Helvetica', '10', 'bold'), command=sortalpha)
bu.place(x=530, y=150)

# Функция для сортировки заметок по ID (в порядке возрастания)
def sortnum():
    try:
        # Подключение к базе данных
        con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
        cursor = con.cursor()
        # SQL-запрос для сортировки заметок по ID
        query_show = "SELECT * from test ORDER BY id ASC"
        cursor.execute(query_show)
        data = cursor.fetchall()  # Получение всех отсортированных данных
        raw = list(data)  # Преобразование данных в список

        # Создание нового окна для отображения отсортированных заметок
        root = Tk()
        root.title("List of notes (Sorted in ASC Numbers)")
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)  # Позиционирование полосы прокрутки
        root.geometry("500x800")  # Установка размеров окна

        # Листбокс для вывода отсортированных заметок
        mylist = Listbox(root, width="900", yscrollcommand=scrollbar.set, font=('Helvetica', '15', 'italic'))
        for l in raw:
            mylist.insert(END, l)  # Добавление каждой заметки в листбокс
        mylist.pack(side=LEFT, fill=BOTH)

        # Связывание прокрутки с листбоксом
        scrollbar.config(command=mylist.yview)
        root.mainloop()

        con.commit()  # Подтверждение изменений
    except pm.DatabaseError as e:
        if con:
            con.rollback()  # Откат транзакции при ошибке
            print(e)
    finally:
        con.close()  # Закрытие соединения
        cursor.close()

# Кнопка для сортировки заметок по номерам (ID)
bu1 = Button(root, text="By Numbers >>", bg="red", padx=25, pady=5, bd=5, fg='white',
             font=('Helvetica', '10', 'bold'), command=sortnum)
bu1.place(x=820, y=150)

# #################################### ВЫХОД ИЗ ПРИЛОЖЕНИЯ #############################################################

# Кнопка для выхода из приложения
butt6 = Button(root, text="Exit", command=root.destroy, bg="red", fg='white', padx=50, pady=10, bd=5,
               font=('Helvetica', '10', 'bold'))
butt6.place(x=710, y=750)

# Запуск главного цикла обработки событий
root.mainloop()