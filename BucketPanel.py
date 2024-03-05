from pyFrame.JPanel import JPanel
from pyFrame.Timer import Timer
from pyFrame.Graphic import Graphics
from fcps.Bucket import Bucket

class BucketPanel(JPanel):
    def __init__(self) -> None:
        super().__init__()

        self.__timer=Timer(10,self.__listener)
        self.__timer.start()

    def paintComponent(self, g: Graphics):
        g.drawImage(Bucket.getImage(),0,0)

    def __listener(self):  
        self.repaint()