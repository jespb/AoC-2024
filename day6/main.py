
filename = "input2.txt"


# Part I

f=open(filename)
mapa= [line.strip() for line in f]
visits=[ [0 for _ in line] for line in mapa]

pos = [0,0,0]
for y in range(len(mapa)):
	for x in range(len(mapa[0])):
		if mapa[y][x] == "^":
			pos=[y,x,0]
			visits[y][x] += 1



try:
	while visits[pos[0]][pos[1]] != 4:
		if pos[2] == 0: #N
			if  mapa[pos[0]-1][pos[1]]=="#":
				pos[2] = (pos[2]+1)%4
				#pos[1] += 1
			else:
				pos[0] -= 1
		elif pos[2] == 1: #E
			if mapa[pos[0]][pos[1]+1]=="#":
				pos[2] = (pos[2]+1)%4
				#pos[0] += 1
			else:
				pos[1] += 1
		elif pos[2] == 2: #S
			if mapa[pos[0]+1][pos[1]]=="#":
				pos[2] = (pos[2]+1)%4
				#pos[1] -= 1
			else:
				pos[0] += 1
		elif pos[2] == 3: #W
			if  mapa[pos[0]][pos[1]-1]=="#":
				pos[2] = (pos[2]+1)%4
				#pos[0] -= 1
			else:
				pos[1] -= 1
		
		visits[pos[0]][pos[1]] += 1

except: #Out of bounds when leaving the matrix
	pass

acc = len(mapa)*len(mapa[0])
for line in visits:
	acc -= line.count(0)



print(acc)





# Part II


def getStruck(mapa, pos):
	visits=[ [0 for _ in line] for line in mapa]

	try:
		# if it visits the same place 4 times, it got stuck
		while visits[pos[0]][pos[1]] != 4:
			if pos[2] == 0: #N
				if  mapa[pos[0]-1][pos[1]]=="#":
					pos[2] = (pos[2]+1)%4
					#pos[1] += 1
				else:
					pos[0] -= 1
			elif pos[2] == 1: #E
				if mapa[pos[0]][pos[1]+1]=="#":
					pos[2] = (pos[2]+1)%4
					#pos[0] += 1
				else:
					pos[1] += 1
			elif pos[2] == 2: #S
				if mapa[pos[0]+1][pos[1]]=="#":
					pos[2] = (pos[2]+1)%4
					#pos[1] -= 1
				else:
					pos[0] += 1
			elif pos[2] == 3: #W
				if  mapa[pos[0]][pos[1]-1]=="#":
					pos[2] = (pos[2]+1)%4
					#pos[0] -= 1
				else:
					pos[1] -= 1
			
			# python allows negative indices (indicating the solder escaped)
			if pos[0]==-1 or pos[1]==-1:
				return False

			visits[pos[0]][pos[1]] += 1

	except: #Out of bounds when leaving the matrix
		return False

	return True


f=open(filename)
mapa= [line.strip() for line in f]
visits_by_default = visits # visits in part I and non^zero
visits=[ [0 for _ in line] for line in mapa]\

pos = [0,0,0]
for y in range(len(mapa)):
	for x in range(len(mapa[0])):
		if mapa[y][x] == "^":
			pos=[y,x,0]
			visits[y][x] += 1

acc = 0
for y in range(len(mapa)):
	for x in range(len(mapa[0])):
		# blocking a cell that is not visited will not affect the results
		if not mapa[y][x] in "#^" and visits_by_default[y][x]>0:
			mapa2 = [list(line) for line in mapa]
			pos2 = pos[:]
			mapa2[y][x] = "#"

			if getStruck(mapa2, pos2):
				acc += 1

print(acc)
