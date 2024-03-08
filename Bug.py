class Bug:
    def __init__(self, x=0, y=0):
        self.__myX = x
        self.__myY = y

    def getX(self):
        return self.__myX

    def getY(self):
        return self.__myY

    def walkTowards(self, arg, percent):
        if percent < 0 or percent > 1:
            return
        self.__myX = int(self.getX() + percent * (arg.__myX - self.__myX))
        self.__myY = int(self.getY() + percent * (arg.__myY - self.__myY))

    def sameSpot(self, arg):
        return self.getX() == arg.getX() and self.getY() == arg.getY()
