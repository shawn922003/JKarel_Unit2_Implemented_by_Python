from pyFrame.JFrame import JFrame
from pyFrame.JPanel import JPanel
from pyFrame.Timer import Timer
from Ball import Ball  # Assuming Ball class is properly implemented in Python
from Polkadot import Polkadot  # Assuming Polkadot class is properly implemented in Python
from Bumper import Bumper  # Assuming Bumper class is properly implemented in Python
from BumperCollision import BumperCollision  # Assuming BumperCollision is properly implemented in Python
from pyFrame.Color import Color
from pyFrame.Graphic import Graphics
from pyFrame.BufferedImage import BufferedImage

class BumperPanel(JPanel):
    __FRAME = 400
    __BACKGROUND = (204, 204, 204)
    __BALL_COLOR = Color.BLACK
    __PRIZE_COLOR = Color.RED
    __BUMPER_COLOR = Color.BLUE
    __BALL_DIAM = 50
    __PRIZE_DIAM = 25
    __BUMPER_X_WIDTH = 75
    __BUMPER_Y_WIDTH = 125

    def __init__(self):
        super().__init__()
        self.__img = BufferedImage(self.__FRAME, self.__FRAME)
        self.__img.setColor(self.__BACKGROUND)

        self.__ball = Ball(d=self.__BALL_DIAM, c=self.__BALL_COLOR)
        self.__prize = Polkadot(d=self.__PRIZE_DIAM, c=self.__PRIZE_COLOR)
        self.__bumper = Bumper(50, 50, self.__BUMPER_X_WIDTH, self.__BUMPER_Y_WIDTH, self.__BUMPER_COLOR)
        self.__hits = 0

        # Ensure ball and prize are not inside the bumper
        while self.__bumper.inBumper(self.__ball) or self.__bumper.inBumper(self.__prize):
            self.__ball.jump(self.__FRAME, self.__FRAME)
            self.__prize.jump(self.__FRAME, self.__FRAME)

        self.__timer = Timer(5, self.__listener)
        self.__timer.start()

    def paintComponent(self, g:Graphics):
        g.drawImage(self.__img,0,0)

    def __listener(self):
        # Clear and move
        self.__img.setColor(self.__BACKGROUND)
        self.__img.fillRect(0,0,self.__FRAME,self.__FRAME)

        self.__ball.move(self.__FRAME, self.__FRAME)
        BumperCollision.collide(self.__bumper, self.__ball)
        self.__collide(self.__ball, self.__prize)
        # Ensure prize is not inside the bumper
        self.__ball.draw(self.__img)
        self.__prize.draw(self.__img)
        self.__bumper.draw(self.__img)

        while self.__bumper.inBumper(self.__prize):
            self.__prize.jump(self.__FRAME, self.__FRAME)


        self.__img.setColor(Color.BLACK)
        self.__img.setFont("Arial",None,24)
        self.__img.drawString("Count: " + str(self.__hits), self.__FRAME - 150, 25)
        self.repaint()

    def __collide(self, ball:Ball, prize:Polkadot):
        dist = self.__distance(ball.getX(), ball.getY(), prize.getX(), prize.getY())
        if dist < prize.getRadius() + ball.getRadius():
            self.__hits += 1
            prize.jump(self.__FRAME, self.__FRAME)

    @staticmethod
    def __distance(x1, y1, x2, y2):
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
