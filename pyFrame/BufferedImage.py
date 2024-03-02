from PIL import Image,ImageDraw
from pyFrame.Color import Color

class BufferedImage:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.__img=Image.new('RGB',(width,height),'yellow')
        self.__drawObj=ImageDraw.Draw(self.__img)
    
    def __getattr__(self,name):    
        return getattr(self.__img,name)
    

    def setStroke(self,width:int):
        self.width=width

    def setColor(self,color:tuple)->None: # type: ignore
        self.color=Color.Color(color)
    
    def drawRect(self,x:int,y:int,width:int,height:int)->None:
        pass

    def fillRect(self,x:int,y:int,width:int,height:int)->None:
        self.__drawObj.rectangle(((x,y),(x+width,y+height)),fill=self.color)

    def drawOval(self,x:int,y:int,width:int,height:int)->None:
        pass

    def fillOval(self,x:int,y:int,width:int,height:int)->None:
        self.__drawObj.ellipse((x,y,x+width,y+height),fill=self.color)

    def setFont(self,name:str,style:tuple,size:int)->None:
        '''
            name: 字體(請查閱 tkinter.Canvas提供何種字體)
            style: 設定粗體、底線、斜體字，不設置則設為None
            size: 字體大小
        '''
        self.font=[name,size,style]

    def drawString(self,string:str,x:int,y:int):
        pass

    def drawLine(self,x1:int,y1:int,x2:int,y2:int):
        pass

    def drawPolygon(self,xPoints:tuple,yPoints:tuple)->None:
        '''
            xPoints = (x1, x2, x3, ...)
            yPoints = (y1, y2, y3, ...)

            和java的Polygon一樣，除了不用輸入頂點數
        '''
        assert len(xPoints) != yPoints, "xPoints長度需等於yPoints長度"

        

    def drawPolyLine(self,xPoints:tuple,yPoints:tuple)->None:
        '''
            xPoints = (x1, x2, x3, ...)
            yPoints = (y1, y2, y3, ...)
            
            和java的Polygon一樣，除了不用輸入頂點數
        '''
        assert len(xPoints) != yPoints, "xPoints長度需等於yPoints長度"
            
        

    