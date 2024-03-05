from Polkadot import Polkadot
from pyFrame.Color import Color
import random

class Ball(Polkadot):
    def __init__(self, **kargs):
        if len(kargs) == 0:
            kargs['x']=200
            kargs['y']=200
            kargs['d']=50
            kargs['c']=Color.BLACK
        super().__init__(**kargs)

        self.__dx=random.random()*20-10
        self.__dy=random.random()*20-10

    def setdx(self,x):
        self.__dx=x

    def setdy(self,y):
        self.__dy=y

    def getdx(self):
        return self.__dx
    
    def getdy(self):
        return self.__dy
    
    def move(self,rightEdge, bottomEdge):
        self.setX(self.getX()+self.__dx)
        self.setY(self.getY()+self.__dy)

        if self.getX() >= rightEdge - self.getRadius():
            self.__dx *= -1
        elif self.getX() <= self.getRadius():
            self.__dx *= -1
        elif self.getY() <= self.getRadius():
            self.__dy *= -1
        elif self.getY() >= bottomEdge - self.getRadius():
            self.__dy *= -1

        

