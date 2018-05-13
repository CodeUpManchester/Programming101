from turtle import *

angleResult = input("How sharp are the star points? Angle (degrees): ")
angle = 27 if angleResult == "" else int(angleResult)

sideLengthAnswer = input("How long are the sides? ")
sideLength = 200 if sideLengthAnswer == "" else int(sideLengthAnswer)

goto(-sideLength/2, 0)
startX = position()[0]
startY = position()[1]

hideturtle()
color("orange", "red")
speed(10)
##begin_fill()

pendown()
while True:
    forward(sideLength)
    right(180 - angle)

    currentX = position()[0]
    currentY = position()[1]
    if currentX == startX and currentY == startY:
        break
penup()
##end_fill()
