from collections import defaultdict
import numpy as np

# This class represents a directed graph using
# adjacency list representation
class Graph:
    # Constructor itu yang __init___ (Double underscore method / dander)
    # Self = Pointer (Otomatis diisi oleh pyhton interpreter)
    def __init__(self):
        # default dictionary (berfungsi untuk Kalau key nya tidak ada, akan ditambahkan secara otomatis) to store graph
        # Self.graph = tolong akses graph milik saya
        self.graph = defaultdict(list)

    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Print the graph
    def print(self):
        for k in self.graph:
            print(k, self.graph[k])

    def bfs(self, s):
        # Visited status
        visited = [False] * (len(self.graph))
        # Create a queue for BFS (empty list)
        queue = np.array([])

        # Queue initialite with start node
        queue.add(s)
        visited([[s]]) = True
        
        while queue:
            # Dequeue  vertex dari si queue
            # .pop berfungsi untuk mengerluarkan nilai dari dalam queue
            v = queue.pop(0)
            print(v, end = " ")

            for i in self.graph[v]:
                if visited([[i]]) == False:
                    queue.add([[i]])
                    visited([[i]]) == True
        return visited


        