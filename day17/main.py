
filename  = "input2.txt"

# Part I


def combo(_a, _b, _c, value):
	# 0-3 literal value
	# 4 - A
	# 5 - B
	# 6 - C
	# 7 - Invalid ?
	if value < 4:
		return value 
	if value == 4:
		return _a 
	if value == 5:
		return _b 
	if value == 6:
		return _c
	
	assert False

def run(_A, _B, _C, program):
	i = 0
	ret = []
	while i < len(program):
		op = program[i]
		val = program[i+1]
		#print(i, op, val)

		if op == 0: # 0, 6 and 7 are "the same"
			_A = _A // 2** combo(_A, _B, _C, val) 
			i+=2
		elif op == 1:
			_B = _B ^ val
			i+=2
		elif op == 2:
			_B = combo(_A, _B, _C, val) % 8
			i+=2
		elif op == 3:
			if _A != 0:
					i = val
			else:
				i+=2
		elif op == 4:
			_B = _B ^ _C
			i+=2
		elif op == 5:
			ret.append("%d" % (combo(_A, _B, _C, val)%8) )
			i+=2
		elif op == 6: # 0, 6 and 7 are "the same"
			_B = _A // 2** combo(_A, _B, _C, val)
			i+=2
		elif op == 7: # 0, 6 and 7 are "the same"
			_C = _A // 2** combo(_A, _B, _C, val) 
			i+=2
	return _A, _B, _C, ",".join(ret)


f = open(filename)
_A = int(f.readline().strip().split(": ")[1])
_B = int(f.readline().strip().split(": ")[1])
_C = int(f.readline().strip().split(": ")[1])
f.readline()
program = [int(x) for x in f.readline().strip().split(": ")[1].split(",")]

# Part I
#print("original", program)
print(run(_A, _B, _C, program[:])[3])
#print(run(_A, _B, _C, program[:]))


# Part II

orig_p = ",".join(str(x) for x in program)
_a = 1
tl = len(orig_p)
p = ""
lb = 0
ub = 0
while len(p) <= tl:
	a,b,c,p = run(_a, _B, _C, program[:])
	_a *= 2

	if len(p)<tl:
		lb = _a
	if len(p)>tl:
		ub =_a

	#print(a,b,c, "%50s" %p, _a)

from difflib import SequenceMatcher


if False: # Step 1
	tmp = 0
	for _a in range(lb, ub, ):
		a,b,c,p = run(_a, _B, _C, program[:])
		if p == orig_p:
			print(_a)
		
		#if SequenceMatcher(None, p, orig_p).ratio() > 0.7:
		if p[:13]=="2,4,1,1,7,5,4":
			print(_a, "sim", SequenceMatcher(None, p, orig_p).ratio())
			print(p)
			print(orig_p)
			print(_a-tmp)
			tmp =  _a

# finetune after "step 1"
# step 2
if False:
	lb = 35184378915370
	tmp = 0
	jumps = [3,2,16777211]
	i = 0
	p = ""
	_a = lb
	while p != orig_p:
		_a += jumps[i]
		a,b,c,p = run(_a, _B, _C, program[:])
		if p == orig_p:
			print(_a)
		i = (i+1)%3
		
		#if SequenceMatcher(None, p, orig_p).ratio() > 0.7:
		if p[:25]=="2,4,1,1,7,5,4,6,0,3,1,4,5":
			print(_a, "sim", SequenceMatcher(None, p, orig_p).ratio())
			print(p)
			print(orig_p)
			print(_a-tmp)
			tmp =  _a


# step 3
lb = 35846407858730
tmp = 0
jumps = [3,2,1099511627771]
i = 0
p = ""
_a = lb
while p != orig_p:
	_a += jumps[i]
	a,b,c,p = run(_a, _B, _C, program[:])
	i = (i+1)%3
	

print(_a)
#lower bound for _a:  35184372088832
#upper bound for _a: 562949953421312