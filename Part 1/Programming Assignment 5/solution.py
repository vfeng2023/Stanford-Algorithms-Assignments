# read graph
# implement dijkstra
# print the values for the relevant vertices
from heapq import heappush, heappop, heapify
"""
In this programming problem you'll code up Dijkstra's shortest-path algorithm.

Download the following text file (Right click and select "Save As..."): dijkstraData.txt

The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex and vertex 1, we'll define the shortest-path distance between 1 and to be 1000000.

You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197. Enter the shortest-path distances using the fields below for each of the vertices.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Dijkstra's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing the heap-based version. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
"""
graph = dict()
with open("dijkstraData.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.split()
        node = int(line[0])
        graph[node] = []
        for i in range(1, len(line)):
            neighbor, weight = list(map(int, line[i].split(",")))
            graph[node].append((neighbor, weight))

def search(start, graph):
    dists = {n:float('inf') for n in graph.keys()}

    # dists[start] = 0
    heap = []
    dists = dict()
    heappush(heap, (0, start))
    while len(heap) > 0:
        dikdist, node = heappop(heap)
        if node not in dists:
            dists[node] = dikdist
            # visited.add(node)
            for neighbor, weight in graph[node]:
                heappush(heap, (dikdist + weight, neighbor))
    return dists

results = search(1, graph)
for i in [7,37,59,82,99,115,133,165,188,197]:
    print(i, results[i])
