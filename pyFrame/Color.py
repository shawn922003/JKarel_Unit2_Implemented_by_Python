

class Color:
    WHITE = (255, 255, 255)
    LIGHT_GRAY = (192, 192, 192)
    GRAY = (128, 128, 128)
    DARK_GRAY = (64, 64, 64)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    PINK = (255, 175, 175)
    ORANGE = (255, 200, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)

    def __init__(self) -> None:
        pass

    @staticmethod
    def __tuple_to_hex_color(color_tuple):
        hex_color='#'
        for i in range(3):
            if color_tuple[i]<16:
                hex_color+=f'0{color_tuple[i]:1x}'
            else:
                hex_color+=f'{color_tuple[i]:2x}'
        return hex_color

    @staticmethod
    def Color(color:tuple):
        return Color.__tuple_to_hex_color(color)
