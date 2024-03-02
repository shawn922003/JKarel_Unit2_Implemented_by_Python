from PIL import ImageTk
from pyFrame.Graphic import Graphics
from pyFrame.event.MouseAdapter import MouseAdapter
from pyFrame.event.KeyAdapter import KeyAdapter
from pyFrame.event.MouseEvent import _MouseTemplateTransform
from pyFrame.event.KeyEvent import _KeyTemplateTransform
import time

class JLabel:
    def __init__(self) -> None:
        self.__canvas=None
        self.__pilImg=None
        self.__tkImg=[None,None]
        self.__mouse=None
        self.__key=None
        self.__mouseTransform=_MouseTemplateTransform()
        self.__keyTransform=_KeyTemplateTransform()

    def paintComponent(self,g:Graphics):
        raise NotImplementedError("paintComponent method must be overridden in a subclass")
    
    def addMouseListener(self,Mouse:MouseAdapter):
        self.__mouse=Mouse
        self.__mouseTransform.setMouseApp(self.__mouse)

    def addKeyListener(self,Key:KeyAdapter):
        self.__key=Key
        self.__keyTransform.setKeyApp(self.__key)


    def _setCanvas(self,canvas):
        self.__canvas=canvas
        self.__mouseBinding()
        self.__keyBinding()

    def _setPilImg(self,pilImg):
        self.__pilImg=pilImg

    def __mouseBinding(self):
        if hasattr(self.__mouse,'mousePressed'):
            self.__canvas.bind('<Button-1>',self.__mouseTransform.mousePressed, add='+' )
            self.__canvas.bind('<Button-2>',self.__mouseTransform.mousePressed, add='+')
            self.__canvas.bind('<Button-3>',self.__mouseTransform.mousePressed, add='+' )

        if hasattr(self.__mouse,'mouseClicked'):
            self.__canvas.bind('<Button-1>',self.__mouseTransform.mouseClicked, add='+' )
            self.__canvas.bind('<Button-2>',self.__mouseTransform.mouseClicked, add='+' )
            self.__canvas.bind('<Button-3>',self.__mouseTransform.mouseClicked, add='+' )

        if hasattr(self.__mouse,'mouseReleased'):
            self.__canvas.bind('<ButtonRelease-1>',self.__mouseTransform.mouseReleased, add='+' )
            self.__canvas.bind('<ButtonRelease-2>',self.__mouseTransform.mouseReleased, add='+' )
            self.__canvas.bind('<ButtonRelease-3>',self.__mouseTransform.mouseReleased, add='+' )

        if hasattr(self.__mouse,'mouseEntered'):
            self.__canvas.bind('<Enter>',self.__mouseTransform.mouseEntered, add='+' )

        if hasattr(self.__mouse,'mouseExited'):
            self.__canvas.bind('<Leave>',self.__mouseTransform.mouseExited, add='+' )

        if hasattr(self.__mouse,'mouseDragged'):
            self.__canvas.bind('<Motion>',self.__mouseTransform.mouseDragged, add='+' )
            self.__canvas.bind('<Motion>',self.__mouseTransform.mouseDragged, add='+' )
            self.__canvas.bind('<Motion>',self.__mouseTransform.mouseDragged, add='+' )

        if hasattr(self.__mouse,'mouseMoved'):
            self.__canvas.bind('<Motion>',self.__mouseTransform.mouseMoved, add='+' )
            self.__canvas.bind('<Motion>',self.__mouseTransform.mouseMoved, add='+' )
            self.__canvas.bind('<Motion>',self.__mouseTransform.mouseMoved, add='+' )


        
    def __keyBinding(self):
        self.__canvas.focus_set()
        if hasattr(self.__key,'keyTyped'):
            self.__canvas.bind('<KeyPress>',self.__keyTransform.keyTyped, add='+')
        
        if hasattr(self.__key,'keyPressed'):
            self.__canvas.bind('<KeyPress>',self.__keyTransform.keyPressed, add='+')

        if hasattr(self.__key,'keyReleased'):
            self.__canvas.bind('<KeyRelease>',self.__keyTransform.keyReleased, add='+')
        


    def repaint(self):
        while self.__pilImg is None:
            time.sleep(0.01)
        tk_img=ImageTk.PhotoImage(self.__pilImg)
        self.__tkImg.append(tk_img) 
        self.__tkImg.pop(0)
        self.__canvas.create_image(0, 0, image=self.__tkImg[-1],anchor='nw')
