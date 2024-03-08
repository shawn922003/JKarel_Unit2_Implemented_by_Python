from pyFrame.JFrame import *
from TurtlePanel import TurtlePanel
from pyFrame.Color import Color
from TwistyTurtle import TwistyTurtle

from threading import Thread


def myTurtle():    
    TwistyTurtle().drawShape(5,400,10,123)

      
    
if __name__=="__main__":
    frame=JFrame(title="Build a House")
    frame.setSize(600,600)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(TurtlePanel())
    frame.setVisible(True)

    Thread(target=myTurtle).start()


    frame.fixSetting()

