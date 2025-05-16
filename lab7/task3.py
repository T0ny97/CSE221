import heapq
n,m = map(int,input().split())


adj = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

def minimize_danger(adj):
    danger = [float('inf')] * (n + 1)
    danger[1] = 0
    heap = [(0, 1)]

    while heap:
        cur_danger, u = heapq.heappop(heap)

        if cur_danger > danger[u]:
            continue

        for v, w in adj[u]:
            new_danger = max(cur_danger, w)
            if new_danger < danger[v]:
                danger[v] = new_danger
                heapq.heappush(heap, (new_danger, v))

    result = []
    for i in range(1, n + 1):
        if danger[i] == float('inf'):
            result.append(-1)
        else:
            result.append(danger[i])
    print(' '.join(map(str, result)))

minimize_danger(adj)