import heapq

N, M, S, D = map(int, input().split())
weights = list(map(int, input().split()))

adj = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    adj[u].append((v))

cost = [float('inf')] * (N + 1)
cost[S] = weights[S - 1] 
heap = [(cost[S], S)] 

while heap:
    cur_cost, u = heapq.heappop(heap)

    if cur_cost > cost[u]:
        continue

    for v in adj[u]:
        path_cost = cur_cost + weights[v - 1]
        if path_cost < cost[v]:
            cost[v] = path_cost
            heapq.heappush(heap, (cost[v], v))

if cost[D] == float('inf'):
    print(-1)
else:
    print(cost[D])