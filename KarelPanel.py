from pyFrame.JPanel import JPanel
from pyFrame.Timer import Timer
from pyFrame.Color import Color
from pyFrame.Graphic import Graphics
from pyFrame.BufferedImage import BufferedImage
from PIL import Image

class KarelPanel(JPanel):
    __WIDTH=395
    __HEIGHT=391
    __BACKGROUND=(204,204,204)

    def __init__(self) -> None:
        super().__init__()

        self.__img=BufferedImage(self.__WIDTH,self.__HEIGHT)
        self.__myArray=[]
        self.__myArray.append(Image.open('karele.gif'))
        self.__myArray.append(Image.open('kareln.gif'))
        self.__myArray.append(Image.open('karelw.gif'))
        self.__myArray.append(Image.open('karels.gif'))

        self.__dir=0
        self.__xPos=5
        self.__yPos=self.__HEIGHT-3-self.__myArray[self.__dir].size[1]

        self.__t=Timer(250,self.__listener)
        self.__t.start()

    def paintComponent(self, g: Graphics):
        g.drawImage(self.__img,0,0)

    def __listener(self):
        self.__img.setColor(self.__BACKGROUND)
        self.__img.fillRect(0,0,self.__HEIGHT,self.__WIDTH)
        self.__img.setColor(Color.RED)
        for x in range(17,self.__WIDTH,30):
            self.__img.drawLine(x,0,x,self.__HEIGHT)

        for y in range(9,self.__HEIGHT,28):
            self.__img.drawLine(0,y,self.__WIDTH,y)
        
        self.__img.fillRect(107,121,180,56)
        self.__img.setColor(Color.BLACK)
        self.__img.setFont("Arial",None,24)
        self.__img.drawString("Karel the Robot",125,155)

        if self.__yPos >= self.__HEIGHT - 30 - self.__myArray[self.__dir].size[1] and self.__xPos <= self.__WIDTH - 40 - self.__myArray[self.__dir].size[0]:
            self.__dir = 0
            self.__xPos += 30
        elif self.__yPos >= 3 and self.__xPos >= self.__WIDTH - 40 - self.__myArray[self.__dir].size[0]:
            self.__dir = 1
            self.__yPos -= 28 
        elif self.__yPos <= 3 and self.__xPos >= 45:
            self.__dir = 2
            self.__xPos -= 30
        elif self.__yPos <= self.__HEIGHT - 30 - self.__myArray[self.__dir].size[1] and self.__xPos < 45:
            self.__dir = 3
            self.__yPos += 28  

        self.__img.drawImage(self.__myArray[self.__dir],self.__xPos,self.__yPos)

        self.repaint()
        
