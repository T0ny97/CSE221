import sys
sys.setrecursionlimit(2*100000+5)

n,m = map(int,input().split())
adj = [[] for _ in range(n)]
k = list(map(int,input().split()))
l = list(map(int,input().split()))

for i in range(m):
    adj[k[i]-1].append(l[i])
    adj[l[i]-1].append(k[i])


def DFS(adj,s,c):
    c[s] = 1
    print(s, end = " ")
    for i in adj[s-1]:
        if c[i]==0:
            DFS(adj,i,c)


c = [0]*(len(adj)+1)
DFS(adj,1,c)            