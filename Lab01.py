from pyFrame.JPanel import JPanel
from pyFrame.Graphic import Graphics
from pyFrame.JFrame import *
from pyFrame.Color import Color

class Panel01(JPanel):
    def __init__(self) -> None:
        super().__init__()

    def paintComponent(self,g:Graphics):
        g.setColor(Color.LIGHT_GRAY)
        g.fillRect(0, 0, 400, 400)

        g.setFont("Arial", 'bold',20)
        g.setColor(Color.WHITE)
        g.drawString("Welcome Home", 40, 40)

        g.setColor(Color.YELLOW)
        g.fillOval(300, 75, 50, 50)

        g.setColor(Color.BLACK)
        g.drawPolygon((75,175,275), (200,150,200))

        g.setColor(Color.RED)
        g.drawRect(100, 200, 150, 150)

        g.setColor(Color.BLACK)
        g.fillRect(150, 275, 50, 75)

        g.setStroke(20)
        g.setColor(Color.GREEN)
        g.drawLine(0, 350, 400, 350)

        g.setColor(Color.WHITE)
        for i in range(0,400,40):
            g.fillOval(i,80,50,25)


if __name__=="__main__":
    frame=JFrame(title="Build a House")
    frame.setSize(400,400)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(Panel01())
    frame.setVisible(True)
    frame.fixSetting()
