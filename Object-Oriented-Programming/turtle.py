from turtle import Turtle, Screen
from prettytable import PrettyTable

# nicky = Turtle()
# my_screen = Screen()
#
# nicky.shape("turtle")
# nicky.color("ForestGreen")
# nicky.forward(100)
# my_screen.exitonclick()
#
# print(nicky)
# print(my_screen.canvheight)

table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)

