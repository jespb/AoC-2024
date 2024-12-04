

filename = "input2.txt"

# Part I

f = open(filename)
m = [line.strip() for line in f]

count = 0
for y in range(len(m)):
	for x in range(len(m[0])):
		if m[y][x]=="X":
			if y>2 and m[y-1][x] == "M" and m[y-2][x] == "A" and m[y-3][x] == "S": # N
				count += 1
			if y<len(m)-3 and m[y+1][x] == "M" and m[y+2][x] == "A" and m[y+3][x] == "S": # S
				count += 1
			if x>2 and m[y][x-1] == "M" and m[y][x-2] == "A" and m[y][x-3] == "S": # W
				count += 1
			if x<len(m[0])-3 and m[y][x+1] == "M" and m[y][x+2] == "A" and m[y][x+3] == "S": # E
				count += 1
			if y>2 and x>2 and m[y-1][x-1] == "M" and m[y-2][x-2] == "A" and m[y-3][x-3] == "S": # NW
				count += 1
			if y>2 and x<len(m[0])-3 and m[y-1][x+1] == "M" and m[y-2][x+2] == "A" and m[y-3][x+3] == "S": # NE
				count += 1
			if y<len(m)-3 and x>2 and m[y+1][x-1] == "M" and m[y+2][x-2] == "A" and m[y+3][x-3] == "S": # SW
				count += 1
			if y<len(m)-3 and x<len(m[0])-3 and m[y+1][x+1] == "M" and m[y+2][x+2] == "A" and m[y+3][x+3] == "S": # SE
				count += 1

print(count)



# Part II

f = open(filename)
m = [line.strip() for line in f]

count = 0
for y in range(1,len(m)-1):
	for x in range(1,len(m[0])-1):
		if m[y][x]=="A":

			if m[y-1][x-1] == "M" and m[y+1][x+1] == "S" and m[y+1][x-1] == "M" and m[y-1][x+1] == "S": # N
				count += 1
			if m[y-1][x-1] == "M" and m[y+1][x+1] == "S" and m[y+1][x-1] == "S" and m[y-1][x+1] == "M": # N
				count += 1
			if m[y-1][x-1] == "S" and m[y+1][x+1] == "M" and m[y+1][x-1] == "M" and m[y-1][x+1] == "S": # N
				count += 1
			if m[y-1][x-1] == "S" and m[y+1][x+1] == "M" and m[y+1][x-1] == "S" and m[y-1][x+1] == "M": # N
				count += 1

print(count)







