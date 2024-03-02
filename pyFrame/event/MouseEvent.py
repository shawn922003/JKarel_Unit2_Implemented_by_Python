class MouseEvent:
    BUTTON1=1
    BUTTON2=2
    BUTTON3=3
    def __init__(self,event) -> None:
        self.__event=event

    def isShiftDown(self):
        return self.__event.state & 0x0001

    def getBotton(self):
        return self.__event.num

    def getX(self):
        return self.__event.x

    def getY(self):
        return self.__event.y
    
class _MouseTemplateTransform:
    def __init__(self) -> None:
        self.__mouseApp=None

    def setMouseApp(self,mouseApp):
        self.__mouseApp=mouseApp

    def mousePressed(self,event):
        mouseEvent=MouseEvent(event)
        self.__mouseApp.mousePressed(mouseEvent)

    def mouseClicked(self,event):
        mouseEvent=MouseEvent(event)
        self.__mouseApp.mouseClicked(mouseEvent)
    
    def mouseReleased(self,event):
        mouseEvent=MouseEvent(event)
        self.__mouseApp.mouseReleased(mouseEvent)

    def mouseEntered(self,event):
        mouseEvent=MouseEvent(event)
        self.__mouseApp.mouseEntered(mouseEvent)

    def mouseExited(self,event):
        mouseEvent=MouseEvent(event)
        self.__mouseApp.mouseExited(mouseEvent)

    def mouseDragged(self,event):
        mouseEvent=MouseEvent(event)
        self.__mouseApp.mouseDragged(mouseEvent)

    def mouseMoved(self,event):
        mouseEvent=MouseEvent(event)
        self.__mouseApp.mouseMoved(mouseEvent)
    

