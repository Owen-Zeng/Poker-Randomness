handList = ["High Card", "Pair", "Two Pair", "Three Of A Kind", "Straight", "Flush", "Full House", "Straight Flush"]

# USER INPUT===========================================
selectHand = menu(bind = handMenu,  choices = handList)
selectIterations = (bind = iterations, )



def handMenu(evt):
    return selectHand.value


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

print(rand(X[deckSize]))

    