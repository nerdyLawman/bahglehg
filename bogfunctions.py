import time

delay = 0.0075
organic = 30

#WRITE FUNCTIONS
def write(out):
    if env.BLESSED:
        global y
        with term.hidden_cursor():
            print(term.move(y-1, xpad) + style.SCREEN + out)
    else:
        sys.stdout.write(out)
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

#SCREEN PAINTING
def paintLine():
    with term.hidden_cursor():
        print(style.SCREEN + ' ' * term.width)

def paintBackground(ypos, color):
    if env.BLESSED:
        with term.location(0, ypos):
            print(color + ' ' * term.width)

def paintHeader(ypos):
    if env.BLESSED:
        msg = "B0GGY L3GGY v0.2"
        half = term.width/2 - len(msg)/2
        adjust = term.width - half*2 - len(msg)
        with term.location(0,ypos-1):
            print(style.HEADER + ' '*half + msg + ' '*half + ' '*adjust)

def headline(msg):
    if env.BLESSED:
        global y
        half = (term.width - len(msg) - xpad*2) / 2
        with term.location(xpad, y):
            print(style.HEADER + ' '*half + msg + ' '*half)
        line()

#OUTPUT STYLES
def lineOut(inLine):
    write(inLine)
    pauseO()
    line()

def typeOut(inLine):
    outline = ''
    for char in inLine:
        outline += char
        if env.BLESSED:
            write(outline)
        else:
            write(style.HOLD + outline)
        pause()
    line()

def wordOut(inLine):
    words = inLine.split(' ')
    outword = ''
    for word in words:
        outword += word + ' '
        if env.BLESSED:
            write(outword)
        else:
            write(style.HOLD + outword)
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
    if env.BLESSED:
        testLine = inLine + ' ' + '-' * math + style.HIGHLIGHT + state + style.RESET + style.SCREEN
    else:
        testLine = inLine + ' ' + '-' * math + state
    write(testLine)
    pauseO()
    line()

def sameOut(inLine):
    words = inLine.split(' ')
    for word in words:
        if env.BLESSED:
            write(word)
        else:
            write(style.HOLD + word)
        pauseO()
    line()

def loadOut():
    for i in range(101):
        if env.BLESSED:
            write(str(i) + '%')
        else:
            write(style.HOLD + str(i) + '%')
        pauseS()
    line()

def dotOut(inLine):
    for i in range(4):
        if env.BLESSED:
            write(inLine + ('.' * i))
        else:
            write(style.HOLD + inLine + ('.' * i))
        pauseRL()
    line()
