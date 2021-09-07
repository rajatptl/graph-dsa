from collections import defaultdict



class Graph:
    def __init__(self):
        
        self.graph=defaultdict(list)

    def addEdge(self,src,dest):
        self.graph[src].append(dest)

    def BFS(self, start):
        visited=[False]*(max(self.graph)+1)
        qu=[]
        qu.append(start)
        visited[start]=True

        while(qu):
            temp=qu.pop(0)
            print(temp,end=' ')
            for i in self.graph[temp]:
                if visited[i]==False:
                    qu.append(i)
                    visited[i]=True

    
    


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is DFS from (starting from vertex 2)")
g.BFS(2)
