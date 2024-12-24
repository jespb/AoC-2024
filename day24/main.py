
filename = "input2.txt"

# Part I

d = {}

f = open(filename)

line = f.readline().strip()
while line != "":
    line = line.split(": ")
    d[line[0]] = line[1]=="1"
    line = f.readline().strip()

for line in f:
    line = line.strip().split(" ")
    d[line[-1]] = line[:3]

def solveDic(dictionary, key):
    r = dictionary[key]
    if type(r) == list:
        if r[1] == "AND":
            tmp = solveDic(dictionary, r[0]) and solveDic(dictionary, r[2])
            dictionary[key] = tmp
        elif r[1] == "OR":
            tmp = solveDic(dictionary, r[0]) or  solveDic(dictionary, r[2])
            dictionary[key] = tmp
        elif r[1] == "XOR":
            tmp = solveDic(dictionary, r[0]) != solveDic(dictionary, r[2])
            dictionary[key] = tmp

    return dictionary[key]


for key in d.keys():
    solveDic(d,key)

keys = sorted(d.keys())#, reverse=True)


exp = 0
acc = 0
for k in keys:
    if k[0] == "z":
        if d[k]:
            acc += 2**exp
        exp += 1

print(acc)