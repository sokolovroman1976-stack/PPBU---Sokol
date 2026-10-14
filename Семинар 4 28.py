import tkinter as tk

class EveningPlanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("План вечера")
        self.root.geometry("680x620")
        self.root.minsize(600, 500)

        self.tasks = []  # {name, duration, is_urgent}

        # --- Верхняя часть: поле ввода и срочность ---
        frame_top = tk.Frame(root)
        frame_top.pack(fill=tk.X, padx=15, pady=10)

        self.entry_name = tk.Entry(frame_top, font=("Arial", 12))
        self.entry_name.pack(fill=tk.X, pady=(0, 8))
        self.entry_name.focus_set()

        self.var_urgent = tk.BooleanVar(value=False)
        self.check_urgent = tk.Checkbutton(
            frame_top, text="Срочно", variable=self.var_urgent,
            font=("Arial", 11)
        )
        self.check_urgent.pack(anchor=tk.W)

        # --- Длительность: радиокнопки ---
        frame_radios = tk.Frame(root)
        frame_radios.pack(pady=5)

        self.var_duration = tk.IntVar(value=30)
        radio_opts = [15, 30, 45]
        for d in radio_opts:
            rb = tk.Radiobutton(
                frame_radios,
                text=f"{d} мин",
                variable=self.var_duration,
                value=d,
                font=("Arial", 11)
            )
            rb.pack(side=tk.LEFT, padx=12)

        # --- Кнопка «Добавить» — сразу под radiobutton ---
        btn_add = tk.Button(
            root,
            text="Добавить",
            command=self.add_task,
            font=("Arial", 10),
            width=12
        )
        btn_add.pack(pady=(5, 10))

        # --- Список дел ---
        self.listbox = tk.Listbox(
            root,
            selectmode=tk.SINGLE,
            height=10,
            font=("Consolas", 11),
            exportselection=False
        )
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        # --- Остальные кнопки: Удалить, Вверх, Очистить план ---
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=8)

        btn_style = {"font": ("Arial", 10), "width": 12}
        tk.Button(frame_buttons, text="Удалить", command=self.delete_task, **btn_style).pack(side=tk.LEFT, padx=6)
        tk.Button(frame_buttons, text="Вверх", command=self.move_up, **btn_style).pack(side=tk.LEFT, padx=6)
        tk.Button(frame_buttons, text="Очистить план", command=self.clear_plan, **btn_style).pack(side=tk.LEFT, padx=6)

        # --- Сводка ---
        self.label_stats = tk.Label(
            root,
            text="Дел: 0 | Время: 0 мин",
            font=("Arial", 11, "bold"),
            anchor=tk.CENTER
        )
        self.label_stats.pack(pady=(5, 15))

    # --- Логика ---

    def add_task(self):
        name = self.entry_name.get().strip()
        if not name:
            return

        duration = self.var_duration.get()
        is_urgent = self.var_urgent.get()

        self.tasks.append({
            "name": name,
            "duration": duration,
            "is_urgent": is_urgent
        })

        urgency_text = "срочно" if is_urgent else "обычно"
        display_text = f"{duration} мин | {urgency_text} | {name}"
        self.listbox.insert(tk.END, display_text)

        self.entry_name.delete(0, tk.END)
        self.entry_name.focus_set()
        self.update_stats()

    def delete_task(self):
        selection = self.listbox.curselection()
        if not selection:
            return

        index = selection[0]
        del self.tasks[index]
        self.listbox.delete(index)
        self.listbox.selection_clear(0, tk.END)
        self.update_stats()

    def move_up(self):
        selection = self.listbox.curselection()
        if not selection:
            return

        index = selection[0]
        if index <= 0:
            return

        self.tasks[index], self.tasks[index - 1] = self.tasks[index - 1], self.tasks[index]
        self.rebuild_listbox()

        self.listbox.selection_set(index - 1)
        self.listbox.activate(index - 1)

    def clear_plan(self):
        self.tasks.clear()
        self.listbox.delete(0, tk.END)
        self.listbox.selection_clear(0, tk.END)
        self.update_stats()

    def rebuild_listbox(self):
        self.listbox.delete(0, tk.END)
        for t in self.tasks:
            urgency_text = "срочно" if t["is_urgent"] else "обычно"
            display_text = f"{t['duration']} мин | {urgency_text} | {t['name']}"
            self.listbox.insert(tk.END, display_text)

    def update_stats(self):
        count = len(self.tasks)
        total_time = sum(t["duration"] for t in self.tasks)
        self.label_stats.config(text=f"Дел: {count} | Время: {total_time} мин")



root = tk.Tk()
app = EveningPlanApp(root)
root.mainloop()
