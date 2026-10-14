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
    count = ideas_listbox.size()
    count_label.config(text=f"Идей: {count}")

root = tk.Tk()
root.title("Ловец идей")
root.geometry("520x480")

# Пустое Entry
idea_entry = tk.Entry(root, font=("Arial", 15))
idea_entry.pack(pady=15, padx=20, fill="x")

# Кнопка «Добавить»
add_btn = tk.Button(root, text="Добавить", width=50, height=2, command=add_idea)
add_btn.pack(pady=5)

# Listbox: одиночный выбор (по умолчанию selectmode=SINGLE), изначально ничего не выделено
ideas_listbox = tk.Listbox(root, font=("Arial", 11), height=12)
ideas_listbox.pack(pady=20, padx=20, fill="both", expand=True)

# Надпись «Идей: 0»
count_label = tk.Label(root, text="Идей: 0", font=("Arial", 12))
count_label.pack(pady=50)

root.mainloop()
