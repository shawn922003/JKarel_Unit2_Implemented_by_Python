class KeyEvent:
    '''
        英文有分大小寫，shift、alt、ctrl只有左鍵有用
    '''
    VK_ENTER          = 'Enter'
    VK_BACK_SPACE     = 'BackSpace'
    VK_TAB            = 'Tab'
    VK_CANCEL         = 0x03
    VK_CLEAR          = 0x0C
    VK_SHIFT          = 'Shift_L'
    VK_CONTROL        = 'Ctrl_L'
    VK_ALT            = 'Alt_L'
    VK_PAUSE          = 'Pause'
    VK_CAPS_LOCK      = 'Caps_Lock'
    VK_ESCAPE         = 'Escape'
    VK_SPACE          = 'space'
    VK_PAGE_UP        = 'Prior'
    VK_PAGE_DOWN      = 'Next'
    VK_END            = 'End'
    VK_HOME           = 'Home'
    VK_LEFT           = 'Left'
    VK_UP             = 'Up'
    VK_RIGHT          = 'Right'
    VK_DOWN           = 'Down'
    VK_COMMA          ='comma'
    VK_MINUS          = 'minus'
    VK_PERIOD         = 0x2E
    VK_SLASH          = 'slash'
    VK_0              = '0'
    VK_1              = '1'
    VK_2              = '2'
    VK_3              = '3'
    VK_4              = '4'
    VK_5              = '5'
    VK_6              = '6'
    VK_7              = '7'
    VK_8              = '8'
    VK_9              = '9'
    VK_SEMICOLON      = ';'
    VK_EQUALS         = 'equal'
    VK_A              = 'A'
    VK_B              = 'B'
    VK_C              = 'C'
    VK_D              = 'D'
    VK_E              = 'E'
    VK_F              = 'F'
    VK_G              = 'G'
    VK_H              = 'H'
    VK_I              = 'I'
    VK_J              = 'J'
    VK_K              = 'K'
    VK_L              = 'L'
    VK_M              = 'M'
    VK_N              = 'N'
    VK_O              = 'O'
    VK_P              = 'P'
    VK_Q              = 'Q'
    VK_R              = 'R'
    VK_S              = 'S'
    VK_T              = 'T'
    VK_U              = 'U'
    VK_V              = 'V'
    VK_W              = 'W'
    VK_X              = 'X'
    VK_Y              = 'Y'
    VK_Z              = 'Z'
    VK_a = 'a'
    VK_b = 'b'
    VK_c = 'c'
    VK_d = 'd'
    VK_e = 'e'
    VK_f = 'f'
    VK_g = 'g'
    VK_h = 'h'
    VK_i = 'i'
    VK_j = 'j'
    VK_k = 'k'
    VK_l = 'l'
    VK_m = 'm'
    VK_n = 'n'
    VK_o = 'o'
    VK_p = 'p'
    VK_q = 'q'
    VK_r = 'r'
    VK_s = 's'
    VK_t = 't'
    VK_u = 'u'
    VK_v = 'v'
    VK_w = 'w'
    VK_x = 'x'
    VK_y = 'y'
    VK_z = 'z'
    VK_OPEN_BRACKET   = 0x5B
    VK_BACK_SLASH     = 'backslash'
    VK_CLOSE_BRACKET  = 0x5D
    VK_NUMPAD0        = 0x60
    VK_NUMPAD1        = 0x61
    VK_NUMPAD2        = 0x62
    VK_NUMPAD3        = 0x63
    VK_NUMPAD4        = 0x64
    VK_NUMPAD5        = 0x65
    VK_NUMPAD6        = 0x66
    VK_NUMPAD7        = 0x67
    VK_NUMPAD8        = 0x68
    VK_NUMPAD9        = 0x69
    VK_MULTIPLY       = 0x6A
    VK_ADD            = 'plus'
    VK_SEPARATER      = 0x6C
    VK_SEPARATOR      = VK_SEPARATER
    VK_SUBTRACT       = 0x6D
    VK_DECIMAL        = 0x6E
    VK_DIVIDE         = 0x6F
    VK_DELETE         = 0x7F
    VK_NUM_LOCK       = 0x90
    VK_SCROLL_LOCK    = 'Scroll_Lock'
    VK_F1             = 'F1'
    VK_F2             = 'F2'
    VK_F3             = 'F3'
    VK_F4             = 'F4'
    VK_F5             = 'F5'
    VK_F6             = 'F6'
    VK_F7             = 'F7'
    VK_F8             = 'F8'
    VK_F9             = 'F9'
    VK_F10            = 'F10'
    VK_F11            = 'F11'
    VK_F12            = 'F12'
    VK_F13            = 0xF000
    VK_F14            = 0xF001
    VK_F15            = 0xF002
    VK_F16            = 0xF003
    VK_F17            = 0xF004
    VK_F18            = 0xF005
    VK_F19            = 0xF006
    VK_F20            = 0xF007
    VK_F21            = 0xF008
    VK_F22            = 0xF009
    VK_F23            = 0xF00A
    VK_F24            = 0xF00B
    VK_PRINTSCREEN    = 0x9A
    VK_INSERT         = 0x9B
    VK_HELP           = 0x9C
    VK_META           = 0x9D
    VK_BACK_QUOTE     = 0xC0
    VK_QUOTE          = 0xDE
    VK_KP_UP          = 0xE0
    VK_KP_DOWN        = 0xE1
    VK_KP_LEFT        = 0xE2
    VK_KP_RIGHT       = 0xE3
    VK_DEAD_GRAVE               = 0x80
    VK_DEAD_ACUTE               = 0x81
    VK_DEAD_CIRCUMFLEX          = 0x82
    VK_DEAD_TILDE               = 0x83
    VK_DEAD_MACRON              = 0x84
    VK_DEAD_BREVE               = 0x85
    VK_DEAD_ABOVEDOT            = 0x86
    VK_DEAD_DIAERESIS           = 0x87
    VK_DEAD_ABOVERING           = 0x88
    VK_DEAD_DOUBLEACUTE         = 0x89
    VK_DEAD_CARON               = 0x8a
    VK_DEAD_CEDILLA             = 0x8b
    VK_DEAD_OGONEK              = 0x8c
    VK_DEAD_IOTA                = 0x8d
    VK_DEAD_VOICED_SOUND        = 0x8e
    VK_DEAD_SEMIVOICED_SOUND    = 0x8f
    VK_AMPERSAND                = 0x96
    VK_ASTERISK                 = 0x97
    VK_QUOTEDBL                 = 0x98
    VK_LESS                     = 0x99
    VK_GREATER                  = 0xa0
    VK_BRACELEFT                = 0xa1
    VK_BRACERIGHT               = 0xa2
    VK_AT                       = 0x0200
    VK_COLON                    = 0x0201
    VK_CIRCUMFLEX               = 0x0202
    VK_DOLLAR                   = 0x0203
    VK_EURO_SIGN                = 0x0204
    VK_EXCLAMATION_MARK         = 0x0205
    VK_INVERTED_EXCLAMATION_MARK = 0x0206
    VK_LEFT_PARENTHESIS         = 0x0207
    VK_NUMBER_SIGN              = 0x0208
    VK_PLUS                     = 0x0209
    VK_RIGHT_PARENTHESIS        = 0x020A
    VK_UNDERSCORE               = 0x020B
    VK_WINDOWS                  = 'Win_L'
    VK_CONTEXT_MENU             = 0x020D


    def __init__(self,event) -> None:
        self.__event=event

    def getKeyCode(self):
        return self.__event.keysym

    def getKeyChar(self):
        return self.__event.char

class _KeyTemplateTransform:
    def __init__(self) -> None:
        self.__keyApp=None

    def setKeyApp(self,keyApp):
        self.__keyApp=keyApp

    def keyTyped(self,event):
        keyEvent=KeyEvent(event)
        self.__keyApp.keyTyped(keyEvent)

    def keyPressed(self,event):
        keyEvent=KeyEvent(event)
        self.__keyApp.keyPressed(keyEvent)

    def keyReleased(self,event):
        keyEvent=KeyEvent(event)
        self.__keyApp.keyReleased(keyEvent)

    


    

