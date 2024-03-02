class KeyEvent:
    VK_ENTER          = '\n'
    VK_BACK_SPACE     = '\b'
    VK_TAB            = '\t'
    VK_CANCEL         = 0x03
    VK_CLEAR          = 0x0C
    VK_SHIFT          = 0x10
    VK_CONTROL        = 0x11
    VK_ALT            = 0x12
    VK_PAUSE          = 0x13
    VK_CAPS_LOCK      = 0x14
    VK_ESCAPE         = 0x1B
    VK_SPACE          = 0x20
    VK_PAGE_UP        = 0x21
    VK_PAGE_DOWN      = 0x22
    VK_END            = 0x23
    VK_HOME           = 0x24
    VK_LEFT           = 'Left'
    VK_UP             = 'Up'
    VK_RIGHT          = 'Right'
    VK_DOWN           = 'Down'
    VK_COMMA          = 0x2C
    VK_MINUS          = 0x2D
    VK_PERIOD         = 0x2E
    VK_SLASH          = 0x2F
    VK_0              = 0x30
    VK_1              = 0x31
    VK_2              = 0x32
    VK_3              = 0x33
    VK_4              = 0x34
    VK_5              = 0x35
    VK_6              = 0x36
    VK_7              = 0x37
    VK_8              = 0x38
    VK_9              = 0x39
    VK_SEMICOLON      = 0x3B
    VK_EQUALS         = 0x3D
    VK_A              = 0x41
    VK_B              = 0x42
    VK_C              = 0x43
    VK_D              = 0x44
    VK_E              = 0x45
    VK_F              = 0x46
    VK_G              = 0x47
    VK_H              = 0x48
    VK_I              = 0x49
    VK_J              = 0x4A
    VK_K              = 0x4B
    VK_L              = 0x4C
    VK_M              = 0x4D
    VK_N              = 0x4E
    VK_O              = 0x4F
    VK_P              = 0x50
    VK_Q              = 0x51
    VK_R              = 0x52
    VK_S              = 0x53
    VK_T              = 0x54
    VK_U              = 0x55
    VK_V              = 0x56
    VK_W              = 0x57
    VK_X              = 0x58
    VK_Y              = 0x59
    VK_Z              = 0x5A
    VK_OPEN_BRACKET   = 0x5B
    VK_BACK_SLASH     = 0x5C
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
    VK_ADD            = 0x6B
    VK_SEPARATER      = 0x6C
    VK_SEPARATOR      = VK_SEPARATER
    VK_SUBTRACT       = 0x6D
    VK_DECIMAL        = 0x6E
    VK_DIVIDE         = 0x6F
    VK_DELETE         = 0x7F
    VK_NUM_LOCK       = 0x90
    VK_SCROLL_LOCK    = 0x91
    VK_F1             = 0x70
    VK_F2             = 0x71
    VK_F3             = 0x72
    VK_F4             = 0x73
    VK_F5             = 0x74
    VK_F6             = 0x75
    VK_F7             = 0x76
    VK_F8             = 0x77
    VK_F9             = 0x78
    VK_F10            = 0x79
    VK_F11            = 0x7A
    VK_F12            = 0x7B
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
    VK_WINDOWS                  = 0x020C
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

    


    
