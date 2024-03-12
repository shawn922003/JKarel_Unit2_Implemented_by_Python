from pyFrame.JFrame import *
from RiddlePanel import RiddlePanel

    
if __name__=="__main__":
    frame=JFrame(title="Build a House")
    frame.setSize(400,400)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(RiddlePanel())
    frame.setVisible(True)
    frame.fixSetting()


