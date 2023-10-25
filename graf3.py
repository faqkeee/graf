iimport sys
def mindistance(dist,s):
    min_value=sys.maxsize
    nr_v=-1
    for i in range(len(dist)):
        if dist[i]<min_value and i not in s:
            min_value = dist[i]
            nr_v=i
    return nr_v
def zxc(graph,dist,start):
    dist[start]=0
    s=[]
    q=[]
    for i in range(len(dist)):
        q.append(i)
    while len(q)>0:
        u=mindistance(dist,s)
        if u>-1:
            ss = graph[u]
            for i in range(len(ss)):
                if ss[i]!=0 and dist[i]>dist[u]+ss[i]:
                    dist[i]=dist[u]+ss[i]
            s.append(u)
            q.remove(u)
            print(s,q)


g=[[0,10,3,0,0],[0,0,1,2,0],[0,4,0,8,2],[0,0,0,0,7],[0,0,0,9,0]]

dist=[sys.maxsize]*len(g)
d=[3,2,1,4,5]
s=[2,4]
zxc(g,dist,0)
print(dist)
print(mindistance(d,s))
