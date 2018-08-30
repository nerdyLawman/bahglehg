import time
from random import randint

class timing:
    DELAY = 0.0075
    ORGANIC = 30

#GIVE ME PAUSE
def pause():
    time.sleep(timing.DELAY)

def pauseO():
    time.sleep(timing.DELAY * randint(1, timing.ORGANIC))

def pauseS():
    time.sleep(timing.DELAY/2)

def pauseL():
    time.sleep(timing.DELAY*15)

def pauseRL():
    time.sleep(timing.DELAY*30)

#OUTPUT STYLES
def lineOut(b, inLine):
    b.write(inLine)
    pauseO()
    b.line()

def lineAt(b, inLine, at):
    b.writeAt(inLine, at)
    pauseO()
    #b.line()

def typeOut(b, inLine):
    outline = ''
    for char in inLine:
        outline += char
        b.write(outline)
        pause()
    b.line()

def wordOut(b, inLine):
    words = inLine.split(' ')
    outword = ''
    for word in words:
        outword += word + ' '
        b.write(outword)
        pauseO()
    b.line()

def shiftOut(b, inLine, shift):
    pad = ''
    for i in range(shift):
        pad += ' '
    b.write(pad + inLine)
    pauseO()
    b.line()

def centerOut(b, inLine):
    b.centerWrite(inLine)
    pause()
    b.line()

def rightOut(b, inLine):
    b.rightWrite(inLine)
    pause()
    b.line()

def testOut(b, inLine, state):
    math = b.term.width-(b.xpad*2+(len(state)+2)+len(inLine))
    testLine = inLine + ' ' + '-' * math + b.theme.HIGHLIGHT + state + b.theme.SCREEN
    b.write(testLine)
    pauseO()
    b.line()

def sameOut(b, inLine):
    words = inLine.split(' ')
    for word in words:
        b.write(word)
        pauseO()
    b.line()

def loadOut(b, inLine):
    for i in range(101):
        b.write(str(i) + '%')
        pauseS()
    pauseL()
    b.write('100% ' + inLine)
    b.line()

def dotOut(b, inLine):
    for i in range(4):
        b.write(inLine + ('.' * i))
        pauseRL()
    b.line()

def cmdBreak(b):
    b.paintHeader(0)
    b.paintBackground(b.height-2, b.theme.SCREENBG)
