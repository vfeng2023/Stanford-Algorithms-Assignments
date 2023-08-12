from heapq import heappush, heappop, heapify
filename = "edges.txt"
with open(filename, "r") as f:
    lines = f.readlines()
    nodes,numedges = list(map(int, lines[0].strip().split()))
    edges = []
    graph = [[] for i in range(501)]
    for line in lines[1:]:
        u,v,cost = list(map(int, line.strip().split()))

        # edges.append((cost, u,v))
        graph[u].append((v,cost))
        graph[v].append((u,cost))


# apply prims algo to arr of edges

def prims(graph):
    # heapify edge list
    # while edgelist has edges:
        # remove edges
        # if edge crosses the cut X, V-X, add to tree
    # visited = set()
    # heapify(edgelist)
    # mincost = 0
    # while len(edgelist) > 0:
    #     cost, u,v = heappop(edgelist)
    #     if u in visited and v in visited:
    #         pass
    #     else:
    #         mincost += cost
    #         visited.add(u)
    #         visited.add(v)
    # return mincost
    heap = []
    visited = set()
    # visited.add(1)
    heappush(heap, (0, 1)) # node
    minCost = 0
    while len(heap) > 0:
        cost, node = heappop(heap)
        if node not in visited:
            minCost += cost
            visited.add(node)
            for neighbor, c in graph[node]:
                heappush(heap, (c, neighbor))
    return minCost



result = prims(graph)
print("MST cost: ", result)

"""
Output:
MST cost:  -2664308
"""