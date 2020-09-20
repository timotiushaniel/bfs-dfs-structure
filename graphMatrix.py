class Graph:

    def __init__(self, vertices, is_undirected=True): # Fungsi buat inisialisasi
        self.v = vertices  # Jumlah simpul / vertex nya
        self.edge_list = []  # list awal untuk nyimpen simpul dan hubungannya
        self.is_undirected = is_undirected # True kalau undirected graph

    # method for adding an edge to the graph
    def add_edge(self, u, v): # Fungsi buat bikin si edge nya mau kemana arahnya
        self.edge_list.append([u, v]) #Memasukkan nilai dari si node [u, v] buat jadi edge nya ke arah mana aja
        if self.is_undirected: # Kalau misalkan si graphnya undirected, maka..... (lanjut kebawah penjelasannya)
            self.edge_list.append([v, u]) #...... Nambahin [v,u] kedalam si list edge_list ATAU Nilai si Node nya boleh di bolak balik juga (Jadi undirected)

    def make_adjacency_list(self): #Fungsi buat bikin ajdacency List
        adj_list = {key: [] for key in range(self.v)} #Buat KEY yang masih kosong, terus masukkin nilai Key nyari Value nya di range si self V
        for edge in self.edge_list: #Looping buat nyari EDGE yang ada didalem list
            edge_val = edge[1] # Ngambil edge di index 1 di si edge nya
            adj_list[edge[0]].append(edge_val) #Nambahin edge_val di index 0 pada edge_list sesuai dengan vertexnya (vertexnya adalah index 0 pd edge)
        self.__adj_list = adj_list #self._edgelist di definisiin sebagai adj_list yang udah di visit
        return adj_list


    def adjMatrix (self,adjlist): #Fungsi untuk membuat adj matrix dengan parameter adjlist
        #bikin adjacency matrix dalam bentuk nasted list isi 0 (sebanyak: baris=panjang adjacency list, kolom=panjang adj list)
        adjMatrix2 = [[0 for i in range(len(adjlist))] for j in range (len(adjlist))] # nambah kolom (yang j) & baris (yang i) sama 0
        for i in range (0,len(adjlist)): # Looping sebanyak berapa panjang si adjacency list nya (dimulai dari index ke 0)
            namavertex=i # Nyimpen nama si vertex yang lagi di visit
            hubunganvertex=adjlist[namavertex] # Ngambil simpul yang ada hubungannya sama simpul yang lagi di visit (mis: 1:[0,2])
            for j in range (0,len(hubunganvertex)): # Looping selama ada hubungan antar node (di cek perbaris mis: 01,02,03..... trus 11,12,....)
                namahubunganvertex=hubunganvertex[j] # Ngambil nama simpul pas lagi di visit
                adjMatrix2[i][namahubunganvertex]=1 # i itu index baris i , kolom kedua [namahubunganvertex] buat index kolom yang lagi di visit
        return adjMatrix2

    # Fungsi yang bertujuan untuk melakukan DFS Matrix pake parameter simpul pertama mulai dari matrixnya
    def dfs_matrix(self,start,matrix):
        visited=[] # List visited nya masih kosong
        stack=[] # Belom ada nilai pada stack
        stack.append(start) # Nambahin simpul pertama ke dalem stack

        while not stack == []: # Selama stack nya ga kosong, maka.....
            ss=stack.pop() # Ngeluarin isi stack terus di simpen di variabel ss
            if ss not in visited: # Kalau ss belom ada di list visited
                visited.append(ss) # Maka ss ditambahin ke list yang udah di visit
                for i in range (0,len(matrix)): # Looping sepanjang matrix (misL dari a00 - selesai)
                    if matrix[ss][i]==1: # Kalau matrix di baris ss kolom i nilainya = 1 (ada hubungan antara node nya)
                        stack.append(i) # Maka i ditambahin ke dalem stack nya
        return visited

    def bfs_matrix(self,start,matrix):
        queue = []
        #visited status
        visited = []
        #create a queue for BFS (simpan node yg akan dikunjungi)
        
        #queue initialize with start node
        queue.append(start)

        while not queue == []: # Selama nilai si queue tidak kosong, makaa....
            v = queue[0] #dequeue 1 vertex dari queue
            queue.remove(v) # Ngehapus nilai si V didalem queue
            if v not in visited: #Kalau V belom di visit
                visited.append(v) # Nilai V dimasukkin kedalam list visited
                for i in range (0,len(matrix)): # looping matrix nya terus sepanjang matrix nya
                    if matrix[v][i]==1: # Kalau matrix di baris v kolom i nilainya = 1
                        queue.append(i) # Maka nilai si i dimasukkin ke dalem stack nya
        return visited