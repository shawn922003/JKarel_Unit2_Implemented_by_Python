from pyFrame.Color import Color
from pyFrame.event.MouseAdapter import MouseAdapter
from pyFrame.Graphic import Graphics
from pyFrame.JLabel import JLabel
from pyFrame.BufferedImage import BufferedImage
from pyFrame.Timer import Timer
from Ball import Ball
from Polkadot import Polkadot
import math
import random

class PrizePanel(JLabel):
    __FRAME=400
    __BACKGROUND=(204,204,204)

    def __init__(self) -> None:
        super().__init__()
        self.__myImage=BufferedImage(self.__FRAME,self.__FRAME)
        self.ball=Ball() # 假如有內部類需要使用成員，成員建議設定成public
        self.pd=Polkadot()
        self.__hits=0

        self.__myImage.setColor(self.__BACKGROUND)
        self.__myImage.fillRect(0,0,self.__FRAME,self.__FRAME)

        self.addMouseListener(self.Mouse(self)) # self代表PrizePanel本身，由於Mouse類需要使用到PrizePanel的屬性，因此需要傳入self

        self.__t=Timer(10,self.listener)
        self.__t.start()


    def paintComponent(self, g: Graphics):
        g.drawImage(self.__myImage,0,0) 

    def __distance(self,x1: float, y1: float, x2: float, y2: float)->float:
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    def __collide(self,b:Ball, pd: Polkadot)->None:
        d=self.__distance(b.getX(), b.getY(), pd.getX(), pd.getY())
        if d<= b.getRadius()+pd.getRadius():
            self.__hits+=1
            pd.jump(self.__FRAME,self.__FRAME)

    def listener(self):
        self.__myImage.setColor(self.__BACKGROUND)
        self.__myImage.fillRect(0, 0, self.__FRAME, self.__FRAME)
        self.ball.move(self.__FRAME,self.__FRAME)
        self.__collide(self.ball,self.pd)
        self.ball.draw(self.__myImage)
        self.pd.draw(self.__myImage)
        self.__myImage.setColor(Color.BLACK)
        self.repaint()

    class Mouse(MouseAdapter):
        def __init__(self,outClass):
            self.outClass=outClass

        def mousePressed(self, e):
            if e.state & 0x0001 and e.num==1: # 0x0001表示shift的遮掩碼，num==1表示左鍵按下，num==2表示中鍵按下，num==3表示右鍵按下
                self.outClass.ball.setdx(random.random()*20-10)
                self.outClass.ball.setdy(random.random()*20-10)

            elif e.num==1:
                self.outClass.pd.setX(e.x) # 假如pd是私有，那此指令需改成 self.outClass._PrizePanel__pd.setX(e.x) ，其他的pd需要用如此方式做修正
                self.outClass.pd.setY(e.y)

            elif e.num==3:
                self.outClass.ball.setX(e.x)
                self.outClass.ball.setY(e.y)
                




