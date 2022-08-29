from turtle import Turtle, Screen
import heroes

nick = Turtle()
nick.shape("turtle")
nick.color("red")

for shape in range(3, 11):
    for edge in range(0, shape):
        nick.right(360 / shape)
        nick.forward(100)

print(heroes.gen())

screen = Screen()
screen.exitonclick()
