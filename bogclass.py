from blessed import Terminal
import sys

class env:
    DEBUG = False
    BLESSED = True
    LOGIN = False
    INTRO = True
    BOOTUP = True

#STYLE CLASSES
class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSE = '\033[7m'
    DISABLE = '\033[02m'
    HOLD = '\n\033[F\033[K'
    SCREENFG = BOLD + fg.BLUE
    SCREENBG = bg.WHITE
    SCREEN = SCREENFG + SCREENBG
    HEADERFG = fg.WHITE
    HEADERBG = bg.BLUE
    HEADER = HEADERFG + HEADERBG
    HIGHLIGHT = HEADER

class BOG:

    def __init__(self):
        self.term = Terminal()
        self.x = 0
        self.y = 0
        self.xpad = 4
        self.width = self.term.width
        self.height = self.term.height
        self.window = "\x1b]2;BOHHHGLEHHGGGGGGGGG!!!!!???!!!?!?\x07"
        self.header = "B0GGY L3GGY v0.2"
        self.host = ''
        self.prompt = '$' + self.host + ':> '
        self.statusprompt = ' | h for HELP | exit to quit'

    def updateHost(self, host):
        self.host = host
        self.prompt = '$' + host + ':> '

    #WRITE FUNCTIONS
    def write(self, out):
        if env.BLESSED:
            with self.term.hidden_cursor():
                print(self.term.move(self.y-1, self.xpad) + style.SCREEN + out)
        else:
            sys.stdout.write(style.HOLD + out)
            sys.stdout.flush()

    def centerWrite(self, out):
        if env.BLESSED:
            with self.term.hidden_cursor():
                print(style.SCREEN + self.term.center(self.term.move_y(self.y-1) + out))
        else:
             self.write(out)

    def rightWrite(self, out):
        if env.BLESSED:
            with self.term.hidden_cursor():
                print(style.SCREEN + self.term.move(self.y-1, self.term.width-len(out)-self.xpad-1) + out)
        else:
            self.write(out)

    def line(self):
        if env.BLESSED:
            if self.y < self.term.height - 2:
                self.y += 1
                self.paintHeader(0)
            else:
                self.paintBackground(self.y+1, style.SCREENBG)
                self.paintHeader(1)
        else:
            print('')

    def jump(self, j):
        for i in range(j):
            self.line()

    #SCREEN PAINTING
    def paintLine(self):
        with self.term.hidden_cursor():
            print(style.SCREEN + ' ' * self.term.width)

    def paintBackground(self, ypos, color):
        with self.term.location(0, ypos):
            print(color + ' ' * self.term.width)

    def paintHeader(self, ypos):
        msg = self.header
        half = self.term.width/2 - len(msg)/2
        adjust = self.term.width - half*2 - len(msg)
        with self.term.location(0,ypos-1):
            print(style.HEADER + ' '*half + msg + ' '*half + ' '*adjust)

    def headline(self, msg, ypos):
        half = (self.term.width - len(msg) - self.xpad*2) / 2
        with self.term.location(self.xpad, ypos):
            print(style.HEADER + ' '*half + msg + ' '*half)
        self.line()
