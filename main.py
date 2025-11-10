
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
for key, value, in handValues:
    
    

iterations = [1,10,100,1000,10000,100000,1000000,10000000]
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

# USER INPUT===========================================
selectHand = menu(bind = handMenu,  choices = handList)
selectIterations = menu(bind = iterations, choices = iterationsList)
start = button(bind = startSim, text = "Start Simulation")



def handMenu(evt):
    return selectHand.value

def iterations(evt):
    return iterations.value

def startSim(evt):
    running = True

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

for i in range(1, N, 1):
    X[i] = logistic(r,X[i-1])    
    # d.plot(i, X[i])
    # c.plot(i, X[i])


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
    for i in range(0,6,1):
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
        else:
            return False

def isStraight(current):

def firstCommon(current):
    numCount = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0, 6, 1):
        numCount[i] += 1
    for i in range(0, 6, 1):




def secondCommon(current):

def categorize(current):
    #handList = {"High Card" : 0, "Pair" : 0, "Two Pair" : 0, "Three Of A Kind" : 0, "Straight" : 0, "Flush" : 0, "Full House" : 0, "Four-Of-A-Kind" : 0, "Straight Flush:" : 0}
    for i in range(0, current.len-1, 1):
        numDict = {'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king'}
        suitDict = {"diamonds", "clubs", "hearts", "spades"}
        output += numList[num//4]
        output += suitList[num%4]
    
    

    




    