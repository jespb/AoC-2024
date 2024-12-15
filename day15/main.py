filename = "input2.txt"

# Part I 

f = open(filename)
mapa = []
line = f.readline().strip()
while line != "":
    mapa.append(list(line))
    line = f.readline().strip()

p = None
for y in range(len(mapa)):
    if "@" in mapa[y]:
        p = y, mapa[y].index("@")


def canPushDir(mapa, p, dir):
    y,x = p 
    if mapa[y][x] == "#":
        return False
    elif mapa[y][x] == ".":
        return True
    else:
        if dir == "^":
            return canPushDir(mapa, (y-1, x), dir)
        if dir == "v":
            return canPushDir(mapa, (y+1, x), dir)
        if dir == "<":
            return canPushDir(mapa, (y, x-1), dir)
        if dir == ">":
            return canPushDir(mapa, (y, x+1), dir)

def push(mapa, p, c, dir):
    y,x = p 
    if mapa[y][x] == ".":
        mapa[y][x] = c
    elif mapa[y][x] in "O@":
        oc = mapa[y][x]
        mapa[y][x] = c
        if dir == "^":
            return push(mapa, (y-1, x), oc, dir)
        if dir == "v":
            return push(mapa, (y+1, x), oc, dir)
        if dir == "<":
            return push(mapa, (y, x-1), oc, dir)
        if dir == ">":
            return push(mapa, (y, x+1), oc, dir)


for line in f:
    line = line.strip()
    for dir in line:
        if canPushDir(mapa, p, dir):
            push(mapa, p, "@", dir)
            y,x = p 
            mapa[y][x]="."
            if dir == "^":
                p = (y-1, x)
            if dir == "v":
                p = (y+1, x)
            if dir == "<":
                p = (y, x-1)
            if dir == ">":
                p = (y, x+1)


acc = 0
for y in range(len(mapa)):
    for x in range(len(mapa[0])):
        if mapa[y][x] == "O":
            acc += 100*y + x

print(acc)




# Part II

f = open(filename)
mapa = []
line = f.readline().strip()
while line != "":
    line = line.replace("#","##")
    line = line.replace("O","[]")
    line = line.replace(".","..")
    line = line.replace("@","@.")
    mapa.append(list(line))
    line = f.readline().strip()

p = None
for y in range(len(mapa)):
    if "@" in mapa[y]:
        p = y, mapa[y].index("@")

def canPushDir(mapa, p, dir):
    y,x = p 
    if mapa[y][x] == "#":
        return False
    elif mapa[y][x] == ".":
        return True
    else:
        if dir == "^":
            if mapa[y][x] == "[":
                return canPushDir(mapa, (y-1, x), dir) and canPushDir(mapa, (y-1, x+1), dir)
            elif mapa[y][x] == "]":
                return canPushDir(mapa, (y-1, x), dir) and canPushDir(mapa, (y-1, x-1), dir)
            else:
                return canPushDir(mapa, (y-1, x), dir)
        if dir == "v":
            if mapa[y][x] == "[":
                return canPushDir(mapa, (y+1, x), dir) and canPushDir(mapa, (y+1, x+1), dir)
            elif mapa[y][x] == "]":
                return canPushDir(mapa, (y+1, x), dir) and canPushDir(mapa, (y+1, x-1), dir)
            else:
                return canPushDir(mapa, (y+1, x), dir)
        if dir == "<":
            return canPushDir(mapa, (y, x-1), dir)
        if dir == ">":
            return canPushDir(mapa, (y, x+1), dir)

def push(mapa, p, c, dir):
    y,x = p 
    if mapa[y][x] == ".":
        mapa[y][x] = c
    elif mapa[y][x] in "[]@":
        oc = mapa[y][x]
        mapa[y][x] = c
        if dir == "^":
            if oc == "@":
                push(mapa, (y-1, x), oc, dir)
            elif oc == "[":
                mapa[y][x+1]="."
                push(mapa, (y-1, x), oc, dir)
                push(mapa, (y-1, x+1), "]", dir)
            else:
                mapa[y][x-1]="."
                push(mapa, (y-1, x), oc, dir)
                push(mapa, (y-1, x-1), "[", dir)
        if dir == "v":
            if oc == "@":
                push(mapa, (y+1, x), oc, dir)
            elif oc == "[":
                mapa[y][x+1]="."
                push(mapa, (y+1, x), oc, dir)
                push(mapa, (y+1, x+1), "]", dir)
            else:
                mapa[y][x-1]="."
                push(mapa, (y+1, x), oc, dir)
                push(mapa, (y+1, x-1), "[", dir)
        if dir == "<":
            push(mapa, (y, x-1), oc, dir)
        if dir == ">":
            push(mapa, (y, x+1), oc, dir)


for line in f:
    line = line.strip()
    for dir in line:
        if canPushDir(mapa, p, dir):
            push(mapa, p, "@", dir)
            y,x = p 
            mapa[y][x]="."
            if dir == "^":
                p = (y-1, x)
            if dir == "v":
                p = (y+1, x)
            if dir == "<":
                p = (y, x-1)
            if dir == ">":
                p = (y, x+1)


acc = 0
for y in range(len(mapa)):
    for x in range(len(mapa[0])):
        if mapa[y][x] == "[":
            acc += 100*y + x

print(acc)