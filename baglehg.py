import sys
import os
import socket

from bogclass import BOG, env, common
from bogfiles import *
from bogfunctions import pause, pauseRL
from bogprograms import bootup, intro, windowdress, login, colOut, reader, cmdBreak

def main():

    #THE ALL IMPORTANT CLASS
    bog = BOG()

    #LOGIN
    if env.LOGIN:
        login()

    #SET WINDOW
    os.system('clear')
    bog.updateHost(socket.gethostbyname(socket.gethostname()))
    sys.stdout.write(bog.window)
    pauseRL()
    if env.BLESSED:
        windowdress(bog)

    #BOOTUP
    if env.BOOTUP:
        bootup(bog)

    #INTRO
    if env.INTRO:
        intro(bog)

    #MAIN PROGRAM
    cmd = ''
    run = True
    while run:
        if env.BLESSED:
            cmd = bog.updatePrompt()
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

        # THEMES
        if cmd == 'theme':
            if env.BLESSED:
                bog.updateTheme('default')
        if cmd == 'theme red':
            if env.BLESSED:
                bog.updateTheme('red')
        if cmd == 'theme cyan':
            if env.BLESSED:
                bog.updateTheme('cyan')
        if cmd == 'theme black':
            if env.BLESSED:
                bog.updateTheme('black')

    #CLEAN UP
    print(common.RESET)
    os.system('clear')

if __name__ == '__main__':
    main()
