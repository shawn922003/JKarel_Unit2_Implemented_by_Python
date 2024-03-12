from Ball import Ball
from Bumper import Bumper

class BumperCollision:
    __nearestX = 0  # 用来大致估算球与保险杠碰撞的点
    __nearestY = 0

    @staticmethod
    def collide(bumper:Bumper, ball:Ball):
        if bumper.inBumper(ball):
            # 将球移动到刚好在保险杠外
            while bumper.inBumper(ball):
                ball.setX(ball.getX() - ball.getdx() / 10.0)
                ball.setY(ball.getY() - ball.getdy() / 10.0)
            
            # 找到与球最近的保险杠边缘点
            BumperCollision.__findImpactPoint(bumper, ball)
            
            ux = BumperCollision.__nearestX - ball.getX()
            uy = BumperCollision.__nearestY - ball.getY()
            ur = (ux**2 + uy**2)**0.5
            ux /= ur
            uy /= ur
            dx, dy = ball.getdx(), ball.getdy()
            dot_1 = ux * dx + uy * dy
            dot_2 = -uy * dx + ux * dy
            dot_1 *= -1  # 实现反弹
            d = [dot_1 * ux - dot_2 * uy, dot_1 * uy + dot_2 * ux]
            dx, dy = round(d[0]), round(d[1])
            ball.setdx(dx)
            ball.setdy(dy)

    @staticmethod
    def __findImpactPoint(bumper:Bumper, ball:Ball):
        BumperCollision.__nearestX = bumper.getX()
        BumperCollision.__nearestY = bumper.getY()
        

        for x in range(bumper.getX(), bumper.getX() + bumper.getXWidth() + 1):
            BumperCollision.__updateIfCloser(x, bumper.getY(), ball)
            BumperCollision.__updateIfCloser(x, bumper.getY() + bumper.getYWidth(), ball)
        
        for y in range(bumper.getY(), bumper.getY() + bumper.getYWidth() + 1):
            BumperCollision.__updateIfCloser(bumper.getX(), y, ball)
            BumperCollision.__updateIfCloser(bumper.getX() + bumper.getXWidth(), y, ball)

    @staticmethod
    def __updateIfCloser(x, y, ball:Ball):
        if BumperCollision.__distance(x, y, ball.getX(), ball.getY()) < BumperCollision.__distance(BumperCollision.__nearestX, BumperCollision.__nearestY, ball.getX(), ball.getY()):
            BumperCollision.__nearestX = x
            BumperCollision.__nearestY = y

    @staticmethod
    def __distance(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
