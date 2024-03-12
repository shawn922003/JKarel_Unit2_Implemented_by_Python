from pyFrame.JFrame import *
from pyFrame.Timer import Timer
from pyFrame.JPanel import JPanel
from pyFrame.Graphic import Graphics
from pyFrame.JFrame import *
from pyFrame.Color import Color
from pyFrame.BufferedImage import BufferedImage
from Pinball import Pinball
from Spot import Spot

class Prize(Spot):
    def __init__(self, width=None, height=None):
        super().__init__(width, height)

    def lightup(self):
        self.setColor(Color.YELLOW)

class PrizePanel(JPanel):
    __FRAME=600

    def __init__(self) -> None:
        super().__init__()
        self.__num=500

        self.__img=BufferedImage(self.__FRAME,self.__FRAME)

        self.__prizeArr=[Prize(self.__FRAME,self.__FRAME) for _ in range(self.__num)]

        self.__pb=Pinball(self.__FRAME,self.__FRAME)

        Timer(10,self.__listener).start()
    
    def paintComponent(self, g: Graphics):
        g.drawImage(self.__img,0,0)

    def __listener(self):
        self.__img.setColor(Color.WHITE)
        self.__img.fillRect(0,0,self.__FRAME,self.__FRAME)
        for k in range(self.__num):
            if self.__pb.intersect(self.__prizeArr[k]):
                self.__prizeArr[k].lightup()
            
            self.__prizeArr[k].drawme(self.__img)
        
        self.__pb.tick()
        self.__pb.drawme(self.__img)
        self.repaint()

if __name__=="__main__":
    frame=JFrame(title="Build a House")
    frame.setSize(600,600)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(PrizePanel())
    frame.setVisible(True)
    frame.fixSetting()


