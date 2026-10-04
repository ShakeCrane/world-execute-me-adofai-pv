"""Original code-drawn shapes. No game sprites, fonts or screenshots."""
from pathlib import Path
import math
import sys
from PIL import Image, ImageDraw

# Reuse the upstream cached font loader, not its palette or mutable frame state.
TUI = Path(__file__).resolve().parents[1] / "tui_pv_world_execute_20260926"
if str(TUI) not in sys.path:
    sys.path.insert(0, str(TUI))
from tuikit import font

BG = (7, 10, 20)
WHITE = (231, 233, 242)
GREY = (107, 119, 140)
RED = (240, 68, 98)
GREEN = (117, 165, 139)
ICE = (199, 228, 236)
MONO = "C:/Windows/Fonts/consola.ttf"
FONT_FILE = Path(MONO)


def colour(c, alpha=1):
    return tuple(round(v * max(0, min(1, alpha))) for v in c)


def text(d, xy, s, size=26, fill=WHITE, anchor=None):
    d.text(xy, s, font=font(MONO, size), fill=fill, anchor=anchor)


def heart(d, xy, scale=2, fill=RED):
    x, y = xy
    points = [(-6,-3),(-6,-6),(-3,-8),(0,-5),(3,-8),(6,-6),(6,-3),(0,4)]
    d.polygon([(round(x+a*scale), round(y+b*scale)) for a,b in points], fill=fill)


def hand(d, xy, reach=0, scale=1, fill=ICE):
    """Open palm reaching toward input; no copied sprite anatomy."""
    x, y = xy
    pts = [(-34,16),(-12,10),(-3,0),(7,-9),(14,-12),(16,-8),(8,1),
           (30,-1),(35,3),(33,8),(20,12),(32,13),(33,18),(19,20),
           (26,23),(24,28),(8,29),(-10,25),(-34,30)]
    d.polygon([(round(x+(a+reach)*scale), round(y+b*scale)) for a,b in pts], fill=fill)


def kris(d, xy, scale=1, alpha=1, reach=0):
    """Hair obscures face; striped clothes mark an original silhouette study."""
    x, floor = xy
    def pts(seq):
        return [(round(x+a*scale), round(floor+b*scale)) for a,b in seq]
    d.polygon(pts([(-32,-87),(30,-87),(38,-27),(20,-20),(-24,-20),(-38,-27)]), fill=colour(GREEN, alpha))
    d.polygon(pts([(-35,-65),(34,-65),(35,-54),(-36,-54)]), fill=colour((206,187,131), alpha))
    d.polygon(pts([(-23,-22),(-3,-22),(-7,0),(-33,0)]), fill=colour((39,45,63), alpha))
    d.polygon(pts([(4,-22),(24,-22),(31,0),(8,0)]), fill=colour((39,45,63), alpha))
    d.polygon(pts([(-24,-111),(22,-111),(22,-85),(-23,-85)]), fill=colour((174,166,145), alpha))
    d.polygon(pts([(-33,-111),(-21,-136),(12,-139),(34,-122),(28,-93),(15,-106),(1,-100),(-9,-109),(-29,-94)]), fill=colour((32,34,48), alpha))
    d.line(pts([(-31,-79),(-48,-58),(-63,-57)]), fill=colour(GREEN, alpha), width=max(1, round(12*scale)))
    hand(d, (x-61*scale, floor-65*scale), reach, scale*.65, colour(ICE, alpha))
    d.line(pts([(30,-80),(44,-53),(56,-57)]), fill=colour(GREEN, alpha), width=max(1, round(11*scale)))


def noelle(d, xy, scale=1, alpha=.45):
    """Secondary distant mirror; never a villain face or final solo subject."""
    x, floor = xy
    def pts(seq):
        return [(round(x+a*scale), round(floor+b*scale)) for a,b in seq]
    d.polygon(pts([(-23,-72),(20,-72),(28,-16),(-26,-16)]), fill=colour((171,154,128), alpha))
    d.polygon(pts([(-15,-19),(-1,-19),(-4,0),(-18,0)]), fill=colour(GREY, alpha))
    d.polygon(pts([(3,-19),(16,-19),(20,0),(5,0)]), fill=colour(GREY, alpha))
    d.polygon(pts([(-20,-82),(-16,-111),(15,-111),(23,-80),(11,-91),(0,-87),(-12,-94)]), fill=colour((200,186,147), alpha))
    d.line(pts([(-13,-106),(-25,-125),(-27,-140)]), fill=colour((200,186,147), alpha), width=3)
    d.line(pts([(12,-106),(22,-126),(28,-137)]), fill=colour((200,186,147), alpha), width=3)
    d.line(pts([(-19,-65),(-52,-58),(-64,-57)]), fill=colour(ICE, alpha), width=5)


def world(image, n, movement=0, alpha=1, hand_reach=0):
    d = ImageDraw.Draw(image)
    # Water lives within the world pane; the main carrier is drawn afterwards.
    d.rectangle((405,155,1223,587), fill=colour((11,19,32), alpha))
    d.polygon([(406,414),(564,411),(626,429),(781,446),(945,445),(1224,411),(1224,589),(406,589)], fill=colour((18,33,47), alpha))
    for i in range(7):
        y = 465+i*16
        for j in range(5):
            x = 438+j*152 + 8*math.sin(n/100+i+j)
            d.line((x,y,x+60,y), fill=colour((36,55,70), alpha), width=1)
    d.line((426,172,426,558), fill=colour((38,48,62), alpha))
    d.arc((773,190,1134,470), 192, 333, fill=colour((43,59,76), alpha), width=2)
    noelle(d, (974+movement,475), scale=1.05, alpha=.5*alpha)
    kris(d, (724+movement,480), scale=1.65, alpha=alpha, reach=hand_reach)


def base(n, movement=0, hand_reach=0):
    image = Image.new("RGB", (1280,720), BG)
    world(image, n, movement, hand_reach=hand_reach)
    d = ImageDraw.Draw(image)
    d.line((24,114,24,604,1256,604,1256,56,368,56), fill=WHITE, width=2)
    d.line((24,56,24,89), fill=WHITE, width=2)
    text(d, (48,53), "world.execute(me);", 25, anchor="lt")
    d.line((385,114,385,588), fill=(52,59,78), width=1)
    text(d, (49,136), "KRIS", 20, GREY)
    # Close-up hand persists in the subject pane while the body is in the world.
    d.line((67,286,179,286,225,306), fill=GREEN, width=23)
    hand(d, (245,286), scale=1.6)
    d.line((50,344,349,344), fill=(37,43,59))
    return image
