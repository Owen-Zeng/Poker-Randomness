Web VPython 3.2

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
    aBox = box(pos = vec(x,y,z), length = 0.1, height = 50, width = 0.1, color = color.white )
def drawSuit(x, y, suit,num):
    if(suit == "diamond"):
        drawDiamond(x,y)
    if(suit == "clubs"):
        drawClubs(x,y)
    if(suit == "clover"):
        drawClover(x,y)
    if(suit == "hearts"):
        drawHearts(x,y)
def drawDiamond(x,y):
    b = box(pos = vector(x,y,0.03), length = 0.15, height = 0.15, width = 0.001, color = color.red)
    b.rotate(angle = pi/4, axis = vector(0,0,1), origin = b.pos)
drawBackgroundCards(-3,0,0)
drawBackgroundCards(-2,0,0)
drawBackgroundCards(-1,0,0)
drawBackgroundCards(0,0,0)
drawBackgroundCards(1,0,0)
drawBackgroundCards(2,0,0)
drawBackgroundCards(3,0,0)
drawSuit(-3,0,"diamond")
drawSuit(-2,0,"diamond")
drawSuit(-1,0,"diamond")
drawSuit(-0,0,"diamond")
drawSuit(1,0,"diamond")
selfHand(-2.5,.5,0)
dealt(1,.5,0)
separate(-1.5,0,0)
