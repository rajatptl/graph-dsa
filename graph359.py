from collections import defaultdict



class Graph:
    def __init__(self):
        
        self.graph=defaultdict(list)

    def addEdge(self,src,dest):
        self.graph[src].append(dest)

    def DFScycle(self,start,v,t):
        
        v.add(start)
        # print(start,end=' ')
        for i in self.graph[start]:
            if i  in v:
                t=True 
                break  
            self.DFScycle(i,v,t)

        return t
        
        




    def DFS(self,start):
        v=set()
        t=False
        t=self.DFScycle(start,v,t)
        print(t)



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
t=False 
print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
