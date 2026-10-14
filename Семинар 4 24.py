import tkinter as tk

def create_card():
    # Получаем текст и убираем пробелы только с краёв
    name = name_entry.get().strip()
    project = project_entry.get().strip()

    # Проверка на пустоту
    if not name or not project:
        result_label.config(text="Ошибка: заполните имя и проект")
        return

    # Определяем статус связи
    if messages_var.get():
        status = "связь: открыта"
    else:
        status = "связь: закрыта"

    # Формируем итоговую строку
    result_text = f"{name} / {project} / {status}"
    result_label.config(text=result_text)


root = tk.Tk()
root.title("Визитка участника")
root.geometry("620x520")

# --- Блок с полями ввода (группа 1) — голубой фрейм ---
input_frame = tk.Frame(root, width=100, height=10, bg="#ADD8E6", padx=15, pady=15)  # голубой цвет через HEX
input_frame.pack(pady=10, padx=40, anchor="w", fill="x")

name_label = tk.Label(input_frame, text="Имя", bg="#ADD8E6")
name_label.pack(anchor="w")

name_entry = tk.Entry(input_frame)
name_entry.pack(fill="x", pady=5)

project_label = tk.Label(input_frame, text="Проект", bg="#ADD8E6")
project_label.pack(anchor="w")

project_entry = tk.Entry(input_frame)
project_entry.pack(fill="x", pady=5)

# --- Блок с настройками связи (группа 2) — без цвета, как раньше ---
settings_frame = tk.Frame(root)
settings_frame.pack(pady=10, padx=40, anchor="w")

# --- Блок с полями ввода (группа 1) — голубой фрейм ---
input_frame = tk.Frame(root, bg="#ADD8E6", padx=15, pady=15)  # голубой цвет через HEX
input_frame.pack(pady=30, padx=40, anchor="w", fill="x")

messages_var = tk.BooleanVar(value=True)  # По условию флажок изначально включён
messages_cb = tk.Checkbutton(input_frame, text="Открыт к сообщениям", variable=messages_var, width=40, height=2, bg="#ADD8E6")
messages_cb.pack(anchor="w")

# Кнопка «Собрать карточку»
collect_btn = tk.Button(root, text="Собрать карточку", font=("Arial", 10, "bold"), width=35, height=2, command=create_card)
collect_btn.pack(pady=25)

# Фрейм с фоном — широкий и стабильный
result_frame = tk.Frame(
    root,
    bg="#d4edda",
    highlightthickness=1,
    highlightbackground="#c3e6cb",
    width=400,
    height=50
)
# Надпись результата
result_label = tk.Label(result_frame, text="Карточка не создана",width=40, height=2, font=("Arial", 12, "bold"),bg="#d4edda")
result_label.pack(pady=15)

result_frame.pack(pady=20, padx=20, fill="x")

root.mainloop()
