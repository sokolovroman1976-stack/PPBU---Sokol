import tkinter as tk

def add_task():
    raw_text = task_entry.get().strip()
    if not raw_text:
        return

    # Приоритет фиксируется в момент добавления
    if urgent_var.get():
        entry = f"Срочно: {raw_text}"
    else:
        entry = f"Обычно: {raw_text}"

    tasks_listbox.insert(tk.END, entry)
    task_entry.delete(0, tk.END)
    update_counter()
    # Выделение не сбрасываем — сохраняется старое или отсутствует


def delete_task():
    selection = tasks_listbox.curselection()
    if not selection:
        return

    idx = selection[0]
    tasks_listbox.delete(idx)
    tasks_listbox.selection_clear(0, tk.END)  # снимаем выделение
    update_counter()


def move_up():
    selection = tasks_listbox.curselection()
    if not selection:
        return

    idx = selection[0]
    # Нельзя поднять первую строку
    if idx == 0:
        return

    current_text = tasks_listbox.get(idx)
    prev_text = tasks_listbox.get(idx - 1)

    # Удаляем оба элемента
    tasks_listbox.delete(idx - 1, idx)
    # Вставляем в обратном порядке
    tasks_listbox.insert(idx - 1, current_text)
    tasks_listbox.insert(idx, prev_text)

    # Перемещаем выделение на новую позицию строки
    tasks_listbox.selection_set(idx - 1)
    tasks_listbox.see(idx - 1)


def update_counter():
    count = tasks_listbox.size()
    counter_label.config(text=f"Дел: {count}")


root = tk.Tk()
root.title("Очередь с приоритетом")
root.geometry("620x520")

# Entry для названия задачи
task_entry = tk.Entry(root, font=("Arial", 12))
task_entry.pack(pady=15, padx=20, fill="x")

# Фрейм для флажка «Срочно» и кнопки «Добавить»
controls_frame = tk.Frame(root)
controls_frame.pack(pady=5, padx=20, anchor="w", fill="x")

urgent_var = tk.BooleanVar(value=False)
urgent_cb = tk.Checkbutton(controls_frame,  font=("Arial", 10), text="Срочно", variable=urgent_var)
urgent_cb.pack(side="left", anchor="w")

add_btn = tk.Button(controls_frame,  font=("Arial", 10, "bold"), text="Добавить", width=12, height=2, command=add_task)
add_btn.pack(side="right", anchor="e")  # кнопка справа от флажка

# Listbox: одиночный выбор, ничего не выделено
tasks_listbox = tk.Listbox(root, font=("Arial", 11), height=6)
tasks_listbox.pack(pady=10, padx=20, fill="both", expand=True)

# Панель кнопок «Удалить» и «Вверх»
btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

delete_btn = tk.Button(btn_frame, font=("Arial", 10, "bold"),  text="Удалить", width=12, height=2, command=delete_task)
delete_btn.pack(side="left", padx=8)

up_btn = tk.Button(btn_frame,  font=("Arial", 10, "bold"), text="Вверх", width=12, height=2, command=move_up)
up_btn.pack(side="left", padx=8)

result_frame = tk.Frame(
    root,
    bg="#d4edda",
    highlightthickness=1,
    highlightbackground="#c3e6cb",
    width=400,
    height=50
)
# Надпись со счётчиком
counter_label = tk.Label(result_frame, text="Дел: 0", font=("Arial", 12), bg="#d4edda")
counter_label.pack(pady=20)
result_frame.pack(pady=20, padx=20, fill="x")

root.mainloop()
