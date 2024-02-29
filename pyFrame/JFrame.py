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
        self.window=tk.Tk()
        self.window.title(self.title)
        self.width=400
        self.height=400
        self.x_location=0
        self.y_location=0
        self.close_operation=3
        self.visible=False
        self.window.geometry(f"{self.width}x{self.height}+{self.x_location}+{self.y_location}")
        self.setVisible(False)
        self.canvas=tk.Canvas(self.window,width=self.width,height=self.height)
        self.canvas.place(x=0,y=0)
        self.graphics=Graphics(self.canvas)

    def setSize(self,width:int,height:int)->None:
        self.width=width
        self.height=height
        self.window.geometry(f"{self.width}x{self.height}+{self.x_location}+{self.y_location}")
        self.canvas.config(width=self.width, height=self.height)

    def setLocation(self,x:int,y:int)->None:
        self.x_location=x
        self.y_location=y
        self.window.geometry(f"{self.width}x{self.height}+{self.x_location}+{self.y_location}")


    def __on_close(self,mode):
        if mode == 0:  # DO_NOTHING_ON_CLOSE
            pass
        elif mode == 1:  # HIDE_ON_CLOSE
            self.window.withdraw()
        elif mode == 2:  # DISPOSE_ON_CLOSE
            self.window.destroy()
        elif mode == 3:  # EXIT_ON_CLOSE
            self.window.quit()

    def setDefaultCloseOperation(self,operation:int):
        if operation == self.DO_NOTHING_ON_CLOSE:
            self.window.protocol("WM_DELETE_WINDOW", lambda: self.__on_close(0))
        elif operation == self.HIDE_ON_CLOSE:
            self.window.protocol("WM_DELETE_WINDOW", lambda: self.__on_close(1))
        elif operation == self.DISPOSE_ON_CLOSE:
            self.window.protocol("WM_DELETE_WINDOW", lambda: self.__on_close(2))
        elif operation == self.EXIT_ON_CLOSE:
            self.window.protocol("WM_DELETE_WINDOW", lambda: self.__on_close(3))

    def setContentPane(self,contentPane:JLabel)->None:
        self.ContentPane=contentPane
        self.ContentPane.paintComponent(self.graphics)
        self.ContentPane.setPilImg(self.graphics._getPilImg())
        self.ContentPane.setXY(self.width,self.height)

    def setVisible(self,b:bool)->None:
        self.visible=b
        if self.visible:
            self.window.deiconify()
        else:
            self.window.withdraw()

    def fixSetting(self)->None:
        self.window.mainloop()
    