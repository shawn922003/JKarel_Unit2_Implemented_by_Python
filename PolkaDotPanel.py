from Polkadot import Polkadot
from pyFrame.Timer import Timer
from pyFrame.JPanel import JPanel
from pyFrame.Graphic import Graphics
from pyFrame.JFrame import *
from pyFrame.Color import Color
from pyFrame.BufferedImage import BufferedImage


class PolkaDotPanel(JPanel):
    __FRAME=400
    __BACKGROUND=(204,204,204)


    def __init__(self) -> None:
        super().__init__()
        self.__ball1=Polkadot()
        self.__ball2=Polkadot()
        self.__ball2.setColor(Color.GREEN)
        self.__ball2.setRadius(20)

        self.__imageBuffer=BufferedImage(self.__FRAME,self.__FRAME)

        self.__imageBuffer.setColor(self.__BACKGROUND)
        self.__imageBuffer.fillRect(0,0,self.__FRAME,self.__FRAME)

        self.__t=Timer(500,self.__listener)
        self.__t.start()
        
    def paintComponent(self,g: Graphics):
        g.drawImage(self.__imageBuffer,0,0)

        

    def __listener(self):
        self.__imageBuffer.setColor(self.__BACKGROUND)
        self.__imageBuffer.fillRect(0,0,self.__FRAME,self.__FRAME)
        self.__ball1.jump(self.__FRAME,self.__FRAME)
        self.__ball1.draw(self.__imageBuffer)
        self.__ball2.jump(self.__FRAME,self.__FRAME)
        self.__ball2.draw(self.__imageBuffer)
        self.repaint()





