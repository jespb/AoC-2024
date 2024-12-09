filename = "input2.txt"

# Part I

f = [int(x) for  x in open(filename).readline().strip()]
mem = [-1]*sum(f)
file = True
ind = 0
fileid = 0
for v in f:
	for i in range(ind, ind+v):
		if file:
			mem[i] = fileid//2
		else:
			mem[i] = "."

	fileid += 1
	file = not file
	ind += v 

i = 0
j = len(mem)-1
while i<j:
	if mem[i] == ".":
		found = mem[j] != "."
		while not found and i<j:
			j -= 1
			found = mem[j] != "."
		if i<j:
			mem[i]=mem[j]
			mem[j]="."
	i += 1

acc = 0
i = 0
while mem[i] != ".":
	acc += mem[i]*i
	i += 1

print(acc)





# Part I




f = [int(x) for  x in open(filename).readline().strip()]
mem = [-1]*sum(f)
file = True
ind = 0
fileid = 0
mem_dic = {}
for v in f:
	for i in range(ind, ind+v):
		if file:
			mem[i] = fileid//2
			mem_dic[fileid//2] = v
		else:
			mem[i] = "."

	fileid += 1
	file = not file
	ind += v 


def earliestFit(mem, mem_dic, key, max_search):
	length = mem_dic[key]
	for i in range(len(mem)):
		if mem[i] == ".":
			z = i 
			while z < max_search and mem[z] == "." :
				z += 1
			z = z-i
			if z >= length:
				return i 
	return None


for key in list(mem_dic.keys())[::-1]:
	fo = mem.index(key)
	ind = earliestFit(mem, mem_dic, key, fo)
	if not ind is None and ind < fo:
		for ww in range(len(mem)):
			if mem[ww] == key:
				mem[ww] = "."
		for j in range(mem_dic[key]):
			mem[ind+j] = key



acc = 0
i = 0
for i in range(len(mem)):
	if mem[i] != ".":
		acc += mem[i]*i
		i += 1

print(acc)
