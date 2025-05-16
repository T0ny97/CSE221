import sys
sys.setrecursionlimit(2*100000+5)

n, m = map(int,input().split())

adj = [[] for _ in range(n)]
for i in range(m):
    x,y = map(int,input().split())
    adj[x-1].append(y-1)



def DFS(adj,s,c):
    c[s] = 1
    for i in adj[s]:
        if c[i]==1:
            return True
        if c[i]==0:
            if DFS(adj,i,c):
                return True
    c[s] = 2
    return False

f = False

c = [0]*(len(adj))

for i in range(n):
    if c[i]==0:
        f = DFS(adj,i,c)
        if f:
            break

if f==True:
    print("YES")
else:
    print("NO")
