from bogclass import env, common
from bogfunctions import *
from bogstandards import *

def windowdress(bog):
    print(bog.term.move(0,1))
    for ypos in range(1,bog.term.height+1):
        bog.paintBackground(ypos, bog.theme.SCREENBG)
    pauseRL()
    bog.jump(3)

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

def bootup(bog):
    bog.jump(2)
    formatted = format(bog, boot)
    lines = formatted.split('\n')
    for line in lines:
        if line[:4] == '[ty]':
            typeOut(bog, line[4:])
        elif line[:4] == '[ok]':
            testOut(bog, line[4:], '[OK]')
        elif line[:4] == '[fa]':
            testOut(bog, line[4:], '[FAIL]')
        elif line[:4] == '[pa]':
            testOut(bog, line[4:], '[PASS]')
        elif line[:4] == '[sm]':
            sameOut(bog, line[4:])
        elif line[:4] == '[wo]':
            wordOut(bog, line[4:])
        elif line[:4] == '[el]':
            dotOut(bog, line[4:])
        elif line[:4] == '[ri]':
            rightOut(bog, line[4:])
        elif line[:4] == '[ce]':
            centerOut(bog, line[4:])
        elif line[:4] == '[%p]':
            loadOut(bog, line[4:])
        elif line[:2] == '[:':
            for i in range(len(line)-1):
                pauseO()
        else:
            lineOut(bog, line)

def intro(bog):
    bog.jump(2)
    for i in range(3):
        pauseRL()
    if bog.width -bog.xpad*2 >= 100:
        logo = boglog.split('\n')
    else:
        logo = boglog.split('\n')
    for log in logo:
        centerOut(bog, log)
        pauseO()
    bog.jump(2)

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

def reader(bog, inLines):
    height = 1
    i = 0
    cmd = ''
    lines = inLines.split('\n')
    if env.BLESSED:
        bog.headline('LOG READER', bog.y)
        bog.jump(2)
        horiz = len(max(lines, key=len))
        shift = bog.term.width/2 - horiz/2 - bog.xpad
    else:
        print('\nLOG READER\n')
    while i <= len(lines)-1:
        with bog.term.location(1,0):
            bog.paintHeader(0)
            print(bog.theme.HEADER + 'LOG.txt: ' + str(i) + ' of ' + str(len(lines)))
        if cmd == 'q':
            bog.paintBackground(bog.term.height+1, bog.theme.SCREENBG)
            break
        if cmd == 'up':
            print(bog.term.move(1,3))
            print(bog.term.clear())
            i -= 10
            cmd = ''
        height += 1
        if env.BLESSED:
            shiftOut(bog, lines[i], shift)
        else:
            lineOut(bog, lines[i])
        i += 1
        if height > bog.term.height-20:
            if env.BLESSED:
                with bog.term.location(1,0):
                    bog.paintHeader(1)
                    print(bog.theme.HEADER + 'LOG.txt: ' + str(i) + ' of ' + str(len(lines)))
                with bog.term.location(0,bog.term.height-2):
                    cmd = raw_input(bog.theme.SCREEN + ' continue (q to quit): ' + bog.theme.SCREEN)
                bog.paintBackground(bog.term.height-2, bog.theme.SCREENBG)
            else:
                print('')
                cmd = raw_input('')
            height -= 10
