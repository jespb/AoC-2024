filename = "input3.txt"

# Part I


def getZeros(mapa):
	ret = []
	for y in range(len(mapa)):
		for x in range(len(mapa[0])):
			if mapa[y][x] == 0:
				ret.append( (y,x) )
	return ret

def explore(pos, mapa, v):
	y,x = pos
	h = mapa[y][x]
	if h == 9:
		v.append(str((y,x)))
	if y>0 and mapa[y-1][x]==h+1:
		explore( (y-1, x), mapa, v )
	if x>0 and mapa[y][x-1]==h+1:
		explore( (y, x-1), mapa, v )
	if y<len(mapa)-1 and mapa[y+1][x]==h+1:
		explore( (y+1, x), mapa, v )
	if x<len(mapa[0])-1 and mapa[y][x+1]==h+1:
		explore( (y, x+1), mapa, v )


f = open(filename)
mapa = [ [int(x) for x in line.strip()] for line in f ]


zeros = getZeros(mapa)
acc = 0
for z in zeros:
	v = []
	explore(z, mapa, v)
	acc += len(list(set(v)))
print(acc)


# Part II


def getZeros(mapa):
	ret = []
	for y in range(len(mapa)):
		for x in range(len(mapa[0])):
			if mapa[y][x] == 0:
				ret.append( (y,x) )
	return ret

def explore(pos, mapa, v):
	y,x = pos
	h = mapa[y][x]
	if h == 9:
		v.append(str((y,x)))
	if y>0 and mapa[y-1][x]==h+1:
		explore( (y-1, x), mapa, v )
	if x>0 and mapa[y][x-1]==h+1:
		explore( (y, x-1), mapa, v )
	if y<len(mapa)-1 and mapa[y+1][x]==h+1:
		explore( (y+1, x), mapa, v )
	if x<len(mapa[0])-1 and mapa[y][x+1]==h+1:
		explore( (y, x+1), mapa, v )


f = open(filename)
mapa = [ [int(x) for x in line.strip()] for line in f ]


zeros = getZeros(mapa)
acc = 0
for z in zeros:
	v = []
	explore(z, mapa, v)
	acc += len(v)
print(acc)