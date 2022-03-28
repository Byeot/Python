import turtle as t
import random

t.shape('turtle')
t.pensize(5)

def drawCircle(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(50)


def randomDrawCircle(x, y):
    t.color("blue")
    for i in range(50):
        rX=random.randrange(-600,600)
        rY=random.randrange(-600,600)
        t.penup()
        t.goto(rX, rY)
        t.pendown()
        t.circle(50)

t.onscreenclick(randomDrawCircle,1)

t.done()