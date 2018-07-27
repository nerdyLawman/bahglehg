import time
import sys

H = """
###   ###
###   ###
#########
###   ###
###   ###
"""

R = """
#########
###   ###
########
###   ###
###   ###
"""

delay = 0.3
height = 6
holdLine = '\033[F\033[K'

def write(out):
    sys.stdout.write((holdLine * height) + out)
    sys.stdout.flush()

def pause():
    time.sleep(delay)

def main():

    hep = "HRRH"
    for char in hep:
        if char == 'H':
            write(H)
            pause()
        if char == 'R':
            write(R)
            pause()
    print('')

if __name__ == '__main__':
    main()
