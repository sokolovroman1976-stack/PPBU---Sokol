import turtle

# Настройки экрана
screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Цветик-семицветик")

# Настройки черепашки
t = turtle.Turtle()
t.speed(9)
t.pensize(2)

# Цвета лепестков (радуга)
colors = [
    "#FF0000",  # Красный
    "#FF7F00",  # Оранжевый
    "#FFFF00",  # Желтый
    "#00FF00",  # Зеленый
    "#00BFFF",  # Голубой
    "#0000FF",  # Синий
    "#8B00FF"  # Фиолетовый
]


def draw_petal(color_name):
    """Функция для рисования одного лепестка"""
    t.fillcolor(color_name)
    t.begin_fill()

    # Рисуем дугу влево, затем дугу вправо, чтобы получился лепесток
    t.circle(100)
    t.left(60)
    t.circle(100)
    t.left(60)
    t.circle(100)
    t.left(60)
    t.circle(100)
    t.left(60)
    t.circle(100)
    t.left(60)
    t.circle(100)
    t.left(60)
    t.end_fill()


# Рисуем 7 лепестков по кругу
for color in colors:
    draw_petal(color)
    # Поворачиваем черепашку для следующего лепестка (360 градусов / 7 лепестков ≈ 51.4)
    t.left(360 / 7)

# Рисуем сердцевину цветка
t.penup()
t.goto(0, -25)  # Смещаемся вниз, чтобы центр круга совпал с центром цветка
t.pendown()
t.fillcolor("#FFD700")  # Золотисто-желтый
t.begin_fill()
t.circle(25)
t.end_fill()

# Прячем черепашку и завершаем работу
t.hideturtle()
screen.mainloop()

