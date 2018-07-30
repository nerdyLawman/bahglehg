import time
import sys
import os
from random import randint
from blessed import Terminal

smallboy = """MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWNKXXNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMKxoccloOXMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMN0ddOXd::;:o0WMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMXxk0XXx:,,;:cd0XWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMN0dokko,     .:okO0XMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMXkol:,..         '::odxKWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNk:::;:'            .:c,,lkNMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMWKkd:',:;.              .',:::l0WMMMMMMMMMMMMMMM
MMMMMMMMMMMNkolc::;.                  ,c:''lOO0NMMMMMMMMMMMM
MMMMMMMMMWKoll;,;'...'..   ..          .'.,oddlo0NMMMMMMMMMM
MMMMMMMNOxkkkoc:,,;:,,:;,....   ...,,;'',',:'.,'.,dXWMMMMMMM
MMMMMMXxd0WXxkOd,..,,,;;;:,. ..;;',,''..,:::l:'...:dxxONMMMM
MMMMWKdkKOddkOl'......';,,ol'..;c::;,'..''.,cc.  ..;oOOOXWMM
MMMMWXXO:.  ''....''..',:lo'    .:dc;'.......,;.'''. .;oKWMM
MMMMMMOc:;..,'..';;,.  'kK:  'c. .lo'..,;ccc'.,;'''..  ;0MMM
MMMMMXddl'.....''.      co.  ..   ',  ..:Ok;. ..',. . .cKMMM
MMMMMNKx..'.  ;l',;.    .,.       ..     dO'  .. ;;lxc,lXMMM
MMMMMMWo  ,'  ;:,kx'...'lx:..  ..'ok:..'c0X:  .. ,ckMWNXWMMM
MMMMMMWOoodd:.;..ONd'lXNWNo...':ONW0;..cKMX;  .':ox0MMMMMMMM
MMMMMMMMMMW0c,.  o0, :XMWx.  .;cOWNl  .'lXk.   'kNMMMMMMMMMM
MMMMMMMMMMNc     .:. .;dO;   .,,l00,    'o,  ''.oWMMMMMMMMMM
MMMMMMMMMMWd.     ...   '.       .c.   .'.   ;l,xMMMMMMMMMMM
MMMMMMMMMMWO:.      .,,,:'       .l:.',.  .  'dONMMMMMMMMMMM
MMMMMMMMMMMWNk'   ...'';odoc:;;:lxOdc;.      '0MMMMMMMMMMMMM
MMMMMMMMMMMMMWo.. ;oxk,   .,ol;,'':,,dc,. .'.oNMMMMMMMMMMMMM
MMMMMMMMMMMMW0::d,:KW0'    .kOoc. cOOXNx..cxONMMMMMMMMMMMMMM
MMMMMMMMMMMMNOOXko0WMNc.:, .xMMNo.oWMMKc;xNMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNWMMMMOo0Xo;OMMMXkKMMMKOXMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWWMMNNWMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"""

