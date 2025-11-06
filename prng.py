Web VPython 3.2

r = 4
X0 = 0.1
N = 1000

X = []
X[0] = X0

def logistic(r, currX):
    return r * currX * (1 - currX)

Graph = graph(title = "Pop Fraction vs Iterate Number", xtitle = "Iterate Number", ytitle = "Pop Fraction", ymin = 0, ymax = 1)
d = gdots(graph = Graph)
#c = gcurve(graph = Graph)

d.plot(0, X[0])
#c.plot(0, X[0])

for i in range(1, N, 1):
    X[i] = logistic(r,X[i-1])    
    d.plot(i, X[i])
    #c.plot(i, X[i])

def rand(iterate):
    for i in range(0, 52, 1):
        if (i * 1/52 > iterate):
            return i
    return -1

print(rand(X[999]))


