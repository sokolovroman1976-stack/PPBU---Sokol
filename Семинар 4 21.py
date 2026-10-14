import tkinter as tk

def plan_time():
    # Получаем текущее значение ползунка (оно уже целое из‑за шага 5)
    minutes = time_scale.get()
    result_label.config(text=f"План: {minutes} мин")

root = tk.Tk()
root.title("Запас времени")
root.geometry("520x420")

# Горизонтальный Scale: от 5 до 60, шаг 5, начальное значение 25
# showvalue=True оставляет отображение текущего значения (по умолчанию включено)
time_scale = tk.Scale(
    root,
    from_=5,
    to=60,
    resolution=5,
    orient=tk.HORIZONTAL,
    length=350,
    tickinterval=5,          # метки через каждые 5 единиц
        # подпись над шкалой (не отдельный Label)
    command=None             # НЕ используем обработчик при движении — по условию
)
time_scale.set(25)            # начальное значение
time_scale.pack(pady=40)

# Кнопка «Запланировать»
plan_btn = tk.Button(
    root,
    text="Запланировать",
    width=50,
    height=2,
    command=plan_time
)
plan_btn.pack(pady=20)

result_frame = tk.Frame(
    root,
    bg="#d4edda",
    highlightthickness=1,
    highlightbackground="#c3e6cb",
    width=400,
    height=50
)
result_frame.pack(pady=20, padx=20, fill="x")
result_frame.pack_propagate(False)

# Надпись с результатом
result_label = tk.Label(result_frame,
    text="План: не задан",
    font=("Arial", 14),
bg="#d4edda"
)
result_label.pack(pady=10, padx=20)

root.mainloop()