bogboy = """MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOoclooddd0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKc;cdd::clccdKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXko;cKMXo,'...:ookNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXdclcdXMMWXkdddc'':lxXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXc:0MMMMW0c.   .:xo,ckkOXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0llKNK00Ol.       'olcOX0kOXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOolddlcoo;.          .';coO0kxONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXx:coo;'....              .:l,.:OockXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMXd,;oo;.;l'       .           'l;.cx;.:oKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWK:.,xc..cdc.       .     .      'xx,..,occKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNOoc:,',.'okc.                       .::;;,:loldXMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWOoldxd,.':l;.                            'lo,.',.:KWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXlckOl;;lddc'                             .:loxd:. .:oddkXMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWK:.cc. 'clc'.              .. . ....         ';;,..,ok0KOl:xNMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNd,,lo;,,,'',,...,;::'.   ...                   .:;. .:c:oO0o,oKWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWKxloONWXxlcc;;cooc;'..,;'.....'''.    .....,::;::..', .;do.  .'...,ckNMMMMMMMMMMMMMMM
MMMMMMMMMMMMW0c,cONKd:''',;:,,,::;;';ll:::;.        .....','.';:,';c'.,.,;...,;'   'lOXWWMMMMMMMMMMM
MMMMMMMMMMMNx;c0WMMXdokXNNKo'..':::;,;::::cl;      'ol,.'::'..,'...:cclc:::,..''. .lxc::cdONMMMMMMMM
MMMMMMMMMMNo;xNMMMMMMWWMXd:..'.  .'. .,,'..,oo:;;;;:dxc,.;:;;,,'..',;'';lx0O:.    .;oxOOkxloONMMMMMM
MMMMMMMMWOl:xNXOoc::cdOd,..  .'. .','';::'':x0x;....:ol:;;,','.. .,;'. ..',,.   .'.   ,xKWN0xkNMMMMM
MMMMMMMMNkONW0;.     ''.... ...'. ..''';,''ckl        .dKOo:;;.. .,'. .  ..;dc.  :;..   .,cd0WMMMMMM
MMMMMMMMMWMMK:.'.  .;',,......;ll:'.....,lxxl.   ...   'odl;;:;'..,,.......',;::..,'c,      ;kNMMMMM
MMMMMMMMMMWk'.:o;..,'....';',llol'..   .dNM0'    lXd.   ;0Nd.. .,,'c::llc..;c,....;.''..   .lKWMMMMM
MMMMMMMMMMK:,kklc. .,c:''..'c,         .lKWx.    ;o:     ok.    ;;,kKkOko'  .':c..c.  .;. .,c0MMMMMM
MMMMMMMMMNl:KK:....''.  ..',.      ..    ;Oc             ;:     .. ,0Nx'.      ..;o.  .   .;l0MMMMMM
MMMMMMMMMNkONx. .'.    .looc  :c.        .c'             .,         cNX:    .'   'o, ckc'. .oXMMMMMM
MMMMMMMMMMMM0,   co.   .oo:'.oKc         .l'             'l.        :XMx.    ,'   oo;OMWN0lcxXMMMMMM
MMMMMMMMMMMM0'   .o,    ;k:.cNXc. ..   ..oKx,...      ..'dXk:'...,;cOWMO.    .,. .oc,OMMMMWWMMMMMMMM
MMMMMMMMMMMMO.....;o'   ,o' cNMXOc':x000XWMW0l,.....'o0KNWMXo,...:0WMMMk.    .;. ,l'.kMMMMMMMMMMMMMM
MMMMMMMMMMMMNkOXXOkKOc;;l;  ,KMMO' .dMMMMMM0;    ..'cOWMMMNl   .''dWMMWd.     ;l;xKkONMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWOlc;'.  .kMNc   oWMMMMNl     ;odxONMMMO.   ,c,;kWMX;      .dKXMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNd'..      ;Kk.   :KWMMMk.      ...cKMMNl    ..  '0Wd.       .kWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMM0'          co.    .:oKNc      ,loddkXMK,        'Ok.    ,o,  oWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNo.          ,,       ,o'            'kO.        ;l.     :Ko .xMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMK,           .,'     .'.             ,o.      ';,.      .kd.;KMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNo'.           .;c:'. .,.             'o,   .:l:.  .'.   .xxl0MMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNO00: ..         .,loxOKk;.          ,xN0olll;.    ..     oNWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNo.      .;. '. .,cx0XKOdlccccldONWXOd:,.            .dWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWo      oO',Ox.    ..;clloooooolc:c' .dk' .'    .'. ,KMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMx. ''  :kd0MNl        .co,      .dk'.xNd;o:    co.'OWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMK: ,0O' :XMMM0'        .kWx;::.   lNkoKMWNK;   cxclKWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMXx;'cKWd..kWMMMO,  ,,    .kMWNWX:  .kMMMMMMWx. .cKWNWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMXOOKWWO;:0WMMMMMO' :x;    cNMMMWO; .OMMMMMWk. ,OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMXKNMMMMMMMK; cXXOc  cNMMMMMk'lNMMMMMXlckXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWkdXMMM0;cKMMMMMMKkXMMMMMMWNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"""

