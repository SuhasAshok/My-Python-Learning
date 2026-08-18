import turtle
from turtle import Turtle, Screen
import random
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 25)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (125, 36, 24), (187, 158, 51), (170, 104, 56), (5, 57, 83), (222, 223, 226), (200, 216, 204), (108, 67, 85), (39, 36, 35), (86, 142, 59), (20, 122, 176), (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186), (209, 200, 115), (179, 174, 177), (151, 176, 165), (93, 142, 156), (28, 80, 59)]

tim = Turtle()
turtle.colormode(255)
tim.penup()
tim.hideturtle()
tim.speed("fastest")
# tim.teleport(-250, 200)
# x = -250
# y = 200
# for _ in range(10):
#     tim.teleport(x, y)
#     for _ in range(10):
#         tim.dot(20, random.choice(color_list))
#         tim.forward(50)
#     y -= 50

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
dot_count = 100

for dots in range(1, dot_count + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dots % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






screen = Screen()
screen.exitonclick()
