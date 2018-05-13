from turtle import *

def drawShape(numSides, sideLength, colour = 'black', \
              doFill = False, startX = -1, startY = -1):
    if (doFill):
        begin_fill()

    if startX >= 0 and startY >= 0:
        goto(startX, startY)

    color(colour, "")
    pendown()
    
    turningAngle = 360.0 / numSides
    for n in range(numSides):
        forward(sideLength)
        right(turningAngle)

    penup()

    if (doFill):
        end_fill()

##numSidesAnswer = input("How many sides on the shape? ")
##numSides = 6 if numSidesAnswer == "" else int(numSidesAnswer)

sideLengthAnswer = input("How long are the sides? ")
sideLength = 50 if sideLengthAnswer == "" else int(sideLengthAnswer)

numShapesAnswer = input("How many shapes? ")
numShapes = 30 if numShapesAnswer == "" else int(numShapesAnswer)

angleStep = 360 // numShapes
colours = ['', '', '', 'red', 'orange', 'yellow', 'green', 'blue']

hideturtle()
speed(0)
for n in range(7, 2, -1):
    for i in range(0, 360, angleStep):
        ##drawShape(numSides, sideLength)
        drawShape(n, sideLength * n / 3, colours[n])
        right(angleStep)
