import turtle

my_turtle_cursor = turtle.Turtle()
my_turtle_screen = turtle.Screen()
y_coordinate = -125

def draw_circle_on_top_of_stick(fill_color, border_color, x, y, radius):
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(3)
    my_turtle_cursor.color(fill_color)
    my_turtle_cursor.fillcolor(border_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.circle(radius)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

def draw_candle_for_cake(fill_color, border_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.forward(25)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(60)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(25)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(60)
    my_turtle_cursor.left(90)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

def draw_stick_on_candle(fill_color, x, y, cursor_size):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(fill_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pensize(cursor_size)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.right(90)
    my_turtle_cursor.forward(12)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

def write_happy_inside_circle(text_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(text_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.write("Happy", font=("sans-serif", 26, "bold"))
    my_turtle_cursor.getscreen().update()

def write_birthday_inside_circle(text_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(text_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.write("Birthday", font=("sans-serif", 26, "bold"))
    my_turtle_cursor.getscreen().update()

def draw_stick(fill_color, border_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(3)
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.left(180)
    my_turtle_cursor.forward(200)
    my_turtle_cursor.end_fill()

def draw_toppings_on_cake(fill_color, border_color, x, y, radius):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.forward(10)
    my_turtle_cursor.left(90)
    my_turtle_cursor.circle(radius, extent = 180)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(10)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

def draw_layer_of_the_cake(fill_color, border_color, cursor_size, x, y, width, height):
    my_turtle_cursor.hideturtle()
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(cursor_size)
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()

    for i in range(2):
        my_turtle_cursor.forward(width)
        my_turtle_cursor.left(90)
        my_turtle_cursor.forward(height)
        my_turtle_cursor.left(90)

    my_turtle_cursor.end_fill()
    my_turtle_cursor.setheading(0)
    my_turtle_cursor.getscreen().update()

my_turtle_screen.bgcolor("#FFFDD0")

parts_of_cake = []
parts_of_cake.append(["#A020F0", "#000000", 3, 30])
parts_of_cake.append(["#55FF55", "#000000", 3, 20])
parts_of_cake.append(["#B87333", "#000000", 3, 60])

draw_layer_of_the_cake("#FFC0CB", "#000000", 3, -220, y_coordinate - 70, 400, 10)

for parts in parts_of_cake:
    draw_layer_of_the_cake(parts[0], parts[1], parts[2], -135, y_coordinate - 60, 240, parts[3])
    y_coordinate += parts[3]

draw_toppings_on_cake("#C20067", "#000000", -120, y_coordinate - 60, 10)
draw_toppings_on_cake("#FFFF00", "#000000", -80, y_coordinate - 60, 10)
draw_toppings_on_cake("#FF0000", "#000000", 25, y_coordinate - 60, 10)
draw_toppings_on_cake("#0000FF", "#000000", 59, y_coordinate - 60, 10)
draw_toppings_on_cake("#FFA500", "#000000", -135, y_coordinate - 80, 10)
draw_toppings_on_cake("#E4E6EB", "#000000", -135, y_coordinate - 100, 10)
draw_toppings_on_cake("#FFA500", "#000000", -135, y_coordinate - 120, 10)
draw_toppings_on_cake("#181A18", "#000000", -80, y_coordinate - 80, 10)
draw_toppings_on_cake("#0000FF", "#000000", -65, y_coordinate - 110, 10)
draw_toppings_on_cake("#FFD700", "#000000", -95, y_coordinate - 140, 10)
draw_toppings_on_cake("#181A18", "#000000", 10, y_coordinate - 80, 10)
draw_toppings_on_cake("#E4E6EB", "#000000", -20, y_coordinate - 110, 10)
draw_toppings_on_cake("#181418", "#000000", 35, y_coordinate - 140, 10)
draw_toppings_on_cake("#FFA500", "#000000", 75, y_coordinate - 80, 10)
draw_toppings_on_cake("#E4E6EB", "#000000", 75, y_coordinate - 110, 10)
draw_toppings_on_cake("#FFD700", "#000000", 75, y_coordinate - 140, 10)
draw_candle_for_cake("#FFF44F", "#000000", -40, y_coordinate - 60)
draw_stick_on_candle("#181A18", -26, y_coordinate + 15, 7)
draw_stick("#181A18", "#181A18", 0, y_coordinate - 60)
draw_circle_on_top_of_stick("#181A18", "#FFFDD0", 100, y_coordinate + 235, 100)
write_happy_inside_circle("#000000", -70, y_coordinate + 240)
write_birthday_inside_circle("#000000", -80, y_coordinate + 190)

turtle.done()