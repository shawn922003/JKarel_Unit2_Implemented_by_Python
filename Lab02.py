from pyFrame.JPanel import JPanel
from pyFrame.Graphic import Graphics
from pyFrame.JFrame import *
from pyFrame.Color import Color
from PIL import Image

class Panel02(JPanel):
    def __init__(self) -> None:
        super().__init__()
        self.__img=Image.open("tj.jpg")

    def paintComponent(self,g:Graphics):
        g.setColor(Color.RED)
        g.fillRect(0, 0, 400, 400)

        g.setColor(Color.YELLOW)
        for i in range(130,136+128+21,20):
            for j in range(34,40+169+21,20):
                g.fillOval(i-10,j-10,25,25)

        g.drawImage(self.__img, 136, 43)

        g.setColor(Color.WHITE)
        g.setFont("Arial",'bold',20)
        g.drawString("Our Fearless Leader", 100, 300)


if __name__=="__main__":
    frame=JFrame(title="Our Fearless Leader")
    frame.setSize(400,400)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(Panel02())
    frame.setVisible(True)
    frame.fixSetting()
