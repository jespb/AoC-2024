
filename="input2.txt"


# Part I

def possible(target, lista, current=0):
	if len(lista) == 0:
		return target == current
	if current > target:
		return False
	return possible(target, lista[1:], current+lista[0]) or possible(target, lista[1:], max(current, 1)*lista[0])

f = open(filename)

acc = 0
for line in f:
	line=line.strip().replace(":","").split(" ")
	line = [int(x) for x in line]
	if possible(line[0], line[1:]):
		acc += line[0]

print(acc)


# Part II

def possible(target, lista, current=0):
	if len(lista) == 0:
		return target == current
	if current > target:
		return False
	return 	possible(target, lista[1:], current+lista[0]) or \
			possible(target, lista[1:], max(current, 1)*lista[0]) or \
			possible(target, lista[1:], current*10**len(str(lista[0]))+lista[0])

f = open(filename)

acc = 0
for line in f:
	line=line.strip().replace(":","").split(" ")
	line = [int(x) for x in line]
	if possible(line[0], line[1:]):
		acc += line[0]

print(acc)