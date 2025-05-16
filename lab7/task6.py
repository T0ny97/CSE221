import heapq
n,m,s,d = map(int,input().split())


adj = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

def second_shortest_path(adj, n, s, d):

    dist1 = [float('inf')] * (n + 1)
    dist2 = [float('inf')] * (n + 1)
    
    dist1[s] = 0
    q = [(0, s)]  

    while q:
        cost, u = heapq.heappop(q)

        for v, w in adj[u]:
            new_dist = cost + w
            if new_dist < dist1[v]:
                dist2[v] = dist1[v]
                dist1[v] = new_dist
                heapq.heappush(q, (new_dist, v))
            elif dist1[v] < new_dist < dist2[v]:
                dist2[v] = new_dist
                heapq.heappush(q, (new_dist, v))

    return dist2[d] if dist2[d] != float('inf') else -1

print(second_shortest_path(adj, n, s, d))