log = """   The  use  of  antibiotics  for  the  prevention  of  infective
endocarditis has been a problem for the practitioner. This is due
to  the  wide  range of clinical  entities  requiring  antibiotic
coverage  along with the multitude of prophylaxis regimens  which
have  been recommended.  Advancements in medical treatment (i.e.,
organ  transplantation) have necessitated the development of  new
clinical  management protocols.  The medicolegal implications  of
prophylactic  antibiotic  use  (or misuse) makes  the  subject  a
confusing one indeed.

   This   article  will  outline  and  categorize   the   medical
conditions  requiring  antibiotic coverage,  and state  the  most
appropriate antibiotic regimen for each.

Infective endocarditis defined

   Infective  endocarditis  is  an infection on  the  endocardial
lining  of the heart.  The term Subacute  Bacterial  Endocarditis
(SBE)  implies that the infection is of bacterial  origin.  Since
endocardial  fungal,  viral,  and rickettsial infections are  not
unknown,  the  term  infective  endocarditis is a  more  complete
description  of  the disorder.  Such infections arise  after  the
implantation  and subsequent vegetative proliferation  of  blood-
borne microorganisms and platelet-fibrin deposits.

   Generally,  three  conditions  must be present  for  infective
endocarditis to develop (see figure 1).

-Firstly,  an  area  of damaged endocardium provides a  focus  at
which  the infection process may begin;  this could be a diseaesd
valve, a structural defect, or a prosthetic valve or implant.

-Secondly,  hemodynamic  turbulence  favours  the  deposition  of
sterile thrombi.

-Thirdly, a bacteremia is necessary to initiate the process.

   Since  transient  bacteremias have been found to  be  elicited
during  invasive dental procedures,  infective  endocarditis  can
occur.  The  most reasonable method of interrupting this triad of
events  leading  to  infective endocarditis  is  to  decrease  or
eliminate  the  effects  of  the bacteremia  by  administering  a
regimen of prophylactic antibiotic coverage.

   The chance of developing infective endocarditis subsequent  to
a  dental procedure is related to two factors:  the nature of the
dental  procedure  precipitating the bacteremia and the  type  of
heart lesion involved.

   Dental procedures that produce gingival or mucosal  hemorrhage
are most likely to cause bacteremia.  Thus,  a procedure which is
unlikely   to  produce  intraoral  hemorrhage  doea  not  require
antibiotic coverage. The risk of infective endocarditis increases
as the nature of the dental procedure becomes more invasive.  For
example,  an extraction will cause a greater bacteremia than will
a prophylaxis.

   Cardiac  conditions vary in their susceptibility to  infective
endocarditis.   These  conditions  may  be  divided  into   high,
intermediate,  and  very  low or negligible risk  categories  for
simplicity.

   High  risk conditions are those which requir special attention
to  endocarditis  prophyaxis  because of the  high  incidence  of
infective  endocarditis  in unprotected patients (see  table  1).
Included  in  this category are patients  with  prosthetic  heart
valves.  They  usually  require  parenteral  antibiotic  coverage
because  of  their extremely high risk.  All other conditions  in
this  category  require the standard  regimen,  unless  otherwise
directed by the patient's physician (see table 6).

   Intermediate risk conditions also require antibiotic  covergae
(see table 2). Here, the standard regimen is recommended.

   The   use  of  prophylactic  antibiotics  for  very  low  risk
conditions is controversial. On the one hand, this condition does
represent a risk,  albeit a small one.  On the other  hand,  some
investigators  have calculated that the risk of a severe  adverse
reaction to the antibiotic in the covered patient is much greater
than  the  risk of infectve andocarditis in the  patient  without
coverage.

   For this category of conditions, antibiotic coverage should be
optional; therefore, some element of clinical judgement should be
exercised (see table 3). For instance, a patient in this category
who  requires one or two simple Class II amalgams would  probably
not  need coverage,  even though some degree of gingival bleeding
would be expected during the procedure.  However,  a patient with
very poor oral hygiene who requires flap curettage perhaps should
be covered.
Diagnosing cardiac conditions

   A frequently asked question is "How can these patients at risk
be  identified?"  We cannot overstress the importance of  a  good
medical  history.  Specific questions should be asked  concerning
past  and  present  heart conditions,  such as  rheumatic  fever,
congenital heart defects,  heart murmurs, artifical heart valves,
or any serious illnesses or hospitilization.

   Also, it should be noted that the uneducated patient might not
appreciate  the significance of such information and may  provide
only a brief medical history.  If a medical problem is suspected,
the patient's physician should be contacted. In some instances it
may  be wise to suggest to the physician that the patient  should
consult  with  a  cardiologist.  The patient  may  not  like  the
inconvenience, but the genuine concern for his/her health will be
appreciated.

   Congenital  syndromes frequently exhibit cardiac lesions  (see
Table  4).  All  patients  with congenital  syndromes  should  be
investigated  for cardiac or other medical  conditions.  Patients
with  severe  or  multiple cardiac defects may  be  treated  more
safely in a hospital dental department."""

