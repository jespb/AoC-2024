
filename = "input2.txt"

# Part I

def getHeights(m):
    heights = []
    for i in range(len(m[0])):
        acc = 0 
        for h in range(1,len(m)-1):
            if m[h][i] == "#":
                acc += 1
        heights.append(acc)
    return heights

def isOverlap(k,l):
    ol = False
    for i in range(len(k)):
        if k[i]+l[i]>5:
            ol = True 
    return ol

f = [line.strip() for line in open(filename)]

locks = []
keys = []
for i in range(0, len(f), 8):
    if f[i][0] == "#":
        locks.append(getHeights(f[i:i+7]))
    else:
        keys.append(getHeights(f[i:i+7]))

acc = 0
for k in keys:
    for l in locks:
        if not isOverlap(k,l):
            acc +=1
print(acc)