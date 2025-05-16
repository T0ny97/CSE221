from collections import deque

n,m = map(int,input().split())
adj = [[] for _ in range(n)]
for i in range(m):
    x,y = map(int,input().split())
    adj[x-1].append(y-1)
    adj[y-1].append(x-1)

# adj = [[3, 1], [2, 4, 0], [3, 1], [2, 4, 0], [3, 1]]

color = [0]*n
def BFS(source,adj):
    color[source] = 1
    stk = deque()
    stk.append(source)
    cnt1 = 1
    cnt2 = 0
    while len(stk)!=0:
        u = stk.popleft()
        for i in adj[u]:
            if color[u]==color[i]:
                return -1
            if color[i]==0:
                color[i] = 3 - color[u]
                if color[i]==1:
                     cnt1+=1
                else:
                     cnt2+=1
                stk.append(i)
    return max(cnt1,cnt2)

r,h = 0,0
poss= True
res = 0
for i in range(n):
     if color[i]==0:
          o = BFS(i,adj)
          if o==-1:
            print(-1)
            poss = False
            break
          res+= o



if poss == True:
    print(res)

