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
drawBackgroundCards(-3,0,0)
drawBackgroundCards(-2,0,0)
drawBackgroundCards(-1,0,0)
drawBackgroundCards(0,0,0)
drawBackgroundCards(1,0,0)
drawBackgroundCards(2,0,0)
drawBackgroundCards(3,0,0)
selfHand(-2.5,.5,0)
dealt(1,.5,0)
separate(-1.5,0,0)
