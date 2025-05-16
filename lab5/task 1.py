n,m = map(int,input().split())

adj = [[] for _ in range(n)]

for i in range(m):
    k,j = map(int,input().split())
    adj[k-1].append(j)
    adj[j-1].append(k)

def BFS(adj,s):
    c = [0]*(len(adj)+1)

    c[s] = 1
    q = []
    q.append(s)

    

    while len(q)!=0:
        u = q.pop(0)
        print(u,end=" ")
        for v in adj[u-1]:
            if c[v] == 0:      
                c[v] = 1
                q.append(v)


BFS(adj,1)