import tkinter as tk

def calculate_total():
    # Базовая стоимость по выбранному размеру
    if size_var.get() == "small":
        total = 100
    else:
        total = 160

    # Добавляем услуги, если они включены
    if packaging_var.get():
        total += 20
    if urgent_var.get():
        total += 40

    result_label.config(text=f"Итого: {total} жетонов")


root = tk.Tk()
root.title("Заказ для мастерской")
root.geometry("560x460")

# Переменная для выбора размера
size_var = tk.StringVar(value="small")  # по умолчанию выбран «Малый»


size_frame = tk.Frame(root)
size_frame.pack(pady=20, anchor="w")  # anchor="w" прижимает весь блок влево

small_rb = tk.Radiobutton(size_frame, text="Малый", variable=size_var, value="small")
small_rb.pack(anchor="w", pady=5, padx=30)

large_rb = tk.Radiobutton(size_frame, text="Большой", variable=size_var, value="large")
large_rb.pack(anchor="w", pady=5, padx=30)

# --- Блок услуг (слева, друг под другом) ---
services_frame = tk.Frame(root)
services_frame.pack(pady=15, anchor="w")

packaging_var = tk.BooleanVar(value=False)
packaging_cb = tk.Checkbutton(services_frame, text="Упаковка", variable=packaging_var)
packaging_cb.pack(anchor="w", pady=5, padx=30)  # anchor="w" прижмёт флажок к левому краю строки

urgent_var = tk.BooleanVar(value=False)
urgent_cb = tk.Checkbutton(services_frame, text="Срочно", variable=urgent_var)
urgent_cb.pack(anchor="w", pady=5, padx=30)

# --- Кнопка «Рассчитать» (слева) ---
calc_btn = tk.Button(root, text="Рассчитать", width=25, height=2, command=calculate_total)
calc_btn.pack(pady=25)

# Фрейм с фоном — широкий и стабильный
result_frame = tk.Frame(
    root,
    bg="#d4edda",
    highlightthickness=1,
    highlightbackground="#c3e6cb",
    width=400,
    height=50
)
result_frame.pack(pady=20, padx=20, fill="x")
# --- Надпись с результатом (слева) ---
result_label = tk.Label(result_frame, text="Итого: —", font=("Arial", 12, "bold"),bg="#d4edda")
result_label.pack(pady=10)

root.mainloop()
