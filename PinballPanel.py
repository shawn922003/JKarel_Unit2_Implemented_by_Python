from Ball import Ball
from pyFrame.Timer import Timer
from pyFrame.JPanel import JPanel
from pyFrame.Graphic import Graphics
from pyFrame.JFrame import *
from pyFrame.Color import Color
from pyFrame.BufferedImage import BufferedImage
import random


class PinballPanel(JPanel):
    __FRAME=400
    __BACKGROUND=(204,204,204)

    def __init__(self) -> None:
        super().__init__()

        self.__myImage=BufferedImage(self.__FRAME,self.__FRAME)
        self.__myImage.setColor(self.__BACKGROUND)
        self.__myImage.fillRect(0,0,self.__FRAME,self.__FRAME)

        self.__xPos=random.randrange(50,self.__FRAME-50)
        self.__yPos=random.randrange(50,self.__FRAME-50)

        self.__ball=Ball(x=self.__xPos,y=self.__yPos,d=50,c=Color.BLACK)

        self.__t=Timer(5,self.__listener)
        self.__t.start()

    def paintComponent(self, g: Graphics):
        g.drawImage(self.__myImage,0,0)


    def __listener(self):
        self.__myImage.setColor(self.__BACKGROUND)
        self.__myImage.fillRect(0,0,self.__FRAME,self.__FRAME)
        self.__ball.move(self.__FRAME,self.__FRAME)
        self.__ball.draw(self.__myImage)
        self.repaint()