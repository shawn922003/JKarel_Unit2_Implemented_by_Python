from pyFrame.JFrame import *
from PrizePanel import PrizePanel

    
if __name__=="__main__":
    frame=JFrame(title="Build a House")
    frame.setSize(400,400)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(PrizePanel())
    frame.setVisible(True)
    frame.fixSetting()