boot = """\n\n
Testing testing
[ty]\nThis should <b>be typed</e>\n[/ty]
[ce]\nBuddy Testing\n[/ce]
[ok]\nthis should be OK
this should too\n[/ok]

[ok]\nI'm gonna go ahead and call this okay as well\n[/ok]
[fa]\nAnd maybe this one fails\n[/fa]
[pa]\nBut this passes\n[/pa]
[:*]
back to normal for a spell
[ri]\nbut then right\n[/ri]
[ty]\nbut more typing\n[/ty]

[%]"""

#STYLE CLASSES
class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSE = '\033[7m'
    DISABLE = '\033[02m'
    HOLD = '\n\033[F\033[K'
    SCREENFG = BOLD + fg.BLACK
    SCREENBG = bg.WHITE
    SCREEN = SCREENFG + SCREENBG
    HEADERFG = fg.BLACK
    HEADERBG = bg.BLUE
    HEADER = HEADERFG + HEADERBG
    HIGHLIGHT = HEADER

class env:
    DEBUG = False
    BLESSED = True
    INTRO = True
    BOOTUP = True

term = Terminal()
delay = 0.005
organic = 30
if env.BLESSED:
    width = term.width
else:
    width = 80
xpad = 4
x, y = 0, 0

#HELPER FUNCTIONS
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
        msg = "B0GGY L3GGYv 0.2"
        half = term.width/2 - len(msg)/2
        adjust = 0
        if half%2 == 1:
            adjust = 1
        with term.location(0,ypos-1):
            print(style.HEADER + ' '*half + msg + ' '*half + ' '*adjust)

def headline(msg):
    if env.BLESSED:
        global y
        half = (term.width - len(msg) - xpad*2) / 2
        with term.location(xpad, y):
            print(style.HEADER + ' '*half + msg + ' '*half)
        line()

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

#OUTPUT STYLES
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

