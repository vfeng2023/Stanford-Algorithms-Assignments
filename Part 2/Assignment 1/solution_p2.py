from functools import cmp_to_key
# read file

# compute min cost

def compute(arr):
    def comparator(thing1, thing2):
        w1, l1 = thing1
        w2, l2 = thing2
        if w1 - l1 > w2 - l2:
            return -1
        elif w1-l1 == w2-l2:
            if w1 > w2:
                return -1
            elif w1 == w2:
                return 0
            else:
                return 1
        else:
            return 1
        
    arr.sort(key=cmp_to_key(comparator))
    print(jobs[:5])
    totalcost = 0
    c = 0
    for w, l in arr:
        c += l
        totalcost += c * w

    return totalcost

filename = "jobs.txt"
with open(filename, "r") as f:
    lines = f.readlines()
    count = int(lines[0])
    jobs = []
    for l in lines[1:]:
        l = l.strip()
        weight, job = list(map(int, l.split()))
        jobs.append((weight,job))

cost = compute(jobs)
print("cost with w-l: ",cost)
        

"""
Output:
[(99, 1), (98, 1), (95, 1), (95, 1), (93, 1)]
cost with w-l:  67311454237
"""