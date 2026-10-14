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

    # Формируем итоговую строку (внутренние пробелы и регистр сохраняются в name/project)
    result_text = f"{name} / {project} / {status}"
    result_label.config(text=result_text)


root = tk.Tk()
root.title("Визитка участника")
root.geometry("620x520")

# --- Блок с полями ввода (группа 1) ---
input_frame = tk.Frame(root)
input_frame.pack(pady=30, padx=40, anchor="w", fill="x")

name_label = tk.Label(input_frame, text="Имя")
name_label.pack(anchor="w")

name_entry = tk.Entry(input_frame)
name_entry.pack(fill="x", pady=5)

project_label = tk.Label(input_frame, text="Проект")
project_label.pack(anchor="w")

project_entry = tk.Entry(input_frame)
project_entry.pack(fill="x", pady=5)

# --- Блок с настройками связи (группа 2) ---
settings_frame = tk.Frame(root)
settings_frame.pack(pady=10, padx=40, anchor="w")

messages_var = tk.BooleanVar(value=True)  # По условию флажок изначально включён
messages_cb = tk.Checkbutton(settings_frame, text="Открыт к сообщениям", variable=messages_var)
messages_cb.pack(anchor="w")

# Кнопка «Собрать карточку»
collect_btn = tk.Button(root, text="Собрать карточку", width=25, height=2, command=create_card)
collect_btn.pack(pady=25)

# Надпись результата
result_label = tk.Label(root, text="Карточка не создана", font=("Arial", 12))
result_label.pack(pady=15)

root.mainloop()
