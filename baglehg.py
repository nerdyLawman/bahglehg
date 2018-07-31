import time
import datetime
import sys
import os
import socket
from random import randint
from blessed import Terminal

from bogstandards import *
from bogfiles import *
from bogboot import boot

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

class env:
    DEBUG = False
    BLESSED = True
    LOGIN = False
    INTRO = True
    BOOTUP = True

term = Terminal()
delay = 0.0075
organic = 30
if env.BLESSED:
    width = term.width
else:
    width = 80
xpad = 4
x, y = 0, 0

#HELPER FUNCTIONS
def format(badin):
    goodout = badin.replace('<b>', style.BRIGHT)
    goodout = goodout.replace('<u>', style.UNDERLINE)
    goodout = goodout.replace('<r>', fg.RED)
    goodout = goodout.replace('</r>', style.RESET)
    goodout = goodout.replace('<h>', style.REVERSE)
    if env.BLESSED:
        goodout = goodout.replace('</e>', style.RESET + style.SCREEN)
    else:
        goodout = goodout.replace('</e>', style.RESET)
    return goodout

#WRITE FUNCTIONS
def write(out):
    if env.BLESSED:
        global y
        with term.hidden_cursor():
            print(term.move(y-1, xpad) + style.SCREEN + out)
    else:
        sys.stdout.write(style.HOLD + out)
        sys.stdout.flush()

def centerWrite(out):
    if env.BLESSED:
        global y
        with term.hidden_cursor():
            print(style.SCREEN + term.center(term.move_y(y-1) + out))
    else:
         write(out)

def rightWrite(out):
    if env.BLESSED:
        global y
        with term.hidden_cursor():
            print(style.SCREEN + term.move(y-1, term.width-len(out)-xpad-1) + out)
    else:
        write(out)

def line():
    if env.BLESSED:
        global y
        if y < term.height - 2:
            y += 1
            paintHeader(0)
        else:
            paintBackground(y+1, style.SCREENBG)
            paintHeader(1)
    else:
        print('')

def jump(j):
    for i in range(j):
        line()

#SCREEN PAINTING
def paintLine():
    with term.hidden_cursor():
        print(style.SCREEN + ' ' * term.width)

def paintBackground(ypos, color):
    with term.location(0, ypos):
        print(color + ' ' * term.width)

def paintHeader(ypos):
    msg = "B0GGY L3GGY v0.2"
    half = term.width/2 - len(msg)/2
    adjust = term.width - half*2 - len(msg)
    with term.location(0,ypos-1):
        print(style.HEADER + ' '*half + msg + ' '*half + ' '*adjust)

def headline(msg, ypos):
    half = (term.width - len(msg) - xpad*2) / 2
    with term.location(xpad, ypos):
        print(style.HEADER + ' '*half + msg + ' '*half)
    line()

#GIVE ME PAUSE
def pause():
    time.sleep(delay)

def pauseO():
    time.sleep(delay * randint(1, organic))

def pauseS():
    time.sleep(delay/2)

def pauseL():
    time.sleep(delay*15)

def pauseRL():
    time.sleep(delay*30)

#OUTPUT STYLES
def lineOut(inLine):
    write(inLine)
    pauseO()
    line()

def typeOut(inLine):
    outline = ''
    for char in inLine:
        outline += char
        write(outline)
        pause()
    line()

def wordOut(inLine):
    words = inLine.split(' ')
    outword = ''
    for word in words:
        outword += word + ' '
        write(outword)
        pauseO()
    line()

def shiftOut(inLine, shift):
    pad = ''
    for i in range(shift):
        pad += ' '
    write(pad + inLine)
    pauseO()
    line()

def centerOut(inLine):
    centerWrite(inLine)
    pause()
    line()

def rightOut(inLine):
    rightWrite(inLine)
    pause()
    line()

def testOut(inLine, state):
    math = width-(xpad*2+(len(state)+2)+len(inLine))
    testLine = inLine + ' ' + '-' * math + style.REVERSE + state + style.RESET
    write(testLine)
    pauseO()
    line()

def sameOut(inLine):
    words = inLine.split(' ')
    for word in words:
        write(word)
        pauseO()
    line()

def loadOut(inLine):
    for i in range(101):
        write(str(i) + '%')
        pauseS()
    pauseL()
    write('100% ' + inLine)
    line()

def dotOut(inLine):
    for i in range(4):
        write(inLine + ('.' * i))
        pauseRL()
    line()

#CLI PROGRAMS
def colOut(inList):
    pad = ' ' * 5
    listwidth = len(max(inList.split('\n'), key=len))
    row = ''
    headline('FILES', y)
    jump(2)
    for thing in inList.split('\n'):
        extra = ' ' * (listwidth - len(thing))
        row += thing + pad + extra
        if len(row) >= term.width - xpad*2:
            lineOut(row)
            row = ''

