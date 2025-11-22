Web VPython 3.2

handValues = {"High Card" :0, 
              "Pair" : 0, 
              "Two Pair" : 0, 
              "Three Of A Kind" : 0, 
              "Straight" : 0, 
              "Flush" : 0, 
              "Full House" : 0, 
              "Four-Of-A-Kind" : 0, 
              "Straight Flush" : 0}
              
hands = []
for key in handValues:
    hands.append(key)

probabilities = {"High Card" : 0.174,
                "Pair" : 0.438, 
                "Two Pair" : 0.235, 
                "Three Of A Kind" : 0.048, 
                "Straight" : 0.046, 
                "Flush" : 0.030, 
                "Full House" : 0.026, 
                "Four-Of-A-Kind" : .0017, 
                "Straight Flush:" : 0.00031}

def convert(num):
    numList = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
    suitList = ["diamonds", "clubs", "hearts", "spades"]
    output = ""
    output += numList[num//4]
    output += " of "
    output += suitList[num%4]
    print(output)

# USER INPUT===========================================================
iterations = 0
edgeExclusion = 0
animation = False
running = False

buttonText = wtext(text = "\n Toggle Animation: ")
animationStatus = wtext(text = "Off ")
animationToggle = button(bind = toggleAnimation, text = "Toggle")


wt = wtext(text = "\nSelect Iterations: ")
selectIterations = slider(bind= iterationsSlider, min = 0, max =6, step = 1, disabled = True)
Iwt = wtext(text = "1")


wt = wtext(text = "\nEdge Exclusion: ")
edge = slider(bind = edgeSlider, min = 0, max = 45, step = 5)
Ewt = wtext(text = edge.value + "%")

swt = wtext(text = "\nStarting Seed Value: ")
seedSlider = slider(bind=seedSliderFunc, min=0.05, max=0.95, step=0.01, value=0.1)
seedWt = wtext(text="0.1")

Swt = wtext(text = "\nStart Simulation   ")
start = button(bind = toggleSim, text = "Start")

output = wtext(text = "")

hist_canvas = canvas(title='Hand Histogram', width=600, height=400, align='left', background=color.black)
hist_canvas.camera.pos = vector(5, 0, 15)
hist_bars = {}
hist_labels = {}
hist_count_labels = {}
hist_scale = 20.0 

pearsonGraph = graph(title="Pearson Coefficient vs Edge Exclusion", 
      xtitle="Edge Exclusion (%)", 
      ytitle="Pearson Coefficient",
      xmin=0, xmax=50, ymin=0, ymax=1.1, align='right')

pearsonBars = gvbars(color=color.blue, delta=4)

edgePearsonData = {}

def updatePearson(edgeVal, pearsonVal):
    global edgePearsonData
    edgePearsonData[edgeVal] = pearsonVal
    pearsonBars.delete()

    for edge in sorted(edgePearsonData.keys()):
        pearsonBars.plot(edge, edgePearsonData[edge])

def init_histogram():
    y_pos = 4
    keys = list(handValues.keys())
    for key in keys:
        hist_labels[key] = text(canvas=hist_canvas, pos=vector(-0.5, y_pos-0.1, 0), text=key, height=0.4, align='right', color=color.white)
        hist_bars[key] = box(canvas=hist_canvas, pos=vector(0, y_pos, 0), length=0, height=0.8, width=0.1, color=color.cyan)
        y_pos -= 1

def update_histogram(total_games):
    hist_canvas.select()
    if total_games == 0: return
    y_pos = 4
    keys = list(handValues.keys())
    
    for key in keys:
        count = handValues[key]
        fraction = count / total_games
        bar_len = fraction * hist_scale
        
        start_x = 0
        hist_bars[key].length = bar_len
        hist_bars[key].pos.x = start_x + bar_len / 2
        
        if key not in hist_count_labels:
            hist_count_labels[key] = label(canvas=hist_canvas, pos=vector(bar_len + 0.3, y_pos-0.1, 0), text=str(count), xoffset=20, box=False, opacity=0, height=16, color=color.yellow)
        else:
            hist_count_labels[key].pos = vector(bar_len + 0.3, y_pos-0.1, 0)
            hist_count_labels[key].text = str(count)
        
        y_pos -= 1

def reset_histogram():
    hist_canvas = canvas(title='Hand Histogram', width=600, height=400, align='left', background=color.black)
    hist_canvas.camera.pos = vector(5, 0, 15)
    hist_bars = {}
    hist_labels = {}
    hist_count_labels = {}
    hist_scale = 20.0 

init_histogram()
cardCanvas = scene
cardCanvas.width = 1200
cardCanvas.height = 400
cardCanvas.autoscale = False
cardCanvas.camera.pos = vector(0,0,2)
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

def handMenu(evt):
    return selectHand.value

def iterationsSlider(evt):
    Iwt.text = selectIteraions.value
    return selectIterations.value

def edgeSlider(evt):
    return edge.value

def seedSliderFunc(evt):
    seedWt.text = str(round(seedSlider.value, 2))

def toggleAnimation(evt):
    global animationStatus
    global animation

    animation = not animation

    if(animation):
        animationStatus.text = "On "
    else:
        animationStatus.text = "Off "

def calculate_pearson(observed_counts, total_games):
    probs = [
        0.174,   # High Card
        0.438,   # Pair
        0.235,   # Two Pair
        0.048,   # Three of a Kind
        0.046,   # Straight
        0.030,   # Flush
        0.026,   # Full House
        0.0017,  # Four of a Kind
        0.00031  # Straight Flush
    ]
    
    hand_names = [
        "High Card", "Pair", "Two Pair", "Three Of A Kind", 
        "Straight", "Flush", "Full House", "Four-Of-A-Kind", "Straight Flush"
    ]
    
    observed = []
    expected = []
    
    for i in range(len(hand_names)):
        name = hand_names[i]
        obs = observed_counts.get(name, 0)
        exp = probs[i] * total_games
        
        observed.append(obs)
        expected.append(exp)
        
    n = len(observed)
    sum_x = sum(observed)
    sum_y = sum(expected)
    sum_xy = 0
    sum_x2 = 0
    sum_y2 = 0
    for i in range(n):
        sum_xy += observed[i] * expected[i]
        sum_x2 += observed[i] * observed[i]
        sum_y2 += expected[i] * expected[i]
    
    numerator = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2)) ** 0.5
    
    if denominator == 0:
        return 0
    return numerator / denominator

