
filename = "input2.txt"


# Part I

f = open(filename)
l1 = []
l2 = []
for l in f:
	l = [int(x) for x in l.strip().split("   ")]
	l1.append(l[0])
	l2.append(l[1])
l1.sort()
l2.sort()
print( sum([abs(l1[i]-l2[i]) for i in range(len(l1))]))


# Part II

print( sum([e * l2.count(e) for e in l1]) )