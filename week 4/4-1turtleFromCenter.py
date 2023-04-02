import turtle
import random

myTurtle, tX, tY, tColor, tSize, tShape = [None] * 6
tColor = [0 , 0, 0]
shapeList = []
playerTurtle = []
sWidth, sHeight = 500, 500

if __name__ == '__main__' :
    turtle.title('거북이 리스트 활용')
    turtle.setup(width = sWidth + 50, height = sHeight + 50)
    turtle.screensize(sWidth, sHeight)
    shapeList = turtle.getshapes()
    for i in range(0, 100) :
        random.shuffle(shapeList)
        myTurtle = turtle.Turtle(shapeList[0])
        tX = random.randrange(-sWidth / 2, sWidth / 2)
        tY = random.randrange(-sHeight / 2, sHeight / 2)
        tColor[0] = random.random()
        tColor[1] = random.random()
        tColor[2] = random.random()
        playerTurtle.append([myTurtle, tX, tY, tSize, tColor[0], tColor[1], tColor[2]])

    for tList in playerTurtle :
        myTurtle = tList[0]
        myTurtle.color(tList[4], tList[5], tList[6])
        myTurtle.pencolor(tList[4], tList[5], tList[6])
        myTurtle.goto(tList[1], tList[2])
    turtle.done()
