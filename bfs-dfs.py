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

            for elem in G[ss]:
                stack.push(elem)

    return visited

def main():
    G = {"A" : ["D","E"],
        "B" : ["E"],
        "C" : ["A","G"],
        "D" : ["A", "G"],
        "E" : ["A","B","G"],
        "F" : ["C", "H"],
        "G" : ["D", "E","H"],
        "H" : ["F","G"],
         }

    #print("BFS: ")
    #bfs_trans = bfs(A1, "A")
    #print(bfs_trans)

    print("DFS: ")
    dfs_trans = dfs(G, "A")
    print(dfs_trans)

if __name__ == '__main__':
    main()