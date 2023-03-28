# 소프트웨어학부 2학년 손의현 (2020039083)
# 오픈소스기초프로젝트 1주차 과제 : 거북이

import turtle
import random

def screenLeftClick (x,y) :
    global r,g,b
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)

def screenRightClick (x,y) :
    turtle.penup()
    turtle.goto(x,y)

def screenMidClick (x,y) :
    global r,g,b
    tSize = random.randrange(1,10)
    turtle.turtlesize(tSize)
    r=random.random()
    g=random.random()
    b=random.random()

# initialize global variables
pSize = 10
r,g,b = 0.0,0.0,0.0

# main
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick,1)
turtle.onscreenclick(screenMidClick,2)
turtle.onscreenclick(screenRightClick,3)

turtle.done()