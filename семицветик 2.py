
import turtle

# Настройки экрана
screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Цветик-семицветик")

# Настройки черепашки
t = turtle.Turtle()
t.speed(5)
t.pensize(1)

# Цвета лепестков (радуга)
colors = [
    "#FF0000",  # Красный
    "#FF7F00",  # Оранжевый
    "#FFFF00",  # Желтый
    "#00FF00",  # Зеленый
    "#00BFFF",  # Голубой
    "#0000FF",  # Синий
    "#8B00FF"   # Фиолетовый
]

def draw_petal(color_name):
    """Функция для рисования одного лепестка"""
    t.fillcolor(color_name)
    t.begin_fill()

    # Рисуем лепесток-круг
    t.circle(100)
    t.end_fill()

# Рисуем 7 лепестков по кругу
for color in colors:
    draw_petal(color)
    # Поворачиваем черепашку для следующего лепестка (360 градусов / 7 лепестков ≈ 51.4)
    t.left(360 / 7)

    colors = [
        "#C0C0C0",  # Серебрянный
        "#800080",  # Пурпурный
        "#FF00FF",  # Фукси
        "#0000A0",  # Темносиний
        "#FFA500",  # Оранжевый
        "#808000",  # Оливковый
        "#800000"  # Каштановый
    ]


def draw_petal(color_name):
    """Функция для рисования одного лепестка"""
    t.fillcolor(color_name)
    t.begin_fill()

    # Рисуем дугу влево, затем дугу вправо, чтобы получился лепесток
    t.circle(-70)
    t.end_fill()

# Рисуем 7 лепестков по кругу
for color in colors:
    draw_petal(color)
    # Поворачиваем черепашку для следующего лепестка (360 градусов / 7 лепестков ≈ 51.4)
    t.left(360 / 7)

# Рисуем сердцевину цветка
t.penup()
t.goto(0, -35)  # Смещаемся вниз, чтобы центр круга совпал с центром цветка
t.pendown()
t.fillcolor("#1F45FC")  # Золотисто-желтый
t.begin_fill()
t.circle(50)
t.end_fill()
# Прячем черепашку и завершаем работу
t.hideturtle()
screen.mainloop()

# Рисуем сердцевину цветка
# t.penup()
# t.goto(0, -25)  # Смещаемся вниз, чтобы центр круга совпал с центром цветка
# t.pendown()
# t.fillcolor("#FFD700")  # Золотисто-желтый
# t.begin_fill()
# t.circle(25)
# t.end_fill()