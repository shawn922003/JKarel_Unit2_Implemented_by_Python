import random
from pyFrame.Color import Color
from Spot import Spot  # 假设Spot类已经被正确转换成Python

class Pinball(Spot):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.__rightEdge = width
        self.__bottomEdge = height
        self.__dx = random.randint(-10, 10)
        self.__dy = random.randint(-10, 10)
        self.setColor(Color.BLUE)
        self.setRadius(40)

    def tick(self):
        if self.getX() <= self.getRadius():
            self.__dx = abs(self.__dx)
            self.__littlerandom()
        elif self.getX() >= self.__rightEdge - self.getRadius():
            self.__dx = -abs(self.__dx)
            self.__littlerandom()

        if self.getY() <= self.getRadius():
            self.__dy = abs(self.__dy)
            self.__littlerandom()
        elif self.getY() >= self.__bottomEdge - self.getRadius():
            self.__dy = -abs(self.__dy)
            self.__littlerandom()

        self.setX(self.getX() + self.__dx)
        self.setY(self.getY() + self.__dy)

    def __littlerandom(self):
        self.__dx = int((1 if self.__dx >= 0 else -1) * random.random() * 10)
        self.__dy = int((1 if self.__dy >= 0 else -1) * random.random() * 10)
