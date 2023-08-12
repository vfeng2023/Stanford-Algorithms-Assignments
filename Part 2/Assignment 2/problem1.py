# read file
with open("clustering1.txt", "r") as f:
    lines = f.readlines()
    lookup = dict()
    count = int(lines[0])
    for line in lines[1:]:
        i,j,dist = list(map(int, line.strip().split()))
        lookup[i,j] = dist
        lookup[j,i] = dist
# group

def distance(i,j):
    return lookup[i,j]
def cluster(nodes, distfunc, k):
    # use union find data structure to store the parents of a cluster
    groups = {n:[n] for n in range(1, nodes+1)}
    mindist = float('inf')
    while len(groups) >= 4:
        # compute the minimum distance
        print(len(groups))
        mingroups = 1,1
        mindist = float('inf')
        keys = sorted(groups.keys())
        for idx, g in enumerate(keys): # for each group
            for member in groups[g]: # for the member of that group
                for idxowo in range(idx+1,len(keys)):
                    other = keys[idxowo]
                    # if other!=g:
                    for othermem in groups[other]:
                        distance = distfunc(member, othermem)
                        if distance < mindist:
                            mindist = distance
                            mingroups = g, other
        # merge groups
        if len(groups) == 4:
            break
        p,q = mingroups
        if len(groups) >= 4:
            groups[p].extend(groups[q])
            del groups[q]

    return mindist

result = cluster(count, distance, 4)

print(result)
"""
Output - 106
"""