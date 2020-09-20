from collections import defaultdict

#This class represents a directed graph using
#adjacency list representation
class Graph:
    #Constructor
    def __init__(self):
        #Default dictionary to store graph
        #defaultdict nambah entri otomatis
        #(list) adalah value
        self.graph = defaultdict(list)

    #Function to add an edge to the graph
    def addEdge(self,u,v):
    #mengakses objek graph milik pribadi
        self.graph[u].append(v)

    #Print the graph
    def print(self):
        # looping setiap element yang ada di self.graph
        for k in self.graph:
            print(k, self.graph[k])

    def vertex(self):
        vertex=[]
        for m in self.graph:
            vertex.append(m)
        return vertex
        
    def adjMatrix (self,vertex):
        adjMatrix2 = [[0 for i in range(len(vertex))] for j in range (len(vertex))]
        for i in range (0,len(vertex)):
            namavertex=vertex[i]
            hubunganvertex=self.graph[namavertex]
            for j in range (0,len(hubunganvertex)):
                namahubunganvertex=hubunganvertex[j]
                adjMatrix2[i][vertex.index(namahubunganvertex)]=1
        return adjMatrix2

    
    def bfs_matrix(self,s,matrix,vertex):
        import queue
        queue = queue.Queue(maxsize = 0)
        #visited status
        visited = []
        #create a queue for BFS (simpan node yg akan dikunjungi)
        
        #queue initialize with start node
        queue.put(s)

        while not queue.empty():
            #dequeue 1 vertex from queue
            v = queue.get()
            if v not in visited:
                visited.append(v)
                for i in range (0,len(vertex)):
                    if vertex[i]==v:
                        for j in range (0,len(vertex)):
                            if matrix[i][j]==1:
                                queue.put(vertex[j])
        return visited

    def dfs_matrix(self,start,matrix,vertex):
        visited=[]

        stack=[]
        stack.append(start)

        while not stack == []:
            ss=stack.pop()
            if ss not in visited:
                visited.append(ss)
                for i in range (0,len(vertex)):
                    if vertex[i]==ss:
                        for j in range (0,len(vertex)):
                            if matrix[i][j]==1:
                                stack.append(vertex[j])
        return visited