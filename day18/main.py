
filename = "input2.txt"
w = 71
target= (w,w)
corruption = 1024

# Part I 

def explore(mapa, positions, explored):
    while len(positions) != 0:
        positions.sort(reverse=True)
        cost,y,x = positions.pop()
        if explored[y][x] == -1:
            explored[y][x] = cost 
                
            if mapa[y-1][x]!="#" and explored[y-1][x]  == -1:
                positions.append( ( cost + 1, y-1, x) )
            if mapa[y+1][x]!="#" and explored[y+1][x]  == -1:
                positions.append( ( cost + 1, y+1, x) )
            if mapa[y][x-1]!="#" and explored[y][x-1]  == -1:
                positions.append( ( cost + 1, y, x-1 ) )
            if mapa[y][x+1]!="#" and explored[y][x+1]  == -1:
                positions.append( ( cost + 1, y, x+1 ) )
        



mapa= [list("#"*(w+2))]
for l in range(w):
    mapa.append(list("#" + " "*w + "#"))
mapa.append( list("#"*(w+2)) )

f = open(filename).readlines()
i = 0
for l in f:
    l = [int(x)+1 for x in l.strip().split(",")]
    mapa[l[1]][l[0]] = "#"
    i+=1
    if i == corruption:
        break

for line in mapa:
    print("".join(line))

explored = [ [-1 for c in line ] for line in mapa]

positions = [(0,1,1)]

# Part I
explore(mapa, positions, explored)
print(explored[w][w])

# Part II    
for corruption in range(2000, 3000):
    mapa= [list("#"*(w+2))]
    for l in range(w):
        mapa.append(list("#" + " "*w + "#"))
    mapa.append( list("#"*(w+2)) )

    i = 0
    for l in f:
        l = [int(x)+1 for x in l.strip().split(",")]
        mapa[l[1]][l[0]] = "#"
        i+=1
        if i == corruption:
            break
          
    explored = [ [-1 for c in line ] for line in mapa]

    positions = [(0,1,1)]

    explore(mapa, positions, explored)
    #print(corruption, explored[w][w])
    
    if explored[w][w] == -1:
        print(f[corruption-1])
        break 