from PIL import Image,ImageDraw,ImageFont
from pyFrame.Color import Color

class BufferedImage:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.color = "#000000"  # 預設顏色
        self.font = ImageFont.load_default()  # 預設字體
        self.__img=Image.new('RGB',(width,height),'white')
        self.__drawObj=ImageDraw.Draw(self.__img)

    def __getattr__(self,name):    
        return getattr(self.__img,name)
    
    def setStroke(self,width:int):
        self.width=width

    def setColor(self,color:tuple)->None: # type: ignore
        self.color=Color.Color(color)
    
    def drawRect(self,x:int,y:int,width:int,height:int)->None:
        self.__drawObj.rectangle(((x, y), (x + width, y + height)), outline=self.color)

    def fillRect(self,x:int,y:int,width:int,height:int)->None:
        self.__drawObj.rectangle(((x,y),(x+width,y+height)),fill=self.color)

    def drawOval(self,x:int,y:int,width:int,height:int)->None:
        self.__drawObj.ellipse((x, y, x + width, y + height), outline=self.color)

    def fillOval(self,x:int,y:int,width:int,height:int)->None:
        self.__drawObj.ellipse((x,y,x+width,y+height),fill=self.color)

    def setFont(self,name:str,style:tuple,size:int)->None:
        '''
            name: 字體(請查閱 tkinter.Canvas提供何種字體)
            style: 設定粗體、底線、斜體字，不設置則設為None (在BufferedImage中不支援)
            size: 字體大小
        '''
        self.font = ImageFont.truetype(name.lower(), size,encoding='UTF-8')

    def drawString(self,string:str,x:int,y:int):
        self.__drawObj.text((x, y), string, fill=self.color, font=self.font)

    def drawLine(self,x1:int,y1:int,x2:int,y2:int):
        self.__drawObj.line((x1, y1, x2, y2), fill=self.color)

    def drawPolygon(self,xPoints:tuple,yPoints:tuple)->None:
        '''
            xPoints = (x1, x2, x3, ...)
            yPoints = (y1, y2, y3, ...)

            和java的Polygon一樣，除了不用輸入頂點數
        '''
        assert len(xPoints) != yPoints, "xPoints長度需等於yPoints長度"
        points = list(zip(xPoints, yPoints))
        self.__drawObj.polygon(points, outline=self.color)

    def drawPolyLine(self,xPoints:tuple,yPoints:tuple)->None:
        '''
            xPoints = (x1, x2, x3, ...)
            yPoints = (y1, y2, y3, ...)
            
            和java的Polygon一樣，除了不用輸入頂點數
        '''
        assert len(xPoints) != yPoints, "xPoints長度需等於yPoints長度"
        points = list(zip(xPoints, yPoints))
        self.__drawObj.line(points, fill=self.color)
        

    