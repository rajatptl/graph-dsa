class AdjNode:
    def __init__(self,vertex):
        self.data=vertex
        self.next=None

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=[None]*v

    def add_edge(self,src,dest):
        node=AdjNode(dest)
        node.next=self.graph[src]
        self.graph[src]=node

        node=AdjNode(src)
        node.next=self.graph[dest]
        self.graph[dest]=node


    def printgraph(self):
        for i in range(self.v):
            temp=self.graph[i]
            print("Adjacency list of vertex {}\n head".format(i), end="")
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
 
    g.printgraph()
