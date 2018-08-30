from bogclass import env, common
from bogfunctions import *
from bogstandards import *

def windowdress(b):
    print(b.term.move(0,1))
    for ypos in range(1, b.term.height+1):
        b.paintBackground(ypos, b.theme.SCREENBG)
    pauseRL()
    b.jump(3)

def login():
    init = ''
    while init != '849.9418':
        init = raw_input('IP: ')
    while init != 'bogleg':
        init = raw_input('UN: ')
    while init != 'xxx':
        init = raw_input('PW: ')

def format(b, badin):
    goodout = badin.replace('<b>', common.BRIGHT)
    goodout = goodout.replace('<u>', common.UNDERLINE)
    goodout = goodout.replace('<r>', b.theme.HIGHLIGHT)
    goodout = goodout.replace('</r>', common.RESET)
    goodout = goodout.replace('<h>', common.REVERSE)
    if env.BLESSED:
        goodout = goodout.replace('</e>', common.RESET + b.theme.SCREEN)
    else:
        goodout = goodout.replace('</e>', common.RESET)
    return goodout

def bootup(b):
    b.jump(2)
    formatted = format(b, boot)
    lines = formatted.split('\n')
    for line in lines:
        if line[:4] == '[ty]':
            typeOut(b, line[4:])
        elif line[:4] == '[ok]':
            testOut(b, line[4:], '[OK]')
        elif line[:4] == '[fa]':
            testOut(b, line[4:], '[FAIL]')
        elif line[:4] == '[pa]':
            testOut(b, line[4:], '[PASS]')
        elif line[:4] == '[sm]':
            sameOut(b, line[4:])
        elif line[:4] == '[wo]':
            wordOut(b, line[4:])
        elif line[:4] == '[el]':
            dotOut(b, line[4:])
        elif line[:4] == '[ri]':
            rightOut(b, line[4:])
        elif line[:4] == '[ce]':
            centerOut(b, line[4:])
        elif line[:4] == '[%p]':
            loadOut(b, line[4:])
        elif line[:2] == '[:':
            for i in range(len(line)-1):
                pauseO()
        else:
            lineOut(b, line)

def intro(b):
    b.jump(2)
    for i in range(3):
        pauseRL()
    if b.width -b.xpad*2 >= 100:
        logo = boglog.split('\n')
    else:
        logo = boglog.split('\n')
    for log in logo:
        centerOut(b, log)
        pauseO()
    b.jump(2)

#CLI PROGRAMS
def colOut(b, inList):
    pad = ' ' * 5
    listwidth = len(max(inList.split('\n'), key=len))
    row = ''
    b.headline('FILES', b.y)
    b.jump(2)
    for thing in inList.split('\n'):
        extra = ' ' * (listwidth - len(thing))
        row += thing + pad + extra
        if len(row) >= b.width - b.xpad*2:
            lineOut(b, row)
            row = ''

def reader(b, inLines):
    height = 2
    i = 0
    cmd = ''
    lines = inLines.split('\n')
    if env.BLESSED:
        #b.headline('LOG READER', b.y)
        #b.jump(2)
        horiz = len(max(lines, key=len))
        shift = b.term.width/2 - horiz/2 - b.xpad
    else:
        print('\nLOG READER\n')
    while i < len(lines):
        with b.term.location(1,0):
            b.paintHeader(0)
            print(b.theme.HEADER + 'LOG.txt: ' + str(i) + ' of ' + str(len(lines)))
        if cmd == 'q':
            b.paintBackground(b.term.height+1, b.theme.SCREENBG)
            break
        if cmd == 'up':
            print(b.term.move(1,3))
            print(b.term.clear())
            i -= b.term.height - 7
            height = 2
            cmd = ''
        height += 1
        if env.BLESSED:
            lineAt(b, ' ' * shift + lines[i], height)
        else:
            lineOut(b, lines[i])
        i += 1
        if height > b.term.height-6:
            if env.BLESSED:
                with b.term.location(1,0):
                    b.paintHeader(1)
                    print(b.theme.HEADER + 'LOG.txt: ' + str(i) + ' of ' + str(len(lines)))
                with b.term.location(0, b.term.height-2):
                    cmd = raw_input(b.theme.SCREEN + ' continue (q to quit): ' + b.theme.SCREEN)
                b.paintBackground(b.term.height-2, b.theme.SCREENBG)
            else:
                print('')
                cmd = raw_input('')
            print(b.term.clear())
            height = 2
    if env.BLESSED:
        with b.term.location(1,0):
            b.paintHeader(1)
            print(b.theme.HEADER + 'LOG.txt: ' + str(i) + ' of ' + str(len(lines)))
        with b.term.location(0, b.term.height-2):
            cmd = raw_input(b.theme.SCREEN + ' END OF DOC ' + b.theme.SCREEN)
        b.paintBackground(b.term.height-2, b.theme.SCREENBG)
    else:
        print('')
        cmd = raw_input('')
    print(b.term.clear())
