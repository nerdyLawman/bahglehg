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

class common:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSE = '\033[7m'
    DISABLE = '\033[02m'
    HOLD = '\n\033[F\033[K'

class default:
    SCREENFG = common.BOLD + fg.BLUE
    SCREENBG = bg.WHITE
    SCREEN = SCREENFG + SCREENBG
    HEADERFG = fg.WHITE
    HEADERBG = bg.BLUE
    HEADER = HEADERFG + HEADERBG
    HIGHLIGHT = HEADER

class red:
    SCREENFG = common.BOLD + fg.RED
    SCREENBG = bg.YELLOW
    SCREEN = SCREENFG + SCREENBG
    HEADERFG = fg.YELLOW
    HEADERBG = bg.RED
    HEADER = HEADERFG + HEADERBG
    HIGHLIGHT = HEADER

class cyan:
    SCREENFG = common.BOLD + fg.MAGENTA
    SCREENBG = bg.CYAN
    SCREEN = SCREENFG + SCREENBG
    HEADERFG = fg.CYAN
    HEADERBG = bg.MAGENTA
    HEADER = HEADERFG + HEADERBG
    HIGHLIGHT = HEADER

class black:
    SCREENFG = common.BOLD + fg.WHITE
    SCREENBG = bg.BLACK
    SCREEN = SCREENFG + SCREENBG
    HEADERFG = fg.BLACK
    HEADERBG = bg.WHITE
    HEADER = HEADERFG + HEADERBG
    HIGHLIGHT = HEADER
