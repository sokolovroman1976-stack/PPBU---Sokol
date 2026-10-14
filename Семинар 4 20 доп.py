import tkinter as tk


def apply_settings():
    # Получаем текущий выбранный режим (0, 1 или 2)
    selected = mode_var.get()

    if selected == 0:
        result_label.config(text="Режим: Фокус")
    elif selected == 1:
        result_label.config(text="Режим: Идеи")
    else:
        result_label.config(text="Режим: Отдых")


root = tk.Tk()
root.title("Режим мастерской")
root.geometry("520x420")

# Переменная для хранения выбранного режима (0=Фокус, 1=Идеи, 2=Отдых)
mode_var = tk.IntVar(value=-1)  # -1 означает «ничего не выбрано»

# Radiobutton вместо Checkbutton: они сами следят, чтобы был выбран только один
fokus_rb = tk.Radiobutton(root, text="Фокус", variable=mode_var, value=0)
fokus_rb.pack(pady=10, padx=20, anchor="w")

idei_rb = tk.Radiobutton(root, text="Идеи", variable=mode_var, value=1)
idei_rb.pack(pady=10, padx=20, anchor="w")

relax_rb = tk.Radiobutton(root, text="Отдых", variable=mode_var, value=2)
relax_rb.pack(pady=10, padx=20, anchor="w")

# Кнопка «Включить»
apply_btn = tk.Button(root, text="Включить", width=40, height=2, command=apply_settings)
apply_btn.pack(pady=20)

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
result_frame.pack_propagate(False)

result_label = tk.Label(
    result_frame,
    text="Режим: не выбран",
    font=("Arial Bold", 13),
    bg="#d4edda"
)
result_label.pack(pady=10, padx=20)

root.mainloop()
