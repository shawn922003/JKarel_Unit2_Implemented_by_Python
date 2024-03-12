from threading import Thread
import time

class Timer:
    def __init__(self,period,function) -> None:
        self.__thread=Thread(target=self.__run,daemon=True)
        self.__switch=False
        self.__period=period/1000
        self.__function=function

    def start(self):
        self.__switch=True
        self.__thread.start()

    def stop(self):
        self.__switch=False
    
    def __run(self):
        while True:
            if self.__switch:
                time.sleep(self.__period)
                self.__function()
                