from fcps.Turtle import Turtle
class PolygonTurtle(Turtle):
    def __init__(self, x=0, y=0, h=0, n=50.0, s=6):
        kargs={'x':x,'y':y,'heading':h}
        super().__init__(**kargs)
        self.__mySize = n
        self.__mySides = s

    def setSize(self, n):
        self.__mySize = n

    def setSides(self, s):
        self.__mySides = s

    def drawShape(self):
        angle = 180 - ((self.__mySides - 2) * 180 / self.__mySides)
        for i in range(self.__mySides):
            self.forward(self.__mySize)
            self.turnLeft(angle)

