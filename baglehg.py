import time
import sys
from random import randint

boot = """Testing testing
[ty]\nThis should be typed\n[*ty]
Buddy Testing
[ok]\nthis should be OK
this should too
I'm gonna go ahead and call this okay as well\n[*ok]
[fa]\nAnd maybe this one fails\n[*fa]
[pa]\nBut this passes\n[*pa]
[:*]
back to normal for a spell
[ty]\nbut more typing\n[*ty]
[sm]\nbut what about?\n[*sm]
[%]
[:****]
[wo]\nGet the Word out boyee\n[*wo]
[el]\nAnd I'll think about this one\n[*el]
"""

#CONSTANTS
delay = 0.01
organic = 10
width = 80

holdLine = '\n\033[F\033[K'

#FLAGS

#HELPER FUNCTIONS
def write(out):
    sys.stdout.write(out)
    sys.stdout.flush()

def pause():
    time.sleep(delay)

def pauseO():
    time.sleep(delay * randint(0, organic))

def pauseS():
    time.sleep(delay/2)

def pauseL():
    time.sleep(delay*10)

def pauseRL():
    time.sleep(delay*100)

def line():
    print('')

def jump():
    print('\n')

#OUTPUT STYLES
def typeOut(inLine):
    for char in inLine:
        write(char)
        pause()
    line()

def wordOut(inLine):
    words = inLine.split(' ')
    for word in words:
        write(word + ' ')
        pauseO()
    line()

def lineOut(inLine):
    write(inLine)
    line()
    pauseL()

def okOut(inLine):
    okLine = inLine + ' ' + '-' * (width-len(inLine)-5) + "[OK]"
    write(okLine)
    line()
    pauseL()

def failOut(inLine):
    okLine = inLine + ' ' + '-' * (width-len(inLine)-7) + "[FAIL]"
    write(okLine)
    line()
    pauseL()

def passOut(inLine):
    okLine = inLine + ' ' + '-' * (width-len(inLine)-7) + "[PASS]"
    write(okLine)
    line()
    pauseL()

def sameOut(inLine):
    for char in inLine:
        write(holdLine + char)
        pauseL()
    line()

def loadOut():
    for i in range(101):
        write(holdLine + str(i) + '%')
        pauseS()
    line()

def dotOut(inLine):
    for i in range(4):
        write(holdLine + inLine + ' ' + ('.' * i))
        pauseL()

def main():

    typing = False
    ok = False
    passf = False
    failf = False
    same = False
    word = False
    elip = False

    lines = boot.split('\n')

    for line in lines:
        if line == '[ty]':
            typing = True
        elif line == '[*ty]':
            typing = False
        elif line == '[ok]':
            ok = True
        elif line == '[*ok]':
            ok = False
        elif line == '[sm]':
            same = True
        elif line == '[*sm]':
            same = False
        elif line == '[wo]':
            word = True
        elif line == '[*wo]':
            word = False
        elif line == '[el]':
            elip = True
        elif line == '[*el]':
            elip = False
        elif line == '[fa]':
            failf = True
        elif line == '[*fa]':
            failf = False
        elif line == '[pa]':
            passf = True
        elif line == '[*pa]':
            passf = False
        elif line == '[%]':
            loadOut()
        elif line[:2] == '[:':
            for i in range(len(line)-1):
                pauseO()
        else:
            if typing:
                typeOut(line)
            elif ok:
                okOut(line)
            elif same:
                sameOut(line)
            elif word:
                wordOut(line)
            elif elip:
                dotOut(line)
            elif failf:
                failOut(line)
            elif passf:
                passOut(line)
            else:
                lineOut(line)

if __name__ == '__main__':
    main()
