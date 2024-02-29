import tkinter as tk
from PIL import Image,ImageTk
from pyFrame.Graphic import Graphics


class JLabel:
    def __init__(self) -> None:
        self.__canvas=None
        self.__pilImg=None
        self.__tkImg=[]

    def paintComponent(self,g:Graphics):
        raise NotImplementedError("paintComponent method must be overridden in a subclass")
    
    def setCanvas(self,canvas):
        self.__canvas=canvas

    def setPilImg(self,pilImg):
        self.__pilImg=pilImg

    def setXY(self,x,y):
        self.x=x
        self.y=y

    def repaint(self):
        assert self.__pilImg != [], "method \"repaint()\" needs to use ImageBuffer."
        tk_img=ImageTk.PhotoImage(self.__pilImg[-1])
        self.__tkImg.append(tk_img) # 放進list裡，是避免離開此函數時導致tk_img被釋放掉，導致顯示不出來圖片
        self.__canvas.create_image(self.x, self.y, image=tk_img,anchor='nw')