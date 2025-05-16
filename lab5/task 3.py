from collections import deque

n,m,a,b = map(int,input().split())

class Node:
    def __init__(self,id):
        self.id = id
        self.color = 0
        self.dis = float('inf')
        self.p = None

nodes = [Node(i + 1) for i in range(n)]
adj = [[] for _ in range(n)]


k = list(map(int,input().split()))
l = list(map(int,input().split()))


for i in range(m):
    s = k[i]-1
    d = l[i]-1
    adj[s].append(nodes[d])
    adj[d].append(nodes[s])


for i in range(n):
    rest = sorted(adj[i],key =lambda node:node.id)
    adj[i] = rest


def SP(adj,s,d):
    s.color = 1
    s.dis = 0
    s.p = None
    q = deque()
    q.append(s)


    while len(q)!=0:
        u = q.popleft()
        idx = u.id
        for v in adj[idx-1]:
            if v.color == 0:      
                v.color = 1
                v.dis = u.dis + 1
                v.p = u
                q.append(v)
    
    if d.dis==float('inf'):
        print(-1)
        return

    print(d.dis)
    path  = []
    temp = d
    while temp!=s:
        path.append(temp.id)
        temp = temp.p
    path.append(s.id)
    print(" ".join(map(str, reversed(path))))

    


SP(adj,nodes[a-1],nodes[b-1])
        