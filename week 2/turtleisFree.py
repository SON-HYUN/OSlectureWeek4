# 소프트웨어학부 2학년 손의현 (2020039083)
# 오픈소스기초프로젝트 2주차 과제 : 랜덤하게 움직이는 거북이

import turtle
import random

sWidth,sHeight,pSize,exitCount = 300,300,3,0
r,g,b,angle,dist,curX,curY = [0] * 7

turtle.title('거북이가 마음대로 다니기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width = sWidth+30, height = sHeight+30)
turtle.screensize(sWidth,sHeight)

while True :
    r = random.random(); g = random.random(); b = random.random()
    turtle.pencolor((r,g,b))
    angle = random.randrange(0,360)
    dist = random.randrange(1,100)
    turtle.left(angle)
    turtle.forward(dist)

    curX = turtle.xcor() ; curY = turtle.ycor()

    if (-1*sWidth/2 <= curX and curX <= sWidth/2) \
            and (-1*sHeight/2 <= curY and curY <= sHeight/2) :
        pass
    else :
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        exitCount += 1
        if(exitCount >= 5) :
            break

turtle.done()