import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 11.8*math.cos(k) - 5 * math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)

speed(0)
bgcolor("black")

for i in range(10000):
    x = hearta(i) * 20
    y = heartb(i) * 20
    goto(x, y)
    for j in range(3):
        goto(x, 0)
        color("red")

done()