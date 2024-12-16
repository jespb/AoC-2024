filename = "input2.txt"

# Part I and II

def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)** 0.5

def explore(mapa, positions, explored, target, limit):
    positions.sort(reverse=True)
    cost, pos_seen, _, y, x, dir = positions.pop()
    explored[y][x] +=1
    pos_seen.append((y,x))
    #print(positions)
    if distance( (y,x), target) == 0:
        return cost, pos_seen
    
    #for line in explored:
    #    print(line)

    if mapa[y-1][x]!="#" and explored[y-1][x] < limit:
        positions.append( ( cost + 1 + (1000 if dir != "N" else 0), pos_seen[:], distance((y-1,x), target), y-1, x, "N") )
    if mapa[y+1][x]!="#" and explored[y+1][x] < limit:
        positions.append( ( cost + 1 + (1000 if dir != "S" else 0), pos_seen[:], distance((y+1,x), target), y+1, x, "S") )
    if mapa[y][x-1]!="#" and explored[y][x-1] < limit:
        positions.append( ( cost + 1 + (1000 if dir != "W" else 0), pos_seen[:], distance((y,x-1), target), y, x-1, "W") )
    if mapa[y][x+1]!="#" and explored[y][x+1] < limit:
        positions.append( ( cost + 1 + (1000 if dir != "E" else 0), pos_seen[:], distance((y,x+1), target), y, x+1, "E") )

    return 0,[]

for limit in range(10):
    f = open(filename)
    mapa = [line.strip() for line in f]

    yi = len(mapa)-2
    xi = 1
    yf = 1
    xf = len(mapa[0])-2

    explored = [ [0 for c in line ] for line in mapa]

    cost = 0
    pos_seen = [(yi,xi)]
    positions = [ (0, pos_seen, distance((yi,xi),(yf,xf)), yi, xi, "E") ]

    paths = {}
    while len(positions) > 0:
        cost, ps2 = explore(mapa, positions, explored, (yf,xf), limit)
        if cost != 0:
            if cost in paths.keys():
                paths[cost].extend(ps2)
            else:
                paths[cost] = ps2

    ps = paths[min(paths.keys())]
    ps = list(set(ps))
    print(cost, len(ps))

        
# Low effort solution for P2
# I just increase the number of times i can walk on the same path until the value becomes stable
# EG 4->495 tiles, 5->500 tiles, 6 -> 500 tiles as well so, that should be the answer