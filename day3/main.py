

filename = "input2.txt"

# Part I

f = open(filename)

s = "".join([line.strip() for line in f])

s = s.split("mul(")
acc = 0
for l in s:
	l = l[:10] # to avoid long strings
	try:
		l = [int(x) for x in l.split(")")[0].split(",")]
		acc += l[0]*l[1]
	except:
		pass
f.close()

print(acc)


# Part II

f = open(filename)

s = "".join([line.strip() for line in f])

acc = 0

s = s.split("do()")
for line in s:
	line = line.split("don't()")[0]

	line = line.split("mul(")
	for l in line:
		l = l[:10] # to avoid long strings
		try:
			l = [int(x) for x in l.split(")")[0].split(",")]
			acc += l[0]*l[1]
		except:
			pass
f.close()

print(acc)


