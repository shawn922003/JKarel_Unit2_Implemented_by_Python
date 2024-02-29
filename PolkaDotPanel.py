from Polkadot import Polkadot
from pyFrame.Timer import Timer
from pyFrame.JLabel import JLabel
from pyFrame.Graphic import Graphics
from pyFrame.JFrame import *
from pyFrame.Color import Color
from pyFrame.BufferImage import BufferImage


class PolkaDotPanel(JLabel):
    FRAME=400
    BACKGROUND=(204,204,204)


    def __init__(self) -> None:
        super().__init__()
        self.ball1=Polkadot()
        self.ball2=Polkadot()
        self.ball2.setColor(Color.GREEN)
        self.ball2.setRadius(20)

        self.graphic=None

        self.t=Timer(500,self.listener)
        
        

    def paintComponent(self,g: Graphics):
        self.graphic=g  
        g.setColor(self.BACKGROUND)
        g.fillRect(0,0,self.FRAME,self.FRAME)
        self.t.start()
        

    def listener(self):
        self.graphic.setColor(self.BACKGROUND)
        self.graphic.fillRect(0,0,self.FRAME,self.FRAME)
        self.ball1.jump(self.FRAME,self.FRAME)
        self.ball1.draw(self.graphic)
        self.ball2.jump(self.FRAME,self.FRAME)
        self.ball2.draw(self.graphic)





