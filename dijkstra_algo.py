def dijkstra(self, V, adj, s):
    parent=[-1 for i in range(V)]
    dis=[100000000 for i in range(V)]
    pro=[False for i in range(V)]
    # g=[[0 for i in range(V)] for j in range(V)]
    parent[s]=-1
    dis[s]=0
    for i in range(V):
        u=minima(dis,pro,V)
        # print(u)
        pro[u]=True
        # print(pro)
        for j in adj[u]:
            if(pro[j[0]]==False and (dis[u]+j[1]<dis[j[0]])):
                dis[j[0]]=dis[u]+j[1]
                parent[j[0]]=u                
    return dis

def minima(dis,pro,V):
    mn=1000000000
    for i in range(V):
        if(pro[i]==False and dis[i]<mn):
            ver=i
            mn=dis[i]
    return ver