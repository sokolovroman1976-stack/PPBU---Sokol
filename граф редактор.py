import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Простой графический редактор")
        self.root.geometry("800x600")

        # Переменные состояния
        self.brush_size = 3
        self.color = "black"
        self.drawing_tool = "pencil"  # pencil, line, rect, oval
        self.start_x, self.start_y = None, None
        self.temp_item = None

        # Панель управления
        toolbar = tk.Frame(root, bg="#f0f0f0", pady=5)
        toolbar.pack(fill=tk.X)

        tools = [
            ("Карандаш", "pencil"),
            ("Линия", "line"),
            ("Прямоугольник", "rect"),
            ("Овал", "oval"),
        ]
        for text, tool in tools:
            btn = tk.Button(
                toolbar, text=text, command=lambda t=tool: self.set_tool(t),
                padx=8, pady=4
            )
            btn.pack(side=tk.LEFT, padx=4)

        tk.Label(toolbar, text="Толщина:", bg="#f0f0f0").pack(side=tk.LEFT, padx=8)
        self.size_var = tk.StringVar(value="3")
        size_entry = tk.Entry(toolbar, textvariable=self.size_var, width=3)
        size_entry.pack(side=tk.LEFT)
        size_entry.bind("<Return>", self.update_brush_size)

        btn_color = tk.Button(toolbar, text="Цвет", command=self.choose_color, padx=8, pady=4)
        btn_color.pack(side=tk.LEFT, padx=8)

        btn_clear = tk.Button(toolbar, text="Очистить холст", command=self.clear_canvas, padx=8, pady=4)
        btn_clear.pack(side=tk.RIGHT, padx=8)

        # Холст
        self.canvas = tk.Canvas(root, bg="white", cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Привязка событий
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def set_tool(self, tool):
        self.drawing_tool = tool
        self.canvas.config(cursor="cross" if tool == "pencil" else "plus")

    def choose_color(self):
        color = colorchooser.askcolor(color=self.color)[1]
        if color:
            self.color = color

    def update_brush_size(self, event=None):
        try:
            size = int(self.size_var.get())
            if size < 1:
                size = 1
            self.brush_size = size
        except ValueError:
            pass

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.temp_item = None

        if self.drawing_tool == "pencil":
            # Рисуем точку, чтобы не было разрыва при первом клике
            self.canvas.create_oval(
                event.x - self.brush_size // 2,
                event.y - self.brush_size // 2,
                event.x + self.brush_size // 2,
                event.y + self.brush_size // 2,
                fill=self.color, outline=self.color
            )

    def on_drag(self, event):
        if self.drawing_tool == "pencil":
            self.canvas.create_line(
                self.start_x, self.start_y, event.x, event.y,
                width=self.brush_size, fill=self.color, capstyle=tk.ROUND, smooth=True
            )
            self.start_x, self.start_y = event.x, event.y

        elif self.drawing_tool in ("line", "rect", "oval"):
            # Удаляем предыдущую временную фигуру
            if self.temp_item:
                self.canvas.delete(self.temp_item)

            x0, y0 = self.start_x, self.start_y
            x1, y1 = event.x, event.y

            if self.drawing_tool == "line":
                self.temp_item = self.canvas.create_line(x0, y0, x1, y1,
                                                        width=self.brush_size, fill=self.color)
            elif self.drawing_tool == "rect":
                self.temp_item = self.canvas.create_rectangle(x0, y0, x1, y1,
                                                             outline=self.color, width=self.brush_size)
            elif self.drawing_tool == "oval":
                self.temp_item = self.canvas.create_oval(x0, y0, x1, y1,
                                                         outline=self.color, width=self.brush_size)

    def on_release(self, event):
        if self.drawing_tool in ("line", "rect", "oval") and self.temp_item:
            # Финальная фигура остаётся на холсте
            self.temp_item = None
        # Для карандаша ничего дополнительно не нужно — линии уже нарисованы

    def clear_canvas(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