def readOut(inLines):
    height = 1
    global y
    i = 0
    cmd = ''
    lines = inLines.split('\n')
    print(term.move_down())
    #centerOut(style.HIGHLIGHT + 'LOG READER' + style.RESET + style.SCREEN)
    headline('LOG READER')
    line()
    line()
    horiz = len(max(lines, key=len))
    shift = term.width/2 - horiz/2 - xpad
    while i <= len(lines):
        with term.location(1,0):
            paintHeader(0)
            print(style.HEADER + 'LOG.txt: ' + str(i) + ' of ' + str(len(lines)))
        if cmd == 'q':
            paintBackground(term.height+1, style.SCREENBG)
            print(term.move(term.height-1, 1))
            break
        if cmd == 'up':
            print(term.move(1,3))
            print(term.clear())
            i -= 10
            cmd = ''
        height += 1
        #lineOut(lines[i])
        shiftOut(lines[i], shift)
        i += 1
        if height > term.height-20:
            with term.location(1,0):
                paintHeader(1)
                print(style.HEADER + 'LOG.txt: ' + str(i) + ' of ' + str(len(lines)))
            height -= 10
            with term.location(0,term.height-2):
                cmd = raw_input(style.SCREEN + ' give cmd: ' + style.SCREEN)
            #y -= 1
            paintBackground(term.height-2, style.SCREENBG)

def lineOut(inLine):
    write(inLine)
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
    testLine = inLine + ' ' + '-' * math + style.HIGHLIGHT + state + style.RESET
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

def main():
    global y
    y = 3

    if env.BLESSED:
        height, width = term.height, term.width
    else:
        height, width = 25, 80

    #FLAGS
    typing = False
    ok = False
    passf = False
    failf = False
    same = False
    word = False
    elip = False
    center = False
    right = False

    #SET STAGE
    sys.stdout.write("\x1b]2;BOHHHGLEHHGGGGGGGGG!!!!!???!!!?!?\x07")
    os.system('clear')
    pauseRL()

    if env.BLESSED:
        print(term.move(0,1))
        for ypos in range(1,term.height+1):
            paintBackground(ypos, style.SCREENBG)
        pauseRL()

    #INTRO
    if env.INTRO:
        if width - xpad*2 >= 100:
            bogs = bogboy.split('\n')
        else:
            bogs = smallboy.split('\n')
        for bog in bogs:
            centerOut(bog)
            pauseO()

    #process boot script
    if env.BOOTUP:
        formatted = format(boot)
        lines = formatted.split('\n')
        for line in lines:
            if line == '[ty]':
                typing = True
            elif line == '[/ty]':
                typing = False
            elif line == '[ok]':
                ok = True
            elif line == '[/ok]':
                ok = False
            elif line == '[sm]':
                same = True
            elif line == '[/sm]':
                same = False
            elif line == '[wo]':
                word = True
            elif line == '[/wo]':
                word = False
            elif line == '[el]':
                elip = True
            elif line == '[/el]':
                elip = False
            elif line == '[fa]':
                failf = True
            elif line == '[/fa]':
                failf = False
            elif line == '[pa]':
                passf = True
            elif line == '[/pa]':
                passf = False
            elif line == '[ri]':
                right = True
            elif line == '[/ri]':
                right = False
            elif line == '[ce]':
                center = True
            elif line == '[/ce]':
                center = False
            elif line == '[%]':
                loadOut()
            elif line[:2] == '[:':
                for i in range(len(line)-1):
                    pauseO()
            else:
                if typing:
                    typeOut(line)
                elif ok:
                    testOut(line, '[OK]')
                elif failf:
                    testOut(line, '[FAIL]')
                elif passf:
                    testOut(line, '[PASS]')
                elif center:
                    centerOut(line)
                elif right:
                    rightOut(line)
                elif same:
                    sameOut(line)
                elif word:
                    wordOut(line)
                elif elip:
                    dotOut(line)
                else:
                    lineOut(line)

    #CLI
    cmd = ''
    while cmd != 'exit':
        if env.BLESSED:
            paintHeader(0)
            paintBackground(term.height-2, style.SCREENBG)

            with term.location(xpad, term.height-2):
                cmd = raw_input(style.SCREEN + "$:> " + style.SCREEN)
        else:
            cmd = raw_input("$:> ")

        if cmd == 'log':
            if env.BLESSED:
                paintHeader(0)
                paintBackground(term.height-2, style.SCREENBG)
            readOut(log)

    #CLEAN UP
    print(style.RESET)
    os.system('clear')

if __name__ == '__main__':
    main()
