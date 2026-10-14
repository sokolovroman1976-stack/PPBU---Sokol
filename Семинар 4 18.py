import tkinter as tk

last_result = None
memory_value = None


def calculate(operation):
    global last_result

    try:
        a = int(entry_a.get())
        b = int(entry_b.get())

        if operation == "+":
            last_result = a + b
        else:
            last_result = a - b

        result_label.config(text=f"Результат: {last_result}")

    except ValueError:
        last_result = None
        result_label.config(text="Ошибка: введите целые числа")


def plus():
    calculate("+")


def minus():
    calculate("-")


def swap():
    a = entry_a.get()
    b = entry_b.get()

    entry_a.delete(0, tk.END)
    entry_a.insert(0, b)

    entry_b.delete(0, tk.END)
    entry_b.insert(0, a)


def save_to_memory():
    global memory_value

    if last_result is None:
        memory_label.config(text="Сначала выполните вычисление")
        return

    memory_value = last_result
    memory_label.config(text=f"Память: {memory_value}")


def load_from_memory():
    if memory_value is None:
        memory_label.config(text="Память пуста")
        return

    entry_a.delete(0, tk.END)
    entry_a.insert(0, str(memory_value))
    # Можно также загрузить в entry_b, если нужно — сейчас загружаем только в первое поле
    memory_label.config(text=f"Память: {memory_value}")


window = tk.Tk()
window.title("Мой калькулятор")
window.geometry("420x350")

# Первое число
tk.Label(window, text="Первое число", font=("Arial", 9)).pack(pady=5)
entry_a = tk.Entry(window, font=("Arial", 9))
entry_a.pack(pady=5)

# Второе число
tk.Label(window, text="Второе число", font=("Arial", 9)).pack(pady=5)
entry_b = tk.Entry(window, font=("Arial", 9))
entry_b.pack(pady=5)

# Кнопки операций
ops_frame = tk.Frame(window)
ops_frame.pack(pady=10)

tk.Button(ops_frame, text="Сложить", command=plus).grid(row=0, column=0, padx=10)
tk.Button(ops_frame, text="Вычесть", command=minus).grid(row=0, column=1, padx=10)

# Результат
result_label = tk.Label(window, text="Результат: —", font=("Arial", 8))
result_label.pack(pady=5)

# Кнопка «Поменять местами»
swap_frame = tk.Frame(window)
swap_frame.pack(pady=5)
tk.Button(swap_frame, text="Поменять местами", command=swap).pack()

# Память
memory_label = tk.Label(window, text="Память: пуста", font=("Arial", 8))
memory_label.pack(pady=5)

mem_frame = tk.Frame(window)
mem_frame.pack(pady=5)

tk.Button(mem_frame, text="В память", command=save_to_memory).grid(row=0, column=0, padx=8)
tk.Button(mem_frame, text="Из памяти", command=load_from_memory).grid(row=0, column=1, padx=8)

window.mainloop()
