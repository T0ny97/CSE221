n,q = map(int,input().split())


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

adj = []
adj = [[] * n for _ in range(n)]

for i in range(n):
    for j in range(i+1,n):
        if gcd(i+1,j+1)==1:
            adj[i].append(j+1)
            adj[j].append(i+1)



for i in range(q):
    vert, th = map(int,input().split())
    if th>len(adj[vert-1]):
        print(-1)
    
    else:
        print(adj[vert-1][th-1])

        
    




