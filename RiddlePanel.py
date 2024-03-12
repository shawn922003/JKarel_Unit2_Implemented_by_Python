from pyFrame.Color import Color
from pyFrame.Graphic import Graphics
from pyFrame.JPanel import JPanel
from pyFrame.BufferedImage import BufferedImage
from pyFrame.Timer import Timer
from pyFrame.event.MouseEvent import MouseEvent
from pyFrame.event.KeyEvent import KeyEvent
from Riddle import Riddle

class RiddlePanel(JPanel):
    __FRAME=400
    __BACKGROUND=Color.WHITE
    def __init__(self):
        super().__init__()
        self.__image=BufferedImage(self.__FRAME,self.__FRAME)
        self.__image.setColor(self.__BACKGROUND)
        self.__image.fillRect(0,0,self.__FRAME,self.__FRAME)

        self.__riddle=Riddle()

        self.__t1=Timer(10,self.__listener1)
        self.__t2=Timer(3000,self.__listener2)
        self.__t1.start()

    def paintComponent(self, g: Graphics):
        g.drawImage(self.__image,0,0)

    def __listener1(self):
        self.__image.setColor(self.__BACKGROUND)
        self.__image.fillRect(0,0,self.__FRAME,self.__FRAME)
        if not self.__riddle.move():
            self.__t1.stop()
            self.__t2.start()
            self.__image.setColor(Color.BLACK)
            self.__image.setFont('Arial',None,24)
            self.__image.drawString("123",self.__FRAME-150,200)
        
        self.__riddle.draw(self.__image)
        self.repaint()

    def __listener2(self):
        self.__image.setColor(self.__BACKGROUND)
        self.__image.fillRect(0,0,self.__FRAME,self.__FRAME)
        self.__riddle.draw(self.__image)
        self.__image.setColor(Color.BLACK)
        self.__image.setFont("Arial",None,24)
        self.__image.drawString("123",self.__FRAME-150,200)
        self.__image.drawString("456",self.__FRAME-100,100)
        self.__t2.stop()
        self.repaint()
