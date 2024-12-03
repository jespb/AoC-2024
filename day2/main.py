
filename = "input2.txt"


def inc(l):
	return sum([ 0 if l[i] < l[i+1] else 1 for i in range(len(l)-1)]) == 0

def dec(l):
	return sum([ 0 if l[i] > l[i+1] else 1 for i in range(len(l)-1)]) == 0

def adj(l):
	return sum([ 0 if abs(l[i]-l[i+1])<4 else 1 for i in range(len(l)-1)]) == 0


# Part I

f = open(filename)

c = 0
for l in f:
	l = [ int(x) for x in l.strip().split(" ")]
	if ( inc(l) or dec(l) ) and adj(l):
		c += 1
f.close()

print(c)

# Part II

f = open(filename)

c = 0
for l in f:
	l = [ int(x) for x in l.strip().split(" ")]
	if ( inc(l) or dec(l) ) and adj(l):
		c += 1
	else:
		v = False
		for i in range(len(l)):
			tmp = l[:i]+l[i+1:]
			if ( inc(tmp) or dec(tmp) ) and adj(tmp):
				v = True
		if v:
			c += 1
f.close()

print(c)