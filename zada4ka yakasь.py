graph=[[0,10,3,0,0],[0,0,1,2,0],[0,4,0,8,2],[0,0,0,0,7],[0,0,0,9,0]]

def zxc(graph, s):
    dist = {}  
    for v in graph:
        dist[v] = float('inf')
    dist[s] = 0

    S = set()  
    Q = set(graph.keys())  

    while Q:
        u = min(Q, key=lambda x: dist[x]) 
        Q.remove(u)
        S.add(u)

        for v in graph[u]:  
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    return dist
