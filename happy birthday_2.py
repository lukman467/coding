import turtle

bg = turtle.Screen()
bg.bgcolor("black")

turtle.pensize(3)

turtle.hideturtle()
turtle.penup()
turtle.goto(-165, -180) 
turtle.color("white")
turtle.pendown()
turtle.forward(330)

turtle.penup()
turtle.goto(-155, -150) 
turtle.color("white")
turtle.pendown()
turtle.forward(305)

turtle.penup()
turtle.goto(-145, -120)
turtle.color("white")
turtle.pendown()
turtle.forward(280)

turtle.penup()
turtle.goto(-95, -100)
turtle.color("pink")
turtle.begin_fill()
turtle.pendown()
turtle.forward(190)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(190)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

positions = [-75, -25, 25, 75]
colors = ["red", "blue", "yellow", "green"]

for i, pos in enumerate(positions):
    turtle.penup()
    turtle.goto(pos, 20)
    turtle.color(colors[i])
    turtle.pendown()
    turtle.forward(20)

for pos in positions:
    turtle.penup()
    turtle.goto(pos, 30)
    turtle.color("red")
    turtle.pendown()
    turtle.forward(3)

turtle.penup()
turtle.goto(10, -60)
turtle.pendown()

circle_colors = ["red", "orange", "brown", "green", "blue", "purple", "grey"]
for each_color in circle_colors:
    angle = 360 / len(circle_colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

turtle.penup()
turtle.goto(-160, 50)
turtle.color("white")
turtle.pendown()
turtle.write("happy birthday to you<3", font=("Poppins", 25, "normal"))
turtle.color("lightblue")

turtle.done()