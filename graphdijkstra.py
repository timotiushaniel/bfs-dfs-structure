from collections import defaultdict 
  
class Graph: # Class untuk mempresentasikan sebuah graph

    def __init__(self, nverticles): # n verticles itu buat ngebatasin jumlah vertex nya ada berapa (mis: n ada 9)
        self.n = nverticles
        self.graph = [[0 for column in range(nverticles)] for row in range(nverticles)] # Kolom dan row di susun sebanyak n vertex (jadi m*n)) /// Inisialisasi matrix nya jadi ga usah pake numpy
    
    def print(self):
        for l in self.graph:
            print(l)
  
    # Berfungsi untuk mencari jarak terdekat dari verticles yang masih di list queue 
    def minDistance(self,dist,queue): 
        # Initialize min value and min_index as -1 
        minimum = float("Inf") 
        min_index = -1
          
        # from the dist array,pick one which has min value and is till in queue 
        for vertex in range(len(dist)): 
            if dist[vertex] < minimum and vertex in queue: 
                minimum = dist[vertex] 
                min_index = vertex 
        return min_index 
  
  
    # Function to print shortest path from source to j using parent array 
    def printPath(self, parent, j): 
          
        #Base Case : If j is source 
        if parent[j] == -1 :  
            print (j, end = " ")
            return
        self.printPath(parent , parent[j]) 
        print (j, end = " ")
          
  
    # A utility function to print  the constructed distance  array 
    def printSolution(self, dist, parent): 
        source = 0
        print("Vertex   Distance from Source:    Path") 
        for vertex in range(1, len(dist)): 
            print(source," --> ",vertex," : ",dist[vertex])
            self.printPath(parent,vertex) 
  
  
    '''Function that implements Dijkstra's single source shortest path 
    algorithm for a graph represented using adjacency matrix 
    representation'''
    def dijkstra(self, graph, src): 
  
        row = len(graph) 
        col = len(graph[0]) 
  
        # The output array. dist[i] will hold the shortest distance from source to vertex and Initialize all distances as INFINITE  
        dist = [float("Inf")] * row 
  
        #Parent array to store shortest path tree 
        parent = [-1] * row 
  
        # jarak dari diri sendiri ke diri sendiri itu selalu di set 0
        dist[src] = 0
      
        # Add all vertices in queue 
        queue = [] 
        for vertex in range(row): 
            queue.append(vertex) 
              
        #Find shortest path for all vertices 
        while queue: 
            
            # Pick the minimum distance vertex from the set of vertices still in queue 
            u = self.minDistance(dist,queue)  
            if u!=-1:
                # remove minimum element      
                queue.remove(u) 
    
                # Update dist value and parent   index of the adjacent vertices of the picked vertex. Consider only those vertices which are still in queue 
                for vertex in range(col): 
                    '''Update dist[i] only if it is in queue, there is 
                    an edge from u to i, and total weight of path from 
                    source to i through u is smaller than current value of 
                    dist[i]'''
                    if graph[u][vertex] and vertex in queue: 
                        if dist[u] + graph[u][vertex] < dist[vertex]: 
                            dist[vertex] = dist[u] + graph[u][vertex] 
                            parent[vertex] = u 
            else:
                queue.pop(0)
  
  
        # print the constructed distance array 
        self.printSolution(dist,parent) 
  
if __name__ == '__main__':
    pass