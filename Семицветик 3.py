from turtle import *

colormode(255)
screen = Screen()
speed(0)

r = 255
g = 255
b = 255

br = 75
bg = 45
bb = 120
color((br, bg, bb), (r, g, b))
pensize(2)

for j in range(100,10,-20):
    for i in range(8):
        begin_fill()
        circle(j)
        end_fill()
        rt(45)
    r -= 30
    g -= 30
    b -= 30
    br += 30
    bg += 30
    bb += 30

mainloop()
