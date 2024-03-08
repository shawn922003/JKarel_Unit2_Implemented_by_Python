from pyFrame.JFrame import *
from TurtlePanel import TurtlePanel
from fcps.Turtle import Turtle
from pyFrame.Color import Color
from SqareTurtle import SquareTurtle

from threading import Thread


def myTurtle():
    Turtle.setCrawl(True)     
   
    smidge = SquareTurtle()
    smidge.setColor(Color.BLUE)
    smidge.setThickness(6)
    smidge.drawShape()

    st1 = SquareTurtle(x=100,y=150,heading=45,n=100)
    st1.setColor(Color.RED)
    st1.drawShape()
    st1.setThickness(6)
    st1.setSize(200)
    st1.setThickness(12)
    st1.drawShape()
    
if __name__=="__main__":
    frame=JFrame(title="Build a House")
    frame.setSize(600,600)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(TurtlePanel())
    frame.setVisible(True)

    Thread(target=myTurtle).start()


    frame.fixSetting()

