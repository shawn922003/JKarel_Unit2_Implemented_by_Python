from pyFrame.JFrame import *
from PolkaDotPanel import PolkaDotPanel

    
if __name__=="__main__":
    frame=JFrame(title="Build a House")
    frame.setSize(400,400)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(PolkaDotPanel())
    frame.setVisible(True)
    frame.fixSetting()


