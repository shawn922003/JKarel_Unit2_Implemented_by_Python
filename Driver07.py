from pyFrame.JFrame import *
from TurtlePanel import TurtlePanel
from pyFrame.Color import Color
from PolygonTurtle import PolygonTurtle

from threading import Thread


def myTurtle():    
    smidge = PolygonTurtle(400,300,90,100.0, 3)
    smidge.setColor(Color.BLUE)
    smidge.setThickness(6)
    for i in range(3,11):
        smidge.setSides(i)
        smidge.drawShape()
      
    
if __name__=="__main__":
    frame=JFrame(title="Build a House")
    frame.setSize(600,600)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(TurtlePanel())
    frame.setVisible(True)

    Thread(target=myTurtle).start()


    frame.fixSetting()