def readOut(inLines):
    height = 1
    global y
    i = 0
    cmd = ''
    lines = inLines.split('\n')
    if env.BLESSED:
        headline('LOG READER', y)
        jump(2)
        horiz = len(max(lines, key=len))
        shift = term.width/2 - horiz/2 - xpad
    else:
        print('\nLOG READER\n')
    while i <= len(lines)-1:
        with term.location(1,0):
            paintHeader(0)
            print(style.HEADER + 'LOG.txt: ' + str(i) + ' of ' + str(len(lines)))
        if cmd == 'q':
            paintBackground(term.height+1, style.SCREENBG)
            break
        if cmd == 'up':
            print(term.move(1,3))
            print(term.clear())
            i -= 10
            cmd = ''
        height += 1
        if env.BLESSED:
            shiftOut(lines[i], shift)
        else:
            lineOut(lines[i])
        i += 1
        if height > term.height-20:
            if env.BLESSED:
                with term.location(1,0):
                    paintHeader(1)
                    print(style.HEADER + 'LOG.txt: ' + str(i) + ' of ' + str(len(lines)))
                with term.location(0,term.height-2):
                    cmd = raw_input(style.SCREEN + ' continue (q to quit): ' + style.SCREEN)
                paintBackground(term.height-2, style.SCREENBG)
            else:
                print('')
                cmd = raw_input('')
            height -= 10

def main():

    if env.BLESSED:
        height, width = term.height, term.width
    else:
        height, width = 25, 80

    #LOGIN
    if env.LOGIN:
        init = ''
        while init != '849.9418':
            init = raw_input('IP: ')
        while init != 'bogleg':
            init = raw_input('UN: ')
        while init != 'xxx':
            init = raw_input('PW: ')

    #SET WINDOW
    sys.stdout.write("\x1b]2;BOHHHGLEHHGGGGGGGGG!!!!!???!!!?!?\x07")
    os.system('clear')
    pauseRL()
    if env.BLESSED:
        print(term.move(0,1))
        for ypos in range(1,term.height+1):
            paintBackground(ypos, style.SCREENBG)
        pauseRL()
        jump(3)

    #INTRO
    if env.INTRO:
        for i in range(3):
            pauseRL()
        if width -xpad*2 >= 100:
            bogs = bogboy.split('\n')
        else:
            bogs = smallboy.split('\n')
        for bog in bogs:
            centerOut(bog)
            pauseO()

    #BOOTUP
    if env.BOOTUP:
        jump(2)
        formatted = format(boot)
        lines = formatted.split('\n')
        for line in lines:
            if line[:4] == '[ty]':
                typeOut(line[4:])
            elif line[:4] == '[ok]':
                testOut(line[4:], '[OK]')
            elif line[:4] == '[fa]':
                testOut(line[4:], '[FAIL]')
            elif line[:4] == '[pa]':
                testOut(line[4:], '[PASS]')
            elif line[:4] == '[sm]':
                sameOut(line[4:])
            elif line[:4] == '[wo]':
                wordOut(line[4:])
            elif line[:4] == '[el]':
                dotOut(line[4:])
            elif line[:4] == '[ri]':
                rightOut(line[4:])
            elif line[:4] == '[ce]':
                centerOut(line[4:])
            elif line[:4] == '[%p]':
                loadOut(line[4:])
            elif line[:2] == '[:':
                for i in range(len(line)-1):
                    pauseO()
            else:
                lineOut(line)

    #CLI / MAIN PROGRAM
    cmd = ''
    host = socket.gethostbyname(socket.gethostname())
    while cmd != 'exit':
        if env.BLESSED:
            now = datetime.datetime.now()
            status = now.strftime("%Y-%m-%d %H:%M") + ' | h for HELP | exit to quit'
            paintHeader(0)
            with term.location(xpad, term.height-2):
                paintBackground(term.height-2, style.HIGHLIGHT)
            with term.location(term.width-xpad-len(status), term.height-2):
                print(style.HIGHLIGHT + status)
            with term.location(xpad, term.height-2):
                cmd = raw_input(style.HIGHLIGHT + '$' + host + ':> ' + style.HIGHLIGHT)
        else:
            cmd = raw_input('$' + host + ':> ')

        #CLI PROGRAMS
        #LOG (TO BECOME READER)
        if cmd == 'log':
            if env.BLESSED:
                paintHeader(0)
                paintBackground(term.height-2, style.SCREENBG)
            readOut(log)

        #FILES
        if cmd == 'files':
            if env.BLESSED:
                paintHeader(0)
                paintBackground(term.height-2, style.SCREENBG)
            colOut(files)

    #CLEAN UP
    print(style.RESET)
    os.system('clear')

if __name__ == '__main__':
    main()
