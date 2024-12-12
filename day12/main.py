filename = "input2.txt"

# Part I / II

def checkEdges(mapa, explored):
    mapa2 = [ [0 for _ in range(len(mapa[0])*2+3)] for _ in range(len(mapa)*2+3)]
    for y,x in explored:
        mapa2[(y+1)*2-1][(x+1)*2-1]+=1
        mapa2[(y+1)*2-1][(x+1)*2+1]+=1
        mapa2[(y+1)*2+1][(x+1)*2-1]+=1
        mapa2[(y+1)*2+1][(x+1)*2+1]+=1

    # hammered for the mobius fence case
    for y in range(3,len(mapa2)-2,2):
        for x in range(3,len(mapa2[0])-2,2):
            if mapa2[y][x]==2 and ( (mapa2[y-2][x-2]==0 and mapa2[y+2][x+2]==0) or (mapa2[y-2][x+2]==0 and mapa2[y+2][x-2]==0) ):
                mapa2[y][x] += 1
                mapa2[y-1][x] += 1

    acc = 0
    for line in mapa2:
        acc += line.count(1)
        acc += line.count(3)
    return acc

def explore(mapa, y, x, c):
    explored = []
    toExplore = [(y,x)]
    a = 0
    p = 0
    while len(toExplore) != 0:
        y,x = toExplore.pop()
        explored.append((y,x))
        a += 1
        p += 4
        if y>0  and  mapa[y-1][x]==c  :
            p -= 1
            if not (y-1, x) in toExplore and  not (y-1,x) in explored:
                toExplore.append((y-1, x))
        if x>0  and  mapa[y][x-1]==c :
            p -= 1
            if not (y, x-1) in toExplore and  not (y,x-1) in explored:
                toExplore.append((y, x-1))
        if y<len(mapa)-1  and  mapa[y+1][x]==c :
            p -= 1
            if not (y+1, x) in toExplore and  not (y+1,x) in explored:
                toExplore.append((y+1, x))
        if x<len(mapa[0])-1  and  mapa[y][x+1]==c :
            p -= 1
            if not (y, x+1) in toExplore and  not (y,x+1) in explored:
                toExplore.append((y, x+1))
    for y,x in explored:
        mapa[y][x] = "."

    e = checkEdges(mapa, explored)

    return a,p, e


f = open(filename)
tmp = [list(line.strip()) for line in f]

#
# I dont feel like thinking about cases like the one below
# Increasing the resolution of the map does the trick
#
# 1111
# 1811
# 1181
# 1111
#
mapa = []
for line in tmp:
    l = []
    for a in line:
        l.append(a)
        l.append(a)
    mapa.append(l)
    mapa.append(l)

acc1 = 0
acc2 = 0
for y in range(len(mapa)):
    for x in range(len(mapa[0])):
        if mapa[y][x] != ".":
            a,p, e = explore(mapa, y, x, mapa[y][x])
            acc1 += a*p//4
            acc2 += a*e //4
            
print("Part1: %s" % acc1)
print("Part2: %s" % acc2)
