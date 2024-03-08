from pyFrame.JFrame import *
from TurtlePanel import TurtlePanel
from pyFrame.Color import Color
from FlowerTurtle import FlowerTurtle

from threading import Thread


def myTurtle():    
    ft=FlowerTurtle()
    ft.setColor(Color.RED)
    ft.drawShape()
      
    
if __name__=="__main__":
    frame=JFrame(title="Build a House")
    frame.setSize(600,600)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(TurtlePanel())
    frame.setVisible(True)

    Thread(target=myTurtle).start()


    frame.fixSetting()

