import tkinter as tk
from tkinter import messagebox as mb, Label


def summ():
    s1 = e1.get()
    if not s1.lstrip('-').isdigit():
        mb.showerror("Error", "Please enter a number")
        return
    s2 = e2.get()
    if not s2.lstrip('-').isdigit():
        mb.showerror("Error", "Please enter a number")
        return
    s3 = e3.get()
    if not s3.lstrip('-').isdigit():
        mb.showerror("Error", "Please enter a number")
        return
    slag_1 = int(s1)
    slag_2 = int(s2)
    slag_3 = int(s3)
    summa = slag_1 + slag_2 + slag_3
    m1["text"] = f"{s1} + {s2} + {s3}= {summa}"

def multiply():
    s1 = e1.get()
    if not s1.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Пожалуйста введите число")
        return
    s2 = e2.get()
    if not s2.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Пожалуйста введите число")
        return
    s3 = e3.get()
    if not s3.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Пожалуйста введите число")
        return
    slag_1 = int(s1)
    slag_2 = int(s2)
    slag_3 = int(s3)
    mult = slag_1 * slag_2 * slag_3
    m1["text"] = f"{s1} * {s2} * {s3}= {mult}"


    answer = mb.askretrycancel(title="Вопрос", message="Что дальше делать?")
    if answer:
        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        m1['text'] = " "
    else:
        window.destroy()

window = tk.Tk()
window.title("Калькулятор")
window.geometry("500x300")
m = Label(height = 3, text="Введите три числа и нажмите на кнопку для вычисления суммы или произведения")
m.pack()

e1 = tk.Entry(window)
e1.pack(pady=5)

e2 = tk.Entry(window)
e2.pack(pady=5)

e3 = tk.Entry(window)
e3.pack(pady=5)
e3.pack()
tk.Button(window, text="Сложить три числа", command=summ).pack(pady=5)
tk.Button(window, text="Умножить три числа", command=multiply).pack(pady=5)

m1 = Label(height=3)
m1.pack()


window.mainloop()