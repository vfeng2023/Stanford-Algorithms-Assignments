# read file
with open("clustering_big.txt", "r") as f:
    lines = f.readlines()
    lookup = dict()
    # count = int(lines[0])
    # for line in lines[1:]:
    #     i,j,dist = list(map(int, line.strip().split()))
    #     lookup[i,j] = dist
    #     lookup[j,i] = dist
    nodelist = []
    for line in lines[1:]:
        bitstr = list(map(int, line.strip().split()))
        num = 0
        for b in bitstr:
            num <<=1
            num += b
        nodelist.append(num)
# group

def distance(i,j):
    return (i^j).bit_count()
def cluster(nodeslist, distfunc, k):
    # use union find data structure to store the parents of a cluster
    groups = {n:[n] for n in nodeslist}
    mindist = float('inf')
    while mindist > 3:
        # compute the minimum distance
        print(len(groups), mindist)
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
        if mindist == 3:
            break
        else:
            p,q = mingroups
        # if len(groups) >= 4:
            groups[p].extend(groups[q])
            del groups[q]

    return len(groups)

result = cluster(nodelist, distance, 4)

print(result)