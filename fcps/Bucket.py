from threading import Thread
import time
from pyFrame.JPanel import JPanel
from pyFrame.JFrame import JFrame
from pyFrame.Color import Color
from pyFrame.Graphic import Graphics
from pyFrame.Timer import Timer
from pyFrame.BufferedImage import BufferedImage

from typing import overload

class Bucket:
    __MAX_CAPACITY=8
    __MAX_BUCKETS=3

    __buffer=None
    __diff=None
    __numBuckets=None
    __totalWater=None
    __useTotal=None
    __shownWin=None
    __doneList=[]
    __jugList=[]
    __commands=None

    @overload
    def __init__(self)->None:...

    @overload
    def __init__(self,numGals:int)->None:...

    def __init__(self, numGals=None) -> None:
        if numGals is None:
            self.__capacity=0

        else:
            self.__capacity=numGals

        self.__water=0

        Bucket.__jugList[Bucket.__numBuckets]=self
        Bucket.__numBuckets+=1
        if self.__capacity>Bucket.__MAX_CAPACITY:
            self.__capacity=Bucket.__MAX_CAPACITY

        Bucket.draw()

    @staticmethod
    def useTotal(b:bool):
        Bucket.__useTotal=b

    @staticmethod
    def setSpeed(x:int):
        if x<1 or x>10:
            return
        Bucket.__diff=x*0.1

    def pause(self):
        time.sleep(0.1)

    def fill(self):
        Bucket.__commands+=1
        temp=self.__capacity-int(self.__water)
        while self.__water+Bucket.__diff/100 < self.__capacity:
            self.__water+=Bucket.__diff
            Bucket.draw()
            self.pause()
            if self.__water+self.__diff/100 > self.__capacity:
                self.__water=float(self.__capacity)
                Bucket.draw()
                self.pause()

        self.__water=float(self.__capacity)
        Bucket.__totalWater+=temp
        
        if Bucket.__useTotal:
            Bucket.__doneList[Bucket.__totalWater]=True
        else:
            Bucket.__doneList[int(self.__water)]=True
        Bucket.draw()

    def spill(self):
        Bucket.__commands+=1
        temp=int(self.__water)
        while self.__water > Bucket.__diff/100:
            self.__water-=temp
            Bucket.draw()
            self.pause()

        self.__water=0
        Bucket.__totalWater-=temp
        if Bucket.__useTotal:
            Bucket.__doneList[Bucket.__totalWater]=True
        Bucket.draw()

    def pourInto(self,dest:'Bucket'):
        Bucket.__commands+=1
        w1=self.__water
        w2=dest.__water
        temp=dest.__capacity-int(dest.__water)

        if temp > int(self.__water):
            temp = int(self.__water)

        while self.__water > Bucket.__diff/100 and dest.__water + Bucket.__diff/100 < dest.__capacity:
            dest.__water+=Bucket.__diff
            self.__water -= Bucket.__diff
            Bucket.draw()
            self.pause()

        self.__water = w1 - float(temp)
        dest.__water=w2+float(temp)
        if not Bucket.__useTotal:
            Bucket.__doneList[int(self.__water)]=True
            Bucket.__doneList[int(dest.__water)]=True
        Bucket.draw()

    @staticmethod
    def draw():
        Bucket.__buffer.setFont("Arial", None, 10)
        count = 1
        max = 0
        if Bucket.__useTotal:
            for index in range(Bucket.__numBuckets):
                max += Bucket.__jugList[index].__capacity
        else:
            for index in range(Bucket.__numBuckets):
                if Bucket.__jugList[index].__capacity > max:
                    max = Bucket.__jugList[index].__capacity

        win = True
        if max == 0:
            win = False
        for x in range(60,int(550-550/len(Bucket.__doneList)),int(500/len(Bucket.__doneList))):
            if count > max:
                Bucket.__buffer.setColor(Color.GRAY)
            elif Bucket.__doneList[count]:
                Bucket.__buffer.setColor(Color.RED)
            else:
                Bucket.__buffer.setColor(Color.WHITE)
                win = False
            
            Bucket.__buffer.drawString( str(count), x, 50)
            count+=1
        
    

        Bucket.__buffer.setFont( "Arial", None, 14)
        space = (600 - 50) / Bucket.__MAX_BUCKETS
        for index in range(Bucket.__numBuckets):
            start = 50 + index * space + 10
            end = (index + 1) * space - 10
            scale = 200 / Bucket.__MAX_CAPACITY
            Bucket.__buffer.setColor(Color.BLACK)
            for loop in range(1,Bucket.__jugList[index].__capacity+1):
                Bucket.__buffer.drawString(str( loop), start - 20, 
                            300 - int(scale * (loop - 0.5)))
        
            Bucket.__buffer.setColor(Color.WHITE)
            Bucket.__buffer.fillRect(start, 300 - scale * Bucket.__jugList[index].__capacity,
                        end - start, scale * Bucket.__jugList[index].__capacity)
            Bucket.__buffer.setColor(Color.BLACK)
            Bucket.__buffer.drawRect(start, 300 - scale * Bucket.__jugList[index].__capacity,
                        end - start, scale * Bucket.__jugList[index].__capacity)
            Bucket.__buffer.setColor(Color.BLUE)
            if 301 - int(scale * Bucket.__jugList[index].__water) < 300 - scale * Bucket.__jugList[index].__capacity:
                Bucket.__buffer.fillRect(start + 1, 301 - scale * Bucket.__jugList[index].__capacity,
                            end - start - 1, scale * Bucket.__jugList[index].__capacity - 1)
    
            else:
                Bucket.__buffer.fillRect(start + 1, 301 - int(scale * Bucket.__jugList[index].__water),
                            end - start - 1, int(scale * Bucket.__jugList[index].__water) - 1)
        
    
        if win:
            if not Bucket.__shownWin:
                Bucket.__shownWin = True

                Bucket.__buffer.setColor(Color.YELLOW)
                Bucket.__buffer.setFont( "Arial", None, 25)
                Bucket.__buffer.drawString("Well Done - " + str(Bucket.__commands) + " commands", 160, 330)

            else:
                Bucket.__buffer.setColor(Color.YELLOW)
                Bucket.__buffer.setFont( "Arial", None, 25)
                Bucket.__buffer.drawString("Well Done - " + str(Bucket.__commands) + " commands", 160, 330)


    


    @staticmethod
    def getImage():
        Bucket.__buffer.setColor(Color.GRAY)
        Bucket.__buffer.fillRect(0,375,600,25)
        Bucket.__buffer.setColor(Color.GREEN)
        Bucket.__buffer.fillRect(0,0,600,375)
        Bucket.__buffer.setColor(Color.BLACK)
        Bucket.__buffer.fillRect(25,300,550,50)
        Bucket.__buffer.fillRect(50,350,25,50)
        Bucket.__buffer.fillRect(525,350,25,50)

        return Bucket.__buffer

    @staticmethod
    def staticInitializerBlock():
        Bucket.__buffer=BufferedImage(600,400)
        Bucket.__diff=1
        Bucket.__numBuckets=0
        Bucket.__totalWater=0
        Bucket.__useTotal=False
        Bucket.__shownWin=False
        Bucket.__doneList=[False]*(Bucket.__MAX_BUCKETS*Bucket.__MAX_CAPACITY)
        Bucket.__jugList=[None]*(Bucket.__MAX_BUCKETS)
        Bucket.__commands=0

    
Bucket.staticInitializerBlock()

if __name__=="__main__":
    class Panel(JPanel):
        def __init__(self) -> None:
            super().__init__()

            self.__timer=Timer(10,self.__listener)
            self.__timer.start()

        def paintComponent(self, g: Graphics):
            g.drawImage(Bucket.getImage(),0,0)

        def __listener(self):  
            self.repaint()

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


    frame=JFrame(title="Build a House")
    frame.setSize(600,600)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(Panel())
    frame.setVisible(True)

    Thread(target=bucketAlg,daemon=True).start()

    frame.fixSetting()


