import sys
sys.setrecursionlimit(2*32 - 1)
graph = dict()
grev = dict()

with open("test.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        u,v = list(map(int, l.split()))
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)

        if u not in grev:
            grev[u] = []

        if v not in grev:
            grev[v] = []

        grev[v].append(v)
print("finished reading file")
def kosaraju():
    count = 0
    def dfs(graph, node, fin, visited, counting=False):
        if node not in visited:
            visited.add(node)
            for c in graph[node]:
                if c not in visited:
                    dfs(graph, c, fin, visited)
            fin.append(node)

    # first pass dfs loop
    visited = set()
    fintime = []
    for n in grev:
        if n not in visited:
            dfs(grev, n, fintime, visited)
    fintime.reverse()
    # second pass
    # add node to list of leaderds
    def dfs2(graph, node, visited, sccCount, parent):
        if node not in visited:
            sccCount[parent] += 1
            visited.add(node)
            for c in graph[node]:
                if c not in visited:
                    dfs2(graph, c, visited, sccCount, parent)
    visitedp2 = set()
    p2 = []
    sccCount = dict()
    for n in fintime:
        if n not in visitedp2:
            sccCount[n] = 0
            dfs2(graph, n, visitedp2, sccCount, n)

    result = [sccCount[k] for k in sccCount.keys()]
    result.sort(reverse=True)
    return result

print(kosaraju())