def toggleSim(evt):
    global running
    global animation
    if not running:
        running = True
        start.text = "Running..."
        start.disabled = True
        edge.disabled = True
        selectIterations.disabled = True



        for key in handValues:
            handValues[key] = 0

        # reset_histogram()
                
        num_iterations = int(pow(10, selectIterations.value))
        current_x = seedSlider.value
        
        for i in range(num_iterations):
            if(animation):
                rate(10)
            else:
                rate(10000)


            if(animation):
                for obj in scene.objects:
                    obj.visible = False
                    del obj
            if not (i == num_iterations-1):
                current_x = playOneGame(current_x)
            else:
                animation = True
                for obj in scene.objects:
                    obj.visible = False
                    del obj
                current_x = playOneGame(current_x)
                animation = False
                animationStatus.text = "Off"
                

                

                    
            pearson = calculate_pearson(handValues, num_iterations)
            updatePearson(edge.value, pearson)

            update_histogram(num_iterations)

            result_text = "\nSimulation Complete!\n"
            result_text += "Iterations: " + str(num_iterations) + "\n"
            result_text += "Edge Exclusion: " + str(edge.value) + "%\n\n"
            result_text += "Pearson Correlation: " + str(pearson) + "\n\n"
                
            output.text = result_text
            
            running = False
            start.text = "Start"
            start.disabled = False
            edge.disabled = False
            selectIterations.disabled = False
    else:
        running = False
        start.text = "Start"

while True:
    if(animation):
        rate(1)
    else:
        rate(10000)
    iterations = int( pow(10, selectIterations.value))
    Iwt.text = "" + iterations

    edgeExclusion = int(edge.value)
    Ewt.text = edgeExclusion + "%"



# come back to this later this m value might be another slider


def isFlush(current):
    hold = {"d":0, "c":0, "h":0, "s":0}
    for i in range(len(current)):
        if(current[i] % 4 == 0):
          hold["d"] += 1
        elif(current[i] % 4 == 1):
          hold["c"] += 1
        elif(current[i] % 4 == 2):
          hold["h"] += 1
        elif(current[i] % 4 == 3):
          hold["s"] += 1
    for val in hold.values():
        if (val == 5):
            return True
    return False
    
    
