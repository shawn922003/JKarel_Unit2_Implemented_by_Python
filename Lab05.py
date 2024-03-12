from pyFrame.JPanel import JPanel
from pyFrame.Graphic import Graphics
from pyFrame.JFrame import *
from pyFrame.Color import Color
from pyFrame.BufferedImage import BufferedImage
from Bug import Bug

class Panel05(JPanel):
    __N=400
    def __init__(self) -> None:
        super().__init__()
        self.__img=BufferedImage(self.__N,self.__N)

        bugs = [Bug() for _ in range(4)]
        init_pos = [[0, 0], [0, self.__N-1], [self.__N-1, self.__N-1], [self.__N-1, 0]]

        for i in range(4):
            bugs[i] = Bug(init_pos[i][0], init_pos[i][1])

        while True:
            for i in range(4):
                bugs[i%4].walkTowards(bugs[(i+1)%4], 0.1)
                self.__img.drawLine(bugs[i%4].getX(),bugs[i%4].getY(),bugs[(i+1)%4].getX(),bugs[(i+1)%4].getY())

            if (bugs[0].sameSpot(bugs[1]) or bugs[1].sameSpot(bugs[2]) or 
                bugs[2].sameSpot(bugs[3]) or bugs[3].sameSpot(bugs[0]) or
                bugs[0].sameSpot(bugs[2]) or bugs[1].sameSpot(bugs[3])):
                break


    def paintComponent(self,g:Graphics):
        g.drawImage(self.__img, 0, 0)


if __name__=="__main__":
    frame=JFrame(title="Sun")
    frame.setSize(400,400)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(Panel05())
    frame.setVisible(True)
    frame.fixSetting()
