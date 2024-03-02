from PIL import ImageTk
from pyFrame.Graphic import Graphics
from pyFrame.event.MouseAdapter import MouseAdapter
import time

class JLabel:
    def __init__(self) -> None:
        self.__canvas=None
        self.__pilImg=None
        self.__tkImg=[None,None]
        self.__mouse=None

    def paintComponent(self,g:Graphics):
        raise NotImplementedError("paintComponent method must be overridden in a subclass")
    
    def addMouseListener(self,Mouse:MouseAdapter):
        self.__mouse=Mouse

    def _setCanvas(self,canvas):
        self.__canvas=canvas
        self.__mouseBinding()
        self.__keyBinding()

    def _setPilImg(self,pilImg):
        self.__pilImg=pilImg

    def __mouseBinding(self):

        if hasattr(self.__mouse,'mousePressed'):
            self.__canvas.bind('<Button-1>',self.__mouse.mousePressed, add='+' )
            self.__canvas.bind('<Button-2>',self.__mouse.mousePressed, add='+')
            self.__canvas.bind('<Button-3>',self.__mouse.mousePressed, add='+' )

        if hasattr(self.__mouse,'mouseClicked'):
            self.__canvas.bind('<Button-1>',self.__mouse.mouseClicked, add='+' )
            self.__canvas.bind('<Button-2>',self.__mouse.mouseClicked, add='+' )
            self.__canvas.bind('<Button-3>',self.__mouse.mouseClicked, add='+' )

        if hasattr(self.__mouse,'mouseReleased'):
            self.__canvas.bind('<ButtonRelease-1>',self.__mouse.mouseReleased, add='+' )
            self.__canvas.bind('<ButtonRelease-2>',self.__mouse.mouseReleased, add='+' )
            self.__canvas.bind('<ButtonRelease-3>',self.__mouse.mouseReleased, add='+' )

        if hasattr(self.__mouse,'mouseEntered'):
            self.__canvas.bind('<Enter>',self.__mouse.mouseEntered, add='+' )

        if hasattr(self.__mouse,'mouseExited'):
            self.__canvas.bind('<Leave>',self.__mouse.mouseExited, add='+' )

        if hasattr(self.__mouse,'mouseDragged'):
            self.__canvas.bind('<Motion>',self.__mouse.mouseDragged, add='+' )
            self.__canvas.bind('<Motion>',self.__mouse.mouseDragged, add='+' )
            self.__canvas.bind('<Motion>',self.__mouse.mouseDragged, add='+' )

        if hasattr(self.__mouse,'mouseMoved'):
            self.__canvas.bind('<Motion>',self.__mouse.mouseMoved, add='+' )
            self.__canvas.bind('<Motion>',self.__mouse.mouseMoved, add='+' )
            self.__canvas.bind('<Motion>',self.__mouse.mouseMoved, add='+' )


        
    def __keyBinding(self):
        pass
        


    def repaint(self):
        while self.__pilImg is None:
            time.sleep(0.01)
        tk_img=ImageTk.PhotoImage(self.__pilImg)
        self.__tkImg.append(tk_img) 
        self.__tkImg.pop(0)
        self.__canvas.create_image(0, 0, image=self.__tkImg[-1],anchor='nw')
