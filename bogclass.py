from blessed import Terminal
import datetime
import sys
from bogstyle import *

class env:
    DEBUG = False
    BLESSED = True
    LOGIN = False
    INTRO = True
    BOOTUP = True

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
        self.theme = default

    def updateHost(self, host):
        self.host = host
        self.prompt = '$' + host + ':> '

    def updateTheme(self, newtheme):
        if newtheme == 'red':
            self.theme = red
        elif newtheme == 'cyan':
            self.theme = cyan
        elif newtheme == 'black':
            self.theme = black
        else:
            self.theme = default

    #WRITE FUNCTIONS
    def write(self, out):
        if env.BLESSED:
            with self.term.hidden_cursor():
                print(self.term.move(self.y-1, self.xpad) + self.theme.SCREEN + out)
        else:
            sys.stdout.write(style.HOLD + out)
            sys.stdout.flush()

    def writeAt(self, out, y):
        if env.BLESSED:
            print(self.term.move(y, self.xpad) + self.theme.SCREEN + out)
        else:
            self.write(out)

    def centerWrite(self, out):
        if env.BLESSED:
            with self.term.hidden_cursor():
                print(self.theme.SCREEN + self.term.center(self.term.move_y(self.y-1) + out))
        else:
             self.write(out)

    def rightWrite(self, out):
        if env.BLESSED:
            with self.term.hidden_cursor():
                print(self.theme.SCREEN + self.term.move(self.y-1, self.term.width-len(out)-self.xpad-1) + out)
        else:
            self.write(out)

    def line(self):
        if env.BLESSED:
            if self.y < self.term.height - 2:
                self.y += 1
                self.paintHeader(0)
            else:
                self.paintBackground(self.y+1, self.theme.SCREENBG)
                self.paintHeader(1)
        else:
            print('')

    def jump(self, j):
        for i in range(j):
            self.line()

    #SCREEN PAINTING
    def paintLine(self):
        with self.term.hidden_cursor():
            print(self.theme.SCREEN + ' ' * self.term.width)

    def resetScreen(self):
        for y in range(self.term.height):
            self.paintBackground(y, self.theme.SCREENBG)

    def paintBackground(self, ypos, color):
        with self.term.location(0, ypos):
            print(color + ' ' * self.term.width)

    def paintHeader(self, ypos):
        msg = self.header
        half = self.term.width/2 - len(msg)/2
        adjust = self.term.width - half*2 - len(msg)
        with self.term.location(0,ypos-1):
            print(self.theme.HEADER + ' '*half + msg + ' '*half + ' '*adjust)

    def headline(self, msg, ypos):
        half = (self.term.width - len(msg) - self.xpad*2) / 2
        with self.term.location(self.xpad, ypos):
            print(self.theme.HEADER + ' '*half + msg + ' '*half)
        self.line()

    def updatePrompt(self):
        self.paintHeader(0)
        now = datetime.datetime.now()
        status = now.strftime("%Y-%m-%d %H:%M") + self.statusprompt
        with self.term.location(self.xpad, self.term.height-2):
            self.paintBackground(self.term.height-2, self.theme.HIGHLIGHT)
        with self.term.location(self.width-self.xpad-len(status), self.height-2):
            print(self.theme.HIGHLIGHT + status)
        with self.term.location(self.xpad, self.height-2):
            return raw_input(self.theme.HIGHLIGHT + self.prompt + self.theme.HIGHLIGHT)
