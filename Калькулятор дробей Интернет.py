import tkinter as tk
from tkinter import messagebox
from fractions import Fraction

class FractionCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор дробей")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Поля для ввода первой дроби
        tk.Label(root, text="Дробь 1 (числитель/знаменатель):").pack(pady=5)
        self.entry_num1 = tk.Entry(root, width=5)
        self.entry_num1.pack(pady=2)
        self.entry_den1 = tk.Entry(root, width=5)
        self.entry_den1.pack(pady=2)

        # Выбор операции
        tk.Label(root, text="Операция (+ - * /):").pack(pady=5)
        self.op_var = tk.StringVar(value="+")
        ops_frame = tk.Frame(root)
        ops_frame.pack()
        for op in ["+", "-", "*", "/"]:
            btn = tk.Radiobutton(ops_frame, text=op, variable=self.op_var, value=op)
            btn.pack(side=tk.LEFT, padx=5)

        # Поля для ввода второй дроби
        tk.Label(root, text="Дробь 2 (числитель/знаменатель):").pack(pady=5)
        self.entry_num2 = tk.Entry(root, width=5)
        self.entry_num2.pack(pady=2)
        self.entry_den2 = tk.Entry(root, width=5)
        self.entry_den2.pack(pady=2)

        # Кнопка вычисления
        calc_btn = tk.Button(root, text="Вычислить", command=self.calculate, bg="#dddddd")
        calc_btn.pack(pady=15)

        # Поле результата
        tk.Label(root, text="Результат:").pack()
        self.result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
        self.result_label.pack(pady=5)

    def parse_fraction(self, num_entry, den_entry):
        try:
            num = int(num_entry.get().strip())
            den = int(den_entry.get().strip())
            if den == 0:
                raise ValueError("Знаменатель не может быть нулём.")
            return Fraction(num, den)
        except ValueError as e:
            raise ValueError(f"Некорректный ввод дроби: {e}")

    def calculate(self):
        try:
            f1 = self.parse_fraction(self.entry_num1, self.entry_den1)
            f2 = self.parse_fraction(self.entry_num2, self.entry_den2)
            op = self.op_var.get()

            if op == "+":
                result = f1 + f2
            elif op == "-":
                result = f1 - f2
            elif op == "*":
                result = f1 * f2
            elif op == "/":
                if f2 == 0:
                    raise ZeroDivisionError("Деление на ноль невозможно.")
                result = f1 / f2

            # Форматируем вывод: если знаменатель 1 — показываем как целое число
            if result.denominator == 1:
                display = str(result.numerator)
            else:
                display = f"{result.numerator}/{result.denominator}"

            self.result_label.config(text=display)

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
            self.result_label.config(text="")


root = tk.Tk()
app = FractionCalculator(root)
root.mainloop()
