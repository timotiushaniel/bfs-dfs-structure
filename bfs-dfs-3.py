from collections import defaultdict

class Stack:
    def __init__(self):
        self.stack=[]
        self.TOP=-1

    def push(self, value):
        self.TOP+=1
        self.stack.append(value)

    def pop(self):
        self.TOP=-1
        return self.stack.pop()

    def top(self):
        return self.stack[self.TOP]

    def isEmpty(self):
        return self.stack==[]

    def clear(self):
        self.stack=[]
        self.TOP=-1

    def size(self):
        return len(self.stack)

    def print(self):
        for x in self.stack:
            print(x, end=' ')

st=Stack()


class Queue:
    def __init__(self):
        self.queue=[]
        self.FRONT=0
        self.REAR=-1

    def add(self,value):
        self.REAR+=1
        self.queue.append(value)

    def isEmpty(self):
        return self.queue==[]

    def remove(self):
        self.REAR-=1
        return self.queue.pop(0)

    def clear(self):
        self.queue=[]
        self.FRONT=0
        self.REAR=-1

    def size(self):
        return len(self.queue)

    def remove(self):
        self.REAR -=1
        return self.queue.pop(0)

    def print(self):
        for x in self.queue:
            print(x, end=' ')
q=Queue()


def bfs(G, start):
    # Keep track of visited vertex
    visited = []

    # Keep track of the vertex to be checked
    queue = Queue()
    queue.add(start)

    while not queue.isEmpty():
        ss = queue.remove()
        if ss not in visited:
            visited.append(ss)


            for elem in G[ss]:
                queue.add(elem)

    return visited


def dfs(G,start):
    # Keep track of visited vertex
    visited = []

    # Keep track of the vertex to be checked
    stack = Stack()
    stack.push(start)

    while not stack.isEmpty():
        ss = stack.pop()
        if ss not in visited:
            visited.append(ss)
            if ss == 49:
                break
            for elem in G[ss]:
                stack.push(elem)

    return visited

def main():
    G1 = {1 : [14],
        2 : [3],
        3 : [2,4],
        4 : [3,11],
        5 : [6],
        6 : [5,7],
        7 : [6,8],
        8 : [7,9,21],
        9 : [8,10],
        10 : [9,11,19],
        11 : [4,10,12],
        12 : [11,13],
        13 : [12,14],
        14 : [1,13,15],
        15 : [14,28],
        16 : [17,27],
        17 : [16,26],
        18 : [19,25],
        19 : [10,18,20],
        20 : [19],
        21 : [8,22],
        22 : [21,23,35],
        23 : [22,24],
        24 : [23,25],
        25 : [18,24],
        26 : [17,31],
        27 : [16,30],
        28 : [15,29],
        29 : [28,30],
        30 : [27,29],
        31 : [26,32],
        32 : [31,33],
        33 : [32,34],
        34 : [33,37],
        35 : [22,36],
        36 : [35],
        37 : [34,38],
        38 : [37,39],
        39 : [38,40,46],
        40 : [39,41],
        41 : [40,42],
        42 : [41,43],
        43 : [42,44],
        44 : [43],
        45 : [46],
        46 : [39,45,47],
        47 : [46,48],
        48 : [47,49],
        49 : [48],
         }

    #print("BFS: ")
    #bfs_trans = bfs(G1,1 )
    #print(bfs_trans)

    print("DFS: ")
    dfs_trans = dfs(G1, 1)
    print(dfs_trans)

if __name__ == '__main__':
    main()