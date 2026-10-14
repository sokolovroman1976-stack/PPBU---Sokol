# import turtle as t
# from random import random
# screen = t.Screen()
# screen.setup(600, 600)
# screen.title("Хренотень")
# for i in range(10):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)


# for steps in range(10):
#     for c in ('blue', 'red', 'green'):
#         t.color(c)
#         t.forward(steps)
#         t.right(50)

# import turtle
# t.hideturtle()
# Ugol = 9
# turtle.color('red')
# turtle.begin_fill()
# for i in range(Ugol):
#   turtle.forward(100)
#   turtle.right(360 *4/ Ugol)
# turtle.end_fill()
#
# screen.mainloop()


age = int(input('Введите возраст'))
if age >= 18:  # Если возраст больше или равен 18
    print("Вы совершеннолетний")
else:  # В противном случае
    print("Вы несовершеннолетний")
