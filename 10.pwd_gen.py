# ___ Генератор паролей ___

# импортирование модулей
# import tkinter
from tkinter import Tk, StringVar, Label, Entry, Button
import hashlib


# объект окна
window = Tk()
window.title("Password Generator v.1.0")

# основная функция
def gen(): # def gen(pwd_str: str):
    """
    Функция хеширования строк паролей
    """
    # прием строки сырой пароли
    pwd_str = pwd.get()

    # кодирование в байт-строку
    byte_str = pwd_str.encode() # byte_str = pwd_str.encode()

    # хеширование (применение хеш-функции)
    hash_str = hashlib.sha256(byte_str)

    # преоброзование объект хеш-строки в обычную строку
    hex_str = hash_str.hexdigest()[:10]

    # print(hex_str)

    # запись хеш-строки в объект StringVar
    hash_pwd.set(hex_str)

# gen("password")

# контейнеры для хранения строк 
pwd = StringVar()
hash_pwd = StringVar()

# виджет (компонент) текстовой метки
Label(text="Password:").grid(row=0, column=0, padx=5, pady=5)
# виджет поля ввода
Entry(textvariable=pwd).grid(row=0, column=1, padx=5, pady=5)
# виджет кнопки
btn = Button(text="START", command=gen)
btn.grid(row=1, column=0)
# виджет поля вывода
Entry(textvariable=hash_pwd).grid(row=1, column=1, padx=5, pady=5)

# запуск (точка входа программы)
window.mainloop()