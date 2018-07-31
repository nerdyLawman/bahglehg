from bogfunctions import pauseRL, pauseO, centerOut
from bogstandards import bogboy, smallboy

def intro(width):
    for i in range(3):
        pauseRL()
    if width >= 100:
        bogs = bogboy.split('\n')
    else:
        bogs = smallboy.split('\n')
    for bog in bogs:
        centerOut(bog)
        pauseO()
