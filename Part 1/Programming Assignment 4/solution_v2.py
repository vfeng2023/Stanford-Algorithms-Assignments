import sys
# sys.setrecursionlimit(2*32 - 1)
graph = dict()
grev = dict()

with open("SCC.txt", "r") as f:
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

        grev[v].append(u)
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
    visited = {k:0 for k in grev.keys()}# node colors
    fintime = []
    # https://stackoverflow.com/questions/24051386/kosaraju-finding-finishing-time-using-iterative-dfs
    for n in grev:
        if visited[n] != 2:
            # dfs(grev, n, fintime, visited)
            # visited.add(n)
            # stk = []
            # stk.append(n)
            # use set storing "color" of node
            # node = stk[-1]
            # 0 - not visited, 1 - in progress, 2 - done
            # while len of stk > 0:
                # examine first ode
                # if in progress --> mark as done and append
                # if color is complete -> remove
                # otherwise:
                    # mark as in progress
                    # add children if node is marked as not visited or in progress
            stk = []
            stk.append(n)
            while len(stk) > 0:
                top = stk[-1]
                if visited[top] == 1:
                    fintime.append(top)
                    stk.pop()
                    visited[top] = 2
                elif visited[top] == 2:
                    stk.pop()

                else:
                    visited[top] = 1
                    for c in grev[top]:
                        if visited[c] == 0:
                            stk.append(c)
            
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
            sccCount[n] = 1
            visitedp2.add(n)
            stk = []
            stk.append(n)
            while len(stk) > 0:
                node = stk.pop()
                for c in graph[node]:
                    if c not in visitedp2:
                        stk.append(c)
                        visitedp2.add(c)
                        sccCount[n] += 1
    # print(sccCount)
    result = [sccCount[k] for k in sccCount.keys()]
    result.sort(reverse=True)
    return result

result = kosaraju()
print(result[:5])