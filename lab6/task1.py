import sys
sys.setrecursionlimit(10**6)

n, m = map(int,input().split())
adj = [[] for i in range(n)]

color = [0]*n
cycle = [False]
for i in range(m):
    req, course = list(map(int,input().split()))
    adj[req-1].append(course-1)
out = []

def DFS(u, cycle):
    if cycle[0] == True:
        return 
    if color[u]==1:
        cycle[0] = True
        return
    if color[u]==2:
        return 
    
    color[u]= 1
    for i in adj[u]:
        DFS(i,cycle)
    color[u] = 2
    out.append(u+1)
    
for i in range(n):
    if color[i]==0:
        DFS(i,cycle)

if cycle[0] == True:
    print(-1)
else:
    for j in out[::-1]:
        print(j,end = " ")