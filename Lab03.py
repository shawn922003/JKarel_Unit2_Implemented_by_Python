from pyFrame.JPanel import JPanel
from pyFrame.Graphic import Graphics
from pyFrame.JFrame import *
from pyFrame.Color import Color
from pyFrame.BufferedImage import BufferedImage
import math

class Panel03(JPanel):
    __N=400
    def __init__(self) -> None:
        super().__init__()
        self.__img=BufferedImage(self.__N,self.__N)
        self.__img.setColor(Color.BLUE)
        self.__img.fillRect(0, 0, self.__N, self.__N)
        self.__img.setColor(Color.YELLOW)
        for k in range(51):
            self.__img.drawLine(self.__N * k / 50, 0, self.__N, self.__N * k / 50)

        x=self.__N/2
        y=self.__N/2
        size=100
        r1=60
        r2=55

      
        for i in range(12):
            x1=int(x+size*math.cos(i*30*math.pi/180))
            y1=int(y+size*math.sin(i*30*math.pi/180))
            self.__img.drawLine(x, y, x1, y1)
         
        self.__img.setColor(Color.BLUE)
        self.__img.fillOval(x - r1, y - r1, r1 * 2, r1 * 2)
        self.__img.setColor(Color.YELLOW)
        self.__img.fillOval(x - r2, y - r2, r2 * 2, r2 * 2)

    def paintComponent(self,g:Graphics):
        g.drawImage(self.__img, 0, 0)


if __name__=="__main__":
    frame=JFrame(title="Sun")
    frame.setSize(400,400)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(Panel03())
    frame.setVisible(True)
    frame.fixSetting()
