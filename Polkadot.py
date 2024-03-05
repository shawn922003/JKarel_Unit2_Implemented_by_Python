from pyFrame.Color import Color
from pyFrame.Graphic import Graphics
import random


class Polkadot:
    def __init__(self,**kargs):
        if 'x' in kargs.keys():
            self.__myX=kargs['x']
        else:
            self.__myX=200

        if 'y' in kargs.keys():
            self.__myY=kargs['y']
        else:
            self.__myY=200

        if 'd' in kargs.keys():
            self.__myDiameter=kargs['d']
        else:
            self.__myDiameter=25

        if 'c' in kargs.keys():
            self.__myColor=kargs['c']
        else:
            self.__myColor=Color.RED

        self.__myRadius=self.__myDiameter/2

    def getX(self):
        return self.__myX

    def getY(self):
        return self.__myY
    
    def getDiameter(self):
        return self.__myDiameter
    
    def getRadius(self):
        return self.__myRadius
    
    def setX(self,x:float):
        self.__myX=x

    def setY(self,y:float):
        self.__myY=y

    def setColor(self,c:tuple):
        self.__myColor=c

    def setDiameter(self,d:float):
        self.__myDiameter=d
        self.__myRadius=d/2

    def setRadius(self,r:float):
        self.__myDiameter=r*2
        self.__myRadius=r

    def jump(self,rightEdge:int,buttonEdge:int):
        self.__myX=random.random()*(rightEdge-self.__myDiameter)+self.__myRadius
        self.__myY=random.random()*(buttonEdge-self.__myDiameter)+self.__myRadius

    def draw(self,g:Graphics):
        g.setColor(self.__myColor)
        g.fillOval(self.getX()-self.getRadius(), self.getY()-self.getRadius(), self.getDiameter(), self.getDiameter())

    
        