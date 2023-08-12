from typing import *
from copy import copy
# initialize graph
class Edge:
    def __init__(self, u:int, v:int):
        self.u = u
        self.v = v
    def __eq__(self, __value: object) -> bool:
        return (self.u == __value.u and self.v == __value.v) or (self.u == __value.v and self.v == __value.u)
    
    def __hash__(self) -> int:
        return self.u ^ self.v
class Graph:
    # def __init__(self):
    #     # list of vertices
    #     # list of edges
    #     # enpoints
    #     # incident 
    #     # self.vertices = []
    #     self.edges = [] # map edge to count of edges
    #     self.adjList ={} # map vertex to edge they are part of 
    #     self.nextnode = 1

    # # def addedge()
    # @classmethod
    # def getkey(u,v):
    #     return tuple(sorted([u,v]))
    # def addedge(self, u,v):
    #     key = tuple(sorted([u,v]))
    #     if key in self.edges:
    #         self.edges[key] += 1
    #     else:
    #         self.edges[key] = 1

    #     if u not in self.adjList:
    #         self.adjList[u] = set([key])
    #     if v not in self.adjList:
    #         self.adjList[v] = set([key])

    # def contract(self, u, v):
    #     key = tuple(sorted([u,v]))
    #     # create new node
    #     self.adjList[self.nextnode] = set()

    #     w
    def __init__(self):
        self.edges = dict() # list of edges -> count of edges
        self.adjlist = dict() # maps node -> adjacent nodes
        self.id = 1
        

    def addedge(self, edge):
        if edge in self.edges:
            self.edges[edge] += 1
        else:
            self.edges[edge] = 1

        u,v = edge.u, edge.v
        if u not in self.vertices:
            self.vertices[u] = set()

        if v not in self.vertices:
            self.vertices[v] = set()
        
        self.vertices[u].add(edge)
        self.vertices[v].add(edge)

    def contract(self, edge):
        u,v = edge.u, edge.v
        # remove vertices of that edge
        unodes = self.adjlist[u]
        vnodes = self.adjlist[v]


        # create new node
        self.adjlist[self.id] = set()
        # COMBINE u and v's edges for new node uv
        for n in unodes:
            if n == u or n == v:
                del self.adjlist[Edge(n,u)]
                continue
            key = Edge(u,n)
            newnode = Edge(self.id, n)
            self.adjlist[self.id].add(n)
            if newnode in self.edges:
                self.edges[newnode] += self.edges[key]
            else:
                self.edges[newnode] = self.edges[key]
            del self.edges[key]
        
        for nv in vnodes:
            if nv == u or nv == v:
                del self.adjlist[Edge(n,v)]
                continue
            key = Edge(u,nv)
            newnode = Edge(self.id, nv)
            self.adjlist[self.id].add(nv)
            if newnode in self.edges:
                self.edges[newnode] += self.edges[key]
            else:
                self.edges[newnode] = self.edges[key]
            del self.edges[key]
        # REPLACE all occurences of u and v with uv
        del self.adjlist[u]
        del self.adjlist[v]
        # DELETE u and v from the set
        

# run karger's random contraction algorithm

graph = Graph()
with open("kargerMinCut.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        l = list(map(int, l.split()))

        graph.id = l[0]
        graph.adjlist[l[0]] = set(l[1:])

        for v in range(len(1, len(l))):
            node = l[v]
            key = Edge(v, l[0])
            if key not in graph.edges:
                graph.edges[key] = 1


def mincut(graph:Optional[Graph], iterations):
    oggraph = copy.deepcopy(graph)
    while len(graph.adjlist) > 2:
        # fuck
        pass