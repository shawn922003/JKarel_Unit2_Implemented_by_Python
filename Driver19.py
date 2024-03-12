from pyFrame.JFrame import *
from Ball import Ball
from pyFrame.Timer import Timer
from pyFrame.JPanel import JPanel
from pyFrame.Graphic import Graphics
from pyFrame.JFrame import *
from pyFrame.Color import Color
from pyFrame.BufferedImage import BufferedImage
import random
import math
from Polkadot import Polkadot
from Ball import Ball

class PrizePanel(JPanel):
    __FRAME=400
    __BACKGROUND=(204,204,204)

    def __init__(self) -> None:
        super().__init__()

        self.__myImage=BufferedImage(self.__FRAME,self.__FRAME)
        self.__myImage.setColor(self.__BACKGROUND)
        self.__myImage.fillRect(0,0,self.__FRAME,self.__FRAME)
        self.__hits=0

        self.__ball=Ball()
        self.__pds=[]
        for _ in range(50):
            xPos=random.randrange(50,self.__FRAME-50)
            yPos=random.randrange(50,self.__FRAME-50)
            self.__pds.append(Polkadot(x=xPos,y=yPos,d=10,c=Color.RED))

        self.__t=Timer(5,self.__listener)
        self.__t.start()

    def paintComponent(self, g: Graphics):
        g.drawImage(self.__myImage,0,0)


    def __listener(self):
        
        self.__myImage.setColor(self.__BACKGROUND)
        self.__myImage.fillRect(0, 0, self.__FRAME, self.__FRAME)
        self.__ball.move(self.__FRAME,self.__FRAME)
        self.__collide(self.__ball,self.__pds)
        self.__ball.draw(self.__myImage)
        for pd in self.__pds:
            pd.draw(self.__myImage)

        
        self.__myImage.setColor(Color.BLACK)
        self.__myImage.setFont("Arial",None,24)
        self.__myImage.drawString(f"Count: {self.__hits}",self.__FRAME-150,25)
        self.repaint()


    def __distance(self,x1: float, y1: float, x2: float, y2: float)->float:
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    def __collide(self,b:Ball, pds: Polkadot)->None:
        for pd in pds:
            d=self.__distance(b.getX(), b.getY(), pd.getX(), pd.getY())
            if d<= b.getRadius()+pd.getRadius():
                self.__hits+=1
                pd.jump(self.__FRAME,self.__FRAME)



if __name__=="__main__":
    frame=JFrame(title="Build a House")
    frame.setSize(400,400)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(PrizePanel())
    frame.setVisible(True)
    frame.fixSetting()


