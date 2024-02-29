import tkinter as tk
from PIL import Image,ImageTk
from pyFrame.Graphic import Graphics
import time

class JLabel:
    def __init__(self) -> None:
        self.__canvas=None
        self.__pilImg=None
        self.__tkImg=None

    def paintComponent(self,g:Graphics):
        raise NotImplementedError("paintComponent method must be overridden in a subclass")
    
    def setCanvas(self,canvas):
        self.__canvas=canvas

    def setPilImg(self,pilImg):
        self.__pilImg=pilImg


    def repaint(self):
        while self.__pilImg is None:
            time.sleep(0.01)
        tk_img=ImageTk.PhotoImage(self.__pilImg)
        self.__tkImg=tk_img 
        self.__canvas.create_image(0, 0, image=self.__tkImg,anchor='nw')
