filename = "input2.txt"

# Part I 
def element_exists(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return True
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

def possible_count(towel_d, lens, target, acc):
    #print(acc)
    lt = len(target)
    if lt <= max_len and element_exists(towel_d[lt], target): #target in towel_d[lt]:
        acc[0]+=1
    
    for l in range(lens[0], lens[1]+1):
        sub = target[:l]
        if element_exists(towel_d[l], sub): #sub in towel_d[l]:
            possible_count(towel_d, lens, target[l:], acc)

def possible(towels, lens, target):
    if target=="" or target in towels:
        return True
    else:
        for l in range(lens[0], lens[1]+1):
            sub = target[:l]
            if sub in towels:
                if possible(towels, lens, target[l:]):
                    return True 
    return False


f = open(filename)
towels = f.readline().strip().split(", ")
min_len = min([len(t) for t in towels])
max_len = max([len(t) for t in towels])
towel_d = {}
for i in range(max_len+1):
    towel_d [i] = []
for t in towels:
    towel_d[ len(t)].append(t)
for i in range(max_len+1):
    towel_d [i] = sorted(towel_d [i])
f.readline()
acc_pt1 = 0
acc_pt2 = 0
min_len = min([len(t) for t in towels])
max_len = max([len(t) for t in towels])
lens= (min_len, max_len)
print(min_len, max_len)
for line in f:
    print(line)
    tmp = [0]
    line = line.strip()
    pos = possible(towels, lens, line)
    if pos:
        acc_pt1 += 1
        possible_count(towel_d, lens, line, tmp)
        acc_pt2 += tmp[0]
    print(acc_pt2)
    
print("Part 1:", acc_pt1)
print("Part 2:", acc_pt2)