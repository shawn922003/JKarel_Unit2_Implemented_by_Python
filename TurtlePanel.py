from pyFrame.JPanel import JPanel
from pyFrame.Timer import Timer
from fcps.Turtle import Turtle
from pyFrame.Graphic import Graphics


class TurtlePanel(JPanel):
    def __init__(self):
        super().__init__()
        self.__timer=Timer(10,self.__listener)
        self.__timer.start()

    def paintComponent(self, g: Graphics):
        g.drawImage(Turtle.getImage(),0,0)

    def __listener(self):  
        self.repaint()
