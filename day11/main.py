filename = "input2.txt"

# Part I // II

def blink(line):
    d = {}
    for e in line:
        v = e[0]
        if v in d.keys():
            d[v].append(e[1])
        else:
            d[v]=[e[1]]
    line = []
    for key in d.keys():
        line.append( (key, sum(d[key])) )
        
    ret = []       
    for e in line:
        if e[0] == 0:
            ret.append( (1, e[1]) )
        elif len(str(e[0]))%2==0:
            l = len(str(e[0]))
            ret.append( (e[0]//(10**(l//2)), e[1]) )
            ret.append( (e[0]%(10**(l//2)), e[1])  )
        else:
            ret.append( (e[0]*2024, e[1]) )
    return ret

line = [(int(x),1) for x in open(filename).readline().strip().split(" ")]


for i in range(25):
    line = blink(line)

acc = 0
for e in line:
    acc += e[1]
print(acc)

# Another 50 blinks for Part II
for i in range(50): 
    line = blink(line)

acc = 0
for e in line:
    acc += e[1]
print(acc)

