import tkinter as tk
from tkinter import messagebox

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def calculate_detour():
    try:
        # Считываем координаты
        xA = int(entry_xA.get())
        yA = int(entry_yA.get())
        xB = int(entry_xB.get())
        yB = int(entry_yB.get())
        xC = int(entry_xC.get())
        yC = int(entry_yC.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа во все поля.")
        return

    # Считаем расстояния
    L_AB = manhattan(xA, yA, xB, yB)
    L_AC = manhattan(xA, yA, xC, yC)
    L_CB = manhattan(xC, yC, xB, yB)
    L_ACB = L_AC + L_CB
    extra = L_ACB - L_AB

    # Формируем текст результата
    result_text = (
        f"Кратчайший путь A→B: {L_AB} клеток\n"
        f"Путь через C (A→C→B): {L_ACB} клеток\n"
    )

    if extra == 0:
        result_text += "✅ Точка C лежит на кратчайшем маршруте. Крюка нет."
    else:
        result_text += f"⚠️ Лишний крюк: {extra} клеток."

    label_result.config(text=result_text)

# Создаём главное окно
root = tk.Tk()
root.title("Мини-навигатор: расчёт крюка")
root.geometry("400x500")

# Фрейм для полей ввода
frame_inputs = tk.Frame(root, padx=10, pady=10)
frame_inputs.pack()

# Функция для создания строки с меткой и полем ввода
def create_input_row(parent, label_text, row, col_label=0, col_entry=1):
    lbl = tk.Label(parent, text=label_text, width=12, anchor="e")
    lbl.grid(row=row, column=col_label, padx=5, pady=5)
    entry = tk.Entry(parent, width=10)
    entry.grid(row=row, column=col_entry, padx=5, pady=5)
    return entry

# Поля для точки A
tk.Label(frame_inputs, text="Точка A (x, y)", font=("Arial", 11, "bold")).grid(
    row=0, column=0, columnspan=2, pady=(0, 10)
)
entry_xA = create_input_row(frame_inputs, "x A:", 1)
entry_yA = create_input_row(frame_inputs, "y A:", 2)

# Поля для точки B
tk.Label(frame_inputs, text="Точка B (x, y)", font=("Arial", 11, "bold")).grid(
    row=3, column=0, columnspan=2, pady=(15, 10)
)
entry_xB = create_input_row(frame_inputs, "x B:", 4)
entry_yB = create_input_row(frame_inputs, "y B:", 5)

# Поля для точки C
tk.Label(frame_inputs, text="Точка C (x, y)", font=("Arial", 11, "bold")).grid(
    row=6, column=0, columnspan=2, pady=(15, 10)
)
entry_xC = create_input_row(frame_inputs, "x C:", 7)
entry_yC = create_input_row(frame_inputs, "y C:", 8)

# Кнопка расчёта
btn_calc = tk.Button(
    root,
    text="Посчитать крюк",
    command=calculate_detour,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=5
)
btn_calc.pack(pady=15)

# Метка для вывода результата
label_result = tk.Label(
    root,
    text="Здесь появится результат расчёта",
    justify="left",
    font=("Consolas", 11),
    anchor="w"
)
label_result.pack(fill="both", expand=True, padx=15)

# Запуск цикла событий
root.mainloop()