filename = "input2.txt"

# Part I


f = open(filename)

antennas = {}

mapa = [line.strip() for line in f]

for y in range(len(mapa)):
	for x in range(len(mapa[y])):
		c = mapa[y][x]
		if c != ".":
			if c in antennas.keys():
				antennas[c].append([y,x])
			else:
				antennas[c] = [ [y,x] ]
			
antinodes = [[0 for _ in line] for line in mapa]

for type in antennas.keys():
	pos = antennas[type]
	for i in range(len(pos)):
		p1 = pos[i]
		for p2 in pos:
			if str(p1)!=str(p2):
				yi = 2*p1[0]-p2[0]
				xi = 2*p1[1]-p2[1]
				if yi >= 0 and xi >= 0 and yi < len(mapa) and xi < len(mapa[0]):
					antinodes[yi][xi] = 1

s = sum([sum(line)for line in antinodes])
print(s)




# Part I


f = open(filename)

antennas = {}

mapa = [line.strip() for line in f]

for y in range(len(mapa)):
	for x in range(len(mapa[y])):
		c = mapa[y][x]
		if c != ".":
			if c in antennas.keys():
				antennas[c].append([y,x])
			else:
				antennas[c] = [ [y,x] ]
			
antinodes = [[0 for _ in line] for line in mapa]

for type in antennas.keys():
	pos = antennas[type]
	for i in range(len(pos)):
		p1 = pos[i]
		antinodes[p1[0]][p1[1]] = 1
		for p2 in pos:
			if str(p1)!=str(p2):
				yi = 2*p1[0]-p2[0]
				xi = 2*p1[1]-p2[1]
				while yi >= 0 and xi >= 0 and yi < len(mapa) and xi < len(mapa[0]):
					antinodes[yi][xi] = 1
					yi = yi + p1[0]-p2[0]
					xi = xi + p1[1]-p2[1]
					

s = sum([sum(line)for line in antinodes])
print(s)
