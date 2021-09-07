from collections import defaultdict



class Graph:
    def __init__(self):
        
        self.graph=defaultdict(list)

    def addEdge(self,src,dest):
        self.graph[src].append(dest)

    def DFSutil(self,start,v):
        
        v.add(start)
        print(start,end=' ')
        for i in self.graph[start]:
            if i  not in v:
                self.DFSutil(i,v)
        




    def DFS(self,start):
        v=set()
        self.DFSutil(start,v)



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
