Web VPython 3.2
from vpython import *
theCanvas = canvas(width = 1200, height = 400)
theCanvas.autoscale = False
theCanvas.camera.pos = vector(0,0,2)
def drawBackgroundCards(x,y,z):
    aBox = box(pos = vec(x,y,z), length = 0.5, height = .7, width = 0.01, color = color.white )
def selfHand(x,y,z):
    aText = text(pos = vector(x,y,z), text = 'Players Hand', align = 'center', height = 0.2, color = color.green)
def dealt(x,y,z):
    aText = text(pos = vector(x,y,z), text = 'Dealt Cards', align = 'center', height = 0.2, color = color.blue)
def separate(x,y,z):
    aBox = box(pos = vec(x,y,z), length = 0.1, height = 50, width = 0.01, color = color.white )
def drawSuit(x, y, suit,num):
    if(suit == "diamond"):
        drawDiamond(x,y,num)
    if(suit == "clubs"):
        drawClubs(x,y,num)
    if(suit == "spades"):
        drawSpades(x,y,num)
    if(suit == "hearts"):
        drawHearts(x,y,num)
def drawDiamond(x,y,num):
    hold = str(num)
    if(num == 1):
        hold = 'A'
    if(num == 11):
        hold = 'J'
    if(num == 12):
        hold = 'Q'
    if(num == 13):
        hold = 'K'
    text(pos = vec(x - 0.2, y + 0.2, 0.03), text = hold, color = color.red, height = 0.1)
    text(pos = vec(x + 0.15, y - 0.3, 0.03), text = hold, color = color.red, height = 0.1)
    b = box(pos = vector(x,y,0.03), length = 0.15, height = 0.15, width = 0.001, color = color.red)
    b.rotate(angle = pi/4, axis = vector(0,0,1), origin = b.pos)
def drawClubs(x,y,num):
    hold = str(num)
    if(num == 1):
        hold = 'A'
    if(num == 11):
        hold = 'J'
    if(num == 12):
        hold = 'Q'
    if(num == 13):
        hold = 'K'
    r = 0.04
    a = 0.03
    text(pos = vec(x - 0.2, y + 0.2, 0.03), text = hold, color = color.black, height = 0.1)
    text(pos = vec(x + 0.15, y - 0.3, 0.03), text = hold, color = color.black, height = 0.1)
    left = sphere(pos = vec(x - r*.75, y, a), radius = r, color = color.black)
    right = sphere(pos = vec(x + r*.75, y, a), radius = r, color = color.black)
    topCircle = sphere(pos = vec(x, y + r*1.1, a), radius = r, color = color.black)
    stem = pyramid(pos = vec(x,y-r*1.6,a), size = vec(r*1.2,r*1.8,r*1.2), axis = vec(0,1,0), color = color.black)
def drawSpades(x,y,num):
    hold = str(num)
    if(num == 1):
        hold = 'A'
    if(num == 11):
        hold = 'J'
    if(num == 12):
        hold = 'Q'
    if(num == 13):
        hold = 'K'
    r = 0.05
    a = 0.03
    text(pos = vec(x - 0.2, y + 0.2, 0.03), text = hold, color = color.black, height = 0.1)
    text(pos = vec(x + 0.15, y - 0.3, 0.03), text = hold, color = color.black, height = 0.1)
    topSphere = sphere(pos=vec(x,y+r*.7,a), radius = r, color = color.black)
    bl = sphere(pos = vec(x-r*0.8, y - 0.035*.2, a), radius = r, color = color.black)
    b2 = sphere(pos = vec(x+r*0.8, y- 0.035 * 0.2, a), radius = r, color = color.black)
    p1 = pyramid(pos = vec(x,y-r*2, a), size = vec(r*2.0, r*3.5, r*0.4), axis = vec(0,1,0), color = color.black)
    b11 = box(pos = vec(x,y + r*1.1,a), size = vec(r*0.35, r*1.4, r*0.3), color = color.black)
def drawHearts(x,y,num):
    hold = str(num)
    if(num == 1):
        hold = 'A'
    if(num == 11):
        hold = 'J'
    if(num == 12):
        hold = 'Q'
    if(num == 13):
        hold = 'K'
    r = 0.05
    a = 0.03
    text(pos = vec(x - 0.2, y + 0.2, 0.03), text = hold, color = color.red, height = 0.1)
    text(pos = vec(x + 0.15, y - 0.3, 0.03), text = hold, color = color.red, height = 0.1)
    tl = sphere(pos = vec(x-r*0.7, y+r*0.3, a), radius = r, color = color.red)
    tr = sphere(pos = vec(x+r*0.7, y+r*0.3, a), radius = r, color = color.red)
    p1 = pyramid(pos = vec(x,y-r*0.4, a), size = vec(r*2.3, r*3.2, r*0.3), axis = vec(0,-1,0), color = color.red)
drawBackgroundCards(-3,0,0)
drawBackgroundCards(-2,0,0)
drawBackgroundCards(-1,0,0)
drawBackgroundCards(0,0,0)
drawBackgroundCards(1,0,0)
drawBackgroundCards(2,0,0)
drawBackgroundCards(3,0,0)
#drawSuit(-3,0,"diamond")
#drawSuit(-2,0,"diamond")
#drawSuit(-1,0,"diamond")
#drawSuit(-0,0,"diamond")
#drawSuit(1,0,"diamond")
#drawSuit(1,0,"clubs")
drawSuit(-2,0,"diamond",4)
drawSuit(1,0,"spades",1)
drawSuit(0,0,"clubs",12)
drawSuit(2,0,"hearts",8)
selfHand(-2.5,.5,0)
dealt(1,.5,0)
separate(-1.5,0,0)
