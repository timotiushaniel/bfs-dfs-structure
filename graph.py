from collections import defaultdict

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