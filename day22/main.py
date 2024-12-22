

filename = "input2.txt"

# Part I

def nextValue(v):
    tmp = v * 64
    v = (v ^ tmp) % 16777216
    tmp = int( v / 32 )
    v = (v ^ tmp) % 16777216
    tmp = v * 2048
    v = (v ^ tmp) % 16777216
    return v

acc = 0    
for line in open(filename):
    value = int(line.strip())
    for i in range(2000):
        value = nextValue(value)
    acc += value
print(acc)


# Part II

dic_list = {}

for line in open(filename):
    value = int(line.strip())
    lista = [value%10]
    for i in range(2000):
        value = nextValue(value)
        lista.append(value%10)
    for i in range(len(lista)-4):
        tmp = (lista[i+1]-lista[i],
               lista[i+2]-lista[i+1],
               lista[i+3]-lista[i+2],
               lista[i+4]-lista[i+3])
        if tmp in dic_list.keys():
            dic_list[tmp] += 1
        else:
            dic_list[tmp] = 1

lista2 =[(dic_list[key], key) for key in dic_list.keys()] 
lista2.sort(reverse=True)

def getFirst(value, s):
    seq = []
    for i in range(2000):
        old_value = value%10
        value = nextValue(value)
        seq.append(value%10 - old_value)
        seq = seq[-4:]
        if s == tuple(seq):
            return value%10

    return 0

best_sec = 0
for seq in lista2:
    acc = 0
    for line in open(filename):
        value = int(line.strip())
        acc += getFirst(value, seq[1])

    # Let it run until you stop seeing updates
    # Grab a coffee
    if acc != 0 and acc > best_sec:
        best_sec = acc 
        print(best_sec)

print(best_sec)