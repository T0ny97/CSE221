from collections import deque
n,m,s,d,k = map(int,input().split())
s-= 1
d-=1
k-=1
adj = [[] for i in range(n)]

for i in range(m):
    K,j = map(int,input().split())
    adj[K-1].append(j-1)


def Shortest_path_contains_x_node(adj,h,o):
    lent = len(adj)
    color = [0]*(lent)
    dis = [float('inf')]*(lent)
    p = [None]*(lent)
    color[h],dis[h],p[h] = 1,0,None

    q = deque()
    q.append(h)

    while len(q)!=0:
         u = q.popleft()
         for v in adj[u]:
             if color[v]==0:
                 color[v]=1
                 p[v] = u
                 dis[v] = dis[u] + 1
                 q.append(v)
    if dis[o]==float('inf'):
        return -1, 0
    path  = []
    temp = o
    while temp!=h:
        path.append(temp)
        temp = p[temp]
    path.append(h)

    return dis[o], path[::-1]

d1,p1 = Shortest_path_contains_x_node(adj,s,k)
d2,p2 = Shortest_path_contains_x_node(adj,k,d)



if d1==-1 or d2==-1:
    print(-1)
else:
    print(d1+d2)
    full_path = p1 + p2[1:]
    for i in full_path:
        print(i+1,end=" ")