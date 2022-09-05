from turtle import Turtle, Screen, colormode
import heroes
from random import randint, seed


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    random_c = (red, green, blue)
    return random_c


nick = Turtle()
nick.shape("turtle")
nick.color("red")
nick.pensize(10)
nick.speed("fastest")
colormode(255)
seed()

for shape in range(3, 11):
    for edge in range(0, shape):
        nick.right(360 / shape)
        nick.forward(100)

nick.clear()
nick.reset()
nick.shape("turtle")
nick.pensize(10)
nick.speed("fastest")

for i in range(100):
    color = random_color()
    direction = randint(1, 4)
    nick.pencolor(color)
    if direction == 1:
        nick.setheading(0)
    elif direction == 2:
        nick.setheading(90)
    elif direction == 3:
        nick.setheading(180)
    elif direction == 4:
        nick.setheading(270)
    nick.forward(100)

nick.clear()
nick.reset()
nick.shape("turtle")
nick.speed("fastest")
nick.width(2)

for angle in range(0, 360, 5):
    color = random_color()
    nick.pencolor(color)
    nick.fillcolor(color)
    nick.circle(100)
    nick.left(5)

print(heroes.gen())

screen = Screen()
screen.exitonclick()
