import tkinter as tk


def update_pen_thickness():
    global pen_thickness
    try:
        # получаем текст из Entry и конвертируем в целое число
        thickness = int(entry_thickness.get())
        # можно добавить проверку: thickness > 0
        if thickness <= 0:
            raise ValueError("Толщина должна быть положительным числом")
        pen_thickness = thickness
    except ValueError as e:
        # сообщение об ошибке (можно вывести в Label или через messagebox)
        print(f"Ошибка ввода: {e}")
        # можно показать messagebox.showerror("Ошибка", "Введите целое положительное число")
    finally:
        # при необходимости можно обновить отображение толщины на экране
        pass

def draw():
    # отрисовка (пример: линия)
    canvas.create_line(10, 10, 100, 100, fill="black", width=pen_thickness)

# --- НАЧАЛО (замените на ваш текущий код) ---
root = tk.Tk()
root.title("Графический редактор")
root.geometry("400x300")

# текущая толщина пера
pen_thickness = 2

# поле ввода толщины
entry_thickness = tk.Entry(root, width=10)
entry_thickness.pack(pady=10)

# кнопка установки толщины
button_set_thickness = tk.Button(root, text="Установить толщину", command=update_pen_thickness)
button_set_thickness.pack(pady=5)

# холст для рисования
canvas = tk.Canvas(root, bg="white", width=500, height=400)
canvas.pack()





# запуск рисования
draw()

# --- КОНЕЦ ---
root.mainloop()
