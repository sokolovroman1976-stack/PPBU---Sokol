import tkinter as tk
from fractions import Fraction


def calculate():
    try:
        first = Fraction(int(num1.get()), int(den1.get()))
        second = Fraction(int(num2.get()), int(den2.get()))
        operation = oper.get().strip()

        if operation == "+":
            result = first + second
        elif operation == "-":
            result = first - second
        elif operation == "*":
            result = first * second
        elif operation == "/":
            result = first / second
        else:
            status.config(text="Введите операцию: +, -, * или /")
            return

        sign = "-" if result < 0 else ""
        whole, remainder = divmod(
            abs(result.numerator),
            result.denominator
        )

        if result == 0:
            res_int.config(text="0")
        else:
            res_int.config(text=f"{sign}{whole}" if whole else sign)

        if remainder:
            num3.config(text=str(remainder))
            den3.config(text=str(result.denominator))
        else:
            num3.config(text="")
            den3.config(text="")

        status.config(text="")

    except ValueError:
        status.config(text="Введите целые числа в поля дробей")
    except ZeroDivisionError:
        status.config(text="Знаменатель и делитель не могут быть равны нулю")


root = tk.Tk()
root.title("Калькулятор дробей")
root.geometry("440x190")

frame = tk.Frame(root)
frame.pack(pady=15)

num1 = tk.Entry(frame, width=5, justify="center", font=("Arial", 15))
num1.grid(row=0, column=0)

tk.Label(frame, text="—", font=("Arial", 15)).grid(row=1, column=0)

den1 = tk.Entry(frame, width=5, justify="center", font=("Arial", 15))
den1.grid(row=2, column=0)

oper = tk.Entry(frame, width=3, justify="center", font=("Arial", 15))
oper.grid(row=1, column=1, padx=8)

num2 = tk.Entry(frame, width=5, justify="center", font=("Arial", 15))
num2.grid(row=0, column=2)

tk.Label(frame, text="—", font=("Arial", 15)).grid(row=1, column=2)

den2 = tk.Entry(frame, width=5, justify="center", font=("Arial", 15))
den2.grid(row=2, column=2)

btn = tk.Button(frame, text="=", font=("Arial", 15), command=calculate)
btn.grid(row=1, column=3, padx=8)

res_int = tk.Label(frame, text="0", width=3, bg="light gray",
                   font=("Arial", 15))
res_int.grid(row=1, column=4, padx=4)

num3 = tk.Label(frame, text="", width=5, bg="light gray",
                font=("Arial", 15))
num3.grid(row=0, column=5)

tk.Label(frame, text="—", font=("Arial", 15)).grid(row=1, column=5)

den3 = tk.Label(frame, text="", width=5, bg="light gray",
                font=("Arial", 15))
den3.grid(row=2, column=5)

status = tk.Label(root, text="", fg="red")
status.pack()

root.mainloop()