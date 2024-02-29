from PIL import Image

class BufferImage:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.img=Image.new('RGB',(width,height),'yellow')
    
    def __getattr__(self, name):    
        """
        當嘗試訪問不存在的屬性或方法時調用
        """
        def method(*args, **kwargs):
            """
            如果self.img有對應的方法，則調用該方法
            """
            func = getattr(self.img, name)
            if callable(func):
                return func(*args, **kwargs)
            raise AttributeError(f"'{type(self.img).__name__}' object has no attribute '{name}'")

        return method