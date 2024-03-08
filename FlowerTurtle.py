from fcps.Turtle import Turtle
from pyFrame.Color import Color

class FlowerTurtle(Turtle):
    def __init__(self, x=100, n=50.0, c=Color.RED):
        kargs={'x':x,'y':300,'heading':90}
        super().__init__(**kargs)
        self.__mySize = n
        self.__myColor = c

    def setSize(self, n):
        self.__mySize = n


    def drawPetals(self):
        for i in range(30):
            self.setColor(self.__myColor)
            self.forward(self.__mySize)
            self.back(self.__mySize)
            self.turnLeft(12)

    def drawStem(self):
        self.turnLeft(180)
        self.forward(self.__mySize)
        self.setColor((0,100,0))
        self.forward(self.__mySize * 1.5)
        self.turnLeft(180)
        self.forward(self.__mySize * 0.5)
        self.turnLeft(45)
        self.forward(self.__mySize * 0.5)
        self.back(self.__mySize * 0.5)
        self.turnRight(90)
        self.forward(self.__mySize)

    def drawShape(self):
        self.drawPetals()
        self.drawStem()

