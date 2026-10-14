import tkinter as tk
from tkinter import messagebox


def get_numbers():
    try:
        return [int(entry.get()) for entry in (e1, e2, e3)]
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Введите три целых числа.")
        return None


def summ():
    values = get_numbers()
    if values is not None:
        a, b, c = values
        result_label.config(text=f"{a} + {b} + {c} = {a + b + c}")


def multiply():
    values = get_numbers()
    if values is not None:
        a, b, c = values
        result_label.config(text=f"{a} × {b} × {c} = {a * b * c}")


window = tk.Tk()
window.title("Калькулятор")
window.geometry("440x300")

tk.Label(
    window,
    text="Введите три числа и нажмите на кнопку для вычисления суммы или произведения",
    wraplength=400
).pack(pady=8)

e1 = tk.Entry(window)
e1.pack(pady=5)

e2 = tk.Entry(window)
e2.pack(pady=5)

e3 = tk.Entry(window)
e3.pack(pady=5)

tk.Button(window, text="Сложить три числа", command=summ).pack(pady=5)
tk.Button(window, text="Умножить три числа", command=multiply).pack(pady=5)

result_label = tk.Label(window, text="Результат:")
result_label.pack(pady=8)

window.mainloop()