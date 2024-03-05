from fcps.Bucket import Bucket
from pyFrame.JFrame import JFrame
from BucketPanel import BucketPanel
from threading import Thread

def bucketAlg():
    Bucket.setSpeed(5)
    Bucket.useTotal(True)

    five=Bucket(5)
    three=Bucket(3)

    three.fill()
    three.spill()
    five.fill()
    three.fill()
    three.spill()
    five.pourInto(three)
    three.spill()
    five.pourInto(three)
    five.fill()
    five.pourInto(three)
    three.spill()
    five.pourInto(three)
    three.spill()
    three.fill()
    five.spill()
    three.pourInto(five)
    three.fill()

if __name__=="__main__":


    frame=JFrame(title="Build a House")
    frame.setSize(600,600)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(BucketPanel())
    frame.setVisible(True)

    Thread(target=bucketAlg,daemon=True).start()

    frame.fixSetting()