from pyFrame.Color import Color
from pyFrame.Graphic import Graphics
import random


class Polkadot:
    def __init__(self,**args):
        if 'x' in args.keys():
            self.myX=args['x']
        else:
            self.myX=200

        if 'y' in args.keys():
            self.myY=args['y']
        else:
            self.myY=200

        if 'd' in args.keys():
            self.myDiameter=args['d']
        else:
            self.myDiameter=25

        if 'c' in args.keys():
            self.myY=args['c']
        else:
            self.myColor=Color.RED

        self.myRadius=self.myDiameter/2

    def getX(self):
        return self.myX

    def getY(self):
        return self.myY
    
    def getDiameter(self):
        return self.myDiameter
    
    def getRadius(self):
        return self.myRadius
    
    def setX(self,x:float):
        self.myX=x

    def setY(self,y:float):
        self.myY=y

    def setColor(self,c:tuple):
        self.myColor=c

    def setDiameter(self,d:float):
        self.myDiameter=d
        self.myRadius=d/2

    def setRadius(self,r:float):
        self.myDiameter=r*2
        self.myRadius=r

    def jump(self,rightEdge:int,buttonEdge:int):
        self.myX=random.random()*(rightEdge-self.myDiameter)+self.myRadius
        self.myY=random.random()*(buttonEdge-self.myDiameter)+self.myRadius

    def draw(self,g:Graphics):
        g.setColor(self.myColor)
        g.fillOval(self.getX()-self.getRadius(), self.getY()-self.getRadius(), self.getDiameter(), self.getDiameter())

    
        