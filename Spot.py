import random
from pyFrame.Color import Color
from pyFrame.Graphic import Graphics

class Spot:
    def __init__(self, width=None, height=None, x=None, y=None, r=None, color=None):
        if width is not None and height is not None:
            self.__r = random.randint(0, 20)
            self.__x = random.randint(self.__r, width - 2 * self.__r) + self.__r
            self.__y = random.randint(self.__r, height - 2 * self.__r) + self.__r
            self.__c = Color.RED  # 默认颜色
        else:
            self.__x = x
            self.__y = y
            self.__r = r
            self.__c = color

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y

    def getRadius(self):
        return self.__r

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setRadius(self, r):
        self.__r = r

    def setColor(self, color):
        self.__c = color

    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    
    def intersect(self, ball:'Spot'):
        return Spot.distance(self.__x, self.__y, ball.getX(), ball.getY()) <= self.__r + ball.getRadius()
    
    def drawme(self, g:Graphics):
        g.setColor(self.__c)
        g.fillOval(self.__x - self.__r, self.__y - self.__r, 2 * self.__r, 2 * self.__r)
