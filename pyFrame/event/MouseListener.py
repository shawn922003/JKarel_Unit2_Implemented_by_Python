import abc

class MouseListener:
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def mouseClicked(self,e):
        return NotImplemented
    
    @abc.abstractmethod
    def mousePressed(self,e):
        return NotImplemented
    
    @abc.abstractmethod
    def mouseReleased(self,e):
        return NotImplemented
    
    @abc.abstractmethod
    def mouseEntered(self,e):
        return NotImplemented
    
    def mouseExited(self,e):
        pass