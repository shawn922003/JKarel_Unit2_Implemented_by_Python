from fcps.Turtle import Turtle

class SquareTurtle(Turtle):
    def __init__(self, **kargs):
        super().__init__(**kargs)

        if 'n' in kargs:
            self.__mySize=kargs['n']
        else:
            self.__mySize=50

    def setSize(self,n:float):
        self.__mySize=n

    def drawShape(self):
        for _ in range(4):
            self.forward(self.__mySize)
            self.turnRight(90)


        