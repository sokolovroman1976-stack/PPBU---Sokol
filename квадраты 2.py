# Source - https://translated.turbopages.orghttps://translated.turbopages.org/proxy_u/en-ru.ru.e293d95a-6aa5b6e4-6053746d-74722d776562/https/stackoverflow.com/q
# Posted by user3399362, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-12, License - CC BY-SA 3.0

import random
import turtle


COLORS = [
    "red",
    "blue",
    "green",
    "yellow",
    "black",
    "pink",
    "gold",
    "violet",
    "coral",
    "lemon chiffon",
    "sea green"
]


def random_color():
    return random.choice(COLORS)


def draw_square(t, color, x, y, size):
    """Рисует закрашенный квадрат."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    t.color(color)
    t.begin_fill()

    for _ in range(4):
        t.forward(size)
        t.right(90)

    t.end_fill()


def draw_squares(t):
    for cycle in range(5):
        x = -250 + cycle * 110
        y = 250

        # Вложенные квадраты от большого к маленькому
        for size in range(200, 0, -10):
            draw_square(t, random_color(), x, y, size)

            x += random.randint(-10, 10)
            y -= random.randint(1, 5)

screen = turtle.Screen()
screen.setup(700, 600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

draw_squares(t)

turtle.done()
