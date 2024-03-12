from pyFrame.Color import Color
from pyFrame.Graphic import Graphics
from Polkadot import Polkadot
import random

class Bumper:
    def __init__(self, x=50, y=50, xWidth=100, yWidth=50, color=Color.BLUE):
        self.__x = x
        self.__y = y
        self.__xWidth = xWidth
        self.__yWidth = yWidth
        self.__color = color

    # Accessor methods
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getXWidth(self):
        return self.__xWidth

    def getYWidth(self):
        return self.__yWidth

    def getColor(self):
        return self.__color

    # Modifier methods
    def setX(self, x:int):
        self.__x = x

    def setY(self, y:int):
        self.__y = y

    def setXWidth(self, xWidth:int):
        self.__xWidth = xWidth

    def setYWidth(self, yWidth:int):
        self.__yWidth = yWidth

    def setColor(self, color:Color):
        self.__color = color

    # Instance methods
    def jump(self, rightEdge:int, bottomEdge:int):
        self.__x = random.randint(0, rightEdge - self.__xWidth)
        self.__y = random.randint(0, bottomEdge - self.__yWidth)

    def draw(self, myBuffer:Graphics):
        myBuffer.setColor(self.getColor())
        myBuffer.fillRect(self.getX(), self.getY(), self.getXWidth(), self.getYWidth())

    def inBumper(self, dot:Polkadot):
        for x in range(self.getX(), self.getX() + self.getXWidth() + 1):
            for y in range(self.getY(), self.getY() + self.getYWidth() + 1):
                if self.__distance(x, y, dot.getX(), dot.getY()) <= dot.getRadius():
                    return True
        return False

    def __distance(self, x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
