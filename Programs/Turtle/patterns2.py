from turtle import *

def drawStar(numberOfPoints, sideLength, doFill = False):
    if numberOfPoints < 5:
        angle = 360 // numberOfPoints
    elif numberOfPoints > 4 and numberOfPoints < 7:
        angle = 180 - (360 // numberOfPoints // 2)
    else:
        angle = 180 - (360 // numberOfPoints)

    penup()
    goto(-sideLength/2, 0)

    hideturtle()
    color("orange", "red")
    speed(10)

    if doFill:
        begin_fill()

    pendown()
    for n in range(starPoints):
        forward(sideLength)
        right(angle)
    penup()

    if doFill:
        end_fill()

starPointsResult = input("How many points should the star have? ")
starPoints = 20 if starPointsResult == "" else int(starPointsResult)

sideLengthAnswer = input("How long are the sides? ")
sideLength = 200 if sideLengthAnswer == "" else int(sideLengthAnswer)

drawStar(starPoints, sideLength)

