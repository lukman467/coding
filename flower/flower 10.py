import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

palette = ["yellow", "red", "yellow", "red"]

iterations = 120
for step in range(iterations):
    radius = 200 - step
    for shade in palette:
        t.color(shade)
        t.circle(radius, 100)
        t.left(90)
        t.circle(radius, 100)
        t.right(60)
        t.end_fill()

screen.mainloop()
