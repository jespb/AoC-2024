
filename = "input2.txt"



# Part I


def lineValid(line, pred):
	valid = True
	for i in range(len(line)):
		if line[i] in pred.keys():
			for p in pred[line[i]]:
				if p in line:
					valid &= p in line[:i] and not p in line[i:]
	return valid


f = open(filename)

pred = {}
line = f.readline().strip()
while line != "":
	line = [int(x) for x in line.split("|")]
	if line[1] in pred.keys():
		pred[line[1]].append(line[0])
	else:
		pred[line[1]] = [line[0]]
	line = f.readline().strip()


acc = 0
for line in f:
	line = [int(x) for x in line.split(",")]
	valid = lineValid(line, pred)
	if valid:
		acc += line[ len(line)//2 ]
print(acc)


# Part II

f = open(filename)

pred = {}
line = f.readline().strip()
while line != "":
	line = [int(x) for x in line.split("|")]
	if line[1] in pred.keys():
		pred[line[1]].append(line[0])
	else:
		pred[line[1]] = [line[0]]
	line = f.readline().strip()



acc = 0
for line in f:
	line = [int(x) for x in line.split(",")]
	valid = lineValid(line, pred)
	if not valid:
		tmp = []
		for e in line:
			i = 0
			v = False
			while not v:
				tmp.insert(i, e)
				v = lineValid(tmp, pred)
				if not v:
					tmp.pop(i)
					i+=1

		acc += tmp[ len(line)//2 ]
print(acc)