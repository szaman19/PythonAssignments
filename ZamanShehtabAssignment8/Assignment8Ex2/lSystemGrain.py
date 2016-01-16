#Zaman, M.Shehtab
#szaman5@binghamton.edu
#Lab Section: B55
#CA: Nuri Ra
#Assignment 8: Problem 2
import turtle
ITERATIONS = 5
DISTANCE = 5
ANGLE = 25.7
TURTLE_SPEED = 10
TURTLE_POS_X = 200
INDEX_ZERO = 0
INDEX_ONE = 1
INDEX_TWO = 2
def applyRules(lhch):
    rhstr = ""
    if lhch == 'H':
        rhstr = 'HFX[+H][-H]'   # Rule 1
    elif lhch == 'X':
        rhstr = 'X[-FFF][+FFF]FX'  # Rule 2
    else:
        rhstr = lhch 

    return rhstr


def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr


def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString


def drawLsystem(aTurtle, instructions, angle, distance):
    savedInfoList = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            savedInfoList.append([aTurtle.heading(), aTurtle.xcor(), aTurtle.ycor()])
            #print(savedInfoList)
        elif cmd == ']':
            newInfo = savedInfoList.pop()
            aTurtle.setheading(newInfo[INDEX_ZERO])
            aTurtle.setposition(newInfo[INDEX_ONE], newInfo[INDEX_TWO])


def main():
    instructions = createLSystem(ITERATIONS, "H")   # create the string
    #print(instructions)
    turtleDrawer = turtle.Turtle()            # create the turtle
    window = turtle.Screen()
    turtleDrawer.up()
    turtleDrawer.back(TURTLE_POS_X)
    turtleDrawer.down()
    turtleDrawer.speed(TURTLE_SPEED)
    drawLsystem(turtleDrawer, instructions, ANGLE, DISTANCE)  # draw the picture

    window.exitonclick()

main()

