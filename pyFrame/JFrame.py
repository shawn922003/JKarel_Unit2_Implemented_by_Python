import tkinter as tk
from pyFrame.Graphic import Graphics
from pyFrame.JLabel import JLabel


class JFrame:
    DO_NOTHING_ON_CLOSE = 0
    HIDE_ON_CLOSE = 1
    DISPOSE_ON_CLOSE = 2
    EXIT_ON_CLOSE=3

    def __init__(self,**args):
        if 'title' in args.keys():
            self.title=args['title']
        else:
            self.title=''
        self.__window=tk.Tk()
        self.__window.title(self.title)
        self.width=400
        self.height=400
        self.x_location=0
        self.y_location=0
        self.close_operation=3
        self.visible=False
        self.__window.geometry(f"{self.width}x{self.height}+{self.x_location}+{self.y_location}")
        self.setVisible(False)
        self.__canvas=tk.Canvas(self.__window,width=self.width,height=self.height)
        self.__canvas.place(x=0,y=0)
        self.__graphics=Graphics(self.__canvas)

    def setSize(self,width:int,height:int)->None:
        self.width=width
        self.height=height
        self.__window.geometry(f"{self.width}x{self.height}+{self.x_location}+{self.y_location}")
        self.__canvas.config(width=self.width, height=self.height)

    def setLocation(self,x:int,y:int)->None:
        self.x_location=x
        self.y_location=y
        self.__window.geometry(f"{self.width}x{self.height}+{self.x_location}+{self.y_location}")


    def __on_close(self,mode):
        if mode == 0:  # DO_NOTHING_ON_CLOSE
            pass
        elif mode == 1:  # HIDE_ON_CLOSE
            self.__window.withdraw()
        elif mode == 2:  # DISPOSE_ON_CLOSE
            self.__window.destroy()
        elif mode == 3:  # EXIT_ON_CLOSE
            self.__window.quit()

    def setDefaultCloseOperation(self,operation:int):
        if operation == self.DO_NOTHING_ON_CLOSE:
            self.__window.protocol("WM_DELETE_WINDOW", lambda: self.__on_close(0))
        elif operation == self.HIDE_ON_CLOSE:
            self.__window.protocol("WM_DELETE_WINDOW", lambda: self.__on_close(1))
        elif operation == self.DISPOSE_ON_CLOSE:
            self.__window.protocol("WM_DELETE_WINDOW", lambda: self.__on_close(2))
        elif operation == self.EXIT_ON_CLOSE:
            self.__window.protocol("WM_DELETE_WINDOW", lambda: self.__on_close(3))

    def setContentPane(self,contentPane:JLabel)->None:
        self.__contentPane=contentPane
        self.__contentPane.paintComponent(self.__graphics)
        self.__contentPane._setCanvas(self.__canvas)
        self.__contentPane._setPilImg(self.__graphics._getPilImg())
        

    def setVisible(self,b:bool)->None:
        self.visible=b
        if self.visible:
            self.__window.deiconify()
        else:
            self.__window.withdraw()

    def fixSetting(self)->None:
        self.__window.mainloop()
    