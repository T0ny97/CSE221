import heapq
n,m,s,d = map(int,input().split())

adj = [[] for _ in range(n+1)]

st = list(map(int,input().split()))
end = list(map(int,input().split()))
w = list(map(int,input().split()))

for i in range(len(st)):
    adj[st[i]].append((end[i],w[i]))

def shortest_distance(adj,s):
    dist = [float("inf")]*len(adj)
    prev = [None]*len(adj)
    dist[s] = 0
    q = [(0, s)]
    while q:
        current_dist, u = heapq.heappop(q)

        if current_dist > dist[u]:
            continue

        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heapq.heappush(q, (dist[v], v))

    return dist, prev

dist, prev = shortest_distance(adj,s)
flag = True
if dist[d] == float('inf'):
    print(-1)
    flag = False
if flag == True:
    print(dist[d])
    path = []
    temp = d
    while temp!=None:
        path.append(temp)
        temp = prev[temp]

    path = path[::-1]
    for i in path:
        print(i,end=" ")