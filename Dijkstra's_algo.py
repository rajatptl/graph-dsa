import sys
def minDistance(dis, spt, n):
    m= 100000
    min_i=100000
    for i in range(n):
        if(dis[i]<m and spt[i]==False):
            m = dis[i]
            min_i=i
    
    return min_i


def dijkstra(graph,n,start):
    dis=[100000]*n
    spt=[False]*n
    dis[start]=0
    for i in range(n):
        u=minDistance(dis,spt,n)
        spt[u]=True
        for j in range(n):
            if(graph[u][j]>0 and spt[j]==False and dis[j]>(dis[u]+graph[u][j])):
                dis[j]=dis[u]+graph[u][j]
    print(dis)


g = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
n=9
start=3
dijkstra(g,n,start)

