import datetime
import sys
import os
import socket

#from bogfiles import *
from bogfunctions import pause, pauseRL
from bogclass import BOG, env, fg, bg, style
from bogprograms import bootup, intro, windowdress, login, colOut, reader

def main():

    #THE ALL IMPORTANT CLASS
    bog = BOG()

    #LOGIN
    if env.LOGIN:
        login()

    #SET WINDOW
    bog.updateHost(socket.gethostbyname(socket.gethostname()))
    sys.stdout.write(bog.window)
    os.system('clear')
    pauseRL()
    if env.BLESSED:
        windowdress(bog)

    #BOOTUP
    if env.BOOTUP:
        bootup(bog)

    #INTRO
    if env.INTRO:
        intro(bog)

    #CLI / MAIN PROGRAM
    cmd = ''
    run = True
    while run:
        if env.BLESSED:
            now = datetime.datetime.now()
            status = now.strftime("%Y-%m-%d %H:%M") + bog.statusprompt
            bog.paintHeader(0)
            with bog.term.location(bog.xpad, bog.term.height-2):
                bog.paintBackground(bog.term.height-2, style.HIGHLIGHT)
            with bog.term.location(bog.width-bog.xpad-len(status), bog.height-2):
                print(style.HIGHLIGHT + status)
            with bog.term.location(bog.xpad, bog.height-2):
                cmd = raw_input(style.HIGHLIGHT + bog.prompt + style.HIGHLIGHT)
        else:
            cmd = raw_input(bog.prompt)
        if cmd == 'exit' or cmd == 'q' or cmd == 'quit':
            run = False

        #CLI PROGRAMS

        #LOG (TO BECOME READER)
        if cmd == 'log':
            if env.BLESSED:
                cmdBreak(bog)
            reader(bog, log)

        #FILES
        if cmd == 'files':
            if env.BLESSED:
                cmdBreak(bog)
            colOut(bog, files)

    #CLEAN UP
    print(style.RESET)
    os.system('clear')

if __name__ == '__main__':
    main()
