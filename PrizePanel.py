from pyFrame.Color import Color
from pyFrame.event.MouseAdapter import MouseAdapter
from pyFrame.event.KeyAdapter import KeyAdapter
from pyFrame.Graphic import Graphics
from pyFrame.JPanel import JPanel
from pyFrame.BufferedImage import BufferedImage
from pyFrame.Timer import Timer
from pyFrame.event.MouseEvent import MouseEvent
from pyFrame.event.KeyEvent import KeyEvent
from Ball import Ball
from Polkadot import Polkadot
import math
import random

class PrizePanel(JPanel):
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

        self.addMouseListener(self.__Mouse(self)) # self代表PrizePanel本身，由於Mouse類需要使用到PrizePanel的屬性，因此需要傳入self
        self.addKeyListener(self.__Key(self))

        self.__t=Timer(10,self.__listener)
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

    def __listener(self):
        self.__myImage.setColor(self.__BACKGROUND)
        self.__myImage.fillRect(0, 0, self.__FRAME, self.__FRAME)
        self.ball.move(self.__FRAME,self.__FRAME)
        self.__collide(self.ball,self.pd)
        self.ball.draw(self.__myImage)
        self.pd.draw(self.__myImage)
        self.__myImage.setColor(Color.BLACK)
        self.__myImage.setFont("Arial",None,24)
        self.__myImage.drawString(f"Count: {self.__hits}",self.__FRAME-150,25)
        self.repaint()

    class __Mouse(MouseAdapter):
        def __init__(self,outClass):
            self.__outClass=outClass

        def mousePressed(self, event:MouseEvent):
            if event.isShiftDown(): 
                self.__outClass.ball.setdx(random.random()*20-10)
                self.__outClass.ball.setdy(random.random()*20-10)

            elif event.getBotton()==MouseEvent.BUTTON1:
                self.__outClass.pd.setX(event.getX()) # 假如pd是私有，那此指令需改成 self.outClass._PrizePanel__pd.setX(e.x) ，其他的pd需要用如此方式做修正
                self.__outClass.pd.setY(event.getY())

            elif event.getBotton()==MouseEvent.BUTTON3:
                self.__outClass.ball.setX(event.getX())
                self.__outClass.ball.setY(event.getY())

    class __Key(KeyAdapter):
        def __init__(self,outClass) -> None:
            self.__outClass=outClass

        def keyPressed(self, event:KeyEvent):
            if event.getKeyCode() == KeyEvent.VK_UP and self.__outClass.ball.getY() >= self.__outClass.ball.getRadius()+10:
                self.__outClass.ball.setY(self.__outClass.ball.getY()-10)

            if event.getKeyCode() == KeyEvent.VK_DOWN and self.__outClass.ball.getY() <= self.__outClass._PrizePanel__FRAME-self.__outClass.ball.getRadius()-10:
                self.__outClass.ball.setY(self.__outClass.ball.getY()+10)

            if event.getKeyCode() == KeyEvent.VK_LEFT and self.__outClass.ball.getX() >= self.__outClass.ball.getRadius()-10:
                self.__outClass.ball.setX(self.__outClass.ball.getX()-10)

            if event.getKeyCode() == KeyEvent.VK_RIGHT and self.__outClass.ball.getX() <= self.__outClass._PrizePanel__FRAME-self.__outClass.ball.getRadius()+10:
                self.__outClass.ball.setX(self.__outClass.ball.getX()+10)

            
                
            
                





