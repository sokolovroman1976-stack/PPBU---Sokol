import tkinter as tk

def add_idea():
    # Получаем текст и убираем пробелы только с краёв
    raw_text = idea_entry.get()
    cleaned_text = raw_text.strip()

    # Если после обрезки ничего не осталось — ничего не делаем
    if not cleaned_text:
        return

    # Добавляем в конец списка (дубликаты разрешены)
    ideas_listbox.insert(tk.END, cleaned_text)

    # Очищаем поле ввода
    idea_entry.delete(0, tk.END)

    # Обновляем счётчик
    update_counter()


def delete_selected():
    # Получаем индексы выделенных элементов (кортеж)
    selection = ideas_listbox.curselection()

    # Удаляем только если что-то выбрано (для одиночного выбора достаточно первого элемента)
    if selection:
        idx = selection[0]
        ideas_listbox.delete(idx)
        update_counter()
        # Выделение автоматически снимется; по условию это допустимо


def update_counter():
    count = ideas_listbox.size()
    count_label.config(text=f"Идей: {count}")


root = tk.Tk()
root.title("Ловец идей")
root.geometry("520x480")

# Пустое Entry
idea_entry = tk.Entry(root, font=("Arial", 11))
idea_entry.pack(pady=15, padx=20, fill="x")

# Кнопка «Добавить»
add_btn = tk.Button(root, text="Добавить", width=20, height=2, command=add_idea)
add_btn.pack(pady=5)

# Listbox: одиночный выбор (по умолчанию selectmode=SINGLE), изначально ничего не выделено
ideas_listbox = tk.Listbox(root, font=("Arial", 11), height=12)
ideas_listbox.pack(pady=10, padx=20, fill="both", expand=True)

delete_btn = tk.Button(root, text="Удалить", width=20, height=2, command=delete_selected)
delete_btn.pack(pady=5)

# Фрейм с фоном — широкий и стабильный
result_frame = tk.Frame(
    root,
    bg="#d4edda",
    highlightthickness=1,
    highlightbackground="#c3e6cb",
    width=400,
    height=50
)
count_label = tk.Label(result_frame, text="Идей: 0", font=("Arial", 12),bg="#d4edda")

count_label.pack(pady=10)
result_frame.pack(pady=20, padx=20, fill="x")


root.mainloop()
