import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор (n операций)")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # Переменная для хранения текущего выражения
        self.expression = ""

        # Поле ввода (только для чтения, чтобы пользователь вводил через кнопки)
        self.input_field = tk.Entry(root, font=("Arial", 18), justify="right", state="readonly")
        self.input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

        # Кнопки
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0, 4)  # C занимает 4 колонки
        ]

        for btn in buttons:
            if len(btn) == 4:  # кнопка "C" (очистка)
                text, row, col, colspan = btn
                b = tk.Button(root, text=text, font=("Arial", 14), command=self.clear)
                b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)
            else:
                text, row, col = btn
                if text == "=":
                    b = tk.Button(root, text=text, font=("Arial", 14), bg="#dddddd", command=self.calculate)
                else:
                    b = tk.Button(root, text=text, font=("Arial", 14), command=lambda t=text: self.on_button_click(t))
                b.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Настройка растягивания сетки
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)

    def on_button_click(self, char):
        """Добавляет символ в выражение и обновляет поле ввода"""
        if char in "+-*/.":
            # Не добавляем два оператора подряд
            if self.expression and self.expression[-1] in "+-*/":
                # Заменяем последний оператор на новый (удобно при ошибке)
                self.expression = self.expression[:-1] + char
            else:
                self.expression += char
        else:
            self.expression += char

        self.update_display()

    def clear(self):
        """Очищает всё выражение"""
        self.expression = ""
        self.update_display()

    def calculate(self):
        """Вычисляет результат выражения"""
        try:
            # eval поддерживает цепочки операций: 2+3*4-5 и т.п.
            result = str(eval(self.expression))
            self.expression = result
            self.update_display()
        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Деление на ноль!")
            self.clear()
        except Exception:
            messagebox.showerror("Ошибка", "Некорректное выражение")
            self.clear()

    def update_display(self):
        """Обновляет текст в поле ввода"""
        self.input_field.config(state="normal")
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.expression)
        self.input_field.config(state="readonly")


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
