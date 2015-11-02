# -*- coding: utf-8 -*-
#spirála
from turtle import Turtle
julie = Turtle()
julie.speed(10)

def spiral(n, angle, step):
    for i in range(n):
        julie.forward(n-i)
        julie.left(angle)

spiral(100, 61, 1)

#diamant

def diamant(n, side):
    for i in range(n):
        julie.left(side)
        for j in range(n):
            julie.forward(side)
            julie.left(side)

diamant(12, 30)

#circle
def circle(r):
    for i in range(r):
        julie.forward(pi)
        julie.left(360/r)

circle(90)


