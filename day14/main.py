filename = "input2.txt"

# Part I

ylen = 103
xlen = 101
mapa = [ [0 for _ in range(xlen)] for _ in range(ylen) ]

f = open(filename)
for line in f:
    line = line.strip()
    p = [int(x) for x in line.split("p=")[1].split(" ")[0].split(",")]
    v = [int(x) for x in line.split("v=")[1].split(",")]

    yfin = (p[1]+v[1]*100)%ylen
    xfin = (p[0]+v[0]*100)%xlen
    mapa[yfin][xfin] += 1

midx = len(mapa[0])//2
midy = len(mapa)//2

mult = 1

acc = 0
for i in range(midy):
    acc += sum(mapa[i][:midx])
mult *= acc

acc = 0
for i in range(midy+1, len(mapa)):
    acc += sum(mapa[i][:midx])
mult *= acc

acc = 0
for i in range(midy):
    acc += sum(mapa[i][midx+1:])
mult *= acc

acc = 0
for i in range(midy+1, len(mapa)):
    acc += sum(mapa[i][midx+1:])
mult *= acc

print(mult)




# Part II

ylen = 103
xlen = 101
mapa = [ [0 for _ in range(xlen)] for _ in range(ylen) ]

f = open(filename)
robots = []
for line in f:
    line = line.strip()
    p = [int(x) for x in line.split("p=")[1].split(" ")[0].split(",")]
    v = [int(x) for x in line.split("v=")[1].split(",")]

    robots.append( (p,v) )

for it in range(10000):

    mapa = [ [0 for _ in range(xlen)] for _ in range(ylen) ]
    for r in robots:
        p,v = r
        yfin = (p[1]+v[1]*it)%ylen
        xfin = (p[0]+v[0]*it)%xlen
        mapa[yfin][xfin] += 1
    
    toprint=[]
    t1 = False 
    t2 = False 
    t3 = False 
    toprint.append(str(it))
    for line in mapa:
        toprint.append("".join( "*" if x>0 else " " for x in line))
        # This is what defines a christmas tree right?
        t1 = t1 or " *** " in toprint[-1]
        t2 = t2 or " ***** " in toprint[-1]
        t3 = t3 or " ******* " in toprint[-1]
    
    if t1 and t2 and t3:
        print( "\n".join(toprint))
