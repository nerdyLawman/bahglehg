#[ty] [ok] [pa] [fa] [sm] [wo] [ri] [ce] [%]

boot = """BOGLEG v0.2 INITIALIZING
[el]>> finding secure conncetion
[el]>> establishing network
[el]>> updating repository
[%p]loading
[%p]system
[%p]hoobly

[wo]<h>CHECKING WUBMIS</e>
[ok]pitterpat
[ok]dance fabric
[ok]notched hobocamp
[ok]ghosting the spookware

[ty]he normal amount of typing for a progam like this is probably not
[ty]something you've seen before but then again we're living in a different
[ty]era entirely. Don't forget to bag your boot

[wo]Copyright 1993. Boghlehg Industries PROXXY//.1340 Epsillon Dandry Hypno.
"""

def format(badin):
    goodout = badin.replace('<b>', style.BRIGHT)
    goodout = goodout.replace('<u>', style.UNDERLINE)
    goodout = goodout.replace('<r>', fg.RED)
    goodout = goodout.replace('</r>', style.RESET)
    if env.BLESSED:
        goodout = goodout.replace('</e>', style.RESET + style.SCREEN)
    else:
        goodout = goodout.replace('</e>', style.RESET)
    return goodout

def bootsequence():
    #FLAGS (FOR BOOT)
    typing = False
    ok = False
    passf = False
    failf = False
    same = False
    word = False
    elip = False
    center = False
    right = False

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
        elif line[:4] == '[%$]':
            loadOut()
        elif line[:2] == '[:':
            for i in range(len(line)-1):
                pauseO()
        else:
            lineOut(line)
