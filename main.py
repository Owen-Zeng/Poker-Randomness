# Web VPython 3.2

handValues = {"High Card" :0, 
              "Pair" : 0, 
              "Two Pair" : 0, 
              "Three Of A Kind" : 0, 
              "Straight" : 0, 
              "Flush" : 0, 
              "Full House" : 0, 
              "Four-Of-A-Kind" : 0, 
              "Straight Flush:" : 0}
              
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


wt = wtext("Select Hand: ")
wt.text = "Select Hand: "
selectHand = menu(bind = handMenu,  wtext = "Select a Hand", choices = hands)

wt = wtext(text = "\nSelect Iterations: ")

selectIterations = slider(bind= iterationsSlider, min = 0, max =6, step = 1)
Iwt = wtext(text = "1")


wt = wtext(text = "\nEdge Exclusion: ")
edge = slider(bind = edgeSlider, min = 0, max = 45, step = 5)
Ewt = wtext(text = edge.value)

wt = wtext(text = "\nStart Simulation")
start = button(bind = startSim, text = "Start Simulation")


def handMenu(evt):
    return selectHand.value

def iterationsSlider(evt):
    Iwt.text = selectIteraions.value
    print("buhbuhbuhubh")
    return selectIterations.value

def edgeSlider(evt):
    return edge.value

def startSim(evt):
    running = True
    
while True:
    rate(10)
    iterations = int( pow(10, selectIterations.value))
    Iwt.text = "" + iterations
    
    edgeExclusion = int(edge.value)
    Ewt.text = edgeExclusion + "%"


r = 4
X0 = 0.1
N = 1000

X = []
X[0] = X0


def logistic(r, currX):
    return r * currX * (1 - currX)

# Graph = graph(title = "Pop Fraction vs Iterate Number", xtitle = "Iterate Number", ytitle = "Pop Fraction", ymin = 0, ymax = 1)
# d = gdots(graph = Graph)
# #c = gcurve(graph = Graph)

# d.plot(0, X[0])
#c.plot(0, X[0])


#come back to this later this m value might be another slider
m = 1000
for i in range(1, m, 1):
    X[i] = logistic(r,X[i-1])    



deckSize = 52
def rand(iterate):
    for i in range(0, deckSize, 1):
        if (i * 1/deckSize > iterate):
            deckSize-=1
            return i
    return -1

print(rand(X[deckSize-1]))

current = []
for i in range(0, 1, 7):
    current[i] = rand(X[deckSize-1-i])

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
        print(arrSuits[j])
        if len(arrSuits[j]) >= 5:
            if isStraight(arrSuits[j]): 
                return True
    return False
    
def isStraight(current):
    for j in range(len(current)):
        current[j] = current[j]//4 + 1
    hold = sorted(set(current))
    count = 1
    for i in range(1, len(hold)):
        if hold[i] == hold[i-1] + 1:
            count += 1
            if count == 5:
                return True
        else:
            count = 1
    return False

def firstCommon(currentt):
    current = currentt.copy()
    for i in range(len(current)):
        current[i] = current[i]//4 + 1
    current.sort()
    maxCount = 0
    count = 1
    num = 0
    for i in range(1,len(current)):
        if(current[i] == current[i-1]):
            count+= 1
        else:
            if(count>maxCount):
                maxCount = count
                num = current[i-1]
            count = 1
    if(count > maxCount):
        num = current[-1]
    return num
    
def secondCommon(currentt):
    num2 = firstCommon(currentt)
    current = currentt.copy()
    for i in range(len(current)):
        current[i] = current[i] // 4 + 1
    current.sort()
    maxCount = 0
    count = 1
    num = 0
    for i in range(1, len(current)):
        if(current[i] == current[i-1] and current[i] != num2):
            count+= 1
        else:
            if(count>maxCount):
                maxCount = count
                num = current[i-1]
            count = 1
    if(count > maxCount):
        num = current[-1]
    return num

def categorize(current):
    #Key {"High Card" = 0, "Pair" = 1, "Two Pair" = 2, "Three Of A Kind" = 3, "Straight" = 4, "Flush" = 5, "Full House" = 6, "Four-Of-A-Kind" = 7, "Straight Flush:" = 8}

    if (isStraightFlush(current)):
        handValues["Straight Flush"] = handValues["Straight Flush"]+1
        return 8
    if (firstCommon(current) == 4):
        handValues["Four-Of-A-Kind"] = handValues["Four-Of-A-Kind"]+1
        return 7
    if (firstCommon(current) == 3 and secondCommon(current) >= 2):
        handValues["Full House"] = handValues["Full House"]+1
        return 6
    if (isFlush(current)):
        handValues["Flush"] = handValues["Flush"]+1
        return 5
    if (isStraight(current)):
        handValues["Straight"] = handValues["Straight"]+1
        return 4
    if (firstCommon(current) == 3):
        handValues["Three of A Kind"] = handValues["Three of A Kind"]+1
        return 3
    if (firstCommon(current) == 2 and secondCommon(current)):
        handValues["Two Pair"] = handValues["Two Pair"]+1
        return 2
    if (firstCommon(current) == 2):
        handValues["Pair"] = handValues["Pair"]+1
        return 1
    else:
        handValues["High Card"] = handValues["High Card"]+1
        return 0



