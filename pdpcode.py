L = [2, 2, 3, 3, 4, 5, 6, 7, 8, 10]

width = 0

def partialDigest(L):
    global width
    width = max(L)
    if width in L:
        L.remove(width)
    X = [0, width]
    place(L, X)


def place(L, X):
    if len(L) == 0:
        X.sort()
        print(X)
        return

    y = max(L)
    newL=L.copy()
    L.remove(y)
    firstArr = findD(y, X)
    if all(i in newL for i in firstArr):
        addXandRemoveL(y, X, firstArr, L)
        place(L, X)
        removeXandAddL(y, X, firstArr, L)

    secondArr = findD(abs(width - y), X)
    if all(i in newL for i in secondArr):
        addXandRemoveL(abs(width - y), X, secondArr, L)
        place(L, X)
        removeXandAddL(abs(width - y), X, secondArr, L)


def addXandRemoveL(y, X, d, L):
    X.append(y)
    for v in d:
        if v in L:
            L.remove(v)

def removeXandAddL(y, X, d, L):
    if y in X:
        X.remove(y)
    for a in d:
        L.append(a)


def findD(y, X):
    arr = []

    for v in X:
        arr.append(abs(v - y))

    return arr







partialDigest(L)
