filename = "input1.txt"

# Part I / II

def getFirstSecond(ab, bb, t):

    firstdiv = -1
    seconddiv = -1

    tmp = t[0] % bb[0] 
    tmp2 = (t[0]-ab[0]) % bb[0]
    dt = tmp2-tmp # 0-1  4-2
    cycle = False
    fail = False
    x = 1
    while not cycle:
        v = (t[0] - x * ab[0]) % bb[0]
        x += 1
        if v == 0:
            firstdiv = x-1
            cycle = True
        if v == tmp:
            cycle = True
            #fail = True
    
    if firstdiv != -1 and not fail:
        cycle = False
        tmp = 0
        while not cycle:
            v = (t[0] - x * ab[0]) % bb[0]
            x += 1
            if v == 0:
                seconddiv = x-1
                cycle = True
            elif v == tmp:
                cycle = True
                #fail = True
    
    return firstdiv,seconddiv,fail


def part1(ab, bb, t):
    for a in range(101):
        b = (t[0] - a*ab[0])//bb[0]
        if b>=0 and b<=100 and b * bb[1] + a * ab[1] == t[1] and b * bb[0] + a * ab[0] == t[0]:
            return a,b 
    return 0,0

def bs(ab, bb, t, init_a, step_a, flipped=False):
    n_step = 0
    a = init_a + n_step*step_a
    b = (t[0] - a*ab[0])//bb[0]

    if b * bb[1] + a * ab[1] == t[1] and b * bb[0] + a * ab[0] == t[0]:
        return a,b 
    
    gt = b * bb[1] + a * ab[1] > t[1]
      
    lower_bound = 0    
    upper_bound = 1
    a = init_a + upper_bound * step_a
    b = (t[0] - a*ab[0])//bb[0]
    while (b * bb[1] + a * ab[1] > t[1] if gt else b * bb[1] + a * ab[1] < t[1]) and b > 0:
        upper_bound *= 2
        a = init_a + upper_bound * step_a
        b = (t[0] - a*ab[0])//bb[0]

    #upper_bound = 101 # part I
    midpoint = (lower_bound+upper_bound)//2
    a = init_a + midpoint * step_a
    b = (t[0] - a*ab[0])//bb[0]
    while b * bb[1] + a * ab[1] != t[1] and lower_bound!=upper_bound-1 :
        if b * bb[1] + a * ab[1] > t[1] if gt else b * bb[1] + a * ab[1] < t[1]:
            lower_bound = midpoint
        if b * bb[1] + a * ab[1] < t[1] if gt else b * bb[1] + a * ab[1] > t[1]:
            upper_bound = midpoint
        midpoint = (lower_bound+upper_bound)//2
        a = init_a + midpoint * step_a
        b = (t[0] - a*ab[0])//bb[0]
        #print(a,b, lower_bound, midpoint,upper_bound)
    if lower_bound==upper_bound-1 :
        for lb in range(lower_bound-1, upper_bound+2):
            a = init_a + lb * step_a
            b = (t[0] - a*ab[0])//bb[0]
            if b * bb[1] + a * ab[1] == t[1] and b * bb[0] + a * ab[0] == t[0]:
                return a,b
    

    return a,b


f = [line.strip() for line in open(filename)]

acc = []
pairs = []
acc2 = []

for game in range(0, len(f), 4):
    badpairs = []
    #print()
    ab = f[game].split("+")[1:]
    ab[0] = int(ab[0].split(",")[0])
    ab[1] = int(ab[1])
    bb = f[game+1].split("+")[1:]
    bb[0] = int(bb[0].split(",")[0])
    bb[1] = int(bb[1])
    t = f[game+2].split("=")[1:]
    div = 10000000000000
    t[0] = int(t[0].split(",")[0])  + 10000000000000 
    t[1] = int(t[1]) +10000000000000 


    # Part I
    a_p1,b_p1 = part1(ab,bb,t)
    cost_p1 = a_p1*3+b_p1

    part2 = True
    if part2:
        firstdiv_a, seconddiv_a, fail_a = getFirstSecond(ab, bb, t)
        firstdiv_b, seconddiv_b, fail_b = getFirstSecond(bb, ab, t)

        bad = 99999999999
        a1 = bad
        b1 = bad
        a2 = bad
        b2 = bad
        if firstdiv_a != -1 and not fail_a:
            a,b = bs(ab, bb, t, firstdiv_a, seconddiv_a-firstdiv_a)
            #if a <= 100 and b <= 100 and a >= 0 and b >= 0 and b * bb[1] + a * ab[1] == t[1] and b * bb[0] + a * ab[0] == t[0]:
            if a >= 0 and b >= 0 and b * bb[1] + a * ab[1] == t[1] and b * bb[0] + a * ab[0] == t[0]:
                a1 = a 
                b1 = b
        if firstdiv_b != -1 and not fail_b:
            b,a = bs(bb, ab, t, firstdiv_b, seconddiv_b-firstdiv_b)
            #if a <= 100 and b <= 100 and a >= 0 and b >= 0 and b * bb[1] + a * ab[1] == t[1] and b * bb[0] + a * ab[0] == t[0]:
            if  a >= 0 and b >= 0 and b * bb[1] + a * ab[1] == t[1] and b * bb[0] + a * ab[0] == t[0]:
                a2 = a 
                b2 = b
        
        cost = min( a1*3+b1, a2*3+b2)
        if b1 == bad and b2 == bad:
            cost = 0
    
 
    
    acc.append(cost)
    #print("SCORE:", acc[-1])




print("\nFinal scores:")
print(sum(acc))



if False:
    firstdiv = -1
    seconddiv = -1


    tmp = t[0] % bb[0] 
    tmp2 = (t[0]-ab[0]) % bb[0]
    dt = tmp2-tmp # 0-1  4-2
    cycle = False
    fail = False
    x = 1
    while not cycle:
        v = (t[0] - x * ab[0]) % bb[0]
        x += 1
        if v == 0:
            firstdiv = x-1
            cycle = True
        if v == tmp:
            cycle = True
            #fail = True
    
    if firstdiv != -1 and not fail:
        cycle = False
        tmp = 0
        while not cycle:
            v = (t[0] - x * ab[0]) % bb[0]
            x += 1
            if v == 0:
                seconddiv = x-1
                cycle = True
            elif v == tmp:
                cycle = True
                #fail = True

    print(firstdiv, seconddiv)


    fa = -1
    fb = -1
    if firstdiv != -1 and not fail:
        step = seconddiv-firstdiv
        a = firstdiv
        b = (t[0] - a*ab[0])//bb[0]
        cost = b + a * 3
        validcost = 0
        #print(a,b)
        #if b < 101 and a < 101 and b * bb[1] + a * ab[1] == t[1]:
        if  b * bb[1] + a * ab[1] == t[1]:
            validcost = cost
            fa = a
            fb = b
        costDecline = True 
        a += step
        b = (t[0] - a*ab[0])//bb[0]
        #while costDecline and a >= 0 and b >= 0 and a <= 100:
        while costDecline and a >= 0 and b >= 0 :
            print(a,b)
            cost2 = b + a * 3
            #print(a, b, cost2)
            if cost2 < cost or validcost == 0:
                #print("   ", cost, cost2, a, b)
                cost = cost2 
                if b * bb[1] + a * ab[1] == t[1]:
                    validcost = cost
                    fa = a
                    fb = b
            else:
                costDecline = False
            a += step
            b = (t[0] - a*ab[0])//bb[0]

        acc.append( validcost)
    else:
        acc.append(0)