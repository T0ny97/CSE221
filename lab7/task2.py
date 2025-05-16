import heapq
n,m,s,t = map(int,input().split())

adj = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))


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

    return dist

disX = shortest_distance(adj,s)
disY = shortest_distance(adj,t)

min_time = float('inf')
meeting_node = n+1

for v in range(1, n + 1):
    if disX[v] != float('inf') and disY[v] != float('inf'):
        meet_time = max(disX[v], disY[v])
        if meet_time < min_time or (meet_time == min_time and v < meeting_node):
            min_time = meet_time
            meeting_node = v

if meeting_node == n+1:
    print(-1)
else:
    print(f"{min_time} {meeting_node}")