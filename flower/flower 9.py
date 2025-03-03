from turtle import *
import colorsys

pensize(2)
speed(0)
Screen().bgcolor('black')
penup()
setpos(0, -50) 
pendown()

start_shade = 0.5
color_variation = 0.3

for shape in range(16):
    for layer in range(15):
        color_value = start_shade + (shape/5) * color_variation
        color_value = color_value % 1.0
        
        rgb = colorsys.hsv_to_rgb(color_value, 0.8 + layer/75, 1)
        color(rgb)
        
        right(90)
        circle(200 - layer * 6, 90)
        left(90)
        circle(200 - layer * 6, 90)
        right(180)
    
    circle(60, 24)

exitonclick()
