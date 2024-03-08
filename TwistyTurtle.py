from fcps.Turtle import Turtle
class TwistyTurtle(Turtle):
    def __init__(self):
        super().__init__()


    def drawShape(self,beginLength, endLength, increment, angle):
        for i in range(beginLength, endLength + 1, increment):
            self.forward(i)
            self.turnLeft(angle)
        