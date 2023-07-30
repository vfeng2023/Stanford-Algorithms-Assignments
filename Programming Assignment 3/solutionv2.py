# represent graph as a list of edges and vertices as disjoint set for fast combines
from typing import *
from copy import *
import random
from math import log2
# count vertices,
# count edges
# read graph
class Edge:
    def __init__(self, u:int, v:int):
        self.u = u
        self.v = v
    def __eq__(self, __value: object) -> bool:
        return (self.u == __value.u and self.v == __value.v) or (self.u == __value.v and self.v == __value.u)
    
    def __hash__(self) -> int:
        return self.u ^ self.v


class Graph:
    def __init__(self):
        self.edges = []
        self.vertices = dict() # vertex -> parent

    def find(self,n):
        p = n
        while p !=self.vertices[p]:
            self.vertices[p] = self.vertices[self.vertices[p]]
            p = self.vertices[p]

        return p
    def union(self, v1, v2)->bool:
        """
        unions to subsets. Returns true if union operation was successful
        """
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1==p2:
            return False
        self.vertices[p2] = p1
        return True
    

def minCut(g:"Graph", iterations:int) -> int:
    # for iteration number\
    mincount = len(g.edges)
    for i in range(iterations):
        print("iteration: ", i, end = " ")
        # copy graph
        graph = Graph()
        graph.edges = g.edges[:]
        graph.vertices = g.vertices.copy()
        vertexcount = len(graph.vertices)
        # while number vertices > 2:
            # get edge at random from graph.edges
            # contract that graph
            # remove all edges which are self loops
        random.seed(None)
        while vertexcount > 2:
            edge = random.choice(graph.edges)
            res = graph.union(edge.u, edge.v)
            if res:
                vertexcount -= 1
            newedges = []
            # for edge in graph.edges:
            #     p1 = graph.find(edge.u)
            #     p2 = graph.find(edge.v)
            #     if p1 != p2:
            #         newedges.append(edge)
            # graph.edges = newedges
        
        count = 0
        for edge in graph.edges:
            p1 = graph.find(edge.u)
            p2 = graph.find(edge.v)
            if p1!=p2:
                count += 1
        mincount = min(count, mincount)
        print("mincount: ", mincount)
    return mincount
            
        # mincut = min(edges)

g = Graph()
with open("kargerMinCut.txt", "r") as f:
    lines = f.readlines()
    edgeset = set()
    for l in lines:
        l = list(map(int, l.split()))

        # graph.id = l[0]
        # graph.adjlist[l[0]] = set(l[1:])

        for v in range(1, len(l)):
            node = l[v]
            # if v != l[0]:
            key = Edge(node, l[0])
            if key not in edgeset:
                edgeset.add(key)
        g.vertices[l[0]] = l[0]
    g.edges = list(edgeset)

result = minCut(g, 200*200)
print("min cut:", result)
