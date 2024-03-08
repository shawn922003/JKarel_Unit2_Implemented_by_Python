import abc
import time
from typing import overload

from pyFrame.BufferedImage import BufferedImage
from pyFrame.Color import Color
from pyFrame.Graphic import Graphics
from pyFrame.Timer import Timer
from pyFrame.JPanel import JPanel
from pyFrame.JFrame import JFrame
import math
from threading import Thread

class Turtle:
    WIDTH=600
    HEIGHT=600

    __graphics1=None
    __graphics2=None
    __crawlOff=None
    __crawlSpeed=None
    __list=[]



    def __init__(self, **kargs):
        if 'x' in kargs.keys():
            self.__xPos=kargs['x']
        else:
            self.__xPos=self.WIDTH/2

        if 'y' in kargs.keys():
            self.__yPos=kargs['y']
        else:
            self.__yPos=self.HEIGHT/2

        if 'heading' in kargs.keys():
            self.__heading=kargs['heading']
        else:
            self.__heading=90

        self.__turtleColor=Color.BLACK
        self.__penIsDown=True
        self.__thickness=3.0

        self.__list.append(self)
        for x in range(len(Turtle.__list)):
            Turtle.drawTurtle(Turtle.__graphics2,Turtle.__list[x].__xPos,Turtle.__list[x].__yPos,
                            Turtle.__list[x].__heading,Turtle.__list[x].__turtleColor)

    @staticmethod
    def setCrawl(b:bool):
        Turtle.__crawlOff=not b

    @staticmethod
    def setSpeed(x:int):
        if x<1 or x>10:
            return
        
        Turtle.__crawlOff=False
        Turtle.__crawlSpeed=0.05/x


    @overload
    @staticmethod
    def clear(c:Color)->None:...

    @overload
    @staticmethod
    def clear()->None:...

    @staticmethod
    def clear(c:Color=None):
        if c is None:
            c=Color.WHITE
        Turtle.__graphics1.setColor(c)
        Turtle.__graphics1.fillRect(0,0,Turtle.WIDTH,Turtle.HEIGHT)
        Turtle.__graphics2.drawImage(Turtle.__graphics1,0,0,Turtle.HEIGHT,Turtle.WIDTH)

    @staticmethod
    def drawTurtle(g:Graphics,x:float,y:float,h:float,c:Color):
        body=8
        head=4
        feet=2

        g.setColor(c)

        g.fillOval(int(0.5+x-body),int(0.5+y-body),body*2,body*2)

        g.fillOval(int(0.5+x+body*math.cos(h*math.pi/180))-head,
                   int(0.5+y-body*math.sin(h*math.pi/180))-head,
                   head*2,head*2)
        
        angles = [-45, -135, 45, 135]
        for angle in angles:
            g.fillOval(int(0.5 + x + body * math.cos((h + angle) * math.pi / 180)) - feet,
                    int(0.5 + y - body * math.sin((h + angle) * math.pi / 180)) - feet,
                    feet * 2, feet * 2)
            
    
    def pause(self):
        time.sleep(Turtle.__crawlSpeed*2)

    def setThickness(self,x:int):
        self.__thickness=float(x)

    def forward(self,amount:float):
        dx=amount * math.cos(self.__heading*math.pi/180)
        dy=amount * math.sin(self.__heading*math.pi/180)

        temp1=self.__xPos+dx
        temp2=self.__yPos-dy

        Turtle.__graphics1.setStroke(self.__thickness)

        oldX=self.__xPos
        oldY=self.__yPos

        if Turtle.__crawlOff:
            self.__xPos+=dx
            self.__yPos+=dy

            if self.__penIsDown:
                Turtle.__graphics1.setColor(self.__turtleColor)
                Turtle.__graphics1.drawLine(int(0.5+oldX),int(0.5+oldY),
                                          int(0.5+self.__xPos),int(0.5+self.__yPos))
                Turtle.__graphics2.drawImage(Turtle.__graphics1,0,0,self.WIDTH,self.HEIGHT)
                for x in range(len(Turtle.__list)):
                    Turtle.drawTurtle(Turtle.__graphics2,Turtle.__list[x].__xPos,Turtle.__list[x].__yPos,
                                    Turtle.__list[x].__heading,Turtle.__list[x].__turtleColor)

        else:
            track=3
            sum=0
            done=False
            while not done:
                self.__xPos=oldX+track*math.cos(self.__heading*math.pi/180)
                self.__yPos=oldY-track*math.sin(self.__heading*math.pi/180)

                if self.__penIsDown:
                    Turtle.__graphics1.setColor(self.__turtleColor)
                    Turtle.__graphics1.drawLine(int(0.5+oldX),int(0.5+oldY),
                                                int(0.5+self.__xPos),int(0.5+self.__yPos))
                
                Turtle.__graphics2.drawImage(Turtle.__graphics1,0,0,self.WIDTH,self.HEIGHT)
                for x in range(len(Turtle.__list)):
                    Turtle.drawTurtle(Turtle.__graphics2,Turtle.__list[x].__xPos,Turtle.__list[x].__yPos,
                                  Turtle.__list[x].__heading,Turtle.__list[x].__turtleColor)
                self.pause()
                oldX=self.__xPos
                oldY=self.__yPos
                if sum + 2*track >= amount:
                    done=True

                sum+=track
            
            if self.__penIsDown:
                Turtle.__graphics1.setColor(self.__turtleColor)
                Turtle.__graphics1.drawLine(int(0.5+self.__xPos),int(0.5+self.__yPos),
                                          int(0.5+temp1),int(0.5+temp2))
                
            Turtle.__graphics2.drawImage(Turtle.__graphics1,0,0,self.WIDTH,self.HEIGHT)
            for x in range(len(Turtle.__list)):
                Turtle.drawTurtle(Turtle.__graphics2,Turtle.__list[x].__xPos,Turtle.__list[x].__yPos,
                                  Turtle.__list[x].__heading,Turtle.__list[x].__turtleColor)
            self.pause()
            self.__xPos=temp1
            self.__yPos=temp2
            Turtle.__graphics2.drawImage(Turtle.__graphics1,0,0,self.WIDTH,self.HEIGHT)
            for x in range(len(Turtle.__list)):
                Turtle.drawTurtle(Turtle.__graphics2,Turtle.__list[x].__xPos,Turtle.__list[x].__yPos,
                                  Turtle.__list[x].__heading,Turtle.__list[x].__turtleColor)
            self.pause()

    def back(self,amount:float):
        self.forward(-1*amount)

    def turnRight(self,degrees:float):
        if Turtle.__crawlOff:
            self.__heading-=degrees
        
        else:
            interval=5
            if degrees<0:
                interval = -interval
            temp=self.__heading-degrees

            while abs(self.__heading-temp)>abs(interval):
                self.__heading-=interval
                Turtle.__graphics2.drawImage(Turtle.__graphics1,0,0,self.WIDTH,self.HEIGHT)
                for x in range(len(Turtle.__list)):
                    Turtle.drawTurtle(Turtle.__graphics2,Turtle.__list[x].__xPos,Turtle.__list[x].__yPos,
                                    Turtle.__list[x].__heading,Turtle.__list[x].__turtleColor)
                self.pause()

            self.__heading=temp
            Turtle.__graphics2.drawImage(Turtle.__graphics1,0,0,self.WIDTH,self.HEIGHT)
            for x in range(len(Turtle.__list)):
                Turtle.drawTurtle(Turtle.__graphics2,Turtle.__list[x].__xPos,Turtle.__list[x].__yPos,
                                  Turtle.__list[x].__heading,Turtle.__list[x].__turtleColor)
            self.pause()


    def turnLeft(self,degrees:float):
        self.turnRight(-degrees)

    def getColor(self)->Color:
        return self.__turtleColor
    
    def setColor(self,c:Color):
        self.__turtleColor=c
        Turtle.__graphics1.setColor(self.__turtleColor)

    
    def setPenDown(self,x:bool):
        self.__penIsDown=x

    

    @abc.abstractmethod
    def drawShape(self):
        return NotImplemented
    
    @staticmethod
    def static_initializer_block():
        Turtle.__graphics1 = BufferedImage(Turtle.HEIGHT,Turtle.WIDTH)
        Turtle.__graphics2 = BufferedImage(Turtle.HEIGHT,Turtle.WIDTH)
        Turtle.__crawlOff=False
        Turtle.__crawlSpeed=0.005
        Turtle.clear(Color.GREEN)
    
    @staticmethod
    def getImage():
        if not Turtle.__crawlOff:
            for x in range(len(Turtle.__list)):
                Turtle.drawTurtle(Turtle.__graphics2,Turtle.__list[x].__xPos,Turtle.__list[x].__yPos,
                                  Turtle.__list[x].__heading,Turtle.__list[x].__turtleColor)
                
            
        return Turtle.__graphics2
        

Turtle.static_initializer_block() # 當import 此python檔時，會自動調用static initializer block (沒看過有人把python這樣用)


if __name__=="__main__":
    class Panel(JPanel):
        def __init__(self) -> None:
            super().__init__()

            self.__timer=Timer(10,self.__listener)
            self.__timer.start()

        def paintComponent(self, g: Graphics):
            g.drawImage(Turtle.getImage(),0,0)

        def __listener(self):  
            self.repaint()

    def turtleMove():
        t=Turtle()
        t.setSpeed(10)
        t.forward(250)
        t.turnLeft(90)
        t.forward(250)

    frame=JFrame(title="Build a House")
    frame.setSize(600,600)
    frame.setLocation(100,100)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    frame.setContentPane(Panel())
    frame.setVisible(True)

    Thread(target=turtleMove,daemon=True).start()

    frame.fixSetting()
