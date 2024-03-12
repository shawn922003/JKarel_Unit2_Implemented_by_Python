from pyFrame.Timer import Timer
from pyFrame.JPanel import JPanel
from pyFrame.Graphic import Graphics
from pyFrame.JFrame import *
from pyFrame.Color import Color
from pyFrame.BufferedImage import BufferedImage
from PIL import Image

class Riddle:
    def __init__(self) -> None:
        self.__img=Image.open("tj.jpg")
        self.__speed=3
        self.__position=[40,200]

    def draw(self,g:Graphics):
        head = [-64 + self.__position[0], self.__position[1] - 169]
        body = [self.__position[0], self.__position[1] + 30]
        ass = [self.__position[0], self.__position[1] + 110]
        leftHand = [self.__position[0] - 40, self.__position[1] + 80]
        rightHand = [self.__position[0] + 40, self.__position[1] + 80]
        leftFoot = [self.__position[0] - 40, self.__position[1] + 200]
        rightFoot = [self.__position[0] + 40, self.__position[1] + 200]

        g.setStroke(30.0)
        g.setColor(Color.BLACK)
        g.drawImage(self.__img, head[0], head[1])
        g.drawLine(self.__position[0], self.__position[1], ass[0], ass[1])
        g.drawLine(body[0], body[1], leftHand[0], leftHand[1])
        g.drawLine(body[0], body[1], rightHand[0], rightHand[1])
        g.drawLine(ass[0], ass[1], leftFoot[0], leftFoot[1])
        g.drawLine(ass[0], ass[1], rightFoot[0], rightFoot[1])

    def move(self):
        self.__position[0]+=self.__speed
        return self.__position[0]<=150