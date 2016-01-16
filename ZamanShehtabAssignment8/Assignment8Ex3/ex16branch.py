#Zaman, M.Shehtab
#szaman5@binghamton.edu
#Lab Section: B55
#CA: Nuri Ra
#Assignment 8: Problem 3
import turtle

ITERATIONS = 4
DISTANCE = 5
ANGLE = 25
TURTLE_SPEED = 10
TURTLE_POS_X = 200
INDEX_ZERO = 0
INDEX_ONE = 1
INDEX_TWO = 2

def applyRules(lhch):
    rhstr = ""
    if lhch == 'F':
        rhstr = 'F[-F]F[+F]F'   # Rule 1
    else:
        rhstr = lhch    # no rules apply so keep the character

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
  instructions = createLSystem(ITERATIONS, "F")   # create the string
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