def isStraightFlush(current):
    arrSuits = {0:[], 1:[], 2:[], 3:[]}
    for i in current:
        suit = i % 4
        arrSuits[suit].append(i)
    for j in arrSuits:
        if len(arrSuits[j]) >= 5:
            if isStraight(arrSuits[j]): 
                return True
    return False
    
def isStraight(current):
    ranks = []
    for c in current:
        ranks.append(c // 4 + 1)
    hold = sorted(set(ranks))
    count = 1
    for i in range(1, len(hold)):
        if hold[i] == hold[i-1] + 1:
            count += 1
            if count == 5:
                return True
        else:
            count = 1
    return False

def get_counts(currentt):
    ranks = [c // 4 + 1 for c in currentt]
    counts = {}
    for r in ranks:
        counts[r] = counts.get(r, 0) + 1
    return counts

def firstCommon(currentt):
    counts = get_counts(currentt)
    if not counts: return 0
    return max(counts.values())
    
def secondCommon(currentt):
    counts = get_counts(currentt)
    values = sorted(counts.values(), reverse=True)
    if len(values) >= 2:
        return values[1]
    return 0

def categorize(current):
    #Key {"High Card" = 0, "Pair" = 1, "Two Pair" = 2, "Three Of A Kind" = 3, "Straight" = 4, "Flush" = 5, "Full House" = 6, "Four-Of-A-Kind" = 7, "Straight Flush:" = 8}

    if (isStraightFlush(current)):
        handValues["Straight Flush"] = handValues["Straight Flush"]+1
        if(animation):
            aText = text(pos = vector(1,-1,0), text = 'Straight  Flush', align = 'center', height = 0.2, color = color.white)
        return 8
    if (firstCommon(current) == 4):
        handValues["Four-Of-A-Kind"] = handValues["Four-Of-A-Kind"]+1
        if(animation):
            aText = text(pos = vector(1,-1,0), text = 'Four-Of-A-Kind', align = 'center', height = 0.2, color = color.white)
        return 7
    if (firstCommon(current) == 3 and secondCommon(current) >= 2):
        handValues["Full House"] = handValues["Full House"]+1
        if(animation):
            aText = text(pos = vector(1,-1,0), text = 'Full House', align = 'center', height = 0.2, color = color.white)
        return 6
    if (isFlush(current)):
        handValues["Flush"] = handValues["Flush"]+1
        if(animation):
            aText = text(pos = vector(1,-1,0), text = 'Flush', align = 'center', height = 0.2, color = color.white)
        return 5
    if (isStraight(current)):
        handValues["Straight"] = handValues["Straight"]+1
        if(animation):
            aText = text(pos = vector(1,-1,0), text = 'Straight', align = 'center', height = 0.2, color = color.white)
        return 4
    if (firstCommon(current) == 3):
        handValues["Three Of A Kind"] = handValues["Three Of A Kind"]+1
        if(animation):
            aText = text(pos = vector(1,-1,0), text = 'Three Of A Kind', align = 'center', height = 0.2, color = color.white)
        return 3
    if (firstCommon(current) == 2 and secondCommon(current) == 2):
        if(animation):
            aText = text(pos = vector(1,-1,0), text = 'Two Pair', align = 'center', height = 0.2, color = color.white)
        handValues["Two Pair"] = handValues["Two Pair"]+1
        return 2
    if (firstCommon(current) == 2):
        handValues["Pair"] = handValues["Pair"]+1
        if(animation):
            aText = text(pos = vector(1,-1,0), text = 'Pair', align = 'center', height = 0.2, color = color.white)
        return 1
    else:
        handValues["High Card"] = handValues["High Card"]+1
        if(animation):
            aText = text(pos = vector(1,-1,0), text = 'High Card', align = 'center', height = 0.2, color = color.white)
        return 0

def logistic(r, currX):
    return r * currX * (1 - currX)

def get_next_valid_x(r, current_x, edgeExclusion):
    # edgeExclusion is 0 to 45
    edge_frac = edgeExclusion / 100.0

    while True:
        current_x = logistic(r, current_x)
        if current_x >= edge_frac and current_x <= (1.0 - edge_frac):
            return current_x

def deal_hand(r, current_x, edgeExclusion):
    deck = []
    for i in range(52):
        deck.append(i)
    hand = []

    card_x  = 3
    for i in range(7):
        current_x = get_next_valid_x(r, current_x, edgeExclusion)

        edge_frac = edgeExclusion / 100.0
        x = (current_x - edge_frac) / (1.0 - 2 * edge_frac)
        
        index = int(x * len(deck))
        if index >= len(deck):
            index = len(deck) - 1
        
        card = deck.pop(index)
        hand.append(card)
        if(animation):
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
            suit =   0  
            if(card % 4 == 0):
                suit = "diamond"
            if(card % 4 == 1):
                suit = "clubs"
            if(card % 4 == 2):
                suit = "hearts"
            if(card % 4 == 3):
                suit = "spades"
                
            rank = 1 + card//4
            drawSuit(card_x, 0, suit, rank)
            card_x -= 1



    return hand, current_x

def playOneGame(current_x_seed):
    r = 4.0
    current_x = current_x_seed
    edge_val = edge.value
    hand, next_x = deal_hand(r, current_x, edge_val)
    categorize(hand)
    return next_x


# GRAPHICS AND STUFF


def drawBackgroundCards(x,y,z):
    cardCanvas.select()
    aBox = box(pos = vec(x,y,z), length = 0.5, height = .7, width = 0.01, color = color.white )
def selfHand(x,y,z):
    cardCanvas.select()
    aText = text(pos = vector(x,y,z), text = 'Players Hand', align = 'center', height = 0.2, color = color.green)
def dealt(x,y,z):
    cardCanvas.select()
    aText = text(pos = vector(x,y,z), text = 'Dealt Cards', align = 'center', height = 0.2, color = color.blue)
def separate(x,y,z):
    cardCanvas.select()
    aBox = box(pos = vec(x,y,z), length = 0.1, height = 50, width = 0.01, color = color.white )
def drawSuit(x, y, suit,num):
    cardCanvas.select()
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
    text(pos = vec(x - 0.2, y + 0.2, 0.02), text = hold, color = color.red, height = 0.1)
    text(pos = vec(x + 0.12, y - 0.3, 0.02), text = hold, color = color.red, height = 0.1)
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
    text(pos = vec(x - 0.2, y + 0.2, 0.02), text = hold, color = color.black, height = 0.1)
    text(pos = vec(x + 0.12, y - 0.3, 0.02), text = hold, color = color.black, height = 0.1)
    left = sphere(pos = vec(x - r*.9, y, a), radius = r, color = color.black)
    right = sphere(pos = vec(x + r*.9, y, a), radius = r, color = color.black)
    topCircle = sphere(pos = vec(x, y + r*1.25, a), radius = r, color = color.black)
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
    text(pos = vec(x - 0.2, y + 0.2, 0.02), text = hold, color = color.black, height = 0.1)
    text(pos = vec(x + 0.12, y - 0.3, 0.02), text = hold, color = color.black, height = 0.1)
    # topSphere = sphere(pos=vec(x,y+r*.7,a), radius = r, color = color.black)
    bl = sphere(pos = vec(x-r*0.8, y - 0.035*.2, a), radius = r, color = color.black)
    b2 = sphere(pos = vec(x+r*0.8, y- 0.035 * 0.2, a), radius = r, color = color.black)
    p1 = pyramid(pos = vec(x,y-r*2, a), size = vec(r*2.0, r*3.5, r*0.4), axis = vec(0,1,0), color = color.black)
    b11 = box(pos = vec(x,y + r*1.1,a), size = vec(r*0.35, r*1.4, r*0.3), color = color.black)
    p1 = pyramid(pos = vec(x,y+r*.5, a), size = vec(r*2.0, r*3.5, r*0.4), axis = vec(0,1,0), color = color.black)
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
    text(pos = vec(x - 0.2, y + 0.2, 0.02), text = hold, color = color.red, height = 0.1)
    text(pos = vec(x + 0.12, y - 0.3, 0.02), text = hold, color = color.red, height = 0.1)
    tl = cylinder(pos = vec(x-r*0.85, y+r*0.3, a), radius = r, color = color.red, axis =vec(0,0,.01))
    tr = cylinder(pos = vec(x+r*0.85, y+r*0.3, a), radius = r, color = color.red, axis = vec(0,0,.01))
    p1 = pyramid(pos = vec(x,y-r*0.4, a), size = vec(r*2.3, r*3.2, r*0.3), axis = vec(0,-1,0), color = color.red)