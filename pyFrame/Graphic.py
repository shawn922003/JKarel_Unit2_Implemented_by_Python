from pyFrame.Color import Color
from PIL import Image, ImageTk

class Graphics:
    def __init__(self,canvas) -> None:
        self.__canvas=canvas
        self.color='#FFFFFF'
        self.width=8
        self.font=['Arial',None,20]
        self._pilImg=None
        self._tkImgs=[]
        self.x=0
        self.y=0

    def _setCanvas(self,canvas):
        self.__canvas=canvas
        
    def _getPilImg(self):
        return self._pilImg
    
    def setStroke(self,width:int):
        self.width=width

    def setColor(self,color:tuple)->None: # type: ignore
        self.color=Color.Color(color)
    
    def drawRect(self,x:int,y:int,width:int,height:int)->None:
        self.__canvas.create_rectangle(x,y,x+width,y+height, width=self.width, fill='',outline=self.color)

    def fillRect(self,x:int,y:int,width:int,height:int)->None:
        self.__canvas.create_rectangle(x,y,x+width,y+height, width=0, fill=self.color)

    def drawOval(self,x:int,y:int,width:int,height:int)->None:
        self.__canvas.create_oval(x, y, x+width, y+height, width=self.width, fill='', outline=self.color)

    def fillOval(self,x:int,y:int,width:int,height:int)->None:
        self.__canvas.create_oval(x, y, x+width, y+height, width=0, fill=self.color)

    def setFont(self,name:str,style:tuple,size:int)->None:
        '''
            name: 字體(請查閱 tkinter.Canvas提供何種字體)
            style: 設定粗體、底線、斜體字，不設置則設為None
            size: 字體大小
        '''
        self.font=[name,size,style]

    def drawString(self,string:str,x:int,y:int):
        self.__canvas.create_text(x,y,text=string,fill=self.color,font=self.font,anchor='sw')

    def drawImage(self,img:Image,x:int,y:int):
        '''
            img: 使用PIL.Image
            x: x軸做標
            y: y軸做標
            
            範例:
                from PIL import Image
                img=Image.open('test.jpg')
                drawImage(img,0,0)
        '''
        self.x=x
        self.y=y
        self._pilImg=img
        tkImg=ImageTk.PhotoImage(self._pilImg)
        self._tkImgs.append(tkImg) # 放進list裡，是避免離開此函數時導致tk_img被釋放掉，導致顯示不出來圖片
        self.__canvas.create_image(x, y, image=self._tkImgs[-1],anchor='nw')
        


    def drawLine(self,x1:int,y1:int,x2:int,y2:int):
        self.__canvas.create_line(x1, y1, x2, y2,width=self.width,fill=self.color)

    def drawPolygon(self,xPoints:tuple,yPoints:tuple)->None:
        '''
            xPoints = (x1, x2, x3, ...)
            yPoints = (y1, y2, y3, ...)

            和java的Polygon一樣，除了不用輸入頂點數
        '''
        assert len(xPoints) != yPoints, "xPoints長度需等於yPoints長度"

        arr=[]
        for x,y in zip(xPoints,yPoints):
            arr.append(x)
            arr.append(y)

        self.__canvas.create_polygon(arr , width=self.width, fill='', outline=self.color)

    def drawPolyLine(self,xPoints:tuple,yPoints:tuple)->None:
        '''
            xPoints = (x1, x2, x3, ...)
            yPoints = (y1, y2, y3, ...)
            
            和java的Polygon一樣，除了不用輸入頂點數
        '''
        assert len(xPoints) != yPoints, "xPoints長度需等於yPoints長度"
            
        for i in range(len(xPoints)-1):
            self.__canvas.create_line(xPoints[i], yPoints[i], xPoints[i+1], yPoints[i+1],width=self.width,fill=self.color)